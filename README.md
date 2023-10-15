# more-tech-miSUS
![image](https://github.com/dkshi/more-tech-miSUS/assets/95618433/c8298e24-e3d1-4d3a-8025-2a5fb0a55e9d)

Порядок запуска:

Отредактируйте данные доступа к БД во всех модулях для необходимости.
Изначальные данные:
port: "8080"

db:
  username: "postgres"
  host: "localhost"
  port: "5436"
  dbname: "postgres"
  sslmode: "disable"
  password: "qwerty"

Добавьте файл .env в папку banklocsrv, укажите в нём: DB_PASSWORD=qwerty
По умолчанию данный файл игнорируется GIT для безопасности.

Установите apk файл
Создайте БД вручную или с помощью Docker (предварительно выполнив команду docker pull postgres), командой: docker run --name=bankloc-db -e POSTGRES_PASSWORD='qwerty' -p 5436:5432 -d postgres

Перейдите в папку banklocsrv, поднимите файл миграций командой: migrate -path ./schema -database 'postgres://postgres:qwerty@localhost:5436/postgres?sslmode=disable' up

Вернитесь в основную директорию проекта.
Перейдите в папку python-scripts. Запустите скрипты dbinserting.py, а потом moretech_regres_offices_hours.py для заполнения БД.

Запустите сервер командой go run banklocsrv/cmd/main.go
