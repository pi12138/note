package time_demo

import (
	"fmt"
	"time"
)

func FormatTime() {
	a := time.Now()

	fmt.Println(a.String())
	fmt.Println(a.Format(time.RFC3339))
	fmt.Println(a.Format(time.RFC3339Nano))
}
