"""
Spec:
    Listado:
        List of string
"""


def crearEmpleados():
    """
    Retorna un listado de empleados vacio
    
        Args:
            None

        Returns:
            empleados(list): una lista vacia
    """
    empleados = []
    return empleados


def agregarEmpleado(empleados, e):
    """
    Agrega un empleado al listado de empleados

        Args:
            empleados (Empleados): Listado al cual agregarle el empleado
            e (str): Empleado a ser agregado

        Returns:
            None
    """
    empleados.append(e)


def eliminarEmpleado(empleados, e):
    """
    Elimina un empleado del listado de empleados
        Args:
            empleados (Empleados): Listado del cual eliminar el empleado
            e (str): Empleado a ser eliminado

        Returns:
            None
    """
    empleados.remove(e)


def recuperarEmpleado(empleados, i):
    """
    Retorna el empleado en la posicion i (el indice empieza en 0)

        Args:
            empleados(List): Lista de empleados a recuperar datos
            i (int): Entero en cuya posicion se encuentra el empleado deseado

        Returns:
            empleados[i]: Nombre del empleado en la posicion i (str)
    """
    return empleados[i]


def tamanio(empleados):
    """
    Retorna la cantidad de empleados en el listado

        Args:
            empleados(list): Lista de empleados a la cual leer su longitud

        Returns:
            longitud de la lista (int)
    """
    return len(empleados)
