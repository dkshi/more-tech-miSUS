package repository

import (
	"fmt"

	"github.com/dkshi/banklocsrv"
	"github.com/dkshi/banklocsrv/scripts"
	"github.com/jmoiron/sqlx"
)

const (
	atmsQuery = "SELECT " +
		"a.*, " +
		"s.wheelchair_cap, " +
		"s.wheelchair_act, " +
		"s.blind_cap, " +
		"s.blind_act, " +
		"s.nfc_cap, " +
		"s.nfc_act, " +
		"s.qr_cap, " +
		"s.qr_act, " +
		"s.usd_cap, " +
		"s.usd_act, " +
		"s.chargerub_cap, " +
		"s.chargerub_act, " +
		"s.eur_cap, " +
		"s.eur_act, " +
		"s.rub_cap, " +
		"s.rub_act " +
		"FROM " +
		"atms a " +
		"JOIN " +
		"atms_services s ON a.id = s.atm_id"
)

type AtmsPostgres struct {
	db *sqlx.DB
}

func NewAtmsPostgres(db *sqlx.DB) *AtmsPostgres {
	return &AtmsPostgres{db: db}
}

func (dep *AtmsPostgres) GetAtms() (*[]banklocsrv.ATM, error) {
	var atms []banklocsrv.ATM
	query := atmsQuery
	err := dep.db.Select(&atms, query)

	if err != nil {
		return &[]banklocsrv.ATM{}, err
	}

	return &atms, nil
}

func (dep *AtmsPostgres) SelectAtms(filters banklocsrv.AtmsFilters) (*[]banklocsrv.ATM, error) {
	var atms []banklocsrv.ATM
	query := atmsQuery
	makeFilterAtms(&query, &filters)
	err := dep.db.Select(&atms, query)

	if err != nil {
		return &[]banklocsrv.ATM{}, err
	}

	return &atms, nil
}

func makeFilterAtms(query *string, filters *banklocsrv.AtmsFilters) {
	filter := ""
	counter := 0

	if filters.Wheelchair != nil {
		scripts.CheckFilter(&filter, counter)
		filter += fmt.Sprintf(" wheelchair_act = %t", filters.Wheelchair)
		counter++
	}

	if filters.AllDay != nil {
		scripts.CheckFilter(&filter, counter)
		filter += fmt.Sprintf(" all_day = %t", filters.AllDay)
		counter++
	}

	if filters.Blind != nil {
		scripts.CheckFilter(&filter, counter)
		filter += fmt.Sprintf(" blind_act = %t", filters.Blind)
		counter++
	}

	if filters.Nfc != nil {
		scripts.CheckFilter(&filter, counter)
		filter += fmt.Sprintf(" nfc_act = %t", filters.Nfc)
		counter++
	}

	if filters.Qr != nil {
		scripts.CheckFilter(&filter, counter)
		filter += fmt.Sprintf(" qr_act = %t", filters.Qr)
		counter++
	}

	if filters.Rub != nil {
		scripts.CheckFilter(&filter, counter)
		filter += fmt.Sprintf(" rub_act = %t", filters.Rub)
		counter++
	}

	if filters.Usd != nil {
		scripts.CheckFilter(&filter, counter)
		filter += fmt.Sprintf(" usd_act = %t", filters.Usd)
		counter++
	}

	if filters.Eur != nil {
		scripts.CheckFilter(&filter, counter)
		filter += fmt.Sprintf(" eur_act = %t", filters.Eur)
		counter++
	}
	*query += filter
}
