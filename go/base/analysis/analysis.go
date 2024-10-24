package main

import (
	"fmt"
	"go/ast"
	"go/token"
	"go/types"
	"strings"

	"golang.org/x/tools/go/analysis"
)

var Analyzer = &analysis.Analyzer{
	Name: "goprintffuncname",
	Doc:  "Checks that printf-like functions are named with `f` at the end.",
	Run:  run,
}

func run(pass *analysis.Pass) (interface{}, error) {
	inspect := func(node ast.Node) bool {
		if node == nil {
			return true
		}
		// post := pass.Fset.Position(node.Pos())
		// fmt.Println(post)

		switch n := node.(type) {
		// Comments and fields
		case *ast.FuncDecl:
			// FuncDecl(pass, node, n)
			fmt.Println("funcDecl", n.Name)
			for _, f := range n.Type.Params.List {
				fmt.Println("params", f.Names, f.Type, f.)
			}
		case *ast.GenDecl:
		case *ast.AssignStmt:
			if n.Tok == token.DEFINE {
				for _, expr := range n.Lhs {
					fmt.Println(expr.(*ast.Ident).Obj)
				}
				for _, expr := range n.Rhs {
					e := expr.(*ast.CompositeLit).Type.(*ast.Ident)
					s := pass.Pkg.Scope().Lookup(e.Name).Type().Underlying().(*types.Struct)
					for i := 0; i < s.NumFields(); i++ {
						fmt.Println(s.Field(i).Name())
					}
					// fmt.Println(pass.Pkg.Scope().Lookup(e.Name).Type().Underlying().(*types.Struct))
					// fmt.Println(pass.TypesInfo.Types[expr])
				}
			}
		}
		return true
	}

	for _, f := range pass.Files {
		ast.Inspect(f, inspect)
	}
	return nil, nil
}

func FuncDecl(pass *analysis.Pass, node ast.Node, funcDecl *ast.FuncDecl) bool {
	params := funcDecl.Type.Params.List
	if len(params) != 2 { // [0] must be format (string), [1] must be args (...interface{})
		return true
	}

	firstParamType, ok := params[0].Type.(*ast.Ident)
	if !ok { // first param type isn't identificator so it can't be of type "string"
		return true
	}

	if firstParamType.Name != "string" { // first param (format) type is not string
		return true
	}

	secondParamType, ok := params[1].Type.(*ast.Ellipsis)
	if !ok { // args are not ellipsis (...args)
		return true
	}

	elementType, ok := secondParamType.Elt.(*ast.InterfaceType)
	if !ok { // args are not of interface type, but we need interface{}
		return true
	}

	if elementType.Methods != nil && len(elementType.Methods.List) != 0 {
		return true // has >= 1 method in interface, but we need an empty interface "interface{}"
	}

	if strings.HasSuffix(funcDecl.Name.Name, "f") {
		return true
	}

	pass.Reportf(node.Pos(), "printf-like formatting function '%s' should be named '%sf'",
		funcDecl.Name.Name, funcDecl.Name.Name)
	return true
}
