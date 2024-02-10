FROM python:3.11.7-bookworm
WORKDIR /fast_app

COPY ./pyproject.toml .
COPY ./poetry.lock .

RUN pip install poetry
RUN poetry config virtualenvs.in-project true
RUN poetry run python -m pip install --upgrade pip 
RUN poetry install

COPY . .

CMD ["poetry", "run", "uvicorn", "src.fast_pico_vue_blog.main:app", "--host", "0.0.0.0", "--port", "80"]
