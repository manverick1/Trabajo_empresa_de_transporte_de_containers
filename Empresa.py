from BarcosDirectorio.Barcos import Barco
from Camion import Camion
from Contenedores import Contenedor
from Pedidos import Pedidos
from MetodosViajes import MetodosViajes
# corregir directorio de estas dos
from Excepciones.exceptions import *

from Estados import EstadoMenor100, EstadoMenor1000, EstadoMas10000, EstadoMenor10000


from typing import List


import random

"""
Esta clase es la que deberia controlar todo calculo. En el diagrama no la habiamos hecho.
Pero para definir precios de viajes, calcular kilometros, aceptar y gestionar pedidos, creo
que de eso se deberia encargar esta clase.
"""


# Estos metodos de empresa podrian formar parte de una clase tipo EmpresaDatos que debuelva esas cosas como
# actualizar_barco_trotamundo_o_sedentario, camion_disponible etc.

# habria que hacer otra para la parte de procesar pedidos
class Empresa(MetodosViajes):
    def __init__(self, barcos: List[Barco], camiones: List[Camion]):
        self.__camiones = []
        self.__camiones.append(camiones)
        self.__barcos = []
        self.__barcos.append(barcos)
        
        # para puntos 3 y 4 de SE PIDE
        self.__barco_con_mas_km = None
        self.__barco_con_menos_km = None
        
        self.__contenedores = []
        
        


    'Getters y Setters'
    
    
    def get_contenedores(self):
        return self.__contenedores
    
    def set_contenedores(self, contenedores):
        self.__contenedores = contenedores
    contenedores = property(get_contenedores,set_contenedores)
    
    def get_barcos(self):
        return self.__barcos
    
    def set_barcos(self, barcos):
        self.__barcos = barcos
    barcos = property(get_barcos,set_barcos)
    
    def get_camiones(self):
        return self.__camiones
    
    def set_camiones(self, camiones):
        self.__camiones = camiones
    camiones = property(get_camiones,set_camiones)

    
    def get_barco_con_mas_km(self):
        
        return self.__barco_con_mas_km
    
    def set_barco_con_mas_km(self, barcos):
        self.__barco_con_mas_km = barcos
    barco_con_mas_km = property(get_barco_con_mas_km,set_barco_con_mas_km)


    
    def get_barco_con_menos_km(self):
      
        return self.__barco_con_menos_km
    
    def set_barco_con_menos_km(self, barcos):
        self.__barco_con_menos_km = barcos
    barco_con_menos_km = property(get_barco_con_menos_km,set_barco_con_menos_km)
    
    
    
    
    
    def camion_disponible(self):          
        for camion in self.camiones:
            if (camion.get_disponible()):
                #segun la teoria, esto afecta a la lista de empresa de self.camiones en cualquier parte del codigo
                camion.set_disponible = False
                return camion
        # falta ver donde se catchea esta excepcion (sacar este comentario cuando ya este)
        raise No_hay_camiones_disponibles("En este momento no hay camiones disponibles")
    
    
    def actualizar_barco_trotamundo_o_sedentario(self):
        
        bmenos = self.get_barco_con_menos_km()
        bmas = self.get_barco_con_mas_km()
        
        for barco in self.get_barcos():
            # actualizo barco sedentario
            if barco.get_km_recorridos() < bmenos or bmenos.get_km_recorridos() == 0:
                self.set_barco_con_menos_km(barco)
            
            # actualizo barco trotamundo
            if barco.get_km_recorridos() > bmas:
                self.set_barco_con_mas_km(barco)
        
        return
    
                
           
    #El container que mayor cantidad de veces viajó completo con una única carga.
    def container_con_mas_viajes_con_una_carga(self):
        container_mas_viajes = Contenedor()
        aux = 0

        for barco in self.__barcos:

            for container in barco.get_contenedores():

                if container.get_cant_de_veces_comple_y_carga_unica() > aux:
                    aux = container.get_cant_de_veces_comple_y_carga_unica()
                    container_mas_viajes = container
        
        return container_mas_viajes