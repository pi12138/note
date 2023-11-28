package panicdemo

import (
	"fmt"
	"runtime"

	"github.com/pkg/errors"
)

func getStack() string {
	// var buf []byte
	var buf = make([]byte, 4096)
	n := runtime.Stack(buf, false)
	return string(buf[:n])
}

func HandlePanic() {
	defer func() {
		if r := recover(); r != nil {
			fmt.Println(errors.WithStack(fmt.Errorf("%v", r)))
			// debug.PrintStack()

			fmt.Println(getStack())
		}
	}()

	panic("do panic")
	fmt.Println("do panic after")
}
