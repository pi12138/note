package main

import (
	"encoding/json"
	"flag"
	"fmt"
	"io/ioutil"
)

var (
	file string
)

func init() {
	flag.StringVar(&file, "f", "", "filename")
}

func main() {
	flag.Parse()
	// if file == "" {
	// 	fmt.Printf("-f file\n")
	// 	return
	// }
	data, err := ioutil.ReadFile(file)
	if err != nil {
		fmt.Printf("ReadFile error. %s\n", err)
		return
	}

	if json.Valid(data) {
		return
	} else {
		fmt.Printf("%s json format wrong.\n", file)
		fmt.Printf("%s\n", string(data))
		return
	}
}
