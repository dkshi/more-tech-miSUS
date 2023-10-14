package banklocsrv

type AtmsFilters struct {
	Wheelchair interface{} `json:"wheelchair"`
	AllDay     interface{} `json:"all_day"`
	Blind      interface{} `json:"blind"`
	Nfc        interface{} `json:"nfc"`
	Qr         interface{} `json:"qr"`
	Rub        interface{} `json:"rub"`
	Usd        interface{} `json:"usd"`
	Eur        interface{} `json:"eur"`
}
