"""Main entry point for the FastAPI application."""

import uvicorn
from fastapi import FastAPI

from backend.app.api.v1.routers.example_route import auth_router
from backend.app.config import config

app = FastAPI(title=config.PROJECT_NAME, docs_url="/api/docs", openapi_url="/api")

# Routers
app.include_router(auth_router, prefix="/api", tags=["auth"])


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", reload=True, port=8888)
