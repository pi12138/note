package main

import (
	"encoding/json"
	"fmt"
	"net/http"

	goSet "github.com/deckarep/golang-set/v2"
)

var INTDEFAULT int
var ANYDEFAULT any

type ResponseData struct {
	data    any
	code    int
	headers map[string]string
}

func (res *ResponseData) String() string {
	ret := fmt.Sprintf("data: %T, code: %d, headers: %T", res.data, res.code, res.headers)
	return ret
}

type TestList struct {
	Data int `json:"data"`
}

func main() {
	dict := make(map[int]int)

	dict[1] = 1
	dict[2] = 2

	delete(dict, 3)

	value1, ok := dict[1]
	fmt.Println(value1, ok)

	value4, ok := dict[4]
	fmt.Println(value4, ok)

	array := [3]int{1, 2, 3}
	var slice []int

	fmt.Printf("%T\n", array)
	fmt.Printf("%T\n", slice)

	setOne := goSet.NewSet[int]()
	setTwo := goSet.NewSet[int]()
	setOne.Add(1)
	setOne.Add(2)
	setOne.Add(3)
	setTwo.Add(1)
	setTwo.Add(2)
	setTwo.Add(4)

	fmt.Println(setOne.Difference(setTwo))
	fmt.Println(setTwo.Difference(setOne))
	fmt.Println(goSet.NewSet[int]())
	con := goSet.NewSet[int]()
	if con.Cardinality() == 0 {
		println("false")
	} else {
		println("true")
	}

	if len(slice) == 0 {
		println("false")
	} else {
		println("true")
	}

	var responseData ResponseData
	println(responseData.data, responseData.code, responseData.headers)
	println(responseData.code == INTDEFAULT, responseData.data == ANYDEFAULT, responseData.headers == nil)
	fmt.Printf("responseData: %v， responseData String: %s\n", responseData, responseData.String())

	var headers map[string]string
	str1 := "{\"content-type\": \"json\"}"
	json.Unmarshal([]byte(str1), &headers)
	for key, value := range headers {
		println(key, value)
	}
	for key := range headers {
		println(key)
	}

	resp, _ := http.Get("http://www.baidu.com")
	for k, v := range resp.Header {
		println(k)
		for _, vv := range v {
			println("\t", vv)
		}
	}

	var testList1 []TestList
	testList2 := make([]TestList, 0)
	testList3 := []TestList{}
	fmt.Println("testList1: ", testList1, "testList2: ", testList2, "testList3: ", testList3)
	fmt.Println(testList1 == nil, testList2 == nil, testList3 == nil)
	data1, _ := json.Marshal(testList1)
	data2, _ := json.Marshal(testList2)
	data3, _ := json.Marshal(testList3)
	fmt.Println("json dump data: ", string(data1), string(data2), string(data3))

	UpdateMap()
	TestRet()
}

func printSlice() {
	l1 := make([]int, 0)
	l1 = append(l1, 1)
	l1 = append(l1, 2)
	l1 = append(l1, 3)
	fmt.Printf("a")
}

type TestMap struct {
	name string
	age  int
}

func UpdateMap() {
	map1 := make(map[int]TestMap)
	var testMap1 TestMap
	testMap1.name = "one"
	testMap1.age = 1
	map1[1] = testMap1

	a := map1[1]
	b := map1[1]

	fmt.Printf("before update a: %p, b: %p, testMap1: %p\n", &a, &b, &testMap1)
	testMap1.name = "one-one"
	fmt.Printf("after update a: %p, b: %p, testMap1: %p\n", &a, &b, &testMap1)

	map2 := make(map[int]*TestMap)
	var testMap2 TestMap
	testMap2.name = "two"
	testMap2.age = 2
	map2[2] = &testMap2

	fmt.Printf("before update map2: %v, testMap2: %p\n", map2, &testMap2)
	testMap2.name = "two-two"
	fmt.Printf("after update map2: %v, testMap2: %p\n", map2, &testMap2)
}

func TestRet() bool {
	return true
	return false
}
