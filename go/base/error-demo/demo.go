package errordemo

import "fmt"

func Demo() {
	e1 := fmt.Errorf("this is error one. ")
	e2 := fmt.Errorf("this is error two. %w", e1)
	e3 := fmt.Errorf("this is error three. %w", e2)

	fmt.Printf("e3: %v\n", e3)
}
