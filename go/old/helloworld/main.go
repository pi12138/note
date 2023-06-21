package main

import (
	"calculator2"
	"fmt"
	"os"
	"strconv"

	"calculator"
)

func main() {
	count := sum(os.Args[1], os.Args[2])
	fmt.Println(os.Args[0], count)

	str1 := "hello"
	fmt.Println(str1)
	str1 = swap(&str1)
	fmt.Println(str1)

	count = calculator.Sum(4, 5)
	fmt.Println(count, calculator.Version)
	count = calculator2.Sum(10, 20)
	fmt.Println(count, calculator2.Version)

}

func sum(number1 string, number2 string) int {
	number1_int, _ := strconv.Atoi(number1)
	number2_int, _ := strconv.Atoi(number2)
	return number1_int + number2_int
}

func swap(str1 *string) string {
	*str1 = "world"
	return *str1
}
