FROM python:3.10

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Ensure Poetry binary is in the PATH
ENV PATH="/root/.local/bin:${PATH}"

WORKDIR /app

# Create the src directory and main.py file
RUN mkdir -p src && echo '' > src/main.py

COPY pyproject.toml  poetry.lock* ./

RUN poetry install

# Copy the source code and Alembic files into the container
COPY src /app/src
COPY alembic /app/alembic
COPY alembic.ini /app/alembic.ini

# # Copy the migration script into the container
COPY run_migrations.sh /app/run_migrations.sh

# Make the migration script executable
RUN chmod +x /app/run_migrations.sh

# # Run migrations as part of the build process
RUN ./run_migrations.sh

EXPOSE 8000



