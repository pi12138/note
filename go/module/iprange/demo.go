package main

import (
	"fmt"
	"net/netip"
)

// func RangeIp() {
// 	start := net.IP([]byte("10.1.1.0"))
// 	end := net.IP([]byte("10.1.1.10"))

// 	ran := iprange.New(start, end)
// 	fmt.Printf("range: %v %v\n", ran, ran == nil)
// }

func RangeIp() {
	from, err := netip.ParseAddr("10.1.1.0")
	if err != nil {
		fmt.Println("error: ", err)
	}
	to, err := netip.ParseAddr("10.1.2.10")
	if err != nil {
		fmt.Println("error: ", err)
	}
	// ran := netipx.IPRangeFrom(from, to)
	ips := make([]string, 0)
	for from.Compare(to) <= 0 {
		ips = append(ips, from.String())
		from = from.Next()
	}
	fmt.Printf("ips: %v\n", ips)
}
