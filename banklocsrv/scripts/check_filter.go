package scripts

func CheckFilter(filter *string, count int) {
	if count == 0 {
		*filter += " WHERE"
	}

	if count >= 1 {
		*filter += " AND"
	}
}
