package netip_demo

import (
	"fmt"
	"net/netip"
)

func ParseIp() {
	v4, _ := netip.ParseAddr("192.168.1.1")
	v6, _ := netip.ParseAddr("fe80::7696:af0d:2037:1385")

	if v4.IsValid() && v6.IsValid() {
		fmt.Println(v4, v6)
	}
}
