.PHONY: makemigrations
makemigrations:
	python manage.py makemigrations

.PHONY: migrate
migrate:
	python manage.py migrate

.PHONY: shell
shell:
	python manage.py shell_plus

.PHONY: dbshell
dbshell:
	python manage.py dbshell
