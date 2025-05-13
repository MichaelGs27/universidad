from datetime import datetime

class Libro:
    def __init__(self, codigo, titulo, autor, categoria, identificacion, valor_perdida):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.identificacion = identificacion
        self.valor_perdida = valor_perdida

class Movimiento:
    def __init__(self, libro, socio, fecha_prestamo, fecha_entrega=None):
        self.libro = libro
        self.socio = socio
        self.fecha_prestamo = fecha_prestamo
        self.fecha_entrega = fecha_entrega
        self.multa = 0

    def calcular_multa(self):
        if self.fecha_entrega is not None:
            # Supongamos una multa de $1 por cada día de retraso en la entrega
            dias_de_retraso = (self.fecha_entrega - self.fecha_prestamo).days
            if dias_de_retraso > 0:
                self.multa = dias_de_retraso * 1
        return self.multa

class Socio:
    def __init__(self, numero_socio, nombre, direccion):
        self.numero_socio = numero_socio
        self.nombre = nombre
        self.direccion = direccion

# Ejemplo de uso:

# Crear un libro
libro1 = Libro("L001", "El Gran Gatsby", "F. Scott Fitzgerald", "Ficción", "ISBN12345", 20)

# Crear un socio
socio1 = Socio("S001", "Juan Pérez", "Calle Principal 123")

# Crear un movimiento de préstamo
fecha_prestamo = datetime(2023, 9, 15)
movimiento1 = Movimiento(libro1, socio1, fecha_prestamo)

# Simular la entrega del libro
fecha_entrega = datetime(2023, 9, 20)
movimiento1.fecha_entrega = fecha_entrega

# Calcular la multa (si hay retraso)
movimiento1.calcular_multa()

# Imprimir la multa
print(f"Multa por retraso: ${movimiento1.multa}")
