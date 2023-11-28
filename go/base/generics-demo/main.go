package main

import "log"

type StructA struct {
	Name string
}

type StructB struct {
	Name string
}

type StructInterface interface {
	PrintName()
}

func PrintName(v StructInterface) {
	log.Panicf("name: %s", v.PrintName())
}

func main() {
	var a StructA
	a.Name = "StructA"
	i := StructInterface{}

	log.Printf("a: %v", a)
}
