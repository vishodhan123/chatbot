from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import factory

app = factory.create_app()

origins = "GET,POST,PUT,DELETE"
methods = "*"
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=methods,
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run("main:app",
                port=8080,
                log_level="info",
                proxy_headers=True,
                forwarded_allow_ips='*')
