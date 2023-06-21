package thread_safe_demo

import (
	"fmt"
	"sync"
	"time"
)

func Demo() {
	var c int

	for i := 0; i < 100000; i++ {
		go func() {
			c += 1
		}()
	}
	time.Sleep(2 * time.Second)

	fmt.Printf("c: %d\n", c)
}

var lock sync.Mutex

func LockDemo() {
	var c int

	for i := 0; i < 100000; i++ {
		go func() {
			lock.Lock()
			defer lock.Unlock()
			c += 1
		}()
	}
	time.Sleep(2 * time.Second)

	fmt.Printf("c: %d\n", c)
}

func ChannelDemo() {
	var c int

	for i := 0; i < 10000; i++ {
		go func() {
			lock.Lock()
			defer lock.Unlock()
			c += 1
		}()
	}
	time.Sleep(2 * time.Second)

	fmt.Printf("c: %d\n", c)
}
