package main

import (
	"fmt"
	"net/http"
	"runtime"
	"time"
)

type Ret struct {
	Err       error
	Code      int
	IsSuccess bool
}

func main() {
	TestChanOneP()
}

func TestChanOneP() {
	runtime.GOMAXPROCS(1)

	ch := make(chan int)

	go func() {
		for i := 0; i < 10; i++ {
			ch <- i
		}
	}()
	go func() {
		for i := 0; i < 10; i++ {
			i := <-ch
			fmt.Println(i)
		}

	}()

	time.Sleep(3 * time.Second)
}

func Test() {

	length := 10
	ch := make(chan Ret)
	for i := 0; i < length; i++ {
		go func(c chan Ret) {
			resp, err := http.Get("http://www.baidu.com")
			if err != nil {
				ch <- Ret{
					Err: err,
				}
				return
			}
			if resp.StatusCode != 200 {
				ch <- Ret{
					Err:  fmt.Errorf("code != 200"),
					Code: resp.StatusCode,
				}
				return
			}
			ch <- Ret{
				Code:      resp.StatusCode,
				IsSuccess: true,
			}
		}(ch)
	}

	for c := range ch {
		fmt.Println(c)
		length--
		if length == 0 {
			close(ch)
		}
	}
	// close(ch)
}
