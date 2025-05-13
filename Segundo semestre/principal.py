#Cargo la libreria clases // cNombreTipo = input("Ingrese el nombre del tipo de identificación: ")
import clases

#Creo en el objeto de la clase tipo identificación, para referenciar que es un objeto lo escribo "oTipo"
oLibro = clases.Libros("909000","","","","","","","","","")

#Pedir datos al usuario 
cCodLibro = '909000'
cNomLibro = input("Ingrese el nombre del libro: ")
cAutor = input("Ingrese el autor de libro: ")
nNumeroPag = int(input("Ingrese el número de páginas: "))
cCategoria = input("Ingrese la categoria del libro: ")
nAñopublicacion = int(input("Ingrese el año de la publicación del libro: "))
cEstado = input("Ingrese el estado del libro: ")
cVirualFisi = input("Ingrese si es virtual o fisico: ")
cIdioma = input("Ingrese el idioma del libro: ")
cEditorial = input("Ingrese el editorial del libro: ")

#Modificar valores de las variables 
oLibro.setcCodLibro(cCodLibro)
oLibro.setcNomLibro(cNomLibro)
oLibro.setcAutor(cAutor)
oLibro.setnNumPag(nNumeroPag)
oLibro.setcCategoria(cCategoria)
oLibro.setnAñoPublicacion(nAñopublicacion)
oLibro.setcEstado(cEstado)
oLibro.setcVitualFisico(cVirualFisi)
oLibro.setcIdioma(cIdioma)
oLibro.setcEditoria(cEditorial)

# Resultado en pantalla
print("---------------------------------------------")
print("El codigo de libro es: ",oLibro.getcCodLibro())
print("El nombre del libro es: ",oLibro.getcNomLibro())
print("El autor del libro es: ",oLibro.getcAutor())
print("El número de páginas del libro es: ",oLibro.getnNumPag())
print("La categoria del libro es: ",oLibro.getcCategoria())
print("El año de publicación del libro es: ",oLibro.getnAñoPublicacion())
print("El estado del libro es: ",oLibro.getcEstado())
print("El libro es: ",oLibro.getcVitualFisico())
print("El idioma del libro es: ",oLibro.getcIdioma())
print("El editorial del libro es: ",oLibro.getcEditoria())