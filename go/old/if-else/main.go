package main


import "fmt"


func getNumber() int {
	return -1
}


func main() {

	if num := getNumber(); num > 0 {
		fmt.Println(num, "> 0")
	} else if num == 0 {
		fmt.Println(num, "= 0")
	} else {
		fmt.Println(num, "< 0")
	}

}