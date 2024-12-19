# Frontend

## Add packages

Change to the frontend folder and use `yarn add package_name` to add new packages.

To update the packages in the Docker container you need to do the following.

Remove the Docker container with:
`docker container rm template-frontend-1`

Remove the node_modules volume with:
`docker volume rm template_frontend_node_modules`

## Project Structure

### /pages

Every file in this folder will will create a page, which can be reached by a link created with the name.
The `index.tsx` file is the default page.

### /components

This folder contains files that define components.

### /data

Files in this folder define data types and connections to the backend API.
