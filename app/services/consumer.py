from datetime import date
import json
from kafka import KafkaConsumer
from ..utils.db.connect_db import PostgreDB
from ..crud.student import add_student
from ..schema.student import StudentModel

consumer = KafkaConsumer(
    "student",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda data: json.loads(data.decode("utf-8")),
    max_poll_records=100,  # Giới hạn số record mỗi lần poll (giúp tránh quá tải)
    fetch_max_bytes=1024 * 1024,  # Giới hạn kích thước dữ liệu mỗi lần fetch
    session_timeout_ms=30000,
)


async def consum_student():
    print("===> Consumer start listening...")
    await PostgreDB.create_con()
    pool = await PostgreDB.get_pool()
    try:
        for data in consumer:
            print(f"==> Data receiver: {data.value}")
            student = StudentModel(
                name_student=data.value.get("name_student"),
                class_id=data.value.get("class_id"),
                dob=data.value.get("dob"),
                faculty=data.value.get("faculty"),
            )
            await add_student(pool, student=student)
    except Exception as e:
        print(f"===> Student consumer error: {str(e)}")
