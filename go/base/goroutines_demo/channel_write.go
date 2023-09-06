package goroutinesdemo

import (
	"context"
	"fmt"
	"io/ioutil"
	"os"
	"os/exec"
	"runtime"
	"time"
)

type Msg struct {
	File string
	Data []byte
}

func WriteFile(ctx context.Context, msg chan Msg) {
	var count int
	for {
		select {
		case <-ctx.Done():
			fmt.Printf("[WriteFile] exit. count: %d\n", count)
			return
		case m := <-msg:
			if err := os.WriteFile(m.File, m.Data, 0666); err != nil {
				fmt.Printf("os.WriteFile error. %s\n", err)
			}
			count++
		}
	}
}

func ChannelWrite() {
	runtime.GOMAXPROCS(1)
	msg := make(chan Msg, 10)
	// var wg sync.WaitGroup
	jData1, err := ioutil.ReadFile("./data1.json")
	file := "/tmp/channel.json"
	if err != nil {
		fmt.Printf("ioutil.ReadFile(\"./data1.json\") error. %s", err)
		return
	}
	jData2, err := ioutil.ReadFile("./data2.json")
	if err != nil {
		fmt.Printf("ioutil.ReadFile(\"./data2.json\") error. %s", err)
		return
	}
	ctx, cancel := context.WithCancel(context.Background())
	go func(ctx context.Context, msg chan Msg) {
		// defer wg.Done()
		WriteFile(ctx, msg)
	}(ctx, msg)

	for i := 0; i < 100; i++ {
		msg <- Msg{
			File: file,
			Data: jData1,
		}
		msg <- Msg{
			File: file,
			Data: jData2,
		}
	}

	time.Sleep(2 * time.Second)
	cancel()
	cmd := exec.Command("/opt/tools/jsoncheck", "-f", file)
	output, err := cmd.Output()
	if err != nil {
		fmt.Printf("命令执行出错: %s\n", err)
		return
	} else {
		fmt.Printf("file: %s\n%s\n", file, (output))
	}
}
