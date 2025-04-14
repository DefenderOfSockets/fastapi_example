"""Configuration settings."""

import os

PROJECT_NAME = "Fast API example"

SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

API_V1_STR = "/api/v1"
