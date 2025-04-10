
## Code base structure
    `client.py `: file này dùng để khởi tạo các client và phân bổ data cho client (ở trong bài này đang cho rằng dữ liệu của client đồng đều nhau)
    `federated_learning_operator.py`: chạy federated learning
    `load_data.py`: chia dữ liệu để train và có function để lưu kết quả sau khi train
    `model_train.py`: định nghĩa model ở client và server
    `parameters.py`: định nghĩa các thông số của mô hình như số client...
    `server.py`: tính FedAvg dùng để tính trung bình các tham số cũng như train mô hình

    - folder results để lưu kết quả sau khi train, khi train xong có thể vào đây để xem
    - folder datasets để lưu data train

## Work
- extract file datasets
- Tạo môi trường ảo venv và kích hoạt venv

```
python -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```
- chạy file
```
python federated_learning_operator.py
```

## link tham khảo code



