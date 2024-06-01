# Spec:
#   tarea:
#       nombre: string
#       descripcion: string
#       asignado: string (nombre de empleado)
#       estado: string o tadEstado (pendiente, en progreso, completada)
#       fecha de vencimiento: datetime
from datetime import date


def crearTarea():
    """
    Retorna una tarea vacia.

        Args:
            None
            
        Returns:
            list: Una lista que representa una tarea nueva con los siguientes elementos:
                - Nombre de la tarea (str)
                - Descripcion de la trarea (str)
                - Asignado a (str)
                - Estado de la tarea (str)
                - Fecha de vencimiento (str)
    """
    return ["", "", "", "", 0]


def cargarTarea(tarea, nombre, descripcion, asignado, estado, vencimiento):
    """
    Carga los valores de una tarea

        Args:
            tarea (Tarea): tarea a cargar
            nombre (str): nombre de la tarea
            descripcion (str): descripcion de la tarea
            asignado (str): nombre del empleado a quien se le asigna la tarea
            estado (str): estado de la tarea, valores validos: pendiente, en progreso, completado
            vencimiento (str): fecha de vencimiento de la tarea, formato ISO 8601 (YYYY-MM-DD)

        Returns:
            None
    """
    tarea[0] = nombre
    tarea[1] = descripcion
    tarea[2] = asignado
    tarea[3] = estado
    tarea[4] = date.fromisoformat(vencimiento)


def verNombre(tarea):
    """
    Retorna el nombre de la tarea

        Args:
            tarea(Tarea): Lista con los datos de la tarea

        Returns:
            - nombre de la tarea (str)
    """
    return tarea[0]


def verDescripcion(tarea):
    """
    Retorna la descripcion de la tarea

        Args:
            tarea(Tarea): Lista con los datos de la tarea

        Returns:
            - descripcion de la tarea (str)
    """
    return tarea[1]


def verAsignado(tarea):
    """
    Retorna el nombre del empleado que tiene asignada la tarea

        Args:
            tarea(Tarea): Lista con lo datos de la tarea

        Returns:
            - a quien esta asignada la tarea (str)

    """
    return tarea[2]


def verEstado(tarea):
    """
    Retorna el estado de la tarea

        Args:
            tarea(Tarea): Lista con los datos de la tarea

        Returns:
            - Estado de la tarea: Pendiente, En Progreso, Completado (str)
    """
    return tarea[3]


def verVencimiento(tarea):
    """
    Retorna la fecha de vencimiento de la tarea en formato ISO 8061

        Args:
            tarea(Tarea): Lista con los datos de la tarea

        Returns:
            - Vencimiento de la tarea (isoformat)
    """
    return date.isoformat(tarea[4])


def modNombre(tarea, nombre):
    """
    Modifica el nombre de la tarea

        Args:
            tarea(Tarea): Lista con los datos de la tarea
            nombre(Str): nuevo nombre de la tarea

        Returns:
            None
    """
    tarea[0] = nombre


def modDescripcion(tarea, descripcion):
    """
    Modifica la descripcion de la tarea

        Args:
            tarea(Tarea): Lista con los datos de la tarea
            descripcion(str): Nueva descripcion de la tarea

        Returns:
            None
    """
    tarea[1] = descripcion


def modAsignado(tarea, asignado):
    """
    Modifica el empleado que tiene asignada la tarea

        Args:
            tarea(Tarea): Lista con los datos de la tarea
            asignado(str): Nuevo empleado asignado

        Returns:
            None
    """
    tarea[2] = asignado


def modEstado(tarea, estado):
    """
    Modifica el estado de la tarea
    
        Args:
            tarea(Tarea): Lista con los datos de la tarea
            estado(str): Nuevo estado de la tarea

        Returns:
            None
    """
    tarea[3] = estado


def modVencimiento(tarea, vencimiento):
    """
    Modifica la fecha de vencimiento de la tarea

        Args:
            tarea(Tarea): Lista con los datos de la tarea
            vencimiento(datetime): Nueva fecha de vencimiento de la tarea

        Returns:
            None
    """
    tarea[4] = date.fromisoformat(vencimiento)


def asignarTarea(tareaDestino, tareaFuente):
    """
    Asigna el valor de la tarea fuente a la tarea destino

        Args:
            tareaDestino(Tarea): Tarea a la cual se asignaran los cambios
            tareaFuente(Tarea): Tarea de la cual se leen los datos para luego modificar la tarea destino

        Returns:
            None
    """
    modNombre(tareaDestino, verNombre(tareaFuente))
    modDescripcion(tareaDestino, verDescripcion(tareaFuente))
    modAsignado(tareaDestino, verAsignado(tareaFuente))
    modEstado(tareaDestino, verEstado(tareaFuente))
    modVencimiento(tareaDestino, verVencimiento(tareaFuente))


def sonIguales(tarea1, tarea2):
    """
    Retorna True si tarea1 y tarea2 son exactamente iguales, de lo contrario retorna False

     Args:
        tarea1(Tarea): Una lista que representa una tarea, con los siguientes elementos:
            - Nombre de la tarea (str)
            - Descripción de la tarea (str)
            - Asignado a (str)
            - Estado de la tarea (str)
            - Fecha de vencimiento (str)
        tarea2(Tarea): Otra lista que representa una tarea, con los mismos elementos que tarea1.

    Returns:
        bool: True si las dos tareas son exactamente iguales, False en caso contrario.
    """
    n = verNombre(tarea1) == verNombre(tarea2)
    d = verDescripcion(tarea1) == verDescripcion(tarea2)
    a = verAsignado(tarea1) == verAsignado(tarea2)
    e = verEstado(tarea1) == verEstado(tarea2)
    vUno = verVencimiento(tarea1)
    vDos = verVencimiento(tarea2)
    v = vUno == vDos

    return n and d and a and e and v
