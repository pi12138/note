package cssh

import (
	"fmt"

	"golang.org/x/crypto/ssh"
)

type connection struct {
	username string
	ip       string
	port     uint
	password string
}

func (r connection) String() string {
	return fmt.Sprintf("%s@%s:%d", r.username, r.ip, r.port)
}

func (r connection) Addr() string {
	return fmt.Sprintf("%s:%d", r.ip, r.port)
}

func (r connection) config() *ssh.ClientConfig {
	return &ssh.ClientConfig{
		User: r.username,
		Auth: []ssh.AuthMethod{
			ssh.Password(r.password),
		},
		HostKeyCallback: ssh.InsecureIgnoreHostKey(),
	}
}

func (r connection) Dial() (*ssh.Client, error) {
	return ssh.Dial("tcp", r.Addr(), r.config())
}

func newConn(username, ip, password string) connection {
	return connection{
		username: username,
		ip:       ip,
		password: password,
		port: 22,
	}
}