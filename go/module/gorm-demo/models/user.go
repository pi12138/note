package models

import (
	"database/sql/driver"
	"encoding/json"
	"log"
	"reflect"

	"gorm.io/datatypes"
	"gorm.io/gorm"
)

type Profile struct {
	School         string `json:"school,omitempty"`
	Score          int    `json:"score,omitempty"`
	IsSuperStudent bool   `json:"is_super_student,omitempty"`
}

type FieldOne struct {
	One string `json:"one"`
	Two string `json:"two"`
}

func (r *Profile) Scan(value interface{}) error {
	vt := reflect.TypeOf(value)
	log.Printf("vt Name: %s, vt Kind: %s, value: %s", vt.Name(), vt.Kind(), string(value.([]byte)))
	err := json.Unmarshal(value.([]byte), r)
	return err
}

func (r Profile) Value() (driver.Value, error) {
	value, err := json.Marshal(r)
	return string(value), err
}

type User struct {
	gorm.Model
	Name         string
	Info         datatypes.JSON // {"height": 180, "weight": 80}
	UsernameList datatypes.JSON // ["oldName", "newName"]
	// Pf           Profile
	// FatherId     *uint
	// PfP          *Profile
	// Usernames    []string   `gorm:"type:text"`
	// Usernames2   []string   `gorm:"serializer:json"`
	// One          FieldOne   `gorm:"serializer:json"`
	// Ones         []FieldOne `gorm:"serializer:json"`

	// CreditCards []CreditCard
	// Father      *User `gorm:"foreignKey:FatherId"`
}
