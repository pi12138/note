package cssh

import "fmt"

type Result struct {
	Stdout string
	Stderr string
}

func (r Result) String() string {
	return fmt.Sprintf("stdout: %s, stderr: %s", r.Stdout, r.Stderr)
}
