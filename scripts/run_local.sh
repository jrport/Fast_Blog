#! /usr/bin/bash
sudo poetry run uvicorn src.backend.main:app --port 80 --reload 
