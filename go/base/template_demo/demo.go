package template_demo

import (
	"fmt"
	"os"
	"text/template"
)

var tem = `{{ $.not_exist }}
{{     $.exist     }}
{{ $ }}
{{ $a := $.exist }}
{{ $a }}
{{ range $i, $v := $.list }}
	index: {{ $i }} -- value: {{ $v }}
{{ end }}

{{ if $.none }}
	this is not nil
{{ else }}
	this is nil
{{end}}

{{ if $.value }}
	value: {{ $.value }}
{{ else }}
	value: nil
{{ end }}
`

func TemplateDemo() {
	t, err := template.New("test").Parse(tem)
	if err != nil {
		fmt.Printf("error: %s\n", err)
		os.Exit(1)
	}
	t.Execute(os.Stdout, map[string]any{"exist": true, "list": []int{1, 2, 3}, "none": nil, "value": 10})
}
