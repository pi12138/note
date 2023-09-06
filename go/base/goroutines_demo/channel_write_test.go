package goroutinesdemo

import "testing"

func TestChannelWrite(t *testing.T) {
	ChannelWrite()
}

func BenchmarkChannelWrite(b *testing.B) {
	for i := 0; i < b.N; i++ {
		ChannelWrite()
	}
}