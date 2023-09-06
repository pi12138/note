package map_and_slice

import (
	"math/rand"
	"runtime"
	"sync"
	"time"
)

func init() {
	rand.Seed(time.Now().UnixNano())
}

func ConcurrentWrite() {
	runtime.GOMAXPROCS(1)
	m := make(map[int]int)
	var wg sync.WaitGroup
	f := func() {
		k, v := rand.Int()%50, rand.Int()%1000
		m[k] = v
		// _ = m[k]
		wg.Done()
	}
	for i := 0; i < 1000; i++ {
		wg.Add(1)
		go f()
	}
	wg.Wait()
}

type IntToInt struct {
	mu sync.Mutex
	v  map[int]int
}

func (r *IntToInt) Store(k, v int) {
	r.mu.Lock()
	defer r.mu.Unlock()
	if r.v == nil {
		r.v = make(map[int]int)
	}
	r.v[k] = v
}

func (r *IntToInt) Load(k int) (int, bool) {
	v, ok := r.v[k]
	return v, ok
}

func ConcurrentWriteIntToIntMap() {
	runtime.GOMAXPROCS(1)
	var m IntToInt
	var wg sync.WaitGroup

	f := func() {
		// k, v := rand.Int()%50, rand.Int()%1000
		m.Store(1, 1)
		wg.Done()
	}
	fr := func() {
		_, _ = m.Load(1)
		wg.Done()
	}
	for i := 0; i < 100000; i++ {
		wg.Add(2)
		go f()
		go fr()
	}
	wg.Wait()

}

func ConcurrentWriteSyncMap() {
	runtime.GOMAXPROCS(1)
	var m sync.Map
	var wg sync.WaitGroup

	f := func() {
		k, v := rand.Int()%50, rand.Int()%1000
		m.Store(k, v)
		// m.Store("k", "v")
		// _, _ = m.Load(k)
		wg.Done()
	}
	for i := 0; i < 1000; i++ {
		wg.Add(1)
		go f()
	}
	wg.Wait()

}

func ConcurrentReadWrite(n int) {
	runtime.GOMAXPROCS(1)
	m := make(map[int]int)
	var wg sync.WaitGroup
	f := func() {
		// k, v := rand.Int()%50, rand.Int()%1000
		// m[k] = v
		m[1] = 1
		_ = m[1]
		wg.Done()
	}
	for i := 0; i < n; i++ {
		wg.Add(1)
		go f()
	}
	wg.Wait()
}
