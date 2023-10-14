package repository

import (
	"github.com/dkshi/banklocsrv"
	"github.com/jmoiron/sqlx"
)

type Authorization interface {
	CreateUser(banklocsrv.User) (int, error)
	GetUser(string, string) (banklocsrv.User, error)
}

type Atms interface {
	GetAtms() (*[]banklocsrv.ATM, error)
	SelectAtms(filters banklocsrv.AtmsFilters) (*[]banklocsrv.ATM, error)
}

type Offices interface {
	GetOffices() (*[]banklocsrv.Office, error)
	SelectOffices(filters banklocsrv.OfficeFilters) (*[]banklocsrv.Office, error)
}

type Repository struct {
	Authorization
	Atms
	Offices
}

func NewRepository(db *sqlx.DB) *Repository {
	return &Repository{
		Authorization: NewAuthPostgres(db),
		Atms:          NewAtmsPostgres(db),
		Offices:       NewOfficesPostgres(db),
	}
}
