
list_nombre = []
list_correo = []
list_identificacion = []
list_contacto = []
list_edad = []
list_años_experiencia = []
list_profesion = []
list_ciudad = []
list_sexo = []
import os

def fnt_limpiar():
    os.system('cls')
    print('Autor: Cesar A. Castro')
    print('Fecha: 18 - 04 - 2024')

def fnt_registrar(identificacion, nombre, correo, contacto, edad, años_experiencia, profesion, ciudad, sexo):
    if identificacion == '' or nombre == '' or correo == '' or contacto == '' or edad == '' or años_experiencia == '' or profesion == '' or ciudad == '' or sexo == '':
        enter = input('\nError, debe ingresar todos los datos <ENTER>')
    else:
        list_identificacion.append(identificacion)
        list_nombre.append(nombre)
        list_correo.append(correo)
        list_contacto.append(contacto)
        list_edad.append(edad)
        list_años_experiencia.append(años_experiencia)
        list_profesion.append(profesion)
        list_ciudad.append(ciudad)
        list_sexo.append(sexo)
        fnt_limpiar()
        print('Datos ingresados correctamente')
        enter = input('\nPresione <ENTER> para continuar...')
