package main

import (
	"fmt"

	"github.com/hashicorp/go-multierror"
	"go.uber.org/multierr"
)

type P struct {
}

func (p *P) Print() string {
	return "P struct"
}

func main() {
	error1 := fmt.Errorf("error one")
	error2 := fmt.Errorf("error two")
	error3 := fmt.Errorf("error three")

	var Err1 *multierror.Error
	Err1 = multierror.Append(Err1.ErrorOrNil(), error1)
	Err1 = multierror.Append(Err1.ErrorOrNil(), error2)
	Err1 = multierror.Append(Err1.ErrorOrNil(), error3)

	var err2 error
	err2 = multierr.Append(err2, error1)
	err2 = multierr.Append(err2, error2)
	err2 = multierr.Append(err2, error3)
	err3 := multierr.Combine(error1, error2, error3)

	fmt.Println("hashicorp/go-multierror result: ", Err1.ErrorOrNil())
	fmt.Println("go.uber.org/multierr result: ", err2.Error())
	fmt.Println("go.uber.org/multierr result: ", err3.Error())

	var p *P
	fmt.Println(p.Print())
}
