package main

import (
	"fmt"
	"os"

	"github.com/tufanbarisyildirim/gonginx/config"
	"github.com/tufanbarisyildirim/gonginx/parser"
)

func parseCfg(path string) *config.Config {
	par, err := parser.NewParser(path)
	if err != nil {
		exitByErr(err)
	}
	cfg, err := par.Parse()
	if err != nil {
		exitByErr(err)
	}
	return cfg
}

func main() {
	cfg := parseCfg("/opt/share/nginx/nginx.conf")
	cfg.FindUpstreams()
	directives := cfg.FindDirectives("include")
	var includeFiles = make([]string, 0)
	// var parsedIncludes = make(map[*config.Include]*config.Config)
	for _, i := range directives {
		fmt.Println(i)
		include, ok := i.(*config.Include)
		if ok {
			// fmt.Println("include", include)
			// parsedIncludes[include] = parseCfg(include.IncludePath)
			fmt.Println(include.IncludePath, include.Configs)

			if v, ok := include.GetParent().(*config.Block); ok {
				fmt.Println("HTTP", v.GetName())
			}
		}
		includeFiles = append(includeFiles, i.GetParameters()...)
	}

}

func exitByErr(err error) {
	fmt.Println(err)
	os.Exit(1)
}
