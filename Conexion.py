from pymongo import MongoClient # Importamos la bilbioteca de mongo para hacer uso de su sintaxis

conexionCliente = MongoClient('localhost', 27017)
db = conexionCliente[ "PruebaDB" ]
