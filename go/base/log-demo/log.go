package logdemo

import (
	"fmt"
	"log"
	"os"
	"runtime"
)

var (
	logger *log.Logger
	level  uint
)

const (
	DebugLevel = 10
	InfoLevel  = 20
	WarnLevel  = 30
	ErrorLevel = 40
)

func init() {
	// 设置样式
	file, err := os.OpenFile("./demo.log", os.O_RDWR|os.O_CREATE|os.O_APPEND, 0766)
	if err != nil {
		log.Printf("[initLog] open file error: %s", err)
		return
	}
	logger = log.New(file, "", log.Ldate|log.Ltime|log.Lshortfile)
	log.Println("[initLog] 初始化log成功")
}

func SetLevel(l uint) {
	level = l
}

// // 这个会有性能代价
func getCallerInfo() string {
	_, file, lineNo, ok := runtime.Caller(2)
	if !ok {
		file = "???"
		lineNo = 0
	}
	return fmt.Sprintf("Caller: %s:%d", file, lineNo)
}

func Infof(format string, v ...any) {
	if isLevelEnable(InfoLevel) {
		logger.SetPrefix("[INFO] ")
		logger.Output(2, fmt.Sprintf(format, v...))
	}
}

func Debugf(format string, v ...any) {
	if isLevelEnable(DebugLevel) {
		logger.SetPrefix("[DEBUG] ")
		logger.Output(2, fmt.Sprintf(format, v...))
	}
}

func Warnf(format string, v ...any) {
	if isLevelEnable(WarnLevel) {
		logger.SetPrefix("[WARNING] ")
		logger.Output(2, fmt.Sprintf(format, v...))
	}
}

func Errorf(format string, v ...any) {
	if isLevelEnable(ErrorLevel) {
		logger.SetPrefix("[ERROR] ")
		logger.Output(2, fmt.Sprintf(format, v...))
	}
}

func isLevelEnable(l uint) bool {
	return l >= level
}
