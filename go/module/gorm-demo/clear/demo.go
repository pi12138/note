package clear

import (
	database "gorm-demo/db"
	M "gorm-demo/models"
)

var db = database.GetDB()

func ClearData() {
	var users []M.User
	var cards []M.CreditCard

	db.Find(&users)
	db.Find(&cards)

	db.Delete(&users)
	db.Delete(&cards)
}
