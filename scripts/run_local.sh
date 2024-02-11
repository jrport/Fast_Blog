#! /usr/bin/bash
poetry run uvicorn src.backend.main:app --host 0.0.0.0 --port 80
