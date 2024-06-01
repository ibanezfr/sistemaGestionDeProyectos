"""
Spec:
    Listado:
        List of Tareas
"""


def crearListado():
    """
    Retorna un listado de tareas vacio

        Args:
            None

        Returns:
            - listado: una lista vacia
    """
    listado = []
    return listado


def agregarTarea(listado, t):
    """
    Agrega una tarea al listado de tareas

        Args:
            listado (Listado): Listado al cual agregarle la tarea
            t(Tarea): Tarea a ser agregada

        Returns:
            None
    """
    listado.append(t)


def eliminarTarea(listado, t):
    """
    Elimina una tarea del listado de tareas

        Args:
            listado (Listado): Listado del cual eliminar la tarea
            t (Tarea): Tarea a ser eliminada

        Returns:
            None
    """
    listado.remove(t)


def recuperarTarea(listado, i):
    """
    Retorna la tarea en la posicion i (el indice empieza en 0)

        Args:
            listado(Listado): Listado del cual recuperar la tarea
            i(int): Entero que indica la posicion del listado

        Returns:
            Listado[i]: retorna la tarea en la posicion i (Tarea)
    """
    return listado[i]


def tamanio(listado):
    """
    Retorna la cantidad de tareas en el listado

        Args:
            listado(Listado): Listado a calcular su longitud

        Returns:
            - longitud del listado (int)
    """
    return len(listado)
