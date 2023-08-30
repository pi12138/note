package main

import (
	"fmt"
	"runtime"
	"sync"
)

func main() {
	// 设置要使用的 CPU 核心数
	numCPU := runtime.NumCPU()
	runtime.GOMAXPROCS(numCPU)

	// 设置要使用的 CPU 百分比
	cpuPercentage := 90

	// 计算要使用的 goroutine 数量
	numGoroutines := int(float64(numCPU) * (float64(cpuPercentage) / 100.0))

	// 使用 WaitGroup 来等待所有 goroutine 完成
	var wg sync.WaitGroup
	wg.Add(numGoroutines)

	// 启动 goroutine 来模拟 CPU 密集型任务
	for i := 0; i < numGoroutines; i++ {
		go func() {
			// 模拟 CPU 密集型任务
			for {
				// 无限循环进行计算
			}
			wg.Done()
		}()
	}

	// 等待所有 goroutine 完成
	wg.Wait()
	fmt.Println("CPU load completed.")
}
