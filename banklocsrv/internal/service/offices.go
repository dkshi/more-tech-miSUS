package service

import (
	"github.com/dkshi/banklocsrv"
	"github.com/dkshi/banklocsrv/internal/repository"
)

type OfficesService struct {
	repo repository.Offices
}

func NewOfficesService(repo repository.Offices) *OfficesService {
	return &OfficesService{repo: repo}
}

func (s *OfficesService) GetOffices() (*[]banklocsrv.Office, error) {
	offices, err := s.repo.GetOffices()

	if err != nil {
		return &[]banklocsrv.Office{}, err
	}

	return offices, nil

}

func (s *OfficesService) SelectOffices(filters banklocsrv.OfficeFilters) (*[]banklocsrv.Office, error) {
	offices, err := s.repo.SelectOffices(filters)

	if err != nil {
		return &[]banklocsrv.Office{}, err
	}

	return offices, nil

}
