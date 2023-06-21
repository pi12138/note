package map_and_slice

import (
	"fmt"

	"golang.org/x/exp/maps"
)

func main() {
	// MapDemo()
	// SliceDemo()
	MapUpdate()
}

// MapDemo nil map 无法赋值
func MapDemo() {
	var m1 map[string]any     // nil map
	var m2 = map[string]any{} // 空 map
	m3 := make(map[string]any)

	fmt.Printf("m1: %v, m2: %v, m3: %v\n", m1, m2, m3)
	fmt.Printf("is nil, m1: %t, m2: %t, m3: %t\n", m1 == nil, m2 == nil, m3 == nil)

	// m1["key"] = 10 // > panic: assignment to entry in nil map
	m2["key"] = 20
	m3["key"] = 30

}

func SliceDemo() {

	l1 := []int{0, 1, 2, 3, 4, 5}
	head, tail := l1[0:0], l1[0:]

	fmt.Printf("head: %v, tail: %v\n", head, tail)

	l2 := Insert[int](l1, 2, 20)
	l3 := Insert[int](l1, 0, 0)
	fmt.Printf("l2: %v, l3: %v\n", l2, l3)
}

// Insert for slice
func Insert[T any](iter []T, index uint, value T) []T {
	var result []T
	head, tail := iter[0:index], iter[index:]
	result = append(result, head...)
	result = append(result, value)
	result = append(result, tail...)
	return result
}

// 在map取值取不到时给map赋值
func SetMap() {
	m1 := make(map[int]int)

	if v, ok := m1[1]; !ok {
		v = 1
		m1[1] = v
	}
}

func MapUpdate() {
	var m1 = map[int]int{
		1: 10,
		2: 20,
	}
	var m2 = map[int]int{
		3: 30,
		1: 100,
	}
	maps.Copy(m1, m2)

	fmt.Println(m1)
}
