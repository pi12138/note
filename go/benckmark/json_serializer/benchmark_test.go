
package main

import (
	"encoding/json"
	"fmt"
	"reflect"
	"testing"

	"github.com/guregu/null/v6"
)

// 原生类型结构体
type NativeStruct struct {
	ID          int     `json:"id"`
	Name        string  `json:"name"`
	Age         int     `json:"age"`
	Score       float64 `json:"score"`
	IsActive    bool    `json:"is_active"`
	Description string  `json:"description"`
	Price       float64 `json:"price"`
	Count       int64   `json:"count"`
	Rating      float32 `json:"rating"`
	Category    string  `json:"category"`
}

// 指针类型结构体
type PointerStruct struct {
	ID          *int     `json:"id,omitempty"`
	Name        *string  `json:"name,omitempty"`
	Age         *int     `json:"age,omitempty"`
	Score       *float64 `json:"score,omitempty"`
	IsActive    *bool    `json:"is_active,omitempty"`
	Description *string  `json:"description,omitempty"`
	Price       *float64 `json:"price,omitempty"`
	Count       *int64   `json:"count,omitempty"`
	Rating      *float32 `json:"rating,omitempty"`
	Category    *string  `json:"category,omitempty"`
}

// guregu/null 类型结构体
type NullStruct struct {
	ID          null.Int    `json:"id"`
	Name        null.String `json:"name"`
	Age         null.Int    `json:"age"`
	Score       null.Float  `json:"score"`
	IsActive    null.Bool   `json:"is_active"`
	Description null.String `json:"description"`
	Price       null.Float  `json:"price"`
	Count       null.Int    `json:"count"`
	Rating      null.Float  `json:"rating"`
	Category    null.String `json:"category"`
}

// 创建测试数据
func createNativeData() NativeStruct {
	return NativeStruct{
		ID:          123,
		Name:        "John Doe",
		Age:         30,
		Score:       95.5,
		IsActive:    true,
		Description: "This is a test description for benchmarking purposes",
		Price:       299.99,
		Count:       1000,
		Rating:      4.8,
		Category:    "Electronics",
	}
}

func createPointerData() PointerStruct {
	id := 123
	name := "John Doe"
	age := 30
	score := 95.5
	isActive := true
	description := "This is a test description for benchmarking purposes"
	price := 299.99
	count := int64(1000)
	rating := float32(4.8)
	category := "Electronics"

	return PointerStruct{
		ID:          &id,
		Name:        &name,
		Age:         &age,
		Score:       &score,
		IsActive:    &isActive,
		Description: &description,
		Price:       &price,
		Count:       &count,
		Rating:      &rating,
		Category:    &category,
	}
}

func createNullData() NullStruct {
	return NullStruct{
		ID:          null.IntFrom(123),
		Name:        null.StringFrom("John Doe"),
		Age:         null.IntFrom(30),
		Score:       null.FloatFrom(95.5),
		IsActive:    null.BoolFrom(true),
		Description: null.StringFrom("This is a test description for benchmarking purposes"),
		Price:       null.FloatFrom(299.99),
		Count:       null.IntFrom(1000),
		Rating:      null.FloatFrom(4.8),
		Category:    null.StringFrom("Electronics"),
	}
}

// 创建部分缺失数据（测试 omitempty 和 null 的区别）
func createPartialPointerData() PointerStruct {
	id := 123
	name := "John Doe"
	// 其他字段为 nil
	return PointerStruct{
		ID:   &id,
		Name: &name,
	}
}

func createPartialNullData() NullStruct {
	return NullStruct{
		ID:   null.IntFrom(123),
		Name: null.StringFrom("John Doe"),
		// 其他字段为 null.Type{}
	}
}

// Benchmark 序列化 - 完整数据
func BenchmarkMarshalNative(b *testing.B) {
	data := createNativeData()
	b.ResetTimer()
	b.ReportAllocs()

	for i := 0; i < b.N; i++ {
		_, err := json.Marshal(data)
		if err != nil {
			b.Fatal(err)
		}
	}
}

func BenchmarkMarshalPointer(b *testing.B) {
	data := createPointerData()
	b.ResetTimer()
	b.ReportAllocs()

	for i := 0; i < b.N; i++ {
		_, err := json.Marshal(data)
		if err != nil {
			b.Fatal(err)
		}
	}
}

