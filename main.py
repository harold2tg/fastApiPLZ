from fastapi import FastAPI
from my_movies import movies

app = FastAPI()
app.title = "App fastAPI"
app.version = "0.0.0"

@app.get('/', tags=['Home'])
def message():
    # return HTMLResponse('<h1> Respondiento en html </h1>')
    return 'Configuración lista para arrancar con FastAPI'

@app.get('/movies/',tags=['movies'])
def get_movies():
    return movies

@app.get('/movies/{id}', tags=['movies'])
def get_movies_id(id:int):
    return next((movie for movie in movies if movie["id"] == id),[])


@app.get('/movies', tags=['movies'])
def get_movies_by_category(category:str):
    result = []
    for movie in movies:
        if movie["category"] == category:
            result.append(movie)
    return result



