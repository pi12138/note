package db

import (
	"fmt"
	"os"

	"gorm.io/driver/mysql"
	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
	"gorm.io/gorm/logger"
)

const (
	HOST     = "localhost"
	PORT     = 3306
	USER     = "gormdemo"
	PASSWORD = "password"
	DBNAME   = "gormdemo"
)

var db *gorm.DB

func InitMysqlDB() {
	dsn := fmt.Sprintf("%s:%s@tcp(%s:%d)/%s?charset=utf8&parseTime=True&loc=Local", USER, PASSWORD, HOST, PORT, DBNAME)
	var err error
	db, err = gorm.Open(mysql.Open(dsn), &gorm.Config{
		Logger: logger.Default.LogMode(logger.Info),
	})
	if err != nil {
		os.Exit(1)
	}
}

func InitSqliteDB() {
	var err error
	db, err = gorm.Open(sqlite.Open("gorm.db"), &gorm.Config{
		Logger: logger.Default.LogMode(logger.Info),
	})
	if err != nil {
		os.Exit(1)
	}
}

func GetDB() *gorm.DB {
	if db == nil {
		InitSqliteDB()
	}
	return db
}
