package main

import (
	filedemo "base/file-demo"
	"fmt"
)

func main() {
	// struct_demo.Demo()
	// map_and_slice.MapUpdate()
	// type_assertion_demo.Demo()
	// json_demo.ParseToPointer()
	// time_demo.FormatTime()
	// struct_demo.StructCombination()
	// netip_demo.ParseIp()
	// template_demo.TemplateDemo()
	// // reflection.TestAssignableTo()
	// // reflection.TestNilValue()
	// reflection.IsAnonymous()
	// reflection.SetNilObj()
	// TestVarInit()
	// var a *int
	// fmt.Printf("a: %v\n", *a)
	// TestMapDefaultValue()
	// reflection.JudgeTypeEqual()
	// errordemo.Demo()
	// logdemo.Infof("info")
	// reflection.StructField()

	// runtime.GOMAXPROCS(2)
	// filedemo.Demo()

	// thread_safe_demo.Demo()
	// thread_safe_demo.LockDemo()

	// runtimedemo.Callers()
	// contextdemo.Demo()
	// forrangedemo.RangePonit()
	// forrangedemo.RangeUint()
	// goroutinesdemo.WriteRemoteFile()
	// goroutinesdemo.WriteLocalFile()
	// map_and_slice.CompareEqualAndDeepEqual()
	// packagedemo.Exec()
	// filepath.Demo()
	filedemo.Stat()
}

func TestVarInit() {
	var a int
	a = 10

	var b any
	if a == 10 {
		a, ok := b.(int)
		if ok {
			fmt.Printf("line 38 a: %d\n", a)
		} else {
			fmt.Printf("line 40 a: %d\n", a)
		}
		a = 100
		fmt.Printf("line 43 a: %d\n", a)
	}
	fmt.Printf("line 45 a: %d\n", a)
}

// map[key]value
// map 取值, key 不存在时返回 value 的默认值
// nil map 可以取值，但是不能赋值
// nil slice 和 nil map 可以 range 的，不会抛出异常
// nil slice 和 nil map 可以使用 len 获取长度，返回 0
func TestMapDefaultValue() {
	a := make(map[string]int)
	b := make(map[string]map[string]int)
	av := a["hello"]
	bv := b["hello"]
	bvv := bv["world"]
	fmt.Printf("av: %d, bv: %v, bv == nil: %v, bvv: %v\n", av, bv, bv == nil, bvv)

	var c map[string]int
	cv := c["hellow"]
	fmt.Printf("cv: %v \n", cv)
	// c["hello"] = 10  // > panic

	for k, v := range c {
		fmt.Println(k, v)
	}
	var d []string
	for i, v := range d {
		fmt.Println(i, v)
	}

	fmt.Printf("len c: %d, len d: %d\n", len(c), len(d))
}
