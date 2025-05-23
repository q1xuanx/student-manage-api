# 📘 Student & Class Management API

## 🚀 Công nghệ sử dụng

- **FastAPI**: Framework hiện đại, hiệu suất cao cho việc xây dựng các RESTful API.
- **asyncpg**: Thư viện kết nối PostgreSQL bất đồng bộ, tối ưu cho hiệu năng cao.
- **contextlib (lifespan)**: Dùng để quản lý vòng đời ứng dụng, giúp mở/đóng kết nối cơ sở dữ liệu đúng cách.
- **authx**: Dùng để quản lý JWT Token (tạo, xác thực token từ các request).

---

## 📚 Các nhóm API

### 👨‍🎓 Student API

| Method | Endpoint                                  | Mô tả                         |
|--------|-------------------------------------------|-------------------------------|
| GET    | `/student/health-check`                   | Kiểm tra tình trạng hoạt động |
| POST   | `/student/add-student`                    | Thêm mới một sinh viên        |
| PATCH  | `/student/update-student`                 | Cập nhật thông tin sinh viên  |
| DELETE | `/student/delete-student/{id_student}`    | Xoá sinh viên theo ID         |
| GET    | `/student/search`                         | Tìm kiếm sinh viên            |

---

### 🏫 Class API

| Method | Endpoint              | Mô tả                          |
|--------|-----------------------|--------------------------------|
| GET    | `/class/health-check` | Kiểm tra tình trạng hoạt động |
| POST   | `/class/add`          | Thêm mới lớp học               |
| PATCH  | `/class/update`       | Cập nhật thông tin lớp học     |
| GET    | `/class/classes`      | Lấy danh sách lớp học          |

---

## ⚙️ Quản lý kết nối cơ sở dữ liệu với Lifespan

Sử dụng `lifespan` của FastAPI để mở và đóng kết nối cơ sở dữ liệu PostgreSQL một cách an toàn và hiệu quả:

```python
from contextlib import asynccontextmanager
import asyncpg
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app : FastAPI):
    app.state.db_pool = await connect_db.create_con()
    print('Connect DB Success')
    yield
    await connect_db.close_con(app.state.db_pool)
    print('Close DB') 

app = FastAPI(lifespan=lifespan)
```

### 👨‍💻 Made by [@q1xuanx](https://github.com/q1xuanx)