from fastapi import FastAPI
from schema import Item
from predict import Clustering
import pandas as pd
import uvicorn

app = FastAPI()


@app.get('/', tags = ['Main'])
async def main():
    return {'Welcome to: ' 'Clustering-API'}

@app.post('/cluster', tags=['Cluster'])
async def Cluster(item:Item):
    x = pd.DataFrame([item.dict().values()], columns=item.dict().keys())
    result = Clustering(x)
    return result

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)   