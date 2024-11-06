from typing import Self


class Database:
    _instance: Self = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance or not isinstance(cls._instance, cls):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name: str | None, port: int | None):
        self.name = name
        self.port = port
