from fastapi import FastAPI
from elasticsearch import AsyncElasticsearch

app = FastAPI()
es = AsyncElasticsearch()


@app.on_event("shutdown")
async def app_shutdown():
    await es.close()

@app.get("/")
async def root():
    return {"message": "Hello World"}
