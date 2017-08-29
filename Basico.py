import pymongo # Importamos la bilbioteca de mongo para hacer uso de su sintaxis
import datetime
import pprint
from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.GrupoEscolarBD

coleccion = db.Alumnos

registro = { "autor" : "Alberto" ,
             "texto" : "Primer registro" ,
             "tags" : [ "test" , "prueba" , "registro" ] ,
             "date" : datetime.datetime.utcnow() }

post_id = coleccion.insert_one(registro).inserted_id

print "El id del registro guardado: " + str(post_id)

pprint.pprint(coleccion.find_one())				# Regresar el primer documento encontrado
pprint.pprint(coleccion.find_one({"autor": "Alberto"}))	# Regresar el primer documento que cumpla la condicion
coleccion.find_one({"autor": "Kala"})			# Si no se cumple la condicion, no regresa nada
