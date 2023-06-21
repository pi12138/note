package structs_delete

// import (
// 	"reflect"
// 	"strings"
// )

// const (
// 	TagName = "json"
// )

// func ToMap(v any) map[string]any {
// 	vt := reflect.TypeOf(v)
// 	vv := reflect.ValueOf(v)
// 	if vt.Kind() == reflect.Pointer {
// 		vt = vt.Elem()
// 		vv = vv.Elem()
// 	}

// 	// must be struct
// 	if vt.Kind() != reflect.Struct {
// 		return nil
// 	}

// 	// fields := structFields(vt)

// 	return nil
// }

// func structFields(t reflect.Type) []reflect.StructField {
// 	var f []reflect.StructField

// 	for i := 0; i < t.NumField(); i++ {
// 		field := t.Field(i)
// 		// we can't access the value of unexported fields
// 		if field.PkgPath != "" {
// 			continue
// 		}

// 		// don't check if it's omitted
// 		if tag := field.Tag.Get(TagName); tag == "-" {
// 			continue
// 		}

// 		f = append(f, field)
// 	}

// 	return f
// }

// type tagOptions []string

// // Has returns true if the given option is available in tagOptions
// func (t tagOptions) Has(opt string) bool {
// 	for _, tagOpt := range t {
// 		if tagOpt == opt {
// 			return true
// 		}
// 	}

// 	return false
// }

// // parseTag splits a struct field's tag into its name and a list of options
// // which comes after a name. A tag is in the form of: "name,option1,option2".
// // The name can be neglectected.
// func parseTag(tag string) (string, tagOptions) {
// 	// tag is one of followings:
// 	// ""
// 	// "name"
// 	// "name,opt"
// 	// "name,opt,opt2"
// 	// ",opt"

// 	res := strings.Split(tag, ",")
// 	return res[0], res[1:]
// }
