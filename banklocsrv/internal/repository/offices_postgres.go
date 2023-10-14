package repository

import (
	"fmt"

	"github.com/dkshi/banklocsrv"
	"github.com/dkshi/banklocsrv/scripts"
	"github.com/jmoiron/sqlx"
)

const (
	officesQuery = "SELECT " +
		"o.*, " +
		"oh.monday AS oh_monday, " +
		"oh.tuesday AS oh_tuesday, " +
		"oh.wednesday AS oh_wednesday, " +
		"oh.thursday AS oh_thursday, " +
		"oh.friday AS oh_friday, " +
		"oh.saturday AS oh_saturday, " +
		"oh.sunday AS oh_sunday, " +
		"ohi.monday AS ohi_monday, " +
		"ohi.tuesday AS ohi_tuesday, " +
		"ohi.wednesday AS ohi_wednesday, " +
		"ohi.thursday AS ohi_thursday, " +
		"ohi.friday AS ohi_friday, " +
		"ohi.saturday AS ohi_saturday, " +
		"ohi.sunday AS ohi_sunday " +
		"FROM offices o " +
		"JOIN offices_hours oh ON o.id = oh.office_id " +
		"JOIN offices_hours_individual ohi ON o.id = ohi.office_id"
)

type OfficesPostgres struct {
	db *sqlx.DB
}

func NewOfficesPostgres(db *sqlx.DB) *OfficesPostgres {
	return &OfficesPostgres{db: db}
}

func (dep *OfficesPostgres) GetOffices() (*[]banklocsrv.Office, error) {
	var offices []banklocsrv.Office
	query := officesQuery

	err := dep.db.Select(&offices, query)

	if err != nil {
		return &[]banklocsrv.Office{}, err
	}

	return &offices, nil
}

func (dep *OfficesPostgres) SelectOffices(filters banklocsrv.OfficeFilters) (*[]banklocsrv.Office, error) {
	var offices []banklocsrv.Office
	query := officesQuery
	makeFilterOffices(&query, &filters)

	err := dep.db.Select(&offices, query)

	if err != nil {
		return &[]banklocsrv.Office{}, err
	}

	return &offices, nil
}

func makeFilterOffices(query *string, filters *banklocsrv.OfficeFilters) {
	filter := ""
	counter := 0

	if filters.Ramp != nil {
		scripts.CheckFilter(&filter, counter)
		filter += fmt.Sprintf(" has_ramp = %t", filters.Ramp)
		counter++
	}

	if filters.Kep != nil {
		scripts.CheckFilter(&filter, counter)
		filter += fmt.Sprintf(" kep = %t", filters.Kep)
		counter++
	}

	if filters.MyBranch != nil {
		scripts.CheckFilter(&filter, counter)
		filter += fmt.Sprintf(" my_branch = %t", filters.MyBranch)
		counter++
	}

	if filters.Rko != nil {
		scripts.CheckFilter(&filter, counter)
		filter += fmt.Sprintf(" rko = %t", filters.Rko)
		counter++
	}

	if filters.Suo != nil {
		scripts.CheckFilter(&filter, counter)
		filter += fmt.Sprintf(" suo_availability = %t", filters.Suo)
		counter++
	}
	*query += filter
}
