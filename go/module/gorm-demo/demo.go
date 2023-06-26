package main

import (
	"fmt"
	database "gorm-demo/db"
	"gorm-demo/models"

	"gorm.io/gorm"
)

func TestOrm() {
	var db = database.GetDB()

	var user models.User
	tx1 := db.Model(models.User{})
	tx2 := tx1.Where("id = ?", 10).First(&user)
	tx2.Find(&user)

	fmt.Println(tx1 == tx2)

	err := db.Transaction(func(tx *gorm.DB) error {
		// tx = tx.Last(&user)
		// // tx = tx.Model(models.User{}).Where("id = ?", 10).First(&user)
		// // fmt.Println(tx1 == tx2, tx == tx1)
		// user.ID *= 10
		// tx = tx.Create(&user)
		// user.ID *= 10
		// tx = tx.Create(&user)
		tx = tx.Create(&models.CreditCard{})
		tx = tx.Last(&user)
		return tx.Error
	})
	fmt.Println(err)

}

func TestUpdate() {
	var db = database.GetDB()

	a1 := models.Author{
		Name: "author1",
	}
	a2 := models.Author{
		Name: "author2",
	}

	b1 := models.Blog{
		Title: "bolg1",
	}

	var count int64
	if db.Where(a1).Count(&count); count == 0 {
		db.Create(&a1)
	} else {
		db.Where(a1).First(&a1)
	}
	if db.Where(a2).Count(&count); count == 0 {
		db.Create(&a2)
	} else {
		db.Where(a2).First(&a2)
	}

	if db.Where(b1).Count(&count); count == 0 {
		b1.AuthorId = a1.Id
		db.Create(&b1)
	} else {
		db.Where(b1).Preload("Author").First(&b1)
	}

	// 下面进行修改
	// 把 AuthorId 从 a1.Id -> a2.Id

	db.Where(b1).Preload("Author").First(&b1)
	fmt.Println("1---", b1.AuthorId, b1.Author.Id)

	b1.AuthorId = a2.Id
	fmt.Println("2---", b1.AuthorId, b1.Author.Id)
	db.Save(&b1)
	fmt.Println("3---", b1.AuthorId, b1.Author.Id)
	db.Where(b1).Preload("Author").First(&b1)
	fmt.Println("4---", b1.AuthorId, b1.Author.Id)

}

func TestDel() {
	db := database.GetDB()

	var count int64
	if db.Model(&models.Author{}).Where("`name` = ?", "authDel").Count(&count); count == 0 {
		a1 := models.Author{
			Name: "authDel",
			Blogs: []models.Blog{
				{
					Title: "one",
				},
				{
					Title: "two",
				},
			},
			Company: models.Company{
				Name: "CompanyOne",
			},
		}
		db.Create(&a1)
	}

	var a1 models.Author

	db.Model(&models.Author{}).Where("`name` = ?", "authDel").Preload("Blogs").Preload("Company").First(&a1)
	// > DELETE FROM `blogs` WHERE `blogs`.`author_id` = 1
	// > DELETE FROM `authors` WHERE `authors`.`id` = 1
	// 会删除 has many 的 Blogs
	// 但是不会删除 belongs to 的 Company
	// 官方文档: You are allowed to delete selected has one/has many/many2many relations with Select when deleting records
	db.Select("Blogs", "Company").Delete(&a1)

	/*
		db.Model(&models.Author{}).Where("`name` = ?", "authDel").Preload("Blogs").First(&a1)
		// > DELETE FROM `authors` WHERE `authors`.`id` = 1
		// 不会删除关联关系
		db.Delete(&a1)
	*/

	/*
		db.Model(&models.Author{}).Where("`name` = ?", "authDel").Preload("Blogs").First(&a1)
		// > DELETE FROM `blogs` WHERE `blogs`.`author_id` = 1
		// > DELETE FROM `authors` WHERE `authors`.`id` = 1
		// 将加载出来的 Blogs 删除
		db.Select("Blogs").Delete(&a1)
	*/
}
