package map_and_slice

import "testing"

func TestConcurrentWrite(t *testing.T) {
	// tests := []struct {
	// 	name string
	// }{
	// 	// TODO: Add test cases.
	// }
	// for _, tt := range tests {
	// 	t.Run(tt.name, func(t *testing.T) {
	// 		ConcurrentWrite()
	// 	})
	// }
	ConcurrentWrite()
}

func TestConcurrentRead(t *testing.T) {

	ConcurrentReadWrite(1000000)
}

func TestConcurrentWriteSyncMap(t *testing.T) {
	// tests := []struct {
	// 	name string
	// }{
	// 	// TODO: Add test cases.
	// }
	// for _, tt := range tests {
	// 	t.Run(tt.name, func(t *testing.T) {
	// 		ConcurrentWrite()
	// 	})
	// }
	ConcurrentWriteSyncMap()
}

func BenchmarkConcurrentWrite(b *testing.B) {
	for n := 0; n < b.N; n++ {
		ConcurrentWrite()
	}
}

func BenchmarkConcurrentWriteSyncMap(b *testing.B) {
	for n := 0; n < b.N; n++ {
		ConcurrentWriteSyncMap()
	}
}

func BenchmarkConcurrentWriteIntToIntMap(b *testing.B) {
	for n := 0; n < b.N; n++ {
		ConcurrentWriteIntToIntMap()
	}
}
