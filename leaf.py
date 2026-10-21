import json
from datetime import datetime, date
from typing import Self
from enum import StrEnum
from dataclasses import dataclass


class LeafOperators(StrEnum):
    EQUALS = "="
    NOT_EQUALS = "!="
    GT = ">"
    GTE = ">="
    LT = "<"
    LTE = "<="


@dataclass
class Attribute:
    value: str

    def __post_init__(self) -> None:
        if not isinstance(self.value, str):
            raise ValueError("不正な値が設定されています。")


@dataclass
class Value:
    value: int | str | datetime | date

    def __post_init__(self):
        value_type = type(self.value)
        allowed_type = [int, str, datetime, date]
        if value_type not in allowed_type:
            raise ValueError("不正なデータが入力されています。")
        if value_type == str:
            self.value = self.value.strip()

    def output(self) -> str:
        if isinstance(self.value, str):
            return json.dumps(self.value, ensure_ascii=False)
        if isinstance(self.value, datetime):
            return f'DATETIME("{self.value.isoformat()}")'
        if isinstance(self.value, date):
            return f'DATE("{self.value.isoformat()}")'
        return str(self.value)
