#!/bin/bash

echo "=== JSON Serialization Performance Benchmark ==="
echo "Testing Native types vs Pointers vs guregu/null"
echo

# 确保依赖安装
echo "Installing dependencies..."
go mod tidy
echo

# 运行综合分析
echo "Running comprehensive analysis..."
go run main.go
echo

# 运行各种 benchmark 测试
echo "=== Single Object Marshaling Performance ==="
go test -bench='^BenchmarkMarshal[^S]' -benchmem -count=3

echo
echo "=== Single Object Unmarshaling Performance ==="
go test -bench='^BenchmarkUnmarshal[^P]' -benchmem -count=3

echo
echo "=== Memory Usage Comparison ==="
go test -bench=BenchmarkMemoryUsage -benchmem -count=3

echo
echo "=== Batch Operations (1000 objects) ==="
go test -bench=BenchmarkMarshalSlice -benchmem -count=3

echo
echo "=== Partial Data Tests ==="
go test -bench=Partial -benchmem -count=3

echo
echo "=== Complete Performance Report ==="
go test -bench=. -benchmem -count=5 > benchmark_results.txt
echo "Results saved to benchmark_results.txt"

# 生成性能对比报告
echo
echo "=== Performance Summary ==="
echo "Analyzing results..."

cat << 'EOF' > analyze_results.go
package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"sort"
	"strconv"
	"strings"
)

type BenchResult struct {
	Name       string
	NsPerOp    int64
	Allocs     int64
	BytesAlloc int64
}

func main() {
	file, err := os.Open("benchmark_results.txt")
	if err != nil {
		fmt.Println("Could not read benchmark results")
		return
	}
	defer file.Close()

	results := make(map[string][]BenchResult)
	re := regexp.MustCompile(`^(Benchmark\w+)-\d+\s+\d+\s+(\d+)\s+ns/op\s+(\d+)\s+B/op\s+(\d+)\s+allocs/op`)

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		matches := re.FindStringSubmatch(line)
		if len(matches) == 5 {
			name := matches[1]
			nsPerOp, _ := strconv.ParseInt(matches[2], 10, 64)
			bytesAlloc, _ := strconv.ParseInt(matches[3], 10, 64)
			allocs, _ := strconv.ParseInt(matches[4], 10, 64)

			result := BenchResult{
				Name:       name,
				NsPerOp:    nsPerOp,
				Allocs:     allocs,
				BytesAlloc: bytesAlloc,
			}

			category := getCategoryFromName(name)
			results[category] = append(results[category], result)
		}
	}

	// 分析并打印结果
	for category, benchResults := range results {
		if len(benchResults) == 0 {
			continue
		}

		fmt.Printf("\n=== %s ===\n", category)
		
		// 按类型分组
		typeResults := make(map[string]BenchResult)
		for _, result := range benchResults {
			typeName := getTypeFromName(result.Name)
			if existing, exists := typeResults[typeName]; !exists || result.NsPerOp < existing.NsPerOp {
				typeResults[typeName] = result
			}
		}

		// 排序并显示
		var types []string
		for typeName := range typeResults {
			types = append(types, typeName)
		}
		sort.Strings(types)

		for _, typeName := range types {
			result := typeResults[typeName]
			fmt.Printf("%-10s: %8d ns/op, %6d B/op, %4d allocs/op\n", 
				typeName, result.NsPerOp, result.BytesAlloc, result.Allocs)
		}

		// 性能对比
		if len(typeResults) > 1 {
			baseline := typeResults["Native"]
			fmt.Println("\nPerformance relative to Native:")
			for _, typeName := range types {
				if typeName == "Native" {
					continue
				}
				result := typeResults[typeName]
				speedRatio := float64(result.NsPerOp) / float64(baseline.NsPerOp)
				memRatio := float64(result.BytesAlloc) / float64(baseline.BytesAlloc)
				fmt.Printf("%-10s: %.2fx speed, %.2fx memory\n", typeName, speedRatio, memRatio)
			}
		}
	}
}

func getCategoryFromName(name string) string {
	if strings.Contains(name, "Marshal") && strings.Contains(name, "Slice") {
		return "Batch Marshaling"
	} else if strings.Contains(name, "Marshal") {
		return "Single Marshaling"
	} else if strings.Contains(name, "Unmarshal") {
		return "Single Unmarshaling"
	} else if strings.Contains(name, "MemoryUsage") {
		return "Memory Usage"
	}
	return "Other"
}

func getTypeFromName(name string) string {
	if strings.Contains(name, "Native") {
		return "Native"
	} else if strings.Contains(name, "Pointer") {
		return "Pointer"
	} else if strings.Contains(name, "Null") {
		return "Null"
	}
	return "Unknown"
}
EOF

go run analyze_results.go

echo
echo "=== Recommendations ==="
echo "Based on the benchmark results:"
echo "1. For maximum performance: Use native types if you don't need null handling"
echo "2. For balance of features and performance: Use pointers with omitempty"
echo "3. For best null handling and API clarity: Use guregu/null"
echo "4. Consider your specific use case:"
echo "   - High-frequency APIs: Native or Pointer types"
echo "   - Data with many optional fields: guregu/null"
echo "   - Database integration: guregu/null or sql.Null* types"

# 清理临时文件
rm -f analyze_results.go