from Metodos.metodo_jacobi import metoodo_jacobi
from Metodos.metodo_seidel import metodo_seidel
class Menu:
    def Menu(self):
        instance_metodoJacobi = metoodo_jacobi()
        instance_metodoSeidel = metodo_seidel()
        anwer = input("Elige un metodo:Jacobi(1) Seidel(2)")
        if anwer == "1" :
         instance_metodoJacobi.matriz_jacobi()
        if anwer == "2":
         instance_metodoSeidel.matriz_seidel()
         
        return 