package handler

import (
	"net/http"

	"github.com/dkshi/banklocsrv"
	"github.com/gin-gonic/gin"
)

func (h *Handler) atms(c *gin.Context) {
	atms, err := h.services.Atms.GetAtms()

	if err != nil {
		newErrorResponse(c, http.StatusNotFound, err.Error())
	}

	c.JSON(http.StatusOK, map[string]interface{}{
		"atms": atms,
	})
}

func (h *Handler) filterAtms(c *gin.Context) {
	var filters banklocsrv.AtmsFilters

	if err := c.BindJSON(&filters); err != nil {
		newErrorResponse(c, http.StatusInternalServerError, err.Error())
		return
	}

	atms, err := h.services.SelectAtms(filters)
	if err != nil {
		newErrorResponse(c, http.StatusInternalServerError, err.Error())
		return
	}

	c.JSON(http.StatusOK, map[string]interface{}{
		"offices": &atms,
	})
}
