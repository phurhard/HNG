from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from stage2.models.a2a import JSONRPCResponse
from stage2.services import movies

app = FastAPI()


@app.get("health")
async def health():
    return JSONResponse(
        status_code=200,
        content={
            "jsonrpc": "2.0",
            "message": "Application is healthy"
        }
    )


class DataRequest(BaseModel):
    data: str


@app.post("/", response_model=JSONRPCResponse)
async def sample(request: Request):
    data = await request.json()
    print(data)
    response = await movies.get_movies(data)
    return response


@app.post("/a2a/data")
async def data_request(
    data: DataRequest
):
    response = await movies.get_movies(data)
    return response
