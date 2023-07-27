package main

import (
	"bytes"
	"fmt"
	"log"
	"net/http"
	"os"
	"strconv"
	"strings"
	"time"
)

var file *os.File
var logger *log.Logger
var line uint
var maxLine uint = 100000

func init() {
	var err error
	file, err = os.OpenFile("helloworld.log", os.O_CREATE|os.O_APPEND|os.O_WRONLY, 0666)
	if err != nil {
		panic(err)
	}
	logger = log.New(file, "[INFO] ", log.LstdFlags)
}

func logInfo(format string, v ...any) {
	if line > maxLine {
		if err := file.Truncate(0); err != nil {
			panic(err)
		}
		line = 0
	}
	logger.Printf(format, v...)
	line++
}

func indexHandler(w http.ResponseWriter, r *http.Request) {
	logInfo("indexHandler")
	w.Write([]byte("index"))
}

func HelloWorldHandler(w http.ResponseWriter, r *http.Request) {
	logInfo("HelloWorldHandler")
	w.Write([]byte("helloworld"))
}

func NotFoundHandler(w http.ResponseWriter, r *http.Request) {
	logInfo("NotFoundHandler")
	w.WriteHeader(404)
	w.Write([]byte("not found"))
}

func Body(w http.ResponseWriter, r *http.Request) {
	defer func(start time.Time) {
		log.Printf("[body] cost: %s", time.Since(start))
	}(time.Now())
	Q := r.URL.Query()
	data := Q.Get("data")
	if data == "" {
		w.WriteHeader(400)
		w.Write([]byte("required data."))
		return
	}

	number := data[0 : len(data)-1]
	unit := string(data[len(data)-1])

	Number, err := strconv.ParseUint(number, 10, 64)
	if err != nil {
		w.WriteHeader(400)
		w.Write([]byte(fmt.Sprintf("error: %s", err)))
		return
	}

	_1B := 1
	_1KB := 1024 * _1B
	_1MB := 1024 * _1KB
	_1GB := 1024 * _1MB

	var builder bytes.Buffer

	switch strings.ToUpper(unit) {
	case "K":
		chunk := strings.Repeat("*", _1KB)
		for i := 0; i < (int(Number)*_1KB)/_1KB; i++ {
			builder.WriteString(chunk)
		}
	case "M":
		chunk := strings.Repeat("*", _1MB)
		for i := 0; i < (int(Number)*_1MB)/_1MB; i++ {
			builder.WriteString(chunk)
		}
	case "G":
		chunk := strings.Repeat("*", _1MB)
		for i := 0; i < (int(Number)*_1GB)/_1MB; i++ {
			builder.WriteString(chunk)
		}
	default:
		chunk := strings.Repeat("*", _1KB)
		for i := 0; i < (int(Number)*_1KB)/_1KB; i++ {
			builder.WriteString(chunk)
		}
	}

	w.WriteHeader(200)
	w.Write(builder.Bytes())
}

func main() {
	http.HandleFunc("/", indexHandler)
	http.HandleFunc("/helloworld", HelloWorldHandler)
	http.HandleFunc("/notfound", NotFoundHandler)
	http.HandleFunc("/body", Body)

	ip := os.Getenv("HELLOWORLDSERVER_IP")
	port := os.Getenv("HELLOWORLDSERVER_PORT")
	if ip == "" {
		ip = "0.0.0.0"
	}
	if port == "" {
		port = "22222"
	}

	addr := fmt.Sprintf("%s:%s", ip, port)
	fmt.Printf("listen %s\n", addr)
	http.ListenAndServe(addr, nil)
}
