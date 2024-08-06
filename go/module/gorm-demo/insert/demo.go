package insert

import (
	"fmt"
	database "gorm-demo/db"
	M "gorm-demo/models"

	"gorm.io/gorm"
)

var db = database.GetDB()

// func CreateUser(db *gorm.DB) error {
// 	var users []M.User
// 	for index, _ := range make([]int, 10) {
// 		u := M.User{
// 			Name:         fmt.Sprintf("name%d", index+1),
// 			Info:         datatypes.JSON([]byte(`{"height": 180, "weight": 80}`)), // json insert
// 			UsernameList: datatypes.JSON([]byte(`["Old Name", "New Name"]`)),
// 			Pf:           M.Profile{School: "china", Score: 100, IsSuperStudent: false},
// 		}
// 		users = append(users, u)
// 	}

// 	if result := db.Create(&users); result.Error != nil {
// 		return result.Error
// 	}
// 	return nil
// }

func CreateCreditCard(db *gorm.DB) error {
	var cards []M.CreditCard
	var users []M.User
	db.Find(&users)
	for index, user := range users {
		var userId uint
		if user.ID%2 == 0 {
			userId = user.ID
		}
		c := M.CreditCard{
			Number: fmt.Sprintf("number%d", index),
			UserID: userId,
		}
		cards = append(cards, c)
	}
	if result := db.Create(&cards); result.Error != nil {
		return result.Error
	}
	return nil
}

// func AddUsernames() {
// 	var user M.User
// 	db.Where("id = ?", 21).First(&user)
// 	// user.Usernames = []string{"firstname"}
// 	user.Usernames = nil
// 	user.Usernames2 = []string{"firstname", "secondname", "lastname"}
// 	db.Save(&user)
// }

func Demo() {
	// db.Transaction(func(tx *gorm.DB) error {
	// 	if err := CreateUser(tx); err != nil {
	// 		return err
	// 	}

	// 	if err := CreateCreditCard(tx); err != nil {
	// 		return err
	// 	}
	// 	return nil
	// })
	// CreateUser(db)
	SaveList()
}

func SaveList() {
	var users []M.User
	if err := db.Find(&users).Error; err != nil {
		panic(err)
	}
	for i := 0; i < len(users); i++ {
		users[i].Name = fmt.Sprintf("%s--%d", users[i].Name, i)
	}

	if err := db.Save(&users).Error; err != nil {
		panic(err)
	}
}
