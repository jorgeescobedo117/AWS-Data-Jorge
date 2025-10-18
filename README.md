<<<<<<< HEAD
# Proyecto Final — ETL Serverless AWS + Dashboard

Este proyecto contiene un pipeline ETL con AWS Lambda y un dashboard Streamlit desplegado con Docker y GitHub Actions.
=======
                                                    Configuracion del Entorno 

 Acceso a la Instancia EC2 (SSH)

El primer paso es establecer una conexión segura a la instancia remota utilizando **SSH (Secure Shell)**.

```bash
ssh -i "ruta/a/llave.pem" usuario@IP_de_EC2
```

**Descripción:**
- `-i "ruta/a/llave.pem"` → Especifica la llave privada requerida para la autenticación.  
- `usuario@IP_de_EC2` → Combina el usuario (ej. `ubuntu`) y la IP pública.  

---

 Transferencia Segura de Archivos (SCP)

Utiliza SCP (Secure Copy Protocol) para transferir archivos locales a tu instancia EC2.

```bash
scp -i "ruta/a/llave.pem" archivo_local usuario@IP_de_EC2:/ruta/remota/
```



---

Actualización del Sistema Base

Antes de instalar cualquier software, actualiza los paquetes del sistema.

```bash
sudo apt update
sudo apt upgrade -y
```

Referencias:
- [Documentación oficial de Ubuntu sobre apt](https://wiki.debian.org/apt)  
- [Guía de actualización en Ubuntu](https://help.ubuntu.com/community/AptGet/Howto)

---

Instalación de Python 3.12

Instala Python 3.12 y herramientas esenciales.

```bash
sudo apt install python3.12 python3.12-venv python3.12-dev -y
```

Referencia:** [Documentación oficial de Python 3.12](https://docs.python.org/3.12/)

---

Gestión del Entorno Virtual (venv)

Aísla tus dependencias creando entornos virtuales.

```bash
python3.12 -m venv mi_entorno
source mi_entorno/bin/activate
deactivate
```

Referencia:** [Crear entornos virtuales (venv)](https://docs.python.org/3/library/venv.html)

---

Instalación y Configuración de Docker

Instala Docker y Docker Compose para gestionar contenedores.

```bash
sudo apt install docker.io docker-compose -y
sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -aG docker $USER
```

Reinicia tu sesión SSH para aplicar los permisos del grupo docker

Referencias:
- [Guía oficial de Docker en Ubuntu](https://docs.docker.com/engine/install/ubuntu/)  
- [Guía oficial de Docker Compose](https://docs.docker.com/compose/install/)

---

 Instalación y Uso de Jupyter Notebook

Instala Jupyter Notebook (ideal para análisis y prototipos en Python).

```bash
pip install jupyter
jupyter notebook
```

- El servidor se ejecutará por defecto en el puerto 8888  
- Puede requerir configurar un **túnel SSH** o reglas de seguridad en AWS para el acceso.

Referencias:
- [Instalación oficial de Jupyter](https://jupyter.org/install)  
- [Guía interactiva de uso](https://docs.jupyter.org/en/latest/start/index.html)

---

 Descompresión de Archivos

Si subiste tus archivos comprimidos (.zip o .tar.gz), usa los siguientes comandos:

```bash
sudo apt install unzip -y
unzip archivo.zip
ls -lh
```

Otros formatos útiles:

| Formato | Comando de Descompresión |
|----------|--------------------------|
| `.tar.gz` | `tar -xzvf archivo.tar.gz` |
| `.gz` | `gunzip archivo.gz` |
| `.zip` | `zip -r backup.zip mi_carpeta/` |

Referencias:
- [unzip - Ubuntu Manpages](https://manpages.ubuntu.com/manpages/focal/man1/unzip.1.html)  
- [tar - Linuxize](https://linuxize.com/post/how-to-extract-unzip-tar-gz-file/)  
- [gunzip - Ubuntu Manpages](https://manpages.ubuntu.com/manpages/focal/man1/gunzip.1.html)

---

Verificación del Archivo

Para verificar que un archivo se descomprimió correctamente:

```bash
head -n 5 netflix_titles.csv
```

Muestra las primeras 5 líneas del archivo, confirmando su estructura.

| Herramienta / Comando | Descripción | Documentación Oficial |
|------------------------|--------------|------------------------|
| `unzip` | Descomprime archivos ZIP. | [Ubuntu Manpages](https://manpages.ubuntu.com/manpages/focal/man1/unzip.1.html) |
| `ls` | Lista los archivos y directorios. | [Linuxize](https://linuxize.com/post/ls-command-in-linux/) |
| `tar` | Gestiona archivos `.tar` o `.tar.gz`. | [Linuxize](https://linuxize.com/post/how-to-extract-unzip-tar-gz-file/) |
| `gunzip` | Descomprime archivos `.gz`. | [Ubuntu Manpages](https://manpages.ubuntu.com/manpages/focal/man1/gunzip.1.html) |
| `zip` | Crea archivos ZIP. | [Ubuntu Manpages](https://manpages.ubuntu.com/manpages/focal/man1/zip.1.html) |
| `head` | Muestra las primeras líneas de un archivo. | [Linuxize](https://linuxize.com/post/head-command-in-linux/) |

---

 Resumen del Entorno

Una vez completados los pasos, tu entorno está completamente configurado para trabajar con Python y contenedores Docker dentro de Jupyter Notebook:

1. Conexión a EC2 mediante SSH  
2. Transferencia de archivos con SCP  
3. Sistema base actualizado  
4. Python 3.12 instalado  
5. Entorno virtual funcional  
6. Docker y Docker Compose configurados  
7. Jupyter Notebook listo para uso  

---
>>>>>>> 506eb6f8276f6d15694c089f50db5a4df4e6a817
