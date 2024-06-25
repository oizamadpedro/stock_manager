from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse

async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )

async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": "An unexpected error occurred. Please try again later.", "response": str(exc)},
    )

def exception_handler(func): # TODO: make a better response log
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            return None
    return wrapper