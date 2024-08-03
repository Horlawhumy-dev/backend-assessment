build:
docker-compose build

up:
	docker-compose up -d

migrate:
	docker-compose exec web python manage.py migrate

logs:
	docker-compose logs web

down:
	docker-compose down

restart:
	docker-compose restart

createsuperuser:
	docker-compose exec web python manage.py createsuperuser


