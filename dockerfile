FROM python:3.11.7-bookworm

WORKDIR /fast_app

# Sets env variables for poetry install
ENV POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_NO_INTERACTION=1

# Install poetry
RUN <<EOF
apt-get update
apt-get install -y --no-install-recommends curl
curl -sSL https://install.python-poetry.org | python3
EOF

# Sets necessary dependency registries
COPY ./pyproject.toml ./poetry.lock ./ ./

# Sets poetry as envvar to call directly
ENV PATH="${PATH}:${POETRY_HOME}/bin"

# Installs project dependencies
RUN poetry install --no-root --no-ansi

COPY . .

# Runs app with uvicorn at localhost:80
CMD ["poetry", "run", "uvicorn", "src.backend.routes:app", "--host", "0.0.0.0", "--port", "80"]