func BenchmarkMarshalNull(b *testing.B) {
	data := createNullData()
	b.ResetTimer()
	b.ReportAllocs()

	for i := 0; i < b.N; i++ {
		_, err := json.Marshal(data)
		if err != nil {
			b.Fatal(err)
		}
	}
}

// Benchmark 序列化 - 部分数据
func BenchmarkMarshalPartialPointer(b *testing.B) {
	data := createPartialPointerData()
	b.ResetTimer()
	b.ReportAllocs()

	for i := 0; i < b.N; i++ {
		_, err := json.Marshal(data)
		if err != nil {
			b.Fatal(err)
		}
	}
}

func BenchmarkMarshalPartialNull(b *testing.B) {
	data := createPartialNullData()
	b.ResetTimer()
	b.ReportAllocs()

	for i := 0; i < b.N; i++ {
		_, err := json.Marshal(data)
		if err != nil {
			b.Fatal(err)
		}
	}
}

// Benchmark 反序列化 - 完整数据
func BenchmarkUnmarshalNative(b *testing.B) {
	data := createNativeData()
	jsonData, _ := json.Marshal(data)
	b.ResetTimer()
	b.ReportAllocs()

	for i := 0; i < b.N; i++ {
		var result NativeStruct
		err := json.Unmarshal(jsonData, &result)
		if err != nil {
			b.Fatal(err)
		}
	}
}

func BenchmarkUnmarshalPointer(b *testing.B) {
	data := createPointerData()
	jsonData, _ := json.Marshal(data)
	b.ResetTimer()
	b.ReportAllocs()

	for i := 0; i < b.N; i++ {
		var result PointerStruct
		err := json.Unmarshal(jsonData, &result)
		if err != nil {
			b.Fatal(err)
		}
	}
}

func BenchmarkUnmarshalNull(b *testing.B) {
	data := createNullData()
	jsonData, _ := json.Marshal(data)
	b.ResetTimer()
	b.ReportAllocs()

	for i := 0; i < b.N; i++ {
		var result NullStruct
		err := json.Unmarshal(jsonData, &result)
		if err != nil {
			b.Fatal(err)
		}
	}
}

// Benchmark 反序列化 - 部分数据
func BenchmarkUnmarshalPartialPointer(b *testing.B) {
	data := createPartialPointerData()
	jsonData, _ := json.Marshal(data)
	b.ResetTimer()
	b.ReportAllocs()

	for i := 0; i < b.N; i++ {
		var result PointerStruct
		err := json.Unmarshal(jsonData, &result)
		if err != nil {
			b.Fatal(err)
		}
	}
}

func BenchmarkUnmarshalPartialNull(b *testing.B) {
	data := createPartialNullData()
	jsonData, _ := json.Marshal(data)
	b.ResetTimer()
	b.ReportAllocs()

	for i := 0; i < b.N; i++ {
		var result NullStruct
		err := json.Unmarshal(jsonData, &result)
		if err != nil {
			b.Fatal(err)
		}
	}
}

// 内存占用测试
func BenchmarkMemoryUsageNative(b *testing.B) {
	b.ReportAllocs()
	for i := 0; i < b.N; i++ {
		_ = createNativeData()
	}
}

func BenchmarkMemoryUsagePointer(b *testing.B) {
	b.ReportAllocs()
	for i := 0; i < b.N; i++ {
		_ = createPointerData()
	}
}

func BenchmarkMemoryUsageNull(b *testing.B) {
	b.ReportAllocs()
	for i := 0; i < b.N; i++ {
		_ = createNullData()
	}
}

// 批量操作测试
func BenchmarkMarshalSliceNative(b *testing.B) {
	data := make([]NativeStruct, 1000)
	for i := range data {
		data[i] = createNativeData()
	}

	b.ResetTimer()
	b.ReportAllocs()

	for i := 0; i < b.N; i++ {
		_, err := json.Marshal(data)
		if err != nil {
			b.Fatal(err)
		}
	}
}

