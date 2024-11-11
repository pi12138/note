package db

import (
	"fmt"
	"gorm-demo/models"
	"testing"

	"gorm.io/gorm"
)

func TestInitSqliteDB(t *testing.T) {
	tests := []struct {
		name string
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			InitSqliteDB()
		})
	}
}

func TestGormSession(t *testing.T) {
	InitSqliteDB()
	if err := db.AutoMigrate(&models.Author{}); err != nil {
		t.Errorf("AutoMigrate error. %s", err)
	}
	if err := db.Callback().Create().After("gorm:commit_or_rollback_transaction").Register("TestGormSession:Print", func(d *gorm.DB) {
		fmt.Println("commit_or_rollback_transaction after")
	}); err != nil {
		t.Errorf("Callback Register error. %s", err)
	}

	var author1 models.Author
	author1.Name = "author1"
	if err := db.Create(&author1).Error; err != nil {
		t.Errorf("Create author1 error. %s", err)
	} else {
		defer func(a models.Author) {
			if err := db.Delete(&a).Error; err != nil {
				t.Errorf("Delete a error. %s", err)
			}
		}(author1)
	}

	// authors := make([]models.Author, 0)
	// db.Find(&authors)

}

func TestGormSession2(t *testing.T) {
	InitSqliteDB()
	if err := db.AutoMigrate(&models.Author{}); err != nil {
		t.Errorf("AutoMigrate error. %s", err)
	}
	if err := db.Callback().Create().After("gorm:commit_or_rollback_transaction").Register("TestGormSession:Print", func(d *gorm.DB) {
		t.Log("commit_or_rollback_transaction after")
	}); err != nil {
		t.Errorf("Callback Register error. %s", err)
	}
	// sess1 := db.Session(&gorm.Session{
	// 	NewDB: true,
	// })
	// sess2 := db.Session(&gorm.Session{
	// 	NewDB: true,
	// })

	var author1 models.Author
	author1.Name = "author1"
	if err := db.Transaction(func(tx *gorm.DB) error {
		return tx.Create(&author1).Error
	}); err != nil {
		t.Errorf("db.Transaction error. %s", err)
	} else {
		defer func(a models.Author) {
			if err := db.Delete(&a).Error; err != nil {
				t.Errorf("Delete a error. %s", err)
			}
		}(author1)
	}

	// authors := make([]models.Author, 0)
	// db.Find(&authors)

}

func TestGormSession3(t *testing.T) {
	InitSqliteDB()
	if err := db.AutoMigrate(&models.Author{}); err != nil {
		t.Errorf("AutoMigrate error. %s", err)
	}
	if err := db.Callback().Create().After("gorm:commit_or_rollback_transaction").Register("TestGormSession:Print", func(d *gorm.DB) {
		t.Log("commit_or_rollback_transaction after")
		var authors []models.Author

		if err := d.Find(&authors).Error; err != nil {
			t.Errorf("d.Find(&authors) error. %s", err)
		} else {
			t.Log(authors)
		}
		if err := d.Session(&gorm.Session{
			NewDB: true,
		}).Find(&authors).Error; err != nil {
			t.Errorf("d.Find(&authors) error. %s", err)
		} else {
			t.Log(authors)
		}
	}); err != nil {
		t.Errorf("Callback Register error. %s", err)
	}

	var tranDB *gorm.DB
	var author1 models.Author
	author1.Name = "author1"
	if err := db.Transaction(func(tx *gorm.DB) error {
		tranDB = tx.Session(&gorm.Session{NewDB: true, Initialized: true})
		return tx.Create(&author1).Error
	}); err != nil {
		t.Errorf("db.Transaction error. %s", err)
	} else {
		defer func(a models.Author) {
			if err := db.Delete(&a).Error; err != nil {
				t.Errorf("Delete a error. %s", err)
			}
		}(author1)
	}

	if err := tranDB.Find(&author1, author1.Id).Error; err != nil {
		t.Errorf("tranDB.Find error. %s", err)
	} else {
		t.Log(author1)
	}
	if err := tranDB.Session(&gorm.Session{
		NewDB:       true,
		Initialized: true,
	}).Find(&author1, author1.Id).Error; err != nil {
		t.Errorf("tranDB.Find error. %s", err)
	} else {
		t.Log(author1)
	}

	*tranDB = *db
	if err := tranDB.Session(&gorm.Session{
		NewDB: true,
	}).Find(&author1, author1.Id).Error; err != nil {
		t.Errorf("tranDB.Find error. %s", err)
	} else {
		t.Log(author1)
	}
}
