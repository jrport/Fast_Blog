#! /usr/bin/bash
poetry run uvicorn src.backend.main:app --port 80 --reload 
