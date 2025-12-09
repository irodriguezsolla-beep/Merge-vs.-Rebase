1)Primero creo los archivos vacios Barco.py y Tablero.py
y ademas hacer un commit con el nombre "Misión Inicial: Establecida la estructura de la Flota Base."

Paracer un repositorio primero vamos github, en terminal hacemos un "git init",
despues vamos al desplegable de pycharm a la ventana de git
y le damos al manage remotes y pegamos el link de github.
Ahora hacemos el commit push. Le pasamos el link del repositorio a compi.

2)Ahora para clonar iremos al repositorio copiamos el link de cod, le damos al nombre del proyecto ariva de todo 
y le damos a la opción del desplegables que pone clone repository

3)User 1 (Local): Edita Barco.py (ej. añade la clase Barco) y realiza un commit local: "Barco U1: Implementación del método de tamaño de la unidad.

4)User 2 (Local): Edita Tablero.py (ej. añade la clase Tablero) y realiza un commit local: "Tablero U2: Implementación de la cuadrícula de ataque."

5)User 1 (Sincroniza): Sube su cambio a GitHub (usando el menú de PyCharm: VCS -> Git -> Push).

6)User 2 (Descarga y Fusiona): User 2 detecta que hay una nueva "coordenada remota" y decide fusionarla. Primero descarga los datos: git fetch
en terminal lanzamos el git fetch.  

7)User 2 (Fusiona): User 2 fusiona el cambio de User 1, lo que crea un Merge Commit visible: git merge origin/main,
lanzamos git merge origin/main en la terminal.

8)User 2 (Sube): User 2 sube su historial fusionado a GitHub (usando VCS -> Git -> Push en PyCharm).

9)User 1 actualiza de la misma manera los cambios de User 2