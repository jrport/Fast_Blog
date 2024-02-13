#! /usr/bin/bash
sudo poetry run uvicorn src.backend.routes:app --port 80 --reload
