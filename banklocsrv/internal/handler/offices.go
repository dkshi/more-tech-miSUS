package handler

import (
	"net/http"

	"github.com/dkshi/banklocsrv"
	"github.com/gin-gonic/gin"
)

func (h *Handler) offices(c *gin.Context) {
	offices, err := h.services.Offices.GetOffices()

	if err != nil {
		newErrorResponse(c, http.StatusNotFound, err.Error())
		return
	}

	c.JSON(http.StatusOK, map[string]interface{}{
		"offices": &offices,
	})
}

func (h *Handler) filterOffices(c *gin.Context) {
	var filters banklocsrv.OfficeFilters

	if err := c.BindJSON(&filters); err != nil {
		newErrorResponse(c, http.StatusInternalServerError, err.Error())
		return
	}

	offices, err := h.services.SelectOffices(filters)
	if err != nil {
		newErrorResponse(c, http.StatusInternalServerError, err.Error())
		return
	}

	c.JSON(http.StatusOK, map[string]interface{}{
		"offices": &offices,
	})
}
