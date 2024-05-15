# Các ngôn ngữ, công nghệ sử dụng
* Ngôn ngữ sử dụng: Python, HTML, CSS, SCSS, JavaScript, PHP
* Công cụ lập trình giao diện: Flask (Python)
* IDE sử dụng: IntelliJ IDEA Community Edition, Visual Code
* Cơ sở dữ liệu: MongoDB, MongoDB Compass
* ­Công cụ vẽ sơ đồ phân tích và thiết kế dữ liệu: Draw.io

# Yêu cầu cài đặt
Sử dụng Python 3.11
Sử dụng thư viện Python: flask, flask_wtf, pymongo, plotly, wtforms

# Hướng dẫn cài đặt chương trình
## Bước 1: Mở project bằng hai IDE trên
Sau khi đã mở lên, hãy thêm SDK cho project bằng Python 3.11
## Bước 2: Tải thư viện cần thiết
Mở cmd trong Windows để tiến hành cài đặt
* Flask: `pip install flask`
* pymongo: `pip install pymongo`
* plotly: `pip install plotly`
* pandas: `pip install pandas`
* flask_wtf: `pip install flask-wtf`
* wtforms: `pip install wtforms`
## Bước 3: Tạo cơ sở dữ liệu trong MongoDB
Chúng ta tiến hành tạo cơ sở dữ liệu trong MongoDB qua localhost:27017.
Khi đã tạo local host, hãy tạo một cơ sở dữ liệu mới với tên `new_restaurant_database`. Tạo hai collection là `account` và `restaurants`.
Sau cùng là là Import dữ liệu từ thư mục `database` trong project.

