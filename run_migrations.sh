#!/bin/sh

echo "Starting database migrations..."

poetry run alembic upgrade head

echo "Generating new migration file..."

poetry run alembic revision --autogenerate

echo "Applying the new migration..."

poetry run alembic upgrade head

echo "Database migrations completed successfully."
