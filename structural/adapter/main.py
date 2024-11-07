from structural.adapter.adapter import ConvertAdapter, JSONConverter, ListConverter, \
    DictConverter


class TextObject:
    def __init__(self, content: str):
        self.content = content

    def __str__(self) -> str:
        return self.content

    def get_content_with_prefix(self, prefix: str) -> str:
        """
        Get content with prefix
        :param prefix: str
        :return: str
        """
        return f"{prefix} {self.content}"

    def get_content_with_suffix(self, suffix: str) -> str:
        """
        Get content with suffix
        :param suffix: str
        :return: str
        """
        return f"{self.content} {suffix}"


def main() -> None:
    obj_text: TextObject = TextObject("Hello, world!")
    print(obj_text)

    obj_json_convert: JSONConverter = JSONConverter(obj_text)
    print(obj_json_convert.convert())
    print(obj_json_convert.convert_content_with_prefix(prefix="prefix"))
    print(obj_json_convert.convert_content_with_suffix(suffix="suffix"))

    obj_list_convert: ListConverter = ListConverter(obj_text)
    print(obj_list_convert.convert())
    print(obj_list_convert.convert_content_with_prefix(prefix="prefix"))
    print(obj_list_convert.convert_content_with_suffix(suffix="suffix"))

    obj_dict_convert: DictConverter = DictConverter(obj_text)
    print(obj_dict_convert.convert())
    print(obj_dict_convert.convert_content_with_prefix(prefix="prefix"))
    print(obj_dict_convert.convert_content_with_suffix(suffix="suffix"))


if __name__ == "__main__":
    main()
