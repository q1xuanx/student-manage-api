import os
from dotenv import load_dotenv

load_dotenv()

class Settings: 
    PROJECT_NAME : str = 'Student Management'
    VERSION : str= '1.0.1'

    POSTGRES_USER : str = os.getenv('username_db')
    POSTGRES_PASSWORD : str = os.getenv('password_db')
    POSTGRES_PORT : str = os.getenv('port_db')
    POSTGRES_DB : str = os.getenv('name_db')
    POSTGRES_SERVER : str = os.getenv('server_db')
    API_TOKEN : str = os.getenv('token_api')
    RAW_USERNAME : str = os.getenv('raw_username')
    RAW_PASSWORD : str = os.getenv('raw_password')
    DATABASE_URL : str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

setting = Settings()