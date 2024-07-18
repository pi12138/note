package filedemo

import (
	"fmt"
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

func Stat() {
	FileInfo, err := os.Stat("/opt")
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	fmt.Println(FileInfo.Name(), FileInfo.IsDir(), FileInfo.Mode())
	fmt.Printf("%T %b %b\n", FileInfo.Mode().IsRegular(), FileInfo.Mode().Perm(), FileInfo.Mode().Type())
	fmt.Printf("%d\n", FileInfo.Mode())

	fmt.Printf("%d %d %d\n", 0756&0200, 0756&02, 0756&020)
}
