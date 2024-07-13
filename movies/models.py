from django.db import models

# Con estas clases gestionaremos la conexion a la base de datos y utilizaremos la clase Movie para la creacion de una tabla con el mismo nombre donde especificaremos los detalles de las peliculas

class Movie(models.Model):
    movie_id = models.IntegerField(null=False)
    name = models.CharField(max_length=30, null=False)
    genre = models.CharField(max_length=30, null=False)
    director_name = models.CharField(max_length=30, null=False)
    year = models.IntegerField(null=False)
    synopsis = models.CharField(max_length=150, null=False)

    def __str__(self) -> str:
        return self.name
