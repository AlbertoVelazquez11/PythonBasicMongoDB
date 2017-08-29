import Conexion

def InsertarDocumento( NombreColeccion , Documento ) :
    coleccion = Conexion.db[ NombreColeccion ]
    return coleccion.insert_one( Documento ).inserted_id # Regresa el ID

def BuscarDocumento( NombreColeccion, BuscarNombre ) :
    coleccion = Conexion.db[ NombreColeccion ]
    return coleccion.find_one({"autor": BuscarNombre })
