class Video:
    def __init__(self, titulo, autor, duracion):
        self.titulo = titulo
        self.autor = autor 
        self.duracion = duracion

class Nodo:
    def __init__(self, video):
        self.video = video
        self.siguiente = None

class ListaCircular:
    def __init__(self):
        self.cabeza = None

    def agregarVideo(self, video):
        nuevo_nodo = Nodo(video)
        if self.estaVacia():
            self.cabeza = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza
        else:
            temporal = self.cabeza
            while temporal.siguiente != self.cabeza:
                temporal = temporal.siguiente
            temporal.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza
        

    def imprimirVideo(self):
        if self.estaVacia():
            print("no hay videos dentro de la lista")
        else:
            temporal = self.cabeza
            while True:
                print("Titulo: '{}', autor: '{}', duracion: '{}'".format(temporal.video.titulo, temporal.video.autor, temporal.video.duracion))
                temporal = temporal.siguiente
                if temporal == self.cabeza:
                    break

    def buscarVideo(self, titulo):
        if self.estaVacia():
            print("La lista no contiene videos")
            return None
        temporal = self.cabeza
        while True:
            if temporal.video.titulo == titulo:
                return temporal.video
            temporal = temporal.siguiente
            if temporal == self.cabeza:
                break
            print("el video '{}' no se encontró en la lista".format(titulo))
            return None

    def eliminarVideo():
        pass

    def estaVacia(self):
        return self.cabeza is None


## EJEMPLO DE USO (???

listaVideos = ListaCircular()

# esta vacia
print(listaVideos.estaVacia())

# agregar video
video1 = Video("Silver Tongues", "Louis Tomlinson", "03:00")
video2 = Video("Golden", "Harry Styles", "03:00")
video3 = Video("Heaven", "Niall Horan", "03:00")

listaVideos.agregarVideo(video1)
listaVideos.agregarVideo(video2)
listaVideos.agregarVideo(video3)

# imprimir videos
print("La lista de video es:")
listaVideos.imprimirVideo()

# buscar video
titulo = "Silver Tongues"
video = listaVideos.buscarVideo(titulo)
if video:
    print("titulo: {}, autor: {}, duracion: {}".format(video.titulo, video.autor, video.duracion))

# esta vacia
print(listaVideos.estaVacia())