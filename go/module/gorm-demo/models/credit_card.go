package models

import (
	"fmt"

	"gorm.io/gorm"
)

type CreditCard struct {
	gorm.Model
	Number string
	UserID uint `gorm:"default:null"`

	// foreign key object
	User     *User `gorm:"foreignKey:UserID"`
	BelongTo User `gorm:"foreignKey:UserID"`
}

func (r *CreditCard) String() string {
	return fmt.Sprintf("Card{Number: %s, UserId: %d}", r.Number, r.UserID)
}
