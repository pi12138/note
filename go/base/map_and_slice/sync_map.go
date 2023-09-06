package map_and_slice

import (
	"fmt"
	"sync"
)

func UseSyncMap() {
	var m sync.Map

	// 写
	m.Store("key", "value")
	m.Store("k", "v")
	// 读
	key, ok := m.Load("key")
	fmt.Println(key, ok)

	// 遍历
	ret := make(map[string]string)
	m.Range(func(k, v any) bool {
		ret[k.(string)] = v.(string)
		return true
	})
	fmt.Println(ret)

	// 删除
	m.Delete("k")
	ret2 := make(map[string]string)
	m.Range(func(k, v any) bool {
		ret2[k.(string)] = v.(string)
		return true
	})
	fmt.Println(ret2)

	// 重复写
	m.Store("key", "value2")
	ret3 := make(map[string]string)
	m.Range(func(k, v any) bool {
		ret3[k.(string)] = v.(string)
		return true
	})
	fmt.Println(ret3)
}
