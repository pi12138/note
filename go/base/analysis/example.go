package main

import "log"

type Man struct {
	name string
}

func (m *Man) SetName(s string) {
	m.name = s
}

func myLog(format string, args ...interface{}) {
	const prefix = "[my] "
	log.Printf(prefix+format, args...)
}

func NewMan(s string) Man {
	m := Man{}
	m.SetName(s)
	return m
}
