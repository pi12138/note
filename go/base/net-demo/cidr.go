package netdemo

import (
	"fmt"
	"net"
)

func Demo() {
	inet1 := "10.1.21.9/24"
	inet2 := "10.1.21.209/24"

	_, ipNet1, _ := net.ParseCIDR(inet1)
	_, ipNet2, _ := net.ParseCIDR(inet2)
	
	fmt.Println(ipNet1 == ipNet2, ipNet1.String() == ipNet2.String())
}
