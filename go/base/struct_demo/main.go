package struct_demo

import (
	"fmt"
	"reflect"

	"github.com/fatih/structs"
)

func Demo() {
	// Receive()
	// ToJsonMap()
	ParseSubStruct()
}

type Sub struct {
	Name string `json:"name"`
	Age  int    `json:"age"`
}

type Foo struct {
	Name     string `json:"name"`
	SubOne   Sub    `json:"sub_one"`
	SubTwo   []Sub  `json:"sub_two"`
	SubThree []*Sub `json:"sub_three"`
}

func (r *Foo) SetName(s string) {
	r.Name = s
}

func (r Foo) GetName() string {
	return r.Name
}

// 实现了接收者是值类型的方法，相当于自动实现了接收者是指针类型的方法；而实现了接收者是指针类型的方法，不会自动生成对应接收者是值类型的方法。
// 如果实现了接收者是值类型的方法，会隐含地也实现了接收者是指针类型的方法。
func Receive() {
	f1 := Foo{}
	f2 := &Foo{Name: "foo2"}
	fmt.Printf("f1.name: %s, f2.name: %s\n", f1.GetName(), f2.GetName())
	f1.SetName("foo1")
	f1.GetName()
	f2.GetName()
	f2.SetName("f2")
	fmt.Printf("f1.name: %s, f2.name: %s\n", f1.GetName(), f2.GetName())

	t1 := reflect.TypeOf(f1)
	t2 := reflect.TypeOf(f2)
	t2e := t2.Elem()

	fmt.Println(t1.NumMethod(), t2.NumMethod(), t2e.NumMethod())
	t1MethodNames := []string{}
	t2MethodNames := []string{}
	t2eMethodNames := []string{}
	for i := 0; i < t1.NumMethod(); i++ {
		t1MethodNames = append(t1MethodNames, t1.Method(i).Name)
	}
	for i := 0; i < t2.NumMethod(); i++ {
		t2MethodNames = append(t2MethodNames, t2.Method(i).Name)
	}
	for i := 0; i < t2e.NumMethod(); i++ {
		t2eMethodNames = append(t2eMethodNames, t2e.Method(i).Name)
	}
	fmt.Println(t1MethodNames, t2MethodNames, t2eMethodNames)
}

func ToJsonMap() {
	sub1 := Sub{
		Name: "one",
		Age:  1,
	}
	sub2 := Sub{
		Name: "two",
		Age:  2,
	}
	sub3 := Sub{
		Name: "three",
		Age:  3,
	}
	foo1 := Foo{
		Name:     "foo1",
		SubOne:   sub1,
		SubTwo:   []Sub{sub1, sub2},
		SubThree: []*Sub{&sub1, &sub2, &sub3},
	}

	s := structs.New(foo1)
	s.TagName = "json"
	fmt.Println(s.Map())
}

func ParseSubStruct() {
	sub1 := Sub{
		Name: "one",
		Age:  1,
	}
	sub2 := Sub{
		Name: "two",
		Age:  2,
	}
	sub3 := Sub{
		Name: "three",
		Age:  3,
	}
	foo1 := Foo{
		Name:     "foo1",
		SubOne:   sub1,
		SubTwo:   []Sub{sub1, sub2},
		SubThree: []*Sub{&sub1, &sub2, &sub3},
	}

	v := reflect.ValueOf(&foo1)
	for v.Kind() == reflect.Pointer {
		v = v.Elem()
	}

	sv1 := v.FieldByName("SubOne")
	sv2 := v.FieldByName("SubTwo")

	fmt.Println(sv1.Kind(), sv2.Kind())
	fmt.Println(sv1.Interface())

	if sv1.Kind() == reflect.Struct {

		for i := 0; i < sv1.NumField(); i++ {
			fmt.Println(sv1.Type().Field(i).Name, sv1.Field(i).Interface())
		}
		fmt.Println(sv1.FieldByName("Name").Interface())
	}

	var a *int
	var aa = new(int)
	fmt.Println(a, aa)
}
