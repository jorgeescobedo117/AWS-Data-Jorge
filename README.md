Configuración del Entorno ________________________________________
Acceso a la Instancia EC2 (SSH)
El primer paso es establecer una conexión segura a la instancia remota utilizando SSH (Secure Shell).
Comando	Descripción
ssh -i "ruta/a/llave.pem" usuario@IP_de_EC2	Conéctate a la instancia utilizando la llave privada (-i) y las credenciales (usuario@IP_de_EC2).
Detalles:
o	-i "ruta/a/llave.pem": Especifica la llave privada (.pem) requerida para la autenticación.
o	usuario@IP_de_EC2: Combina el usuario de la instancia (ej. ubuntu) y su IP pública.
o	
•	 Referencia: Uso de SSH en Linux/Ubuntu
________________________________________
Transferencia Segura de Archivos (SCP)
Utiliza SCP (Secure Copy Protocol) para transferir de manera segura archivos locales necesarios a la instancia EC2.
Comando	Descripción
scp -i "ruta/a/llave.pem" archivo_local usuario@IP_de_EC2:/ruta/remota/	Copia archivo_local al directorio remoto especificado.
•	Referencia: Copia de archivos con SCP
________________________________________




 Actualización del Sistema Base
Es una práctica recomendada actualizar los índices de paquetes y el sistema operativo antes de instalar nuevo software.
Comando	Descripción
sudo apt update	Sincroniza la lista de paquetes disponibles desde los repositorios.
sudo apt upgrade	Actualiza todos los paquetes instalados a sus versiones más recientes.
•	Referencias: Documentación oficial de Ubuntu sobre apt | Guía de actualización en Ubuntu
________________________________________
 Instalación de Python 3.12
Instala la versión de Python 3.12 junto con herramientas esenciales para la gestión de entornos y la compilación.
Comando	Descripción
sudo apt install python3.12 python3.12-venv python3.12-dev	Instala el intérprete, la herramienta de entorno virtual (venv) y los archivos de desarrollo (dev).
•	Referencias: Documentación oficial de Python 3.12
________________________________________
Gestión del Entorno Virtual (venv)
Utiliza un entorno virtual para aislar las dependencias de cada proyecto, evitando conflictos globales.
Comando	Descripción
python3.12 -m venv mi_entorno	Crea un nuevo entorno virtual llamado mi_entorno.
source mi_entorno/bin/activate	Activa el entorno virtual para comenzar a usarlo.
deactivate	Desactiva el entorno y regresa al sistema base.
•	Referencia: Crear entornos virtuales (venv)
________________________________________
Instalación y Configuración de Docker
Instala Docker y Docker Compose para la gestión eficiente de aplicaciones en contenedores.
Comando	Descripción
sudo apt install docker.io docker-compose	Instala los paquetes de Docker Engine y Docker Compose.
sudo systemctl enable docker	Configura Docker para que inicie automáticamente al arrancar la instancia.
sudo systemctl start docker	Inicia el servicio de Docker inmediatamente.
sudo usermod -aG docker $USER	Agrega tu usuario al grupo docker para ejecutar comandos sin sudo. (Requiere reiniciar la sesión SSH).
•	Uso: Permite empaquetar y ejecutar aplicaciones de manera consistente en cualquier lugar.
•	 Referencias: Guía oficial de Docker en Ubuntu | Guía oficial de Docker Compose
________________________________________
 Instalación y Uso de Jupyter Notebook
Instala Jupyter Notebook para una experiencia de codificación interactiva y basada en notebooks.
Comando	Descripción
pip install jupyter	Instala Jupyter Notebook (dentro del entorno virtual si está activo).
jupyter notebook	Inicia el servidor de Jupyter para acceder a la interfaz web.
•	Acceso: El comando abrirá una interfaz web a través del puerto 8888 (a menudo requiere configuración de túnel SSH o grupo de seguridad para acceso remoto).
•	Función: Ideal para análisis de datos, prototipado rápido y documentación.
•	Referencias: Documentación oficial de instalación y uso | Guía de uso interactivo de Jupyter Notebook
________________________________________

Resumen del Entorno
Una vez completados todos los pasos, tu entorno de desarrollo está completamente configurado:
1.	Conexión a EC2 mediante SSH
2.	Transferencia de archivos con SCP
3.	Sistema Base Actualizado
4.	Python 3.12 instalado
5.	Capacidad de crear Entornos Virtuales.
6.	Docker y Docker Compose funcionales para contenedores
7.	Jupyter Notebook disponible para trabajo con Python 
________________________________________
Puntos Adicionales para poder extraer un Zip 
 Descomprimir archivos
Si has subido tus archivos de proyecto o datasets comprimidos (comúnmente en formato .zip), necesitarás descomprimirlos con los siguientes comando se podrán decomprimirse 
Comando	Descripción
sudo apt install unzip -y	Instala la utilidad unzip en el sistema (si aún no está disponible).
unzip archive.zip	Descomprime el archivo llamado archive.zip en la ubicación actual.
ls -lh	Lista los archivos en un formato legible para verificar los archivos extraídos.
Comandos de compresión útiles:
Formato	Comando de Descompresión
.tar.gz	tar -xzvf archivo.tar.gz
.gz	gunzip archivo.gz
Crear .zip	zip -r backup.zip mi_carpeta/








 Verificar el archivo 
Para confirmar que el archivo principal se ha extraído correctamente y tiene el formato esperado, puedes usar el comando head para mostrar las primeras líneas.
Comando	Descripción
head -n 5 netflix_titles.csv	Muestra las primeras 5 líneas del archivo netflix_titles.csv para verificar el encabezado y el contenido inicial.

Herramienta / Comando	Descripción	Documentación Oficial 
unzip	Utilidad para descomprimir archivos ZIP.	Página Man (Manual) de (Ubuntu Manpages)

ls	Comando de listado de directorios.	Guía del comando (Linuxize)

tar	Utilidad para gestionar archivos .tar y compresión (.tar.gz).	Cómo usar el comando (Linuxize)

gunzip	Utilidad para descomprimir archivos .gz.	Página Man (Manual) de  (Ubuntu Manpages)

zip	Utilidad para crear archivos ZIP.	Página Man (Manual) de (Ubuntu Manpages)

head	Muestra el inicio de un archivo.	Guía del comando (Linuxize)

