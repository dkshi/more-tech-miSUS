package banklocsrv

type ATM struct {
	Id        int     `json:"id" db:"id"`
	Address   string  `json:"address" db:"address" binding:"required"`
	Latitude  float64 `json:"latitude" db:"latitude" binding:"required"`
	Longitude float64 `json:"longitude" db:"longitude" binding:"required"`
	AllDay    bool    `json:"all_day" db:"all_day" binding:"required"`
	WheelchairCap interface{} `json:"wheelchair_cap" db:"wheelchair_cap"`
	WheelchairAct interface{} `json:"wheelchair_act" db:"wheelchair_act"`
	BlindCap      interface{} `json:"blind_cap" db:"blind_cap"`
	BlindAct      interface{} `json:"blind_act" db:"blind_act"`
	NfcCap        interface{} `json:"nfc_cap" db:"nfc_cap"`
	NfcAct        interface{} `json:"nfc_act" db:"nfc_act"`
	QrCap         interface{} `json:"qr_cap" db:"qr_cap"`
	QrAct         interface{} `json:"qr_act" db:"qr_act"`
	UsdCap        interface{} `json:"usd_cap" db:"usd_cap"`
	UsdAct        interface{} `json:"usd_act" db:"usd_act"`
	ChargeRubCap  interface{} `json:"chargerub_cap" db:"chargerub_cap"`
	ChargeRubAct  interface{} `json:"chargerub_act" db:"chargerub_act"`
	EurCap        interface{} `json:"eur_cap" db:"eur_cap"`
	EurAct        interface{} `json:"eur_act" db:"eur_act"`
	RubCap        interface{} `json:"rub_cap" db:"rub_cap"`
	RubAct        interface{} `json:"rub_act" db:"rub_act"`
}
