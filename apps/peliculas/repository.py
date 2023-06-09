"""
Archivo donde se define la interfaz entre las capas de NEGOCIOS
y DATOS,

CAPA PRESENTACION<--dto.py-->CAPA NEGOCIO<--repository.py-->CAPA DE DATOS
     (jsons)                  clases.py                       models.py
                              (clases)                        (entities)
"""
from django.db import transaction

from core.exception import AppException
from peliculas.classes import Genero, Pelicula
from peliculas.error import PeliculasError
from peliculas.models import GeneroEntity, PeliculaEntity


def list() -> list[int]:
    search = PeliculaEntity.objects.all()
    return [pelicula.id for pelicula in search]


def get(id: int) -> Pelicula:
    pelicula_entity = PeliculaEntity.objects.filter(id=id).first()
    return pelicula_entity.to_class() if pelicula_entity else None


def save(pelicula: Pelicula) -> int:
    with transaction.atomic():
        # Primero se guarda la pelicula
        pelicula_entity = PeliculaEntity.from_class(pelicula)
        pelicula_entity.save()
        # Segundo se guardan los generos
        for genero in pelicula.generos:
            if not (genero_entity := GeneroEntity.get_by_name(genero)):
                genero_entity = GeneroEntity.from_class(genero)
                genero_entity.save()
            # Tercero se gurda la relacion Many to many
            pelicula_entity.generos.add(genero_entity)
        return pelicula_entity.id


def delete(id: int):
    search = PeliculaEntity.objects.filter(id=id)
    if not search.exists():
        msj = f"Pelicula with id {id} not exist"
        raise AppException(PeliculasError.PELICULA_NO_EXISTE, msj)
    search.delete()
