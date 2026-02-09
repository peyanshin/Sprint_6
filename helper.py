
import logging
from faker import Faker
import names

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

faker = Faker()

def generate_registration_data():
    """Генерирует email и пароль для регистрации."""
    email = faker.email()
    password = faker.password(
        length=12,
        special_chars=True,
        digits=True,
        upper_case=True,
        lower_case=True
    )
    logger.info(f"Сгенерированы данные регистрации: email={email}")
    return email, password  #Кортеж (email, password)

def generate_random_name():
    """Генерирует случайное имя."""
    try:
        name = names.get_first_name()
        logger.info(f"Сгенерировано случайное имя: {name}")
        return name
    except Exception as e:
        logger.error(f"Ошибка генерации имени: {e}")
        return "DefaultName"

def generate_random_surname():
    """Генерирует случайную фамилию."""
    try:
        surname = names.get_last_name()  #Исправлено: get_last_name()
        logger.info(f"Сгенерирована случайная фамилия: {surname}")
        return surname
    except Exception as e:
        logger.error(f"Ошибка генерации фамилии: {e}")
        return "DefaultSurname"  #Изменено на "DefaultSurname"