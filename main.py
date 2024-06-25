from fastapi import FastAPI, Request, HTTPException
from port import routes
from utils.exception import global_exception_handler, http_exception_handler
from fastapi.middleware.cors import CORSMiddleware
from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend

app = FastAPI()

origins = [
    "*",
    "http://localhost:3000",  # Adicione os domínios permitidos aqui
    "https://seu-outro-dominio.com",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # ou especifique os métodos permitidos
    allow_headers=["*"],  # ou especifique os cabeçalhos permitidos
)

app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, global_exception_handler)
app.include_router(routes.router, tags=["routes"])

@app.on_event("startup")
async def startup():
    FastAPICache.init(InMemoryBackend())