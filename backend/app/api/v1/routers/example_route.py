"""End-point for login users."""

from fastapi import APIRouter

auth_router = r = APIRouter()


@r.post("/router")
async def router():
    """Login end-point."""
    return {"message": "Route"}
