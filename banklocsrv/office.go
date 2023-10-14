package banklocsrv

type Office struct {
	Id              int         `json:"id" db:"id"`
	SalePointName   interface{} `json:"salepoint_name" db:"salepoint_name"`
	Address         interface{} `json:"address" db:"address"`
	Rko             interface{} `json:"rko" db:"rko"`
	OfficeType      interface{} `json:"office_type" db:"office_type"`
	SalePointFormat interface{} `json:"salepoint_format" db:"salepoint_format"`
	SuoAvailability interface{} `json:"suo_availability" db:"suo_availability"`
	HasRamp         interface{} `json:"has_ramp" db:"has_ramp"`
	Latitude        float64     `json:"latitude" db:"latitude" binding:"required"`
	Longitude       float64     `json:"longitude" db:"longitude" binding:"required"`
	MetroStation    interface{} `json:"metro_station" db:"metro_station"`
	Distance        int         `json:"distance" db:"distance"`
	Kep             interface{} `json:"kep" db:"kep"`
	MyBranch        interface{} `json:"my_branch" db:"my_branch"`
	Monday          string      `json:"oh_monday" db:"oh_monday" binding:"required"`
	Tuesday         string      `json:"oh_tuesday" db:"oh_tuesday" binding:"required"`
	Wednesday       string      `json:"oh_wednesday" db:"oh_wednesday" binding:"required"`
	Thursday        string      `json:"oh_thursday" db:"oh_thursday" binding:"required"`
	Friday          string      `json:"oh_friday" db:"oh_friday" binding:"required"`
	Saturday        string      `json:"oh_saturday" db:"oh_saturday" binding:"required"`
	Sunday          string      `json:"oh_sunday" db:"oh_sunday" binding:"required"`
	MondayIndv      string      `json:"ohi_monday" db:"ohi_monday" binding:"required"`
	TuesdayIndv     string      `json:"ohi_tuesday" db:"ohi_tuesday" binding:"required"`
	WednesdayIndv   string      `json:"ohi_wednesday" db:"ohi_wednesday" binding:"required"`
	ThursdayIndv    string      `json:"ohi_thursday" db:"ohi_thursday" binding:"required"`
	FridayIndv      string      `json:"ohi_friday" db:"ohi_friday" binding:"required"`
	SaturdayIndv    string      `json:"ohi_saturday" db:"ohi_saturday" binding:"required"`
	SundayIndv      string      `json:"ohi_sunday" db:"ohi_sunday" binding:"required"`
}
