package cssh

import (
	"base/common/clog"
	"bytes"
	"io/ioutil"

	"github.com/pkg/sftp"
	"golang.org/x/crypto/ssh"
)

type Client interface {
	Close()
	Run(string) (*Result, error)
	PutFile(string, string) error
	PutFileData(string, []byte) error
}

type client struct {
	conn    connection
	client  *ssh.Client
	session *ssh.Session
}

func NewClient(ip, username, password string) (Client, error) {
	conn := newConn(username, ip, password)
	cli, err := conn.Dial()
	if err != nil {
		return nil, err
	}

	sess, err := cli.NewSession()
	if err != nil {
		return nil, err
	}
	c := client{
		conn:    conn,
		client:  cli,
		session: sess,
	}
	return &c, nil
}

func (r *client) Run(cmd string) (*Result, error) {
	var stdout, stderr bytes.Buffer
	r.session.Stdout = &stdout
	r.session.Stderr = &stderr
	if err := r.session.Run(cmd); err != nil {
		clog.Debugf("Run %s error. %s", cmd, err)
		return nil, err
	}

	ret := Result{
		Stdout: stdout.String(),
		Stderr: stderr.String(),
	}
	clog.Debugf("Run %s success. ret: %s", cmd, ret)
	return &ret, nil
}

func (r *client) PutFile(localFile, remoteFile string) error {
	sftpCli, err := sftp.NewClient(r.client)
	if err != nil {
		return err
	}
	defer sftpCli.Close()

	localData, err := ioutil.ReadFile(localFile)
	if err != nil {
		return err
	}

	remoteF, err := sftpCli.Create(remoteFile)
	if err != nil {
		return err
	}
	defer remoteF.Close()

	_, err = remoteF.Write(localData)
	if err != nil {
		return err
	}

	clog.Debugf("[PutFile] from %s to %s:%s success.", localFile, r.conn, remoteFile)
	return nil
}

func (r *client) PutFileData(remoteFile string, data []byte) error {
	sftpCli, err := sftp.NewClient(r.client)
	if err != nil {
		return err
	}
	defer sftpCli.Close()

	remoteF, err := sftpCli.Create(remoteFile)
	if err != nil {
		return err
	}
	defer remoteF.Close()

	_, err = remoteF.Write(data)
	if err != nil {
		return err
	}

	clog.Debugf("[PutFileData] to %s:%s success.", r.conn, remoteFile)
	return nil
}

func (r client) Close() {
	if err := r.session.Close(); err != nil {
		clog.Errorf("close ssh session error. %s. conn: %s", err, r.conn)
	}
	if err := r.client.Close(); err != nil {
		clog.Errorf("close ssh error. %s. conn: %s", err, r.conn)
	}
}
