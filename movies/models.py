from django.db import models

# Con estas clases gestionaremos la conexion a la base de datos y utilizaremos la clase Movie para la creacion de una tabla con el mismo nombre donde especificaremos los detalles de las peliculas

class Movie(models.Model):
    movie_id = models.IntegerField(max_length=10, null=False)
    name =  
