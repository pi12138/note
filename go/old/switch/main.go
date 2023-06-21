package main

import (
	"fmt"
	"math/rand"
	"regexp"
	"time"
)

func location(city string) (string, string) {
	var country, continent string

	switch city {
	case "xingyang", "nanyang", "zhoukou":
		country, continent = "zhongguo", "henan"
	case "hangzhou", "shaoxing":
		country, continent = "zhongguo", "zhejiang"
	default:
		country, continent = "", ""
	}
	return country, continent
}

func printNum() {
	sec := time.Now().Unix()
	rand.Seed(sec)

	i := rand.Int31n(10)
	fmt.Println(i)

	switch i {
	case 0:
		fmt.Println("zero")
	case 1:
		fmt.Println("one")

	case 2:
		fmt.Println("two")
	default:
		fmt.Println("default")
	}

	fmt.Println("ok")
}

func weekday() {
	switch time.Now().Weekday().String() {
	case "Monday", "Tuesday", "Wednesday", "Thursday", "Friday":
		fmt.Println("it's weekday")
	default:
		fmt.Println("it's weekend")
	}
}

func re() {
	var email = regexp.MustCompile(`^[^@]+@[^@.]+\.[^@.]+`)
	var phoneNumber = regexp.MustCompile(`^[(]?[0-9][0-9][0-9][). \-]*[0-9][0-9][0-9][.\-]?[0-9][0-9][0-9][0-9]`)
	var str1 = "foo@bar.com"

	switch {
	case email.MatchString(str1):
		fmt.Println("email")
	case phoneNumber.MatchString(str1):
		fmt.Println("phone")
	default:
		fmt.Println("not email and phone")
	}
}

func main() {
	printNum()
	fmt.Println(location("xingyang"))
	weekday()
	re()
}
