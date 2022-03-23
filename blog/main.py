from imp import reload
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from blog.routers import desabollador, materiales, trabajo, typoServicio


from .routers import cliente, vehiculo, coche, piesa, servicio, trabajo, empleado, asignacion
from . import models
from .database import engine


app = FastAPI()

origins=[
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(engine)

app.include_router(cliente.router)
app.include_router(vehiculo.router)
app.include_router(coche.router)
app.include_router(piesa.router)
app.include_router(servicio.router)
app.include_router(desabollador.router)
app.include_router(trabajo.router)
app.include_router(empleado.router)
app.include_router(asignacion.router)
app.include_router(materiales.router)
app.include_router(typoServicio.router)


#if __name__ == "__main__":
#   uvicorn.run("blog.main:app", host="0.0.0.0", post=8000, reload=True)