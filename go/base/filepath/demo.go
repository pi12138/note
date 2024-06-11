package filepath

import (
	"fmt"
	"os"
	"path/filepath"
)

func Demo() {
	mats, err := filepath.Glob("/opt/share/nginx/nginx.conf")
	if err != nil {
		errExit(err)
	}

	fmt.Println(mats)

	mats, err = filepath.Glob("/opt/share/nginx/conf.d/*.conf")
	if err != nil {
		errExit(err)
	}

	fmt.Println(mats)

	mats, err = filepath.Glob("/opt/xxx/*.conf")
	if err != nil {
		errExit(err)
	}

	fmt.Println(mats)
}

func errExit(err error) {
	fmt.Println(err)
	os.Exit(1)
}
