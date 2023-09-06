package map_and_slice

import (
	"fmt"
	"math/rand"
	"reflect"
	"time"

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

func CompareEqualAndDeepEqual() {
	v1 := map[int]map[int]string{}
	v2 := map[int]map[int]string{}

	deepCopy := func(v map[int]string) map[int]string {
		vv := make(map[int]string, len(v))
		for key, value := range v {
			vv[key] = value
		}
		return vv
	}

	for i := 0; i < 100; i++ {
		vv := map[int]string{
			i: randomStr(10),
		}
		v1[i] = vv
		v2[i] = deepCopy(vv)
	}

	var count int = 10000
	start := time.Now()
	for i := 0; i < count; i++ {
		Equal(v1, v2)
	}
	fmt.Printf("count: %d, Equal cost: %s\n", count, time.Since(start))

	start = time.Now()
	for i := 0; i < count; i++ {
		reflect.DeepEqual(v1, v2)
	}
	fmt.Printf("count: %d, DeepEqual cost: %s\n", count, time.Since(start))
}

func randomStr(length int) string {
	const charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
	rand.Seed(time.Now().UnixNano())

	b := make([]byte, length)
	for i := range b {
		b[i] = charset[rand.Intn(len(charset))]
	}
	return string(b)
}

func Equal(v1, v2 map[int]map[int]string) bool {
	if len(v1) != len(v2) {
		return false
	}

	equalValue := func(vv1, vv2 map[int]string) bool {
		if len(vv1) != len(vv2) {
			return false
		}
		for k, v := range vv1 {
			if vv, ok := vv2[k]; !ok || v != vv {
				return false
			}
		}
		return true
	}

	for key, value := range v1 {
		if value2, ok := v2[key]; !ok || !equalValue(value, value2) {
			return false
		}
	}
	return true
}

func generateMap(length int) map[int]string {
	m := make(map[int]string)
	for i := 0; i < length; i++ {
		m[i] = randomStr(10)
	}
	return m
}

func RangeMapK(m map[int]string) {
	// m := generateMap(100)
	var tmp string
	for k := range m {
		tmp = m[k]
	}
	_ = tmp
}

func RangeMapKv(m map[int]string) {
	// m := generateMap(100)
	var tmp string
	for _, v := range m {
		tmp = v
	}
	_ = tmp
}

type item struct {
	a int
	b [4096]int
}

func generateStructMap(l int) map[int]item {
	m := make(map[int]item)
	for i := 0; i < l; i++ {
		m[i] = item{}
	}
	return m
}

func RangeStructMapK(m map[int]item) {
	var tmp item
	for k := range m {
		tmp = m[k]
	}
	_ = tmp
}

func RangeStructMapKv(m map[int]item) {
	var tmp item
	for _, v := range m {
		tmp = v
	}
	_ = tmp
}
