package main

import (
	"fmt"
	"io"
	"os"
	"time"

	"golang.org/x/crypto/ssh"
)

func main() {
	var addr = os.Args[1]
	var username string = os.Args[2]
	var password string = os.Args[3]
	var config ssh.ClientConfig
	config.User = username
	config.Auth = []ssh.AuthMethod{
		ssh.Password(password),
	}
	config.HostKeyCallback = ssh.InsecureIgnoreHostKey()
	config.Timeout = 5 * time.Second
	cli, err := ssh.Dial("tcp", addr, &config)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	sess, err := cli.NewSession()
	if err != nil {
		fmt.Println(err)
		os.Exit(2)
	}

	in, _ := sess.StdinPipe()
	out, _ := sess.StdoutPipe()
	errOut, _ := sess.StderrPipe()
	var msg []byte
	msg, err = io.ReadAll(out)
	fmt.Printf("[STDOUT] %s, %s\n", msg, err)
	msg, err = io.ReadAll(errOut)
	fmt.Printf("[STDERR] %s, %s\n", msg, err)

	err = sess.Shell()
	if err != nil {
		fmt.Println(err)
		os.Exit(3)
	}
	fmt.Fprintf(in, "cd /opt\n")
	msg, err = io.ReadAll(out)
	fmt.Printf("[STDOUT] %s, %s\n", msg, err)
	msg, err = io.ReadAll(errOut)
	fmt.Printf("[STDERR] %s, %s\n", msg, err)
	fmt.Fprintf(in, "pwd")
	msg, err = io.ReadAll(out)
	fmt.Printf("[STDOUT] %s, %s\n", msg, err)
	msg, err = io.ReadAll(errOut)
	fmt.Printf("[STDERR] %s, %s\n", msg, err)
	fmt.Fprintf(in, "ls\n")
	// time.Sleep(5 * time.Second)
	msg, err = io.ReadAll(out)
	fmt.Printf("[STDOUT] %s, %s\n", msg, err)
	msg, err = io.ReadAll(errOut)
	fmt.Printf("[STDERR] %s, %s\n", msg, err)
}


/* func handleStdout(out io.Reader) {
    v := make([]byte, 1024)
	var number int
	var err error
	fmt.Printf("[STDOUT] ")
	for {
		number, err = out.Read(v)
		if err != nil {
			fmt.Printf("out.Read error. %s\n", err)
		} else {
			if number == 1024 {
				fmt.Printf("%s", string(v))
			} else {
				fmt.Printf("%s\n", string(v))
				time.Sleep(2 * time.Second)
			}
		}
	}
}

func handleStderr(errOut io.Reader) {
    v := make([]byte, 1024)
	var number int
	var err error
	fmt.Printf("[STDERR] ")
	for {
		number, err = errOut.Read(v)
		if err != nil {
			fmt.Printf("errOut.Read error. %s\n", err)
		} else {
			if number == 1024 {
				fmt.Printf("%s", string(v))
			} else {
				fmt.Printf("%s\n", string(v))
				time.Sleep(2 * time.Second)
			}
		}
	}
} */
