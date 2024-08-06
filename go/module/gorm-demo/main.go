package main

import (
	"encoding/json"
	C "gorm-demo/clear"
	"gorm-demo/db"
	"gorm-demo/insert"
	M "gorm-demo/models"
	S "gorm-demo/select_"
	"log"
	"os"
)

func Demo() {
	// TestJson()
	// TestSlice()
	// TestOrm()
	// TestUpdate()
	// TestDel()
}

func TestJson() {
	var a = map[string]int{}
	var b = &map[string]int{}

	var str = "{\"a\": 10}"

	json.Unmarshal([]byte(str), &a)
	json.Unmarshal([]byte(str), b)

	log.Printf("a: %v, b: %v", &a, *b)
	// log.Printf("value: %v, %v", a["a"], b["a"])

	var j = map[string]any{}
	j["a"] = 1
	j["b"] = "B"
	j["c"] = []int{1, 2, 3}
	j["d"] = []string{"hello", "world"}
	j["e"] = map[string]any{
		"a": 1,
		"b": "B",
	}
	j["f"] = map[int]any{
		1: 1,
	}

	data, err := json.Marshal(j)
	if err != nil {
		log.Printf("err: %s", err)
	}
	log.Printf("json data: %s", data)
}

func TestSlice() {
	// var s []string
	s := make([]string, 1)
	log.Printf("s value: %v, address: %p, s == nil: %v", s, &s, s == nil)
	SliceArgs(s)
	log.Printf("s value: %v, address: %p, s == nil: %v", s, s, s == nil)
}

func SliceArgs(s []string) {
	log.Printf("s value: %v, address: %p, s == nil: %v", s, &s, s == nil)
	// s = append(s, "a")
	s[0] = "a"
	log.Printf("s value: %v, address: %p, s == nil: %v", s, s, s == nil)
}

func main() {

	db.GetDB()

	args := os.Args
	// fmt.Println(args)
	switch args[1] {
	case "select":
		select_()
	case "migrate":
		migrate()
	case "create":
		create()
	case "clear":
		clear()
	case "demo":
		Demo()
	}
}

func migrate() {
	db := db.GetDB()
	db.AutoMigrate(&M.User{}, &M.CreditCard{}, &M.Author{}, &M.Blog{})
}

func create() {
	insert.Demo()
}

func select_() {
	S.Demo()
}

func clear() {
	C.ClearData()
}
