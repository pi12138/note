package packagedemo

import (
	_ "base/package-demo/packageA"
	packageb "base/package-demo/packageB"
	packagec "base/package-demo/packageC"
)

// package 只要被 import 了都会执行 init

func Exec() {
	if true {
		packageb.Do()
	}
	if false {
		packagec.Do()
	}
}

// >>
// packagea init exec.
// packageb init exec.
// packagec init exec.
// packageb Do exec.
