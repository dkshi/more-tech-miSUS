package banklocsrv

type OfficeFilters struct {
	Ramp     interface{} `json:"ramp"`
	Kep      interface{} `json:"kep"`
	MyBranch interface{} `json:"my_branch"`
	Rko      interface{} `json:"rko"`
	Suo      interface{} `json:"suo"`
}
