"""Этот модуль настраивает logger."""

import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime

from pythonjsonlogger import jsonlogger

from app.config import settings


class CustomJsonFormatter(jsonlogger.JsonFormatter):
    """Класс для создания собственного форматтера логов."""

    def add_fields(self, log_record, record, message_dict):
        """
        Метод редактирует поля в записи лога.

        :param log_record: Словарь с данными лога
        :param record: Объект с данными лога
        :param message_dict: Словарь сообщения
        :return: None
        """
        super().add_fields(log_record, record, message_dict)
        if not log_record.get('timestamp'):
            now = datetime.utcnow().strftime('%Y-%m-%d  %H:%M:%S')
            log_record['timestamp'] = now

        if log_record.get('level'):
            log_record['level'] = log_record['level'].upper()
        else:
            log_record['level'] = record.levelname


# Создание форматтера
_formatter = CustomJsonFormatter('%(timestamp)s %(level)s %(name)s %(message)s')

# ------------------------------------------------------------------
# Логгер для обработки запросов к api
endpoint_logger = logging.getLogger('endpoint_info')

log_handler = logging.StreamHandler()

log_handler.setFormatter(_formatter)
endpoint_logger.addHandler(log_handler)
endpoint_logger.setLevel(settings.LOG_LEVEL)

# ------------------------------------------------------------------
# Логгер для обработки ошибок
error_logger = logging.getLogger('error_info')

# Хэндлер для вывода логов в консоль
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(_formatter)


# Хэндлер для вывода логов в файл
file_handler = RotatingFileHandler(
    filename='./app/logs/error_logs.log',
    maxBytes=512 * 1024 * 1024,     # Максимальный размер файла в байтах (512 МБ)
    backupCount=0
)
file_handler.setFormatter(_formatter)

# Добавление хэндлеров к error_logger
error_logger.addHandler(stream_handler)
error_logger.addHandler(file_handler)
error_logger.setLevel(settings.LOG_LEVEL)
