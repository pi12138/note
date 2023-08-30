package goroutinesdemo

import (
	"base/common/clog"
	"base/common/cssh"
	"fmt"
	"io/ioutil"
	"os/exec"
	"runtime"
	"sync"
)

func Demo() {
	runtime.GOMAXPROCS(1)
	wg := sync.WaitGroup{}
	wg.Add(20)
	for i := 0; i < 10; i++ {
		go func(i int) {
			fmt.Println("A", i)
			wg.Done()
		}(i)
	}
	for i := 0; i < 10; i++ {
		go func(i int) {
			fmt.Println("B", i)
			wg.Done()
		}(i)
	}

	wg.Wait()
}

/*
	无论写本地文件还是远程文件，多协程的情况下均会出现文件异常问题
*/

func WriteRemoteFile() {
	runtime.GOMAXPROCS(1)

	wg := sync.WaitGroup{}
	var ip string = "10.1.9.2"
	var username string = "root"
	var password string = "jcwl@123"
	var dumpFilePath string = "/tmp/remote.txt"
	jData1, err := ioutil.ReadFile("./goroutines_demo/data1.json")
	if err != nil {
		fmt.Printf("ioutil.ReadFile(\"./goroutines_demo/data1.json\") error. %s", err)
		return
	}
	jData2, err := ioutil.ReadFile("./goroutines_demo/data2.json")
	if err != nil {
		fmt.Printf("ioutil.ReadFile(\"./goroutines_demo/data2.json\") error. %s", err)
		return
	}
	// jData1, _ := json.Marshal(data1)
	// jData2, _ := json.Marshal(data2)
	for i := 0; i < 500; i++ {
		wg.Add(2)
		go func() {
			defer wg.Done()
			cli, err := cssh.NewClient(ip, username, password)
			if err != nil {
				clog.Errorf("[DumpFileForLua] cssh.NewClient error. %s, %s@%s", err, username, ip)
				return
			}
			cli.PutFileData(dumpFilePath, jData1)
			cli.Close()
		}()
		go func() {
			defer wg.Done()
			cli, err := cssh.NewClient(ip, username, password)
			if err != nil {
				clog.Errorf("[DumpFileForLua] cssh.NewClient error. %s, %s@%s", err, username, ip)
				return
			}
			cli.PutFileData(dumpFilePath, jData2)
			cli.Close()
		}()
	}

	wg.Wait()

	// cmd := exec.Command("/opt/tools/jsoncheck", "-f", dumpFilePath)
	cmd := exec.Command("ssh", "root@10.1.9.2", "/root/tools/jsoncheck -f /tmp/remote.txt")
	output, err := cmd.Output()
	if err != nil {
		fmt.Printf("命令执行出错: %s\n", err)
		return
	}
	fmt.Printf("file: %s\n%s\n", dumpFilePath, (output))
}

func WriteLocalFile() {
	runtime.GOMAXPROCS(1)
	wg := sync.WaitGroup{}
	// var ip string = "10.1.9.2"
	// var username string = "root"
	// var password string = "jcwl@123"
	var dumpFilePath string = "/tmp/local.txt"
	// var data1 = map[string]map[string]string{"1": {"1": "critical", "2": "critical"}, "10": {"28": "critical"}, "11": {"29": "critical"}, "12": {"30": "critical", "31": "critical"}, "13": {"32": "critical", "33": "critical"}, "14": {"34": "critical", "35": "critical", "36": "critical", "37": "critical", "38": "critical"}, "15": {"39": "critical"}, "16": {"40": "health"}, "17": {"41": "health"}, "18": {"42": "health"}, "19": {"43": "health"}, "2": {"14": "critical", "15": "critical"}, "20": {"44": "health"}, "21": {"45": "health"}, "22": {"46": "health"}, "23": {"47": "health", "48": "health"}, "24": {"49": "health"}, "25": {"50": "health"}, "26": {"51": "health"}, "3": {"5": "critical"}, "4": {"6": "critical"}, "5": {"7": "critical", "8": "critical"}, "6": {"10": "critical"}, "7": {"16": "critical", "17": "critical"}, "8": {"18": "critical", "19": "critical", "20": "critical", "21": "critical"}, "9": {"22": "critical", "23": "critical", "24": "critical", "25": "critical", "26": "critical", "27": "critical"}}
	// var data2 = map[string]map[string]string{"1": {"1": "critical", "2": "critical"}, "10": {"28": "critical"}, "11": {"29": "critical"}, "12": {"30": "critical", "31": "critical"}, "13": {"32": "critical", "33": "critical"}, "14": {"34": "critical", "35": "critical", "36": "critical", "37": "critical", "38": "critical"}, "15": {"39": "critical"}, "16": {"40": "health"}, "17": {"41": "health"}, "18": {"42": "health"}, "19": {"43": "health"}, "2": {"14": "critical", "15": "critical"}, "20": {"44": "health"}, "21": {"45": "health"}, "22": {"46": "health"}, "23": {"47": "health", "48": "health"}, "24": {"49": "health"}, "25": {"50": "health"}, "26": {"51": "critical"}, "3": {"5": "critical"}, "4": {"6": "critical"}, "5": {"7": "critical", "8": "critical"}, "6": {"10": "critical"}, "7": {"16": "critical", "17": "critical"}, "8": {"18": "critical", "19": "critical", "20": "critical", "21": "critical"}, "9": {"22": "critical", "23": "critical", "24": "critical", "25": "critical", "26": "critical", "27": "critical"}}
	// jData1, _ := ioutil.ReadFile("./goroutines_demo/data1.json")
	// jData2, _ := ioutil.ReadFile("./goroutines_demo/data2.json")
	// jData1, _ := json.Marshal(data1)
	// jData2, _ := json.Marshal(data2)
	jData1, err := ioutil.ReadFile("./goroutines_demo/data1.json")
	if err != nil {
		fmt.Printf("ioutil.ReadFile(\"./goroutines_demo/data1.json\") error. %s", err)
		return
	}
	jData2, err := ioutil.ReadFile("./goroutines_demo/data2.json")
	if err != nil {
		fmt.Printf("ioutil.ReadFile(\"./goroutines_demo/data2.json\") error. %s", err)
		return
	}
	for i := 0; i < 500; i++ {
		wg.Add(2)
		go func() {
			defer wg.Done()
			ioutil.WriteFile(dumpFilePath, jData1, 0666)
		}()
		go func() {
			defer wg.Done()
			ioutil.WriteFile(dumpFilePath, jData2, 0666)
		}()
	}
	wg.Wait()
	cmd := exec.Command("/opt/tools/jsoncheck", "-f", dumpFilePath)
	output, err := cmd.Output()
	if err != nil {
		fmt.Printf("命令执行出错: %s\n", err)
		return
	}
	fmt.Printf("file: %s\n%s\n", dumpFilePath, (output))
}
