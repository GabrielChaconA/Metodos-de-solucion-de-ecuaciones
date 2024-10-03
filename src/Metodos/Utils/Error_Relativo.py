class Error_Relativo:

    def Error_Relativo(self,x1,x2):
        if x1 == 0 :
         return 0
        error= ((x1-x2)/x1)*100
        if error < 0:
           return error*-1
        return error