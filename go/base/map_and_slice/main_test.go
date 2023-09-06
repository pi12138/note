package map_and_slice

import (
	"testing"
)

func TestEqual(t *testing.T) {
	type args struct {
		v1 map[int]map[int]string
		v2 map[int]map[int]string
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		// 测试用例1: 两个空的 map
		{
			name: "Empty maps",
			args: args{
				v1: map[int]map[int]string{},
				v2: map[int]map[int]string{},
			},
			want: true,
		},
		// 测试用例2: 两个 map 长度不一致
		{
			name: "Different map lengths",
			args: args{
				v1: map[int]map[int]string{1: {1: "a"}},
				v2: map[int]map[int]string{},
			},
			want: false,
		},
		// 测试用例3: 两个 map 中的键值对完全相同
		{
			name: "Maps with identical key-value pairs",
			args: args{
				v1: map[int]map[int]string{1: {1: "a"}, 2: {2: "b"}},
				v2: map[int]map[int]string{1: {1: "a"}, 2: {2: "b"}},
			},
			want: true,
		},
		// 测试用例4: 两个 map 中的键值对不完全相同
		{
			name: "Maps with different key-value pairs",
			args: args{
				v1: map[int]map[int]string{1: {1: "a"}, 2: {2: "b"}},
				v2: map[int]map[int]string{1: {1: "a"}, 2: {2: "c"}},
			},
			want: false,
		},
		// 测试用例5: 一个 map 为空，一个 map 非空
		{
			name: "One map empty, one map non-empty",
			args: args{
				v1: map[int]map[int]string{},
				v2: map[int]map[int]string{1: {1: "a"}},
			},
			want: false,
		},
		// 测试用例6: 两个 map 中的键值对顺序不同
		{
			name: "Maps with different order of key-value pairs",
			args: args{
				v1: map[int]map[int]string{1: {1: "a"}, 2: {2: "b"}},
				v2: map[int]map[int]string{2: {2: "b"}, 1: {1: "a"}},
			},
			want: true,
		},
		// 测试用例7: 两个 map 中的值类型不同
		{
			name: "Maps with different value types",
			args: args{
				v1: map[int]map[int]string{1: {1: "a"}},
				v2: map[int]map[int]string{1: {1: "b"}},
			},
			want: false,
		},
		// 测试用例8: 两个 map 中的键类型不同
		{
			name: "Maps with different key types",
			args: args{
				v1: map[int]map[int]string{1: {1: "a"}},
				v2: map[int]map[int]string{2: {1: "a"}},
			},
			want: false,
		},
		// 测试用例9: 两个 map 中的值为 nil
		{
			name: "Maps with nil values",
			args: args{
				v1: map[int]map[int]string{1: nil},
				v2: map[int]map[int]string{1: nil},
			},
			want: true,
		},
		// 测试用例10: 两个 map 中的值为空的 map
		{
			name: "Maps with empty map values",
			args: args{
				v1: map[int]map[int]string{1: {}},
				v2: map[int]map[int]string{1: {}},
			},
			want: true,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := Equal(tt.args.v1, tt.args.v2); got != tt.want {
				t.Errorf("Equal() = %v, want %v", got, tt.want)
			}
		})
	}
}

func BenchmarkRangeMapK(t *testing.B) {
	m := generateMap(1000)
	for i := 0; i < t.N; i++ {
		RangeMapK(m)
	}
}

func BenchmarkRangeMapKv(t *testing.B) {
	m := generateMap(1000)
	for i := 0; i < t.N; i++ {
		RangeMapKv(m)
	}
}

func BenchmarkRangeStructMapK(t *testing.B) {
	m := generateStructMap(1000)
	for i := 0; i < t.N; i++ {
		RangeStructMapK(m)
	}
}

func BenchmarkRangeStructMapKv(t *testing.B) {
	m := generateStructMap(1000)
	for i := 0; i < t.N; i++ {
		RangeStructMapKv(m)
	}
}