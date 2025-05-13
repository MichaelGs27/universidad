#USER 
import userclass
oUsuario = userclass.User("Michael", "Michael12345") 
print("""-----------------BIENVENIDO----------------
                LOGIN""")
nContador = 0
nContador = nContador +1
while True:
        cUser = input("User: ")
        if oUsuario.VerificarUsuario() == False:
             print("El usuario no existe.")
        elif oUsuario.VerificarUsuario() == True:
            cClave = input("Password: ")
            while True:
                if cClave == oUsuario.getClave():
                    nContador = 0
                    nContador = nContador +1
                    print(f"Va en el intento {nContador}")
                    print("La clave no es valida.")
                    if nContador == 3:
                        print("Usuario bloqueado alcanzo el limite de intentos.")
                    break
            if cClave == oUsuario.getClave():
                print("Bienvenido")
                
                