func BenchmarkMarshalSlicePointer(b *testing.B) {
	data := make([]PointerStruct, 1000)
	for i := range data {
		data[i] = createPointerData()
	}

	b.ResetTimer()
	b.ReportAllocs()

	for i := 0; i < b.N; i++ {
		_, err := json.Marshal(data)
		if err != nil {
			b.Fatal(err)
		}
	}
}

func BenchmarkMarshalSliceNull(b *testing.B) {
	data := make([]NullStruct, 1000)
	for i := range data {
		data[i] = createNullData()
	}

	b.ResetTimer()
	b.ReportAllocs()

	for i := 0; i < b.N; i++ {
		_, err := json.Marshal(data)
		if err != nil {
			b.Fatal(err)
		}
	}
}

// 综合性能测试函数
func runComprehensiveTest() {
	fmt.Println("=== Comprehensive Performance Analysis ===")

	// 测试结构体大小
	fmt.Println("Memory footprint per struct:")
	var native NativeStruct
	var pointer PointerStruct
	var nullType NullStruct

	nativeStruct, nativeTotal := detailedSizeOf(native)
	pointerStruct, pointerTotal := detailedSizeOf(pointer)
	nullStruct, nullTotal := detailedSizeOf(nullType)

	fmt.Printf("Native struct size:  %d bytes (total: %d bytes)\n", nativeStruct, nativeTotal)
	fmt.Printf("Pointer struct size: %d bytes (total: %d bytes)\n", pointerStruct, pointerTotal)
	fmt.Printf("Null struct size:    %d bytes (total: %d bytes)\n", nullStruct, nullTotal)
	fmt.Println()

	// 测试 JSON 输出大小
	nativeData := createNativeData()
	pointerData := createPointerData()
	nullData := createNullData()
	partialPointerData := createPartialPointerData()
	partialNullData := createPartialNullData()

	nativeJSON, _ := json.Marshal(nativeData)
	pointerJSON, _ := json.Marshal(pointerData)
	nullJSON, _ := json.Marshal(nullData)
	partialPointerJSON, _ := json.Marshal(partialPointerData)
	partialNullJSON, _ := json.Marshal(partialNullData)

	fmt.Println("JSON output size (complete data):")
	fmt.Printf("Native:  %d bytes\n", len(nativeJSON))
	fmt.Printf("Pointer: %d bytes\n", len(pointerJSON))
	fmt.Printf("Null:    %d bytes\n", len(nullJSON))
	fmt.Println()

	fmt.Println("JSON output size (partial data):")
	fmt.Printf("Pointer: %d bytes\n", len(partialPointerJSON))
	fmt.Printf("Null:    %d bytes\n", len(partialNullJSON))
	fmt.Println()

	fmt.Println("Sample JSON outputs:")
	fmt.Printf("Partial Pointer: %s\n", string(partialPointerJSON))
	fmt.Printf("Partial Null:    %s\n", string(partialNullJSON))
	fmt.Println()
}

// 增强版本 - 计算结构体的详细内存使用
func detailedSizeOf(v interface{}) (structSize, totalSize uintptr) {
	rv := reflect.ValueOf(v)
	rt := reflect.TypeOf(v)

	structSize = rt.Size()
	totalSize = structSize

	// 如果是结构体，计算指针字段指向的内存
	if rt.Kind() == reflect.Struct {
		for i := 0; i < rt.NumField(); i++ {
			field := rv.Field(i)
			fieldType := rt.Field(i).Type

			if fieldType.Kind() == reflect.Ptr && field.CanInterface() && !field.IsNil() {
				// 指针字段指向的值的大小
				pointedValue := field.Elem()
				if pointedValue.IsValid() {
					totalSize += fieldType.Elem().Size()
				}
			}
		}
	}

	return structSize, totalSize
}

func main() {
	runComprehensiveTest()

	fmt.Println("Run the following commands to execute benchmarks:")
	fmt.Println("go test -bench=BenchmarkMarshal -benchmem")
	fmt.Println("go test -bench=BenchmarkUnmarshal -benchmem")
	fmt.Println("go test -bench=BenchmarkMemoryUsage -benchmem")
	fmt.Println("go test -bench=BenchmarkMarshalSlice -benchmem")
	fmt.Println("go test -bench=. -benchmem")
}
