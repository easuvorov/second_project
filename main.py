# Импорт load_dotenv.
from dotenv import load_dotenv 

# Импорт библиотеки для работы с окружением.
import os  

# Загрузка переменных из .env
load_dotenv()

author = "default"

def print_author():
    # Теперь переменные доступны через os.environ
    author = os.getenv('AUTHOR')
    print(f"Автор проекта: {author}")

print_author()