package models

type Author struct {
	Id    uint
	Name  string
	Email string

	CompanyId uint

	// fk
	Blogs   []Blog
	Company Company `gorm:"foreignKey:CompanyId"`
}
