# Example Project

This is an example project replicating the techstack used. 

## Usage

The project can be run with `docker-compose up`.
This will start the database, backend and frontend.
Initially the backend might fail, due to the database taking too much time initiating. Stopping and restarting docker compose should help.

The frontend can be accessed by opening `localhost:3000`.
The auto generated documentation of the backend can be accessed under `localhost:5001`.

## Development
The code is hot reloaded so you can start coding and see the changes.

For the frontend you could install NodeJs in your environment and install yarn. Then running `yarn` in the frontend folder, creates the node_modules folder. (Also a devcontainer can be used, but not tested)

For the backend a devcontainer config is provided, that can be launched with VSCode to have the Python environment of the backend.

## Task
There are 2 data models defined in the backend. One for users and one for parts.

### Create parts
Add an input to the frontend to add parts.

### Add a comment field to parts
Add a comment field to parts that can be updated.

### Make it look nice
Feel free to improve the beauty.
