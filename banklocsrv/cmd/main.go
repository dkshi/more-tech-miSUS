package main

import (
	"os"

	"github.com/dkshi/banklocsrv"
	"github.com/dkshi/banklocsrv/internal/handler"
	"github.com/dkshi/banklocsrv/internal/repository"
	"github.com/dkshi/banklocsrv/internal/service"
	"github.com/dkshi/banklocsrv/scripts"
	"github.com/joho/godotenv"
	"github.com/sirupsen/logrus"
	"github.com/spf13/viper"
)

func main() {
	logrus.SetFormatter(new(logrus.JSONFormatter))

	if err := initConfig(); err != nil {
		logrus.Fatalf("error initializing configs: %s", err.Error())
	}

	if err := godotenv.Load(); err != nil {
		logrus.Fatalf("error loading environment: %s", err.Error())
	}

	db, err := repository.NewPostgresDB(repository.Config{
		Host:     viper.GetString("db.host"),
		Port:     viper.GetString("db.port"),
		Username: viper.GetString("db.username"),
		Password: os.Getenv("DB_PASSWORD"),
		DBName:   viper.GetString("db.dbname"),
		SSLMode:  viper.GetString("db.sslmode"),
	})

	if err != nil {
		logrus.Fatalf("error connecting database: %s", err.Error())
	}

	officeLoadImitator := scripts.NewOfficeLoadImitator(db)
	go officeLoadImitator.ImitateLoad()

	repo := repository.NewRepository(db)
	services := service.NewService(repo)
	handlers := handler.NewHandler(services)

	srv := new(banklocsrv.Server)
	if err := srv.Run("8080", handlers.InitRoutes()); err != nil {
		logrus.Fatalf("error while running app: %s", err.Error())
	}
}

func initConfig() error {
	viper.AddConfigPath("configs")
	viper.SetConfigName("config")
	return viper.ReadInConfig()
}
