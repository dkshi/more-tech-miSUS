package service

import (
	"github.com/dkshi/banklocsrv"
	"github.com/dkshi/banklocsrv/internal/repository"
)

type AtmsService struct {
	repo repository.Atms
}

func NewAtmsService(repo repository.Atms) *AtmsService {
	return &AtmsService{repo: repo}
}

func (s *AtmsService) GetAtms() (*[]banklocsrv.ATM, error) {
	atms, err := s.repo.GetAtms()

	if err != nil {
		return &[]banklocsrv.ATM{}, err
	}

	return atms, nil
}

func (s *AtmsService) SelectAtms(filters banklocsrv.AtmsFilters) (*[]banklocsrv.ATM, error) {
	atms, err := s.repo.SelectAtms(filters)

	if err != nil {
		return &[]banklocsrv.ATM{}, err
	}

	return atms, nil

}