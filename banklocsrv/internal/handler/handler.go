package handler

import (
	"github.com/dkshi/banklocsrv/internal/service"
	"github.com/gin-gonic/gin"
)

type Handler struct {
	services *service.Service
}

func NewHandler(service *service.Service) *Handler {
	return &Handler{services: service}
}

func (h *Handler) InitRoutes() *gin.Engine {
	router := gin.New()

	auth := router.Group("/auth")
	{
		auth.POST("/sign-up", h.signUp)
		auth.POST("/sign-in", h.signIn)
	}

	departments := router.Group("/departments", h.userIdentity)
	{
		departments.GET("/atms", h.atms)
		departments.GET("/offices", h.offices)
		departments.POST("/filter-offices", h.filterOffices)
		departments.POST("/filter-atms", h.filterAtms)
	}

	check := router.Group("/check", h.userIdentity)
	{
		check.GET("", h.check)
	}

	return router
}
