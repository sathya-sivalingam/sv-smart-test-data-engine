from fastapi import FastAPI, Query
from faker import Faker
import random
import time

app = FastAPI()
fake = Faker()

@app.get("/")
def home():
    return {"message": "Mock API Server"}

@app.get("/mock-user")
def mock_user(delay: float = 0, error: bool = False):
    if delay > 0:
        time.sleep(delay)

    if error:
        return {"error": "Simulated failure"}, 500

    return {
        "name": fake.name(),
        "email": fake.email(),
        "address": fake.address()
    }

@app.get("/mock-orders")
def mock_orders():
    return {
        "order_id": random.randint(1000, 9999),
        "amount": random.uniform(100, 1000)
    }
