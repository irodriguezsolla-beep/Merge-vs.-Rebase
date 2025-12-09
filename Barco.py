class Barco:
   def __init__(self, nombre, longitud):
       self.nombre = nombre
       self.longitud = longitud
       self.golpes_recibidos = 0


   def recibir_impacto(self):
       self.golpes_recibidos += 1


   def esta_hundido(self):
       return self.golpes_recibidos == self.longitud

if __name__ == "__main__":
   submarino = Barco("Submarino", 1)
   buque = Barco("Buque", 3)


   submarino.recibir_impacto()
   print(submarino.esta_hundido())


   buque.recibir_impacto()
   buque.recibir_impacto()
   print(buque.esta_hundido())
   buque.recibir_impacto()
   print(buque.esta_hundido())

   ...