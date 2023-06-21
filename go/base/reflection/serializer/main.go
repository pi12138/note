package serializer

import (
	"errors"
	"fmt"
	"reflect"
	"strings"

	goSet "github.com/deckarep/golang-set"
)

const (
	TagName             string = "dest"
	Source              string = "source"
	SkipField           string = "skip"
	RequiredField       string = "require"
	FuncFormat          string = "Get%sValue"
	UnitSplit           string = ";"
	KVSplit             string = ":"
	ValidateFieldFuncKV string = "ValidateField"
)

func validateType(destType, srcType reflect.Type) error {
	if destType.Kind() != reflect.Pointer {
		return errors.New("dest must be Pointer")
	}
	if destType.Elem().Kind() != reflect.Struct {
		return errors.New("dest must be Struct Pointer")
	}
	if srcType.Kind() != reflect.Pointer {
		return errors.New("src must be Pointer")
	}
	if srcType.Elem().Kind() != reflect.Struct {
		return errors.New("src must be Struct Pointer")
	}
	return nil
}

func AssignAttr(dest any, src any) error {
	destType := reflect.TypeOf(dest)
	srcType := reflect.TypeOf(src)
	if err := validateType(destType, srcType); err != nil {
		return err
	}

	nameToValue, err := GetFieldNameToValue(src)
	if err != nil {
		return err
	}
	destValue := reflect.ValueOf(dest)
	destTypeElem := destType.Elem()
	destValueElem := destValue.Elem()
	for i := 0; i < destType.Elem().NumField(); i++ {
		fieldValue := destValueElem.Field(i)
		fieldType := destTypeElem.Field(i)
		tagMap := ParseSerTag(fieldType.Tag.Get(TagName))
		_, required := tagMap[RequiredField]
		// if len(tagMap) == 0 {
		// 	continue
		// }

		if _, ok := tagMap[SkipField]; ok { // skip this field
			continue
		}
		source := tagMap[Source]
		if source == "" {
			source = fieldType.Name
		}

		funcName := fmt.Sprintf(FuncFormat, fieldType.Name)
		// fmt.Printf("source: %v, requried: %v, funcName: %v\n", source, required, funcName)
		if source == funcName { // func
			f := destValue.MethodByName(funcName)
			in := []reflect.Value{reflect.ValueOf(src)}
			valueList := f.Call(in)
			value := valueList[0]
			fieldValue.Set(value)
		} else { // simple var
			srcValue, ok := nameToValue[source]
			if !ok && required { // dont source field
				return fmt.Errorf("src dont field %s", source)
			}
			if !ok {
				continue
			}
			if srcValue.Type().Kind() != fieldType.Type.Kind() {
				return fmt.Errorf("dest field %s and src field %s type are inconsistent", fieldType.Name, source)
			}
			fieldValue.Set(srcValue)
		}
	}
	return nil
}

func GetFieldNameToValue(src any) (map[string]reflect.Value, error) {
	Type := reflect.TypeOf(src)
	validTypeKind := goSet.NewSet(reflect.Pointer, reflect.Struct)
	if !validTypeKind.Contains(Type.Kind()) {
		return nil, errors.New("src must be Struct or Struct Pointer")
	}
	if Type.Kind() == reflect.Pointer && Type.Elem().Kind() != reflect.Struct {
		return nil, errors.New("src must be Struct or Struct Pointer")
	}

	Value := reflect.ValueOf(src)
	if Type.Kind() == reflect.Pointer {
		Type = Type.Elem()
		Value = Value.Elem()
	}

	result := make(map[string]reflect.Value)
	for i := 0; i < Value.NumField(); i++ {
		fieldType := Type.Field(i)
		fieldValue := Value.Field(i)
		result[fieldType.Name] = fieldValue
	}
	return result, nil
}

func ParseSerTag(tag string) map[string]string {
	result := make(map[string]string)
	tagList := strings.Split(tag, UnitSplit)
	var tagKey, tagValue string
	for _, str := range tagList {
		if str == "" {
			continue
		}
		if strings.Contains(str, KVSplit) {
			kv := strings.Split(str, KVSplit)
			tagKey = kv[0]
			tagValue = kv[1]
		} else {
			tagKey = str
		}
		result[tagKey] = tagValue
	}
	return result
}

// func AssignAttrTosrc(dest any, src any) error {
// 	destType := reflect.TypeOf(dest)
// 	srcType := reflect.TypeOf(src)
// 	if err := validateType(destType, srcType); err != nil {
// 		return err
// 	}

// 	nameToValue, err := GetsrcFieldNameToValue(src)
// 	if err != nil {
// 		return err
// 	}
// 	destValue := reflect.ValueOf(dest)
// 	destTypeElem := destType.Elem()
// 	destValueElem := destValue.Elem()
// 	for i := 0; i < destType.Elem().NumField(); i++ {
// 		fieldValue := destValueElem.Field(i)
// 		fieldType := destTypeElem.Field(i)
// 		tagMap := ParseSerTag(fieldType.Tag.Get(TagName))
// 		if len(tagMap) == 0 {
// 			continue
// 		}

// 		if _, ok := tagMap[SkipField]; ok { // skip this field
// 			continue
// 		}
// 		source := tagMap[Source]
// 		if source == "" {
// 			source = fieldType.Name
// 		}

// 		funcName := fmt.Sprintf(FuncFormat, fieldType.Name)
// 		if source == funcName { // func sikp
// 			continue
// 		} else { // simple var
// 			srcValue, ok := nameToValue[source]
// 			if !ok { // dont source field
// 				return fmt.Errorf("src dont field %s", source)
// 			}
// 			if srcValue.Type().Kind() != fieldType.Type.Kind() {
// 				return fmt.Errorf("dest field %s and src field %s type are inconsistent", fieldType.Name, source)
// 			}
// 			srcValue.Set(fieldValue)
// 		}
// 	}

// 	return nil
// }

func CallValidateFieldFunc(dest any) error {
	destType := reflect.TypeOf(dest)
	if destType.Kind() != reflect.Pointer {
		return errors.New("dest must be Pointer")
	}
	if destType.Elem().Kind() != reflect.Struct {
		return errors.New("dest must be Struct Pointer")
	}

	destValue := reflect.ValueOf(dest)

	for i := 0; i < destType.NumMethod(); i++ {
		f := destValue.Method(i)
		funcName := destType.Method(i).Name
		if !strings.HasPrefix(funcName, ValidateFieldFuncKV) {
			continue
		}
		fieldName := strings.Replace(funcName, ValidateFieldFuncKV, "", 1)
		field := destValue.Elem().FieldByName(fieldName)
		in := []reflect.Value{field}
		res := f.Call(in)
		if err, ok := res[0].Interface().(error); ok {
			return err
		}

	}

	return nil
}
