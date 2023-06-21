package struct_demo

import "fmt"

type Base struct {
	Id   uint
	Name string
}

type BaseTwo struct {
	Age    uint
	Height uint
}

type SubClass struct {
	Base
	BaseTwo  BaseTwo
	ExtraStr string
	ExtraInt int
}

// 结构体组合
func StructCombination() {
	b := Base{
		Id:   1,
		Name: "base 1",
	}

	var sc SubClass
	sc.Base = b

	fmt.Printf("sc id: %d, name: %s\n", sc.Id, sc.Name)

}
