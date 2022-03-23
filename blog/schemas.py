from msilib.schema import Class
from typing import List, Optional
from h11 import Data
from pydantic import BaseModel
from sqlalchemy import true

class PreciosTrabajoBase(BaseModel):
    precio:int
    trabajo_id:int
class PreciosTrabajoCreate(PreciosTrabajoBase):
    pass
class PrecioTrabajo(PreciosTrabajoBase):
    id:int
    class Config:
        orm_mode = True

class TrabajoBase(BaseModel):
    trabajo_tipo:str
class TrabajoCreate(TrabajoBase):
    pass
class Trabajo(TrabajoBase):
    id:int
    preciotrabajo: List[PrecioTrabajo] = []
    class Config:
        orm_mode =True

class PreciopiesBase(BaseModel):
    precio:int
    piesa_id:int
class PreciopiesCreate(PreciopiesBase):
    pass
class Preciopiesa(PreciopiesBase):
    id:int
    class Config:
        orm_mode = True

class PiesaBase(BaseModel):
    piesa:str
class PiesaCreate(PiesaBase):
    pass
class Piesa(PiesaBase):
    id:int
    precio: List[Preciopiesa] = []
    class Config:
        orm_mode =True

class ModeloBase(BaseModel):
    modelo:str
    coche_id:int
class modeloCreate(ModeloBase):
    pass
class Modelo(ModeloBase):
    id:int
    class Config:
        orm_mode = True

class CocheBase(BaseModel):
    marca:str
class CocheCreate(CocheBase):
    pass
class Coche(CocheBase):
    id:int
    modelos: List[Modelo] = []
    class Config:
        orm_mode = True


class AsignacionBase(BaseModel):
    tipo_trabjo:str
    precio_trabajo:int
    empleados_id:int
    desabolladura_id:int
    vehiculo_id:int
class AsignacionCreate(AsignacionBase):
    pass
class Asignacion(AsignacionBase):
    id:int
    class Config:
        orm_mode = True

class EmpleadoBase(BaseModel):
    name:str
    lestname:str
    telefono:str
    cedula:str
    direccion:str 
    codigo_postal:str
class EmpleadoCreate(EmpleadoBase):
    pass
class Empleado(EmpleadoBase):
    id:int
    fecha:str
    hora:str
    asignacion: List[Asignacion] = []
    class Config:
        orm_mode = True

class DesabolladuraBase(BaseModel):
    piesa:str
    precio:int
    servicio_id:int
class DesabolladutaCreate(DesabolladuraBase):
    pass
class Desabolladura(DesabolladuraBase):
    id:int
    servicio_id:int
    asignacion: List[Asignacion] = []
    class Config:
        orm_mode = True

class TypoBase(BaseModel):
    name:str
class TypoCreate(TypoBase):
    pass
class Typo(TypoBase):
    id:int
    class Config:
        orm_mode = True

class ServiciosBase(BaseModel):
    typo:str
    vehiculo_id:int
class ServiciosCreate(ServiciosBase):
    pass
class Servicio(ServiciosBase):
    id:int
    typo_id:int
    vehiculo_id:int
    desabolladuras: List[Desabolladura] = []
    class Config:
        orm_mode = True

class VehiculoBase(BaseModel):
    marca:str
    modelo:str
    color:str
    placa:str
    age:str
class VehiculoCreate(VehiculoBase):
    pass
class Vehiculo(VehiculoBase):
    id:int
    cliente_id:int
    servicios: List[Servicio] = []
    asignacion: List[Asignacion] = []
    class Config:
        orm_mode = True

class ClienteBase(BaseModel):
    name:str
    lestname:str
    telefono:str
    cedula: Optional[str] = None
class ClienteCreate(ClienteBase):
    pass
class Cliente(ClienteBase):
    id:int
    fecha:str
    hora:str
    vehiculos: List[Vehiculo] = []
    class Config:
        orm_mode = True

class MaterialnumeroBase(BaseModel):
    numero:str
    precio:int
    matrales_id:int
class MaterialnumeroCreate(MaterialnumeroBase):
    pass
class Materialnumero(MaterialnumeroBase):
    id:int
    class Config:
        orm_mode = True

class MaterialBase(BaseModel):
    name:str
class MaterialCreate(MaterialBase):
    pass
class Material(MaterialBase):
    id:int
    materialnumero: List[Materialnumero] = []
    class Config:
        orm_mode = True