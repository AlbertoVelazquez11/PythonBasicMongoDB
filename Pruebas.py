import CrudGenerico
import bson

indice = 0
buscar = ""
documento = { "autor" : "" ,
              "edad" : "" ,
              "correo" : "" ,
              "telefono" : "" }

# Guardar 3 documentos
while indice < 3 :
    print "Persona " + str( indice )
    documento[ "autor" ] = raw_input("Ingrese el nombre del autor: ")
    documento[ "edad" ] = raw_input("Ingrese la edad: ")
    documento[ "correo" ] = raw_input("Ingrese el correo: ")
    documento[ "telefono" ] = raw_input("Ingrese numero telefonico: ")
    print "\n"
    CrudGenerico.InsertarDocumento( "Personas" , documento )
    documento.ObjectId = bson.ObjectId()
    indice += 1

# Buscar un documento
buscar = raw_input( "Ingrese el nombre a buscar: " )
x = CrudGenerico.BuscarDocumento( "Personas" , buscar )
print str( x )
