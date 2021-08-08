# Test

# correr el dockerfile
docker build -t pruebas:v1 .

# Crar contenedor
docker run -it -p 8080:8080 -v /workspace/docker-hub-webapp/docker:/docker --name webapp -h webapp webapp:v1

