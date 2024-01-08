package goroutinesdemo

import (
	"context"
	"fmt"
	"net/http"
	"runtime"
	"time"
)

func ExitGoroutine() {
	runtime.GOMAXPROCS(1)
	var v int = 10
	ctx, cancel := context.WithCancel(context.TODO())
	c := make(chan struct{})

	go GoOne(&v)
	go GoTwo(ctx)
	go GoThree(c)

	time.Sleep(time.Second * 4)
	s1 := time.Now()
	v = 0
	s2 := time.Now()
	cancel()
	s3 := time.Now()
	c <- struct{}{}
	s4 := time.Now()

	time.Sleep(time.Second * 5)
	fmt.Printf("s2 - s1: %s\ns3 - s2: %s\ns4 - s3: %s\n", s2.Sub(s1), s3.Sub(s2), s4.Sub(s3))
}

func Request() {
	if _, err := http.Get("http://localhost:8080/sleep?sleep=3"); err != nil {
		fmt.Printf("error: %s\n", err)
	}
}

func GoOne(v *int) {
	defer func(start time.Time) {
		fmt.Printf("GoOne cost: %s\n", time.Since(start))
	}(time.Now())

	for {
		if *v == 0 {
			return
		}

		// do work
		// time.Sleep(time.Second * 3)
		Request()
	}

}

func GoTwo(ctx context.Context) {
	defer func(start time.Time) {
		fmt.Printf("GoTwo cost: %s\n", time.Since(start))
	}(time.Now())

	for {
		select {
		case <-ctx.Done():
			return
		default:
			// time.Sleep(time.Second * 3)
			Request()
		}
	}
}

func GoThree(c chan struct{}) {
	defer func(start time.Time) {
		fmt.Printf("GoThree cost: %s\n", time.Since(start))
	}(time.Now())

	for {
		select {
		case <-c:
			return
		default:
			// time.Sleep(time.Second * 3)
			Request()
		}
	}

}
