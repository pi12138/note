package slicedemo

import "fmt"

func Append() {
	slice1 := make([]int, 0, 30)

	fmt.Printf("slice1 addr: %p\n", slice1)
	for i := 0; i < 50; i++ {
		slice1 = append(slice1, i)
		fmt.Printf("i: %d, slice1 addr: %p, slice1 lens: %d, slice1 caps: %d\n", i, slice1, len(slice1), cap(slice1))
	}
}
