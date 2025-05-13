#Se crea la clase user
class User:
    #Atributos
    User = "Michael"
    Clave = "Michael12345"
    #Constructor
    def __init__(self, User, Clave):
        self.User = User
        self.Clave =Clave
    #Metodos
    def getUser(self):         #User
        return self.User
    def setUser(self, User):
        self.User = User
    
    def getClave(self):         #Clave
        return self.Clave
    def setClave(self, Clave):
        self.Clave = Clave
    #Metodo para verificar el usuario
    def VerificarUsuario(self):
        if self.getUser() == "Michael":
            return True 
        else:
            return False
    #Metodo para verificar la clave
    def Verificarclave(self):
        if self.getClave() == "Michael12345":
            return "Bienvenido"
        else:
            return  "Usuario bloqueado."
