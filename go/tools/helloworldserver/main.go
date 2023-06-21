package main

import (
	"fmt"
	"log"
	"net/http"
	"os"
)

func indexHandler(w http.ResponseWriter, r *http.Request) {
	log.Printf("indexHandler")
	w.Write([]byte("index"))
}

func HelloWorldHandler(w http.ResponseWriter, r *http.Request) {
	log.Printf("HelloWorldHandler")
	w.Write([]byte("helloworld"))
}

func NotFoundHandler(w http.ResponseWriter, r *http.Request) {
	log.Printf("NotFoundHandler")
	w.WriteHeader(404)
	w.Write([]byte("not found"))

}

func main() {
	http.HandleFunc("/", indexHandler)
	http.HandleFunc("/helloworld", HelloWorldHandler)
	http.HandleFunc("/notfound", NotFoundHandler)

	ip := os.Getenv("HELLOWORLDSERVER_IP")
	port := os.Getenv("HELLOWORLDSERVER_PORT")
	if ip == "" {
		ip = "0.0.0.0"
	}
	if port == "" {
		port = "22222"
	}

	addr := fmt.Sprintf("%s:%s", ip, port)
	log.Printf("listen %s", addr)
	http.ListenAndServe(addr, nil)
}
