package scripts

import (
	"fmt"
	"math/rand"
	"time"

	"github.com/jmoiron/sqlx"
	_ "github.com/lib/pq"
	"github.com/sirupsen/logrus"
)

const (
	officesLoadTable = "offices_load"
)

type OfficeLoadImitator struct {
	db *sqlx.DB
}

func NewOfficeLoadImitator(db *sqlx.DB) *OfficeLoadImitator {
	return &OfficeLoadImitator{db: db}
}

func (o *OfficeLoadImitator) ImitateLoad() {
	for {
		go func() {
			query := fmt.Sprintf("SELECT * FROM %s ORDER BY RANDOM() LIMIT 20", officesLoadTable)
			rows, err := o.db.Query(query)
			if err != nil {
				logrus.Fatalf("error selecting random rows from db: %s", err.Error())
			}
			for rows.Next() {
				var (
					id       int
					officeId int
					load     int
				)
				rows.Scan(&id, officeId, &load)
				go func(id int) {
					o.IncrementRow(id)
					time.Sleep(time.Duration(rand.Intn(6)+5) * time.Minute)
					o.DecrementRow(id)
				}(id)
			}
		}()
		time.Sleep(time.Duration(rand.Intn(30)+1) * time.Second)
	}
}

func (o *OfficeLoadImitator) IncrementRow(id int) {
	query := fmt.Sprintf("UPDATE %s SET load = load + 1 WHERE id=$1", officesLoadTable)
	_, err := o.db.Exec(query, id)
	if err != nil {
		logrus.Fatalf("error incrementing random row: %s", err.Error())
	}
}

func (o *OfficeLoadImitator) DecrementRow(id int) {
	query := fmt.Sprintf("UPDATE %s SET load = load - 1 WHERE id=$1", officesLoadTable)
	_, err := o.db.Exec(query, id)
	if err != nil {
		logrus.Fatalf("error incrementing random row: %s", err.Error())
	}
}
