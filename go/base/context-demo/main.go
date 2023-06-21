package contextdemo

import (
	"context"
	"fmt"
)

func Demo() {
	ctx := context.Background()
	FuncOne(ctx)
	fmt.Println(ctx.Value("key"))
}

func FuncOne(ctx context.Context) {
	ctx = context.WithValue(ctx, "key", "value")
}
