package goroutinesdemo

import (
	"fmt"
	"runtime"
	"sync"
	"time"
)

var lock sync.Mutex
var runFuncName = []string{}

func record(v string) {
	runFuncName = append(runFuncName, v+time.Now().Format(time.RFC3339Nano))
}

// LockSwitch 用来测试加锁是否会进行 goroutine 的切换
func LockSwitch() {
	runtime.GOMAXPROCS(1)

	var wg sync.WaitGroup
	wg.Add(3)
	go func() {
		defer wg.Done()
		a()
	}()
	go func() {
		defer wg.Done()
		b()
	}()
	go func() {
		defer wg.Done()
		c()
	}()
	wg.Wait()
	for _, i := range runFuncName {
		fmt.Println(i)
	}
}

func a() {
	record("start a")
	lock.Lock()
	time.Sleep(5 * time.Second)
	lock.Unlock()
	record("end a")
}

func b() {
	record("start b")
	lock.Lock()
	time.Sleep(3 * time.Second)
	lock.Unlock()
	record("end b")
}

func c() {
	record("start c")
	time.Sleep(1 * time.Second)
	record("end c")
}
