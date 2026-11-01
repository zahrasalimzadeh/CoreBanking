from fastapi import FastAPI
from Presentation.API.Endpoints.account_api import router as account_router
from Presentation.API.Endpoints.transaction_api import router as transaction_router

app = FastAPI(title="Core Banking API")

app.include_router(account_router)
app.include_router(transaction_router)


@app.get("/health_check")
def health_check():
    return {"is_health": True}