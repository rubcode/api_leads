from fastapi import FastAPI
from routes.routes import router


app = FastAPI(title="Leads API")

app.include_router(router)