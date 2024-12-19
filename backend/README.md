# Backend

## Development Environment

The VSCode extension "Dev Containers" can be used to set up a development environment for the backend.
Open command palette with Ctrl + Shift + p and run the command "Dev Container: Open Folder in Container" and select the backend folder. A new VsCode window should open. In that one code completion for the Python project should work.

## Add packages

Add new Python packages to the "requirements.txt"

## File Description

### main.py

- This file contains the routes of the REST API
- Mock data can be added in `startup_event()`
- To make development easier the whole database is deleted and created from scratch in that function

### crud.py

- Short for create, read, update and delete
- Contains all functions to read and manipulate data
- A class `CRUDBase` is provided to implement basic functionality
- For each model a class needs to be created that inherits from `CRUDBase`
- The model class and the schema classes are given as parameters
- If the model needs a special read, write functionality, it can be overwritten in a method

### models.py

- Creates a class for each table of the database
- The columns of the tables are given as properties

### schemas.py

- Creates class for each models to define how JSON data on the REST API will look like
- Different schemas for creating, reading and updating

### database.py

- General database setup

### settings.py

- Holds settings, that are needed across the application

### errors.py

- Holds custom error definitions

## Alembic

Alembic is used to keep track of the database.
For development not so relevant, but for production.

Alembic can be used from within the backend Docker container. To access the container use:

```
docker container exec -it template-backend-1 /bin/bash
```

### Initial Setup

Use the following steps to create the alembic folder and alembi.ini file

Alembic is used to keep track of the versions of the database.

To initialize the database, start the backend container change to the `app` directory and run:

```
alembic init alembic
```

This will create an `alembic.ini` file and an `alembic` folder.

Remove the sqlalchemy.url path from `alembic.ini`:

```
sqlalchemy.url =
```

It will be set from the Docker environment.

Add your models metadata to `alembic/env.py`:

```python
from app import database, models

# Set db path from env variable
config.set_main_option("sqlalchemy.url", database.SQLALCHEMY_DATABASE_URL)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = models.Base.metadata
```

To create the first revision run:

```
alembic revision --autogenerate -m "First migration"
```

This will create a `versions` folder and a python file in it with the steps for the migration.

The files get created as root. To change it back to your user use:

```
sudo chown -R user:user alembic
sudo chown -R user:user alembic.ini
```

### Upgrade DB

To apply the migration to the database run:

```
alembic upgrade head
```

Make sure the database container is also running.

You can check if the database was created, by connecting with pgadmin.
