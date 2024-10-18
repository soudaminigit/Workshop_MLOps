docker build -t taxi_web .
docker run -p 8080:80 taxi_web
http://localhost:8080