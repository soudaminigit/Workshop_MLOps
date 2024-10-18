docker build -t taxi_service .
docker run -d -p 5000:5000 taxi_service
curl http://127.0.0.1:5000/show_result
python test_api.py