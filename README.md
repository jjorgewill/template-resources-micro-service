# template-resources-micro-service
Midleware integrado para acceso a recursos protegidos.
Esta plantilla ofrece una arquitectura para crear aplicaciones con django y no empezar a realizar todas las configuraciones desde cero.
en esta plantilla usted puede modificar crear sus propias apps y modelos libremente.



# Requisitos

1 Tener un servidor con redis instalado, porque lo vamos a utilizar para mantener informacion en memoria y evitar sobre cargar al servicio de autenticacion y ofrecer un buen rendimiento.

2 Python 3.5


# Pasos
1. Crear el entorno virtual 

2. pip install -r conf/base/requeriments.txt

3. ./manager.py makemigrate 

4. ./manager.py migrate
