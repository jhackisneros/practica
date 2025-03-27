# Clase Pergamino
class Pergamino:
    def __init__(self, titulo, autor, tipo, estado, casa=None):
        self.titulo = titulo
        self.autor = autor
        self.tipo = tipo
        self.estado = estado
        self.casa = casa

    # Métodos Getters
    def mostrar_titulo(self):
        return self.titulo

    def mostrar_autor(self):
        return self.autor

    def mostrar_tipo(self):
        return self.tipo

    def mostrar_estado(self):
        return self.estado

    def mostrar_casa(self):
        return self.casa

    # Métodos Setters
    def set_estado(self, estado):
        self.estado = estado

    def cambiar_casa(self, casa):
        self.casa = casa

    # Método para verificar si está disponible
    def is_available(self):
        return self.estado == "Disponible"

# Clase Maestre
class Maestre:
    def __init__(self, nombre, rango, lista_de_pergaminos=None):
        if lista_de_pergaminos is None:
            lista_de_pergaminos = []
        self.nombre = nombre
        self.rango = rango
        self.lista_de_pergaminos = lista_de_pergaminos

    def mostrar_nombre(self):
        return self.nombre

    def mostrar_rango(self):
        return self.rango

    def mostrar_lista_de_pergaminos(self):
        return [p.mostrar_titulo() for p in self.lista_de_pergaminos]  # Mostramos solo los títulos

    def cambiar_rango(self, rango):
        self.rango = rango

    def tomar_prestado(self, pergamino):
        if pergamino.is_available():
            pergamino.set_estado("Prestado")
            self.lista_de_pergaminos.append(pergamino)
            print(f"{self.nombre} ha tomado prestado el pergamino: {pergamino.mostrar_titulo()}")
        else:
            print(f"El pergamino '{pergamino.mostrar_titulo()}' no está disponible.")

    def devolver_pergamino(self, pergamino):
        if pergamino in self.lista_de_pergaminos:
            pergamino.set_estado("Disponible")
            self.lista_de_pergaminos.remove(pergamino)
            print(f"{self.nombre} ha devuelto el pergamino: {pergamino.mostrar_titulo()}")
        else:
            print(f"{self.nombre} no tiene el pergamino '{pergamino.mostrar_titulo()}' prestado.")

# Clase Aprendiz
class Aprendiz(Maestre):
    def __init__(self, nombre, rango, mentor, lista_de_pergaminos=None):
        if lista_de_pergaminos is None:
            lista_de_pergaminos = []
        super().__init__(nombre, rango, lista_de_pergaminos)
        self.mentor = mentor
        self.contador = 0

    def mostrar_mentor(self):
        return self.mentor.mostrar_nombre()

    def cambiar_mentor(self, nuevo_mentor):
        self.mentor = nuevo_mentor

    def pedir_consejo(self):
        self.contador += 1
        print(f"{self.nombre} ha pedido consejo a su mentor {self.mentor.mostrar_nombre()}.")

    def mostrar_contador(self):
        return self.contador

# --- Ejemplo de uso ---
maestre1 = Maestre("Maestre Luwin", "Maestre")

# Aprendiz sin pergaminos prestados
aprendiz1 = Aprendiz("Samwell Tarly", "Aprendiz", maestre1)

# Creamos un pergamino
pergamino1 = Pergamino("Historia Antigua", "Archimaestre Marwyn", "HISTORIA", "Disponible")

# Aprendiz con pergaminos prestados desde el inicio
aprendiz2 = Aprendiz("Pate", "Aprendiz", maestre1, [pergamino1])

# Mostramos los pergaminos prestados
print(aprendiz1.mostrar_lista_de_pergaminos())  # []
print(aprendiz2.mostrar_lista_de_pergaminos())  # ['Historia Antigua']
