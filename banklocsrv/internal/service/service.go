package service

import (
	"github.com/dkshi/banklocsrv"
	"github.com/dkshi/banklocsrv/internal/repository"
)

type Authorization interface {
	CreateUser(user banklocsrv.User) (int, error)
	GenerateToken(username, password string) (string, error)
	ParseToken(token string) (int, error)
}

type Atms interface {
	GetAtms() (*[]banklocsrv.ATM, error)
	SelectAtms(filters banklocsrv.AtmsFilters) (*[]banklocsrv.ATM, error)
}

type Offices interface {
	GetOffices() (*[]banklocsrv.Office, error)
	SelectOffices(filters banklocsrv.OfficeFilters) (*[]banklocsrv.Office, error)
}

type Service struct {
	Authorization
	Atms
	Offices
}

func NewService(repo *repository.Repository) *Service {
	return &Service{
		Authorization: NewAuthService(repo.Authorization),
		Atms:          NewAtmsService(repo.Atms),
		Offices:       NewOfficesService(repo.Offices),
	}
}
