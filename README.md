# HNG Stage 0 Backend — FastAPI Profile Service

A minimal FastAPI service that exposes a single endpoint to return user profile information along with a random cat fact fetched from the public Cat Facts API.

- Framework: FastAPI (async)
- HTTP client: httpx (async)
- Runtime server: Uvicorn
- Language: Python 3.10+

## Table of Contents

- [Project Structure](#project-structure)
- [Features](#features)
- [Requirements](#requirements)
- [Setup](#setup)
- [Running the Server](#running-the-server)
- [API Reference](#api-reference)
- [Examples](#examples)
- [Development Notes](#development-notes)
- [Troubleshooting](#troubleshooting)
- [Roadmap / Improvements](#roadmap--improvements)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Project Structure

```
stage0/
└── BE/
    └── app.py
```

- `stage0/BE/app.py` — FastAPI application with one endpoint GET `/me`. It fetches a cat fact from https://catfact.ninja/fact and returns it along with static user details and a UTC timestamp.

## Features

- GET `/me` returns:

  - status: "success"
  - user: { email, name, stack }
  - timestamp: ISO-8601 UTC
  - fact: random cat fact (fallback string when no fact is available)
- Async I/O:

  - Uses `httpx.AsyncClient` with a timeout to call the Cat Facts API.
  - Fully async endpoint for efficient concurrency.

## Requirements

- Python 3.10+ (3.11+ recommended)
- pip (latest)
- Internet access (to reach the Cat Facts API)

Python packages (installed via pip):

- fastapi
- uvicorn[standard]
- httpx

## Setup

1) Create and activate a virtual environment

- Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

- Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

2) Upgrade pip and install dependencies

```bash
python -m pip install --upgrade pip
pip install fastapi uvicorn[standard] httpx
```

## Running the Server

From the repository root (where this README.md lives), run:

```bash
uvicorn stage0.BE.app:app --reload --host 0.0.0.0 --port 8000
```

- Local API: http://localhost:8000/me
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

Notes:

- `--reload` is for development only; omit it in production.
- The import path `stage0.BE.app:app` maps to the `app` instance in `stage0/BE/app.py`.

## API Reference

### GET /me

Returns user details, an ISO-8601 UTC timestamp, and a cat fact.

- Response: 200 OK on success (always when internal logic completes)
- Content-Type: application/json

Example successful response:

```json
{
  "status": "success",
  "user": {
    "email": "phurhardeen@gmail.com",
    "name": "Fuhad Yusuf",
    "stack": "python"
  },
  "timestamp": "2025-10-18T22:14:52.123456+00:00",
  "fact": "Cats have five toes on their front paws, but only four toes on their back paws."
}
```

Behavioral notes:

- If the Cat Facts API responds successfully but without a `fact` field, the service returns `"fact": "No cat fact available"`.
- If the HTTP request to the Cat Facts API fails (network error, timeout, non-2xx with raise_for_status), FastAPI will return a 500 Internal Server Error by default because the exception propagates. See Roadmap for improving this with graceful error handling.

## Examples

Using curl:

```bash
curl -s http://localhost:8000/me | jq
```

Using HTTPie:

```bash
http GET :8000/me
```

Open in browser:

- http://localhost:8000/me
- http://localhost:8000/docs
- http://localhost:8000/redoc

## Development Notes

- Async HTTP:
  - Implemented with `httpx.AsyncClient(timeout=60)`.
  - External call: `GET https://catfact.ninja/fact`.
- Timestamp:
  - `datetime.now(timezone.utc)`; FastAPI auto-serializes to ISO-8601.
- Logging:
  - Currently uses `print(data)` after fetching the cat fact. Consider replacing with structured logging (e.g., Python `logging`).
- CORS:
  - Not configured. If a browser-based frontend will call this API, add `fastapi.middleware.cors.CORSMiddleware`.

### Minimal Code Walkthrough (stage0/BE/app.py)

- `get_cat_fact()`:
  - Calls the Cat Facts endpoint and returns `data.get("fact")`.
  - Raises for non-2xx responses.
- `@app.get("/me")`:
  - Awaits `get_cat_fact()`.
  - Builds the response with user details and `fact`.
  - If `fact` is falsey (empty/missing), uses `"No cat fact available"`.

## Troubleshooting

- Module import error for `stage0.BE.app:app`:
  - Ensure you run `uvicorn` from the repository root so that `stage0` is importable as a package path.
- Missing dependencies:
  - Re-run: `pip install fastapi uvicorn[standard] httpx`
- External API/network issues:
  - Check internet connectivity and that https://catfact.ninja is reachable.
  - Adjust timeout if needed in `get_cat_fact()` (default 60s).
- 500 Internal Server Error:
  - Caused by exceptions in `get_cat_fact()` (e.g., timeouts or non-2xx). See Roadmap for graceful degradation.

## Roadmap / Improvements

- Robust error handling:
  - Catch `httpx` exceptions and return a valid response with a fallback fact instead of 500.
- Observability:
  - Replace `print` with structured logs; add request/response logging for upstream calls.
- Configuration:
  - Extract the Cat Facts API URL and timeout to environment variables.
- Testing:
  - Add unit tests with `pytest` and async test tools (`pytest-asyncio`), mocking httpx calls.
- Security:
  - Add rate limiting or caching to reduce upstream load and improve resiliency.
- Packaging:
  - Add a `requirements.txt` or `pyproject.toml` for pinned dependencies.
- CORS:
  - Configure if a web frontend will call the API from a different origin.
- Docker:
  - Add a production-ready Dockerfile and containerization workflow.

### Example Dockerfile (optional)

You can use this minimal Dockerfile as a starting point:

```dockerfile
FROM python:3.11-slim

WORKDIR /app
# Copy only what's needed for this tiny app; adjust as the project grows
COPY stage0/BE/app.py /app/stage0/BE/app.py

# Install runtime deps
RUN pip install --no-cache-dir fastapi uvicorn[standard] httpx

EXPOSE 8000
CMD ["uvicorn", "stage0.BE.app:app", "--host", "0.0.0.0", "--port", "8000"]
```

Build and run:

```bash
docker build -t hng-stage0-backend .
docker run --rm -p 8000:8000 hng-stage0-backend
```

## Contributing

- Fork the repository and create a feature branch.
- Follow conventional commit messages when possible.
- Include tests for new behavior.
- Open a pull request with a clear description of changes.

## License

No license file is present in this repository. If you intend to open-source, consider adding a LICENSE file (e.g., MIT, Apache-2.0). If proprietary, document the terms accordingly.

## Acknowledgements

- Cat facts provided by https://catfact.ninja
- FastAPI: https://fastapi.tiangolo.com
- httpx: https://www.python-httpx.org
- Uvicorn: https://www.uvicorn.org

Unfortuantely haven't been able to really write codes these past few days, so i just make some posts to keep up with the streak.

Same thing is happening again.

Hopefully, this is the last day i'll do this.Thinkinh of implementing this using express node, as that is a language i intent to learn. so i'll stop using python for this tasks and try using node express henceforth.