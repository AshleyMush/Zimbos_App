FROM python:3.13-bullseye

ENV PYTHONUNBUFFERED=1

# Set up working directory
RUN mkdir /app
WORKDIR /app

# Install Poetry
RUN pip install poetry

# Configure Poetry to avoid using .venv in Docker
RUN poetry config virtualenvs.create false

# Copy dependency files first for caching
COPY pyproject.toml poetry.lock ./

# Install dependencies (no venv, global inside Docker)
RUN poetry install --no-root

# Copy the rest of the app
COPY . .

# Expose Django's port
EXPOSE 8000

# Run server
ENTRYPOINT ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
