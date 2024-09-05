APP_CONTAINER = matrix_app
DC = docker compose
EXEC = docker exec -it
LOGS = docker logs

.PHONY: app
app:
	${DC} up --build -d

app-restart:
	${DC} restart

app-down:
	${DC} down

app-logs:
	${DC} logs -f ${APP_CONTAINER}

app-shell:
	${DC} exec ${APP_CONTAINER} /bin/bash

tests:
	${DC} exec -T ${APP_CONTAINER} pytest -vs

tests-coverage:
	${DC} exec -T ${APP_CONTAINER} pytest --cov=. app/tests

mypy:
	${DC} exec -T ${APP_CONTAINER} mypy --explicit-package-bases .

ruff-check:
	${DC} exec -T ${APP_CONTAINER} ruff check .

ruff-fix:
	${DC} exec -T ${APP_CONTAINER} ruff check . --fix
