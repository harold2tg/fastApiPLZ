from fastapi import FastAPI


app = FastAPI()
app.title = "App fastAPI"
app.version = "0.0.0"

@app.get('/', tags=['Home'])
def message():
    # return HTMLResponse('<h1> Respondiento en html </h1>')
    return 'Configuración lista para arrancar con FastAPI'


