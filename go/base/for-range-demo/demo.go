package forrangedemo

import "fmt"

// RangePonit
func RangePonit() {
	type Customer struct {
		ID      string
		Balance float64
	}

	test := []Customer{
		{ID: "1", Balance: 10},
		{ID: "2", Balance: -10},
		{ID: "3", Balance: 0},
	}

	m := make(map[string]*Customer)
	for _, customer := range test {
		m[customer.ID] = &customer
	}

	for k, v := range m {
		fmt.Println(k, *v)
	}
}

func RangeUint() {
	t1 := []uint{1, 2, 3}
	t2 := []*uint{}

	for _, i := range t1 {
		t2 = append(t2, &i)
	}
	fmt.Println(t2)
}
