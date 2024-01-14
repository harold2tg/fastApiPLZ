from fastapi import FastAPI

app = FastAPI()

@app.get('')
def message():
    return 'configuracion lista para trabajar con FastAPI'