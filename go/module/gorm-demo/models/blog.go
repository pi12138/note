package models

type Blog struct {
	Id       uint
	Title    string
	AuthorId uint

	// fk
	Author Author `gorm:"foreignKey:AuthorId"`
}
