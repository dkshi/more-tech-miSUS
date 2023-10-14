package handler

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func (h *Handler) check(c *gin.Context) {
	c.JSON(http.StatusOK, map[string]interface{}{
		"ok": true,
	})
}
