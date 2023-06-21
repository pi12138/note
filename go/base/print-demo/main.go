package main

import (
	"fmt"
	"io"
	"os"
	"strconv"
)

func main() {
	a := 10
	b := "hello world"
	Print(a, b, "\n")
	fmt.Print()
}

func Print(args ...any) {
	for i, v := range args {
		if i > 0 {
			os.Stdout.WriteString(" ")
		}
		switch vv := v.(type) {
		case string:
			os.Stdout.WriteString(vv)
		case int:
			os.Stdout.WriteString(strconv.Itoa(vv))
		default:
			os.Stdout.WriteString("")
		}
	}
	io.EOF
}
