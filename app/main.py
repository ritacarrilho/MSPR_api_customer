"""
Module with all the API endpoints for customers management.
It includes the operations of creation, lecture, update and delete of customers
"""

from typing import List
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from .database import engine, get_db

app = FastAPI(
    title="Api Customer",
    description=".....",
    summary=".....",
    version="0.0.2",
)
@app.get("/", response_model=dict, tags=["Health Check"])
def api_status():
    """
    Verifies the API status.

    Returns:
        dict: dict with the API status.
    """
    return {"status": "running"}



@app.get("/customers/", tags=["customers"])
def get_customers():
    return {"get customers": "ok"}


@app.get("/customers/{id}", tags=["customers"])
def get_customers():
    return {"get customer by id": "ok"}