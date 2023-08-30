package clog

import (
	"fmt"
	"log"
	"os"
)

var (
	logger  *log.Logger
	level   uint
	logFile *os.File
)

const (
	debugLevel = 10
	infoLevel  = 20
	warnLevel  = 30
	errorLevel = 40
)

func init() {
	Init()
}

func Init() {
	file, err := os.OpenFile("./base.log", os.O_RDWR|os.O_CREATE|os.O_APPEND, 0766)
	if err != nil {
		log.Printf("[initLog] open file error: %s", err)
		return
	}
	logger = log.New(file, "", log.Ldate|log.Ltime|log.Lshortfile)
	logFile = file
	SetLevel(debugLevel)
	Infof("[initLog] 初始化log成功")
}

func Close() {
	logFile.Close()
}

func SetLevel(l uint) {
	level = l
}

func Infof(format string, v ...any) {
	if isLevelEnable(infoLevel) {
		logger.SetPrefix("[INFO] ")
		logger.Output(2, fmt.Sprintf(format, v...))
	}
}

func Debugf(format string, v ...any) {
	if isLevelEnable(debugLevel) {
		logger.SetPrefix("[DEBUG] ")
		logger.Output(2, fmt.Sprintf(format, v...))
	}
}

func Warnf(format string, v ...any) {
	if isLevelEnable(warnLevel) {
		logger.SetPrefix("[WARNING] ")
		logger.Output(2, fmt.Sprintf(format, v...))
	}
}

func Errorf(format string, v ...any) {
	if isLevelEnable(errorLevel) {
		logger.SetPrefix("[ERROR] ")
		logger.Output(2, fmt.Sprintf(format, v...))
	}
}

func isLevelEnable(l uint) bool {
	return l >= level
}
