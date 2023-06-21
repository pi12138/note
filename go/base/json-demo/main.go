package json_demo

import (
	"encoding/json"
	"fmt"
	"os"
)

func Demo() {

}

func DemoOne() {
	// c := 10
	f := Foo{
		A: 1,
		B: "B",
		// C: Bar{1, "B", &c},
		// D: Bar{2, "B", &c},
	}

	data, _ := json.Marshal(f)
	fmt.Printf("data: %s \n", string(data))

	var F Foo
	var B Bar
	F.C = B
	json.Unmarshal(data, &F)
	fmt.Printf("F: %v\n", F)
}

type Foo struct {
	A int    `json:"a"`
	B string `json:"b"`
	C any    `json:"c"`
	D Bar    `json:"d"`
}

type Bar struct {
	A int    `json:"a"`
	B string `json:"b"`
	C *int   `json:"c"`
	D D      `json:"d"`
}

type D struct {
	x string
}

func (r D) String() string {
	return r.x
}

func (r D) MarshalJSON() ([]byte, error) {
	return []byte(r.x), nil
}

func (r *D) UnmarshalJSON(data []byte) error {
	r.x = string(data)
	return nil
}

func ParseToPointer() {
	data := []byte(`
	{
		"a": 1,
		"b": "str",
		"c": 10,
		"d": "100"
	}
	`)

	b := Bar{}
	if err := json.Unmarshal(data, &b); err != nil {
		fmt.Printf("json unmarshal error: %s", err)
		os.Exit(1)
	}
	fmt.Printf("b value: %v, c value: %v\n", b, *b.C)
}
