# Sample Python API

This is a simple Python API built with the FastAPI framework.

## Prerequisites

- Python 3.7+
- FastAPI
- Uvicorn

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ricardosmh/new-sample-python-api.git
   cd new-sample-python-api
   ```

2. Install the dependencies:
   ```bash
   pip install fastapi uvicorn
   ```

## Usage

To run the application, use the following command:

```bash
uvicorn example:app --reload
```

This will start a local development server. You can access the API at `http://127.0.0.1:8000`.

## API Documentation

The API has a single endpoint:

- `GET /`: Returns a JSON object `{"Hello": "World"}`.
