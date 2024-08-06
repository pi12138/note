package select_

import (
	"encoding/json"
	"fmt"
	database "gorm-demo/db"
	M "gorm-demo/models"
	"log"
)

var db = database.GetDB()

// preload 会产生两次 sql
func UseForeignKeyPreload() {
	var card M.CreditCard
	db.Preload("User").First(&card)
	// 这个地方 sql 查询的日志存在问题， 数据库中是先查询 credit_cards 然后在查询的 users
	// [0.607ms] [rows:1] SELECT * FROM `users` WHERE `users`.`id` = 1 AND `users`.`deleted_at` IS NULL
	// [1.537ms] [rows:1] SELECT * FROM `credit_cards` WHERE `credit_cards`.`deleted_at` IS NULL ORDER BY `credit_cards`.`id` LIMIT 1

	// log.Printf("user: %v", card.User) // > 2022/10/31 17:27:01 user: {{1 2022-10-31 17:10:22.687 +0800 CST 2022-10-31 17:10:22.687 +0800 CST {0001-01-01 00:00:00 +0000 UTC false}} name1}
}

// joins 只会参生一次查询
func UseForeignKeyJoins() {
	var card M.CreditCard
	db.Joins("User").First(&card)
	// [0.591ms] [rows:1] SELECT `credit_cards`.`id`,`credit_cards`.`created_at`,`credit_cards`.`updated_at`,`credit_cards`.`deleted_at`,`credit_cards`.`number`,`credit_cards`.`user_id`,`User`.`id` AS `User__id`,`User`.`created_at` AS `User__created_at`,`User`.`updated_at` AS `User__updated_at`,`User`.`deleted_at` AS `User__deleted_at`,`User`.`name` AS `User__name` FROM `credit_cards` LEFT JOIN `users` `User` ON `credit_cards`.`user_id` = `User`.`id` AND `User`.`deleted_at` IS NULL WHERE `credit_cards`.`deleted_at` IS NULL ORDER BY `credit_cards`.`id` LIMIT 1

	// log.Printf("user: %v", card.User) // > 2022/10/31 17:29:47 user: {{1 2022-10-31 17:10:22.687 +0800 CST 2022-10-31 17:10:22.687 +0800 CST {0001-01-01 00:00:00 +0000 UTC false}} name1}
}

func ManyIns() {
	var cards []M.CreditCard
	db.Where("id IN ?", []uint{1, 2, 4}).Preload("User").Preload("BelongTo").Find(&cards)

	// for _, ins := range cards {
	// 	fmt.Println(ins.BelongTo)
	// }
}

func JsonUse() {
	var user M.User
	db.First(&user)
	fmt.Printf("type[Info: %T, UsernameList: %T]]\n", user.Info, user.UsernameList) // > type[Info: datatypes.JSON, UsernameList: datatypes.JSON]
	fmt.Printf("value[Info: %v, UsernameList: %v]\n", user.Info, user.UsernameList) // > value[Info: {"height": 180, "weight": 80}, UsernameList: ["Old Name", "New Name"]]

	// 取数据使用
	data := make(map[string]int)
	if err := json.Unmarshal([]byte(user.Info.String()), &data); err != nil {
		fmt.Printf("err: %s", err)
	}
	fmt.Printf("data: %v\n", data)
}

func ManyWhere() {
	var user M.User
	// [0.450ms] [rows:1] SELECT * FROM `users` WHERE id IN (1,2,3,4) AND `users`.`name` = 'name1' AND `users`.`deleted_at` IS NULL ORDER BY `users`.`id` LIMIT 1
	db.Where("id IN ?", []uint{1, 2, 3, 4}).Where(&M.User{Name: "name1"}).First(&user)

	res := db.Where("id IN ?", []uint{1, 2, 3, 4}).Where(&M.User{Name: "name1"})
	fmt.Println(res.Statement.Clauses)
	for key, value := range res.Statement.Clauses {
		fmt.Printf("key: %v, value: %v\n", key, value)
	}
	var users []M.User
	res.Find(&users)
	fmt.Printf("len users: %d\n", len(users))
}

func CustomDataStruct() {
	var user M.User
	if r := db.First(&user); r.Error != nil {
		log.Printf("error: %s", r.Error)
	}
	fmt.Printf("user: %v\n", user)
	// log.Printf("user pf: %v", user.Pf)
	p := M.Profile{}
	data, _ := json.Marshal(p)
	fmt.Printf("data: %s\n", data)

	p2 := M.Profile{}
	if err := json.Unmarshal(data, &p2); err != nil {
		fmt.Printf("error: %s\n", err)
	} else {
		fmt.Printf("p2: %v\n", p2)
	}

	newUser := M.User{
		Name: "test",
	}
	db.Save(&newUser)

}

func Association() {
	var user M.User
	var cards []M.CreditCard
	db.Where("id IN (?)", db.Model(&M.CreditCard{}).Where("user_id IS NOT NULL").Select("user_id")).First(&user)

	db.Model(&user).Association("CreditCards").Find(&cards)
	log.Printf("user: %v, len(cards): %d", user, len(cards))

	// batch
	var users []M.User
	var BatchCards []M.CreditCard
	db.Where("id IN (?)", db.Model(&M.CreditCard{}).Where("user_id IS NOT NULL").Select("user_id")).Find(&users)

	db.Model(&users).Association("CreditCards").Find(&BatchCards)
	log.Printf("len(users): %v, len(BatchCards): %d", len(users), len(BatchCards))
}

func QueryUseInstance() {
	var cards []M.CreditCard
	db.Model(&M.CreditCard{}).Where("user_id IS NOT NULL").Find(&cards)

	// var subCards []M.CreditCard
	subCards := make([]M.CreditCard, 0)
	log.Printf("subCards type:  %T", subCards)
	db.Model(&cards).Where("id > ?", 25).Find(subCards)

	var cl, scl []uint
	for _, c := range cards {
		cl = append(cl, c.ID)
	}
	for _, c := range subCards {
		scl = append(scl, c.ID)
	}
	log.Printf("cl: %v, scl: %v", cl, scl)
}

// func SelfRelation() {
// 	var user M.User
// 	db.Where("id = ?", 21).Preload("Father").First(&user)
// 	log.Printf("Father: %v", user.Father)
// }

// func DefaultValue() {
// 	var user M.User
// 	db.Where("id = ?", 21).First(&user)
// 	fmt.Printf("user id: %d, user cards: %#v, isnil: %t len: %d, usernames: %#v\n", user.ID, user.CreditCards, user.CreditCards == nil,
// 		len(user.CreditCards), user.Usernames)
// 	fmt.Println(user.One, user.Ones)

// 	db.Model(&user).Association("CreditCards").Find(&user.CreditCards)
// 	fmt.Printf("user id: %d, user cards: %#v, isnil: %t len: %d\n", user.ID, user.CreditCards, user.CreditCards == nil, len(user.CreditCards))

// 	// var card M.CreditCard
// 	// db.Where("id = ?", 21).First(&card)
// 	// fmt.Printf("card id: %d, user: %#v, belongto: %#v\n", card.ID, card.User, card.BelongTo)
// 	// db.Model(&card).Association("User").Find(card.User)
// 	// db.Model(&card).Association("BelongTo").Find(&card.BelongTo)
// 	// fmt.Printf("card id: %d, user: %#v, belongto: %#v\n", card.ID, card.User, card.BelongTo)
// }

func Demo() {
	// UseForeignKeyPreload()
	// UseForeignKeyJoins()
	// ManyIns()
	// JsonUse()
	// ManyWhere()
	// CustomDataStruct()
	// Association()
	// QueryUseInstance()
	// SelfRelation()
	// DefaultValue()
}
