nombre = str(input('Ingresa nombre:'))
apellidos = str(input('Ingresa tus apellidos:'))
telefono = int(input('Ingresa teléfono:'))
correo_electronico = input('Ingresa tu correo electrónico:')
nombre_completo = nombre + ' ' + apellidos

print('Hola ' + nombre_completo + ', en breve recibirás un correo a ' + correo_electronico)