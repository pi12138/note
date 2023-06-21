package main

import (
	"fmt"
	"net"
)

func IntToIp(ip int64) string {
	return fmt.Sprintf("%d.%d.%d.%d", byte(ip>>24), byte(ip>>16), byte(ip>>8), byte(ip))
}

func main() {
	a := 255
	aIp := IntToIp(int64(a))
	fmt.Printf("ip: %s\n", aIp)
	fmt.Printf("v: %v, len: %d, 0: %v\n", net.ParseIP("127.0.0.1"), len(net.ParseIP("127.0.0.1")), net.ParseIP("127.0.0.1")[0])
}
