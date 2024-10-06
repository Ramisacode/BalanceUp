from fastapi import FastAPI

app = FastAPI(title="My FastAPI Application", description="A barebones FastAPI web application template")

from app import views