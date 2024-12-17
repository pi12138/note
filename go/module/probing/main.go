package main

import (
	"fmt"

	probing "github.com/prometheus-community/pro-bing"
)

func main() {
	conn, err := probing.NewPinger("2001:0:0:10::253")

	if err != nil {
		fmt.Println("error:", err)
		return
	}
	fmt.Println("conn:", conn)
}
