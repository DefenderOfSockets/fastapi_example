"""End-point for login users."""

from fastapi import APIRouter, Cookie

auth_router = r = APIRouter()


@r.post("/auth/login")
async def login(auth_cookie: str = Cookie(default=None)):
    """Login end-point."""
    print(auth_cookie)
    return {"auth_cookie": auth_cookie}
