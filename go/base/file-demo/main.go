package filedemo

import (
	"io/ioutil"
	"os"
	"sync"
	"time"
)

var lock sync.Mutex

func Demo() {
	// file, err := os.OpenFile("test.txt", os.O_CREATE|os.O_WRONLY, 0666)
	// if err != nil {
	// 	panic(err)
	// }
	// defer file.Close()

	for i := 0; i < 10000; i++ {
		go ioutil.WriteFile("test.txt", []byte("111\n"), 0666)
		go ioutil.WriteFile("test.txt", []byte("222\n"), 0666)
		// go WriteFile(file, "111\n")
		// go WriteFile(file, "222\n")
	}
	time.Sleep(10 * time.Second)
}

func WriteFile(f *os.File, c string) {
	// lock.Lock()
	// defer lock.Unlock()
	f.WriteString(c)
}
