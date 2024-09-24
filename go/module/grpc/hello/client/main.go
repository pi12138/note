package main

import (
	"context"
	"flag"
	"log/slog"
	"time"

	"grpc-demo/hello/pb"

	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
)

const (
	defaultName = "world"
)

var (
	addr = flag.String("addr", "localhost:50051", "the address to connect to")
	name = flag.String("name", defaultName, "Name to greet")
)

func main() {
	flag.Parse()
	// Set up a connection to the server.
	conn, err := grpc.NewClient(*addr, grpc.WithTransportCredentials(insecure.NewCredentials()))
	if err != nil {
		slog.Error("did not connect","error", err)
	}
	defer conn.Close()
	slog.Info("1", "conn.GetState()", conn.GetState())
	c := pb.NewGreeterClient(conn)

	slog.Info("1", "conn.GetState()", conn.GetState())
	// Contact the server and print out its response.
	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()
	r, err := c.SayHello(ctx, &pb.HelloRequest{Name: *name})
	if err != nil {
		slog.Error("could not greet","error", err)
	} else {
		slog.Info("", "Greeting", r.GetMessage())
	}
	slog.Info("1", "conn.GetState()", conn.GetState())
	for i := 0; i < 10; i++ {
		slog.Info("1", "conn.GetState()", conn.GetState())
		time.Sleep(5 * time.Second)
	}
}
