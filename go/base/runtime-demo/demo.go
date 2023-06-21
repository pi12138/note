package runtimedemo

import (
	"fmt"
	"runtime"
	"strings"
	"sync"
)

var (

	// qualified package name, cached at first use
	logrusPackage string

	// Positions in the call stack when tracing to report the calling method
	minimumCallerDepth int

	// Used for caller information initialisation
	callerInitOnce sync.Once
)

const (
	maximumCallerDepth int = 25
	knownLogrusFrames  int = 3
)

func init() {
	// start at the bottom of the stack before the package-name cache is primed
	minimumCallerDepth = 1
}

func Callers() {
	rpc := make([]uintptr, 10)
	fmt.Println(runtime.Callers(0, rpc))

	cfs := runtime.CallersFrames(rpc)
	for f, ok := cfs.Next(); ok; f, ok = cfs.Next() {
		fmt.Println(f.Function, f.Line, f.File, f.Entry, runtime.FuncForPC(f.Entry).Name())
	}

	fmt.Println(getPackageName("/root/github_projects/go/base/runtime-demo/demo.go"))
	fmt.Println(getCaller())
}

func getCaller() *runtime.Frame {
	// cache this package's fully-qualified name
	callerInitOnce.Do(func() {
		pcs := make([]uintptr, maximumCallerDepth)
		_ = runtime.Callers(0, pcs)

		// dynamic get the package name and the minimum caller depth
		for i := 0; i < maximumCallerDepth; i++ {
			funcName := runtime.FuncForPC(pcs[i]).Name()
			if strings.Contains(funcName, "getCaller") {
				logrusPackage = getPackageName(funcName)
				fmt.Printf("logrusPackage: %s, funcName: %s\n", logrusPackage, funcName)
				break
			}
		}

		minimumCallerDepth = knownLogrusFrames
	})

	// Restrict the lookback frames to avoid runaway lookups
	pcs := make([]uintptr, maximumCallerDepth)
	depth := runtime.Callers(minimumCallerDepth, pcs)
	frames := runtime.CallersFrames(pcs[:depth])
	fmt.Printf("depth: %d\n", depth)
	for f, again := frames.Next(); again; f, again = frames.Next() {
		fmt.Println(f.Function, f.Line, f.File)
		pkg := getPackageName(f.Function)

		// If the caller isn't part of this package, we're done
		if pkg != logrusPackage {
			return &f //nolint:scopelint
		}
	}

	// if we got here, we failed to find the caller's context
	return nil
}

func getPackageName(f string) string {
	for {
		lastPeriod := strings.LastIndex(f, ".")
		lastSlash := strings.LastIndex(f, "/")
		if lastPeriod > lastSlash {
			f = f[:lastPeriod]
		} else {
			break
		}
	}

	return f
}
