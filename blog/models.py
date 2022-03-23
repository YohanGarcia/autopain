from msilib.schema import Class
from unicodedata import name
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import backref, relationship
import datetime

x = datetime.datetime.now()

from .database import Base

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    lestname = Column(String)
    telefono = Column(String)
    cedula = Column(String)

    fecha = Column(String, default=x.strftime("%x"))
    hora = Column(String, default=x.strftime("%X"))

    vehiculos = relationship("Vehiculo", backref="clientes")

class Vehiculo(Base):
    __tablename__ = "vehiculos"

    id = Column(Integer, primary_key=True, index=True)
    marca = Column(String)
    modelo = Column(String)
    color = Column(String)
    placa = Column(String)
    age = Column(String)
    status = Column(String)

    fecha = Column(String, default=x.strftime("%x"))
    hora = Column(String, default=x.strftime("%X"))

    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    servicios = relationship("Servicio", backref="vehiculos")
    asignacion = relationship("Asignacion", backref="vehiculos")

class Coche(Base):
    __tablename__ = "coches"

    id = Column(Integer, primary_key=True, index=True)
    marca = Column(String)
    modelos = relationship("Modelo", backref="coches")

class Modelo(Base):
    __tablename__ = "modelos"
    id = Column(Integer, primary_key=True, index=True)
    modelo = Column(String)
    coche_id = Column(Integer, ForeignKey("coches.id"))

class Servicio(Base):
    __tablename__ = "servicios"
    id = Column(Integer, primary_key=True, index=True)
    status = Column(String)

    fecha = Column(String, default=x.strftime("%x"))
    hora = Column(String, default=x.strftime("%X"))

    desabolladuras = relationship("Desabolladura", backref="servicios")
    vehiculo_id = Column(Integer, ForeignKey("vehiculos.id"))
    typo_id  = Column(Integer, ForeignKey("typos.id"))

class Typo(Base):
    __tablename__ = "typos"
    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)
    servicios = relationship("Servicio", backref="typos")

class Piesa(Base):
    __tablename__ = "piesas"

    id = Column(Integer, primary_key=True, index=True)
    piesa = Column(String)
    precio = relationship('Preciopiesa', backref="piesas")

class Preciopiesa(Base):
    __tablename__ = "preciopiesas"

    id = Column(Integer, primary_key=True, index=True)
    precio = Column(Integer)
    piesa_id = Column(Integer, ForeignKey("piesas.id"))

class Desabolladura(Base):
    __tablename__ = "desabolladuras"

    id = Column(Integer, primary_key=True, index=True)
    piesa =Column(String)
    precio = Column(Integer)

    fecha = Column(String, default=x.strftime("%x"))
    hora = Column(String, default=x.strftime("%X"))

    servicio_id = Column(Integer, ForeignKey("servicios.id"))
    asignacion = relationship("Asignacion", backref="desabollaras")

class Empleado(Base):
    __tablename__ = "empleados"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    lestname = Column(String)
    telefono = Column(String)
    cedula = Column(String)
    direccion = Column(String) 
    codigo_postal = Column(String)
    status = Column(String)


    fecha = Column(String, default=x.strftime("%x"))
    hora = Column(String, default=x.strftime("%X"))

    asignaciones = relationship("Asignacion", backref="empleados")

class Trabajo(Base):
    __tablename__ = "trabajos"
    
    id = Column(Integer, primary_key=True, index=True)
    trabajo_tipo = Column(String)
    status = Column(String)


    fecha = Column(String, default=x.strftime("%x"))
    hora = Column(String, default=x.strftime("%X"))

    preciotrabajo = relationship("Preciotrabajo", backref="trabajos")

class Preciotrabajo(Base):
    __tablename__ = "preciotrabajos"

    id = Column(Integer, primary_key=True, index=True)
    precio = Column(Integer)
    trabajo_id = Column(Integer, ForeignKey("trabajos.id"))

class Asignacion(Base):
    __tablename__ = "asignaciones"

    id = Column(Integer, primary_key=True, index=True)
    tipo_trabjo = Column(String)
    precio_trabajo = Column(Integer)
    status = Column(String)


    fecha = Column(String, default=x.strftime("%x"))
    hora = Column(String, default=x.strftime("%X"))

    empleados_id = Column(Integer, ForeignKey("empleados.id"))
    desabolladura_id = Column(Integer, ForeignKey("desabolladuras.id"))
    vehiculo_id = Column(Integer, ForeignKey("vehiculos.id"))
    
class Material(Base):
    __tablename__ = "materiales"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    materialnumero = relationship("Materialnumero", backref="materiales")

class Materialnumero(Base):
    __tablename__ = "materialnumeros"
    id = Column(Integer, primary_key=True, index=True)
    numero = Column(String)
    precio = Column(Integer)

    matrales_id = Column(Integer, ForeignKey("materiales.id"))

