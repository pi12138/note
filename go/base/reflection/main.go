package main

import (
	"encoding/json"
	"fmt"
	"log"
	"reflect"
	"time"

	// "reflection/demo"
	"strings"
)

func main() {
	// demo.Demo()
	// serializer.Demo()
	// Demo()
	// MapToJson()
	// demo.PointCanSet()
	// SetStruct()
	CanSet()
}

func Demo() {
	a := "aaaxxx"
	b := strings.Replace(a, "a", "", 3)
	fmt.Printf("b: %s\n", b)
}

func MapToJson() {
	m := make(map[string]any)

	m["int"] = 10
	m["string"] = "string"
	m["float"] = 1.1
	m["array"] = [3]string{"a", "b", "c"}
	m["list"] = []string{"a", "b"}
	m["dict"] = map[int]int{1: 1, 2: 2}

	v := 10
	p := &v
	m["pointer"] = p
	data, _ := json.Marshal(m)
	log.Printf("data: %s", string(data))
}

func SetStruct() {
	type People struct {
		Name string
		Age  int
	}
	p := &People{}
	// pt := reflect.TypeOf(p)
	pv := reflect.ValueOf(p)
	v := reflect.New(reflect.TypeOf(&People{}).Elem())
	v = v.Elem()
	name := v.FieldByName("Name")
	age := v.FieldByName("Age")

	if name.CanSet() {
		name.SetString("p-name")
	}
	if age.CanSet() {
		age.SetInt(60)
	}
	if pv.Elem().CanSet() {
		pv.Elem().Set(v)
	}

	fmt.Println(name.CanSet(), age.CanSet(), pv.CanSet(), pv.Elem().CanSet())
	fmt.Println(p)
	fmt.Println(name.Interface(), age.Interface())
}

func CanSet() {
	var p1 *int
	var p2 = new(int)
	p3 := make([]int, 0)
	p3 = append(p3, 1)

	v1 := reflect.ValueOf(p1)
	v2 := reflect.ValueOf(p2)
	v3 := reflect.ValueOf(p3)

	// fmt.Println(p1, *p2)
	fmt.Println(v1.Elem().CanSet())
	fmt.Println(v2.Elem().CanSet())
	fmt.Println(v3.CanSet(), v3.CanAddr(), v3.Len())
	fmt.Println(v3.Index(0))
	// v2.Elem().SetInt(10)
	// fmt.Println(*p2, v1.IsNil(), v1.Elem().IsZero())

	// v1.Elem().SetInt(20)
}

func PointCanSet() {
	var a *int
	b := 10
	a = &b
	v := reflect.ValueOf(a)
	fmt.Printf("v can set: %v, v elem can set: %v\n", v.CanSet(), v.Elem().CanSet())

	var p *int
	pv := reflect.ValueOf(p)
	fmt.Printf("pv can set: %v, pv elem can set: %v\n", pv.CanSet(), pv.Elem().CanSet())

	pv = reflect.ValueOf(&p)
	fmt.Printf("pv can set: %v, pv elem can set: %v, pv elem's elem can set: %v\n", pv.CanSet(), pv.Elem().CanSet(), pv.Elem().Elem().CanSet())
}

type Base struct {
	Name string
	Age  int
}

type Base2 struct {
	Name2 string
	Age2  int
}

type Person struct {
	Weight int
	Height int
	Base
	Base2 Base2
}

func InlineReflect() {
	p := Person{}

	rt := reflect.TypeOf(p)
	// rv := reflect.ValueOf(p)
	fmt.Printf("addr: %p %p\n", &p.Base.Age, &p.Age)
	for i := 0; i < rt.NumField(); i++ {
		f := rt.Field(i)
		fmt.Printf("field: %v %s %v\n", f.Name, f.Type.Kind(), f.Anonymous)

	}
	for _, i := range []string{"Age", "Name", "Age2"} {
		f, ok := rt.FieldByName(i)
		fmt.Printf("ok: %v, field: %v\n", ok, f.Name)
	}
}

func TestAssignableTo() {
	var a, b int
	{
		rtA := reflect.TypeOf(&a)
		rtB := reflect.TypeOf(&b)

		fmt.Printf("a is AssignableTo b: %v\n", rtA.AssignableTo(rtB))
	}

	var ba Base
	var bb Base2

	{
		rtBA := reflect.TypeOf(&ba)
		rtBB := reflect.TypeOf(&bb)

		fmt.Printf("ba is AssignableTo bb: %v\n", rtBA.AssignableTo(rtBB))
	}
}

func TestNilValue() {
	var n any
	rv := reflect.ValueOf(n)
	rv.IsNil()
	fmt.Printf("%s \n", rv.Kind())
}

func IsAnonymous() {
	type D struct {
		Name string
	}
	type Demo struct {
		Time1 time.Time
		Time2 *time.Time
		X     D
		D
	}
	var v Demo
	rv := reflect.ValueOf(&v)
	rv = rv.Elem()
	for i := 0; i < rv.Type().NumField(); i++ {
		fieldT := rv.Type().Field(i)
		kind := fieldT.Type.Kind()
		name := fieldT.Type.Name()
		for kind == reflect.Pointer {
			kind = fieldT.Type.Elem().Kind()
			name = fieldT.Type.Elem().Name()
		}
		fmt.Printf("Name: %s, Type: %s, Kind: %s, Anonymous: %v, is time: %v\n", fieldT.Name, name, kind, fieldT.Anonymous, fieldT.Type == reflect.TypeOf(&time.Time{}))
	}
}

func SetNilObj() {
	var is []int
	rv := reflect.ValueOf(&is)
	// n := reflect.New(rv.Type())

	for rv.Kind() == reflect.Ptr {
		fmt.Printf("CanAddr: %t, CanSet: %t\n", rv.CanAddr(), rv.CanSet())
		rv = rv.Elem()
	}
	fmt.Printf("CanAddr: %t, CanSet: %t\n", rv.CanAddr(), rv.CanSet())
	if rv.CanSet() {
		v := []int{1, 2, 3}
		rv.Set(reflect.ValueOf(&v).Elem())
	}

	var i *int
	rv = reflect.ValueOf(&i)
	for rv.Kind() == reflect.Ptr {
		fmt.Printf("CanAddr: %t, CanSet: %t\n", rv.CanAddr(), rv.CanSet())
		if rv.CanSet() {
			v := 10
			rv.Set(reflect.ValueOf(&v))
		}
		rv = rv.Elem()
	}
	fmt.Printf("CanAddr: %t, CanSet: %t\n", rv.CanAddr(), rv.CanSet())

}

func JudgeTypeEqual() {
	var a int

	rt1 := reflect.TypeOf(a)
	rt2 := reflect.TypeOf(&a)

	fmt.Printf("rt1 == rt2: %t\n", rt1 == rt2)
	fmt.Printf("%t\n", reflect.ValueOf(nil).Kind() == reflect.Invalid)
}

type Child struct {
}

type DemoStruct struct {
	Int         int
	Str         string
	Bool        bool
	Slice       []int
	Array       [10]int
	Map         map[int]int
	Struct      Child
	StructSlice []Child
}

func StructField() {
	rt := reflect.TypeOf(DemoStruct{})

	for i := 0; i < rt.NumField(); i++ {
		sf := rt.Field(i)
		fmt.Println(sf.Name, sf.Index)
	}

	rt = reflect.TypeOf([]DemoStruct{})

	for i := 0; i < rt.NumField(); i++ {
		sf := rt.Field(i)
		fmt.Println(sf.Name, sf.Index)
	}
}
