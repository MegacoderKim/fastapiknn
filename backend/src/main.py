import os
from fastapi import FastAPI
from elasticsearch import AsyncElasticsearch

ELASTIC_HOST = os.environ.get("ES_HOST")

app = FastAPI()
es = AsyncElasticsearch(hosts=(ELASTIC_HOST))


@app.on_event("shutdown")
async def app_shutdown():
    await es.close()

@app.get("/")
async def root():
    return {"message": "Hello World"}
