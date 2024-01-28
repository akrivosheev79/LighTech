from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from database.connection import conn
from routes.users import user_router
from routes.transactions import transaction_router
import uvicorn

app = FastAPI()

# Register routes
app.include_router(user_router, prefix="/user")
app.include_router(transaction_router, prefix="/transaction")

@app.on_event("startup")
def on_startup():
    conn()

@app.get("/")
async def home():
    return {"message": "Welcome"}

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)