import json
from abc import ABC, abstractmethod


class ConvertAdapter(ABC):
    def __init__(self, obj: any):
        self._obj = obj

    @abstractmethod
    def convert(self) -> any:
        ...


class JSONConverter(ConvertAdapter):
    def convert(self) -> json:
        return json.dumps(str(self._obj))

    def convert_content_with_prefix(self, prefix: str) -> json:
        return json.dumps(self._obj.get_content_with_prefix(prefix))

    def convert_content_with_suffix(self, suffix: str) -> json:
        return json.dumps(self._obj.get_content_with_suffix(suffix))


class ListConverter(ConvertAdapter):
    def convert(self) -> list:
        return self._obj.content.split()

    def convert_content_with_prefix(self, prefix: str) -> list:
        return self._obj.get_content_with_prefix(prefix).split()

    def convert_content_with_suffix(self, suffix: str) -> list:
        return self._obj.get_content_with_suffix(suffix).split()


class DictConverter(ConvertAdapter):
    def convert(self) -> dict:
        return {"content": self._obj.content}

    def convert_content_with_prefix(self, prefix: str) -> dict:
        return {prefix: self._obj.get_content_with_prefix(prefix)}

    def convert_content_with_suffix(self, suffix: str) -> dict:
        return {suffix: self._obj.get_content_with_suffix(suffix)}
