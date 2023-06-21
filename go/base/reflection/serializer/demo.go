package serializer

import (
	"fmt"
)

type Myint int

type User struct {
	Name     string
	Age      int
	Height   int
	Weight   int
	P        *int
	Username []string
	My       Myint
}

type UserSerializer struct {
	Name     string   `serializer:"source:GetNameValue"`
	Age      int      `serializer:"source:Age;skip"`
	Height   int      `serializer:"source:Height;skip"`
	Weight   int      `serializer:"source:Weight"`
	P        *int     `serializer:"source:P"`
	Username []string `serializer:"source:Username"`
	My       Myint    `serializer:"source:My"`
	Extra    int
}

func (r *UserSerializer) GetNameValue(instance *User) string {
	return "GetNameField"
}

func (r *UserSerializer) ValidateFieldName(name string) error {
	fmt.Printf("validate field be call.\n")
	return nil
}

func Demo() {

	var p int
	p = 10
	u := User{
		Name:     "user-one",
		Age:      1,
		Height:   180,
		Weight:   75,
		P:        &p,
		Username: []string{"old", "new"},
		My:       10000,
	}
	var us UserSerializer
	var newUser User

	if err := AssignAttr(&us, &u); err != nil {
		fmt.Printf("error: %s\n", err)
	}
	if err := AssignAttr(&newUser, &us); err != nil {
		fmt.Printf("error: %s\n", err)
	}
	fmt.Printf("u: %v, us: %v, newUser: %v \n", u, us, newUser)
	// CallValidateFieldFunc(&us)
}
