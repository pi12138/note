package type_assertion_demo

import (
	"encoding/json"
	"fmt"
)

type Foo struct {
	Value any `json:"value"`
}

type MyInt int32

func Demo() {
	var a any = []int{1, 2, 3}
	var b any = []string{"a", "b", "c"}
	v, ok := a.([]int)
	fmt.Println(v, ok)
	vv, ok := b.([]string)
	fmt.Println(vv, ok)

	var f Foo
	if err := json.Unmarshal([]byte(`{"value": ["a", "b"]}`), &f); err == nil {
		fmt.Println(f.Value)
		for _, i := range f.Value.([]any) {
			fmt.Println(i.(string))
		}
	} else {
		fmt.Println(err)
	}

	// var i1 int
	// var i2 MyInt

	// i1 = 10
	// i2 = 20

	// switch v := i2.

}
