# Productly

Aplicación con CRUD para productos varios

## Requisitos

Asegúrate de tener instalado lo siguiente antes de comenzar:

- Python [versión]
- Pipenv [versión]

## Configuración del Entorno

1. Clona este repositorio en tu máquina local:

```bash
git clone https://github.com/WilSotoA/productly.git
cd productly
```

2. Crea un entorno virtual e instala las dependencias del proyecto utilizando Pipenv:

```bash
Copy code
pipenv install --dev
```

3. Activa el entorno virtual:

```bash
Copy code
pipenv shell
```

4. Configura las variables de entorno necesarias, como las claves secretas, la configuración de la base de datos, etc. Puedes usar un archivo .env para gestionar estas variables. Un ejemplo de archivo .env podría ser:

```bash
SECRET_KEY=TuClaveSecreta
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

5. Aplica las migraciones para crear la base de datos:

```bash
Copy code
python manage.py migrate
```

6. Ejecución del Proyecto
Inicia el servidor de desarrollo de Django:

```bash
Copy code
python manage.py runserver
```

>El proyecto estará disponible en <http://localhost:8000/>.

### Licencia

Este proyecto está bajo la licencia GNU General Public License. Consulta el archivo LICENSE para obtener más detalles.
