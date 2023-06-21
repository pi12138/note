package demo

import (
	"fmt"
	"os"
	"reflect"

	"github.com/fatih/structs"
)

type str string

type Foo struct {
	A int    `json:"a" mser:"source:A"`
	B string `json:"b"`
}

func (r Foo) GetA() int {
	return r.A
}

func Demo() {
	var f Foo
	var i int64
	var s str

	fType := reflect.TypeOf(f)
	iType := reflect.TypeOf(i)
	sType := reflect.TypeOf(s)

	// 类型名称 和 类型的类别
	fmt.Printf("f type name: %s, type kind: %d, %t\n", fType.Name(), fType.Kind(), fType.Kind() == reflect.Struct) // > f type name: Foo, type kind: 25, true
	fmt.Printf("i type name: %s, type kind: %d, %t\n", iType.Name(), iType.Kind(), iType.Kind() == reflect.Int)    // > i type name: int, type kind: 2, true
	fmt.Printf("s type name: %s, type kind: %d, %t\n", sType.Name(), sType.Kind(), sType.Kind() == reflect.String) // > s type name: str, type kind: 24, true

	// 指针类型可以使用 Type.Elem() 获取 Type
	m := make(map[int]string)
	l := make([]string, 0)
	var a interface{}
	a = 1

	fpType := reflect.TypeOf(&f)
	mType := reflect.TypeOf(m)
	lType := reflect.TypeOf(l)
	aType := reflect.TypeOf(a)
	fmt.Printf("f point type name: %s, type kind: %d, %t\n", fpType.Name(), fpType.Kind(), fpType.Kind() == reflect.Pointer) // > f point type name: , type kind: 22, true
	fmt.Printf("f point type Elem: %s\n", fpType.Elem())
	fmt.Printf("m type name: %s, type kind: %d, %t\n", mType.Name(), mType.Kind(), mType.Kind() == reflect.Map)       // > m type name: , type kind: 21, true
	fmt.Printf("l type name: %s, type kind: %d, %t\n", lType.Name(), lType.Kind(), lType.Kind() == reflect.Slice)     // > l type name: , type kind: 23, true
	fmt.Printf("a type name: %s, type kind: %d, %t\n", aType.Name(), aType.Kind(), aType.Kind() == reflect.Interface) // > a type name: int, type kind: 2, false

	var varList = []any{f, i, s, m, l, a, &f}
	for _, v := range varList {
		vt := GetType(v)
		fmt.Printf("type Name: %s, type Kind: %d\n", vt.Name(), vt.Kind())
	}

	ShowStructField(f)
	ShowValue(f)
	fmt.Printf("set before s: %s, i: %d, f: %v\n", s, i, f)
	SetValue(&s, "string")
	SetValue(&i, int64(100))
	SetValue(&f, Foo{10, "B"})
	fmt.Printf("set after s: %s, i: %d, f: %v\n", s, i, f)

	ParseTag(f)
	fmt.Printf("ToJsonMap(f): %v\n", ToJsonMap(f))
}

// GetType 获取变量的 Type
func GetType(v any) reflect.Type {
	switch vt := reflect.TypeOf(v); vt.Kind() {
	case reflect.Pointer, reflect.Map, reflect.Slice, reflect.Chan, reflect.Array:
		return vt.Elem()
	default:
		return vt
	}
}

func ShowStructField(v any) {
	t := GetType(v)
	if t.Kind() != reflect.Struct {
		os.Exit(1)
	}

	fmt.Printf("struct Name: %s, struct Field Count: %d\n", t.Name(), t.NumField())
	for i := 0; i < t.NumField(); i++ {
		f := t.Field(i)
		fmt.Printf("struct Field name: %s, Field type: %s, Field tag: %s\n", f.Name, f.Type.Name(), f.Tag)
	}
}

func ShowValue(v any) {
	vv := reflect.ValueOf(v)
	fmt.Printf("value: %v, kind: %d\n", vv.Interface(), vv.Kind())
}

func SetValue(v any, value any) {
	vv := reflect.ValueOf(v)
	if vv.Kind() != reflect.Pointer {
		os.Exit(1)
	}
	switch kind := vv.Elem().Kind(); kind {
	case reflect.String:
		vv.Elem().SetString(value.(string))
	case reflect.Int64:
		vv.Elem().SetInt(value.(int64))
	case reflect.Struct:
		valueV := reflect.ValueOf(value)
		for i := 0; i < vv.Elem().NumField(); i++ {
			switch t := vv.Elem().Field(i).Type().Kind(); t {
			case reflect.Int:
				vv.Elem().Field(i).SetInt(int64(valueV.Field(i).Interface().(int)))
			case reflect.String:
				vv.Elem().Field(i).SetString(valueV.Field(i).Interface().(string))
			}
		}
	default:
		fmt.Printf("dont handle\n")
	}
}

func ParseTag(v any) {
	vv := reflect.TypeOf(v)
	if vv.Kind() != reflect.Struct {
		os.Exit(1)
	}

	for i := 0; i < vv.NumField(); i++ {
		field := vv.Field(i)
		// fmt.Printf("Field tag: %v", field.Tag)
		fmt.Println(field.Name, field.Tag.Get("json"), field.Tag.Get("mser"))
	}

}

func ToJsonMap(v any) map[string]any {
	s := structs.New(v)
	s.TagName = "json"
	return s.Map()
}
