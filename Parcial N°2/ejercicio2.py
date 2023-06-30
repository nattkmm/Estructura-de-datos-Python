class Tarea:
    def __init__(self, identificador, titulo, descripcion, estado):
        self.identificador = identificador
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado

class ListaBidireccional:
    def __init__(self):
        self.tareas = []

    def agregarTarea(self, tarea):
        self.tareas.append(tarea)

    def eliminarTarea():
        pass

    def buscarTarea(self, tarea, identificador):
        for tarea in self.tareas:
            if tarea.identificador == identificador:
                return tarea
        return None

    def cambiarEstado():
        pass

    def imprimirTarea():
        pass