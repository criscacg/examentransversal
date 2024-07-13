#https://github

import os, random, statistics
from random import randint
from statistics import mean, geometric_mean
nombres = ['Juan Pérez','María García','Carlos López','Ana Martínez','Pedro Rodríguez',
                'Laura Hernández','Miguel Sánchez','sabel Gómez','Francisco Díaz','Elena Fernández']
sueldos=[]
trabajadores=[]

def Asig_sueld_Alea():
    for nombre in nombres:
        trabajadores.append ({'Nombre': nombre, 
                         'sueldo': random.randint (300000 , 2500000)})
    print(f'(trabajador: {trabajadores} resgistro ok')
    
def Clas_sueldos():
    for i in trabajadores:
        if i ['sueldos'] >800000:
            print(f'(nombre empleado: {nombres} sueldo: {sueldos}')
        elif i ['sueldos'] <2000000:
            print(f'(nombre empleado: {nombres} sueldo: {sueldos})')
def Metrica():
    for i in sueldos:
            print(min([sueldos]))
            print(max([sueldos]))
            print(mean([sueldos]))
        
        
        
    
    
    

    

while True:
    print('1) Asignar Sueldos Aleatorios')
    print('2) Clasificar Sueldos')
    print('3) Ver estadisticas')
    print('4) Reporte de Sueldos')
    print('5) Salir del Programa')
    
    opc = input('ingrese opcion: ')
    if opc=="1" :
       Asig_sueld_Alea()
