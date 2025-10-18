from fastapi import FastAPI, HTTPException
from datetime import datetime, timezone
import httpx

app = FastAPI()


async def get_cat_fact():
    """Fetch a random cat fact from the Cat Facts API"""
    try:
        async with httpx.AsyncClient(timeout=60) as client:
            response = await client.get("https://catfact.ninja/fact")
            response.raise_for_status()
            data = response.json()
    except httpx.ConnectError:
        raise HTTPException(status_code=503, detail="Temporary failure in name resolution")
    return data.get("fact")


@app.get("/me")
async def profile():
    """Return my details and a cat fact"""
    cat_fact = await get_cat_fact()
    if not cat_fact:
        return {
            "status": "success",
            "user": {
                "email": "phurhardeen@gmail.com",
                "name": "Fuhad Yusuf",
                "stack": "python"
            },
            "timestamp": datetime.now(timezone.utc),
            "fact": "No cat fact available"
        }

    response = {
        "status": "success",
        "user": {
            "email": "phurhardeen@gmail.com",
            "name": "Fuhad Yusuf",
            "stack": "python"
        },
        "timestamp": datetime.now(timezone.utc),
        "fact": cat_fact
    }
    return response
