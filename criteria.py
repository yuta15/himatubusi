from enum import StrEnum
from typing import Self

from leaf import Attribute, LeafOperators, Value


class CriteriaOperator(StrEnum):
    AND = "AND"
    OR = "OR"


class Criterion:
    def __init__(self):
        self._left:Attribute|None = None
        self._right:Value|None = None
        self._operator: LeafOperators | None = None

    @classmethod
    def initialize(cls, *, attribute:Attribute, value:Value, operator:LeafOperators) -> Self:
        """
        引数チェック
        """
        if all((isinstance(attribute, Attribute), isinstance(value, Value), isinstance(operator, LeafOperators))):
            criterion = cls()
            criterion._left = attribute
            criterion._right = value
            criterion._operator = operator
            return criterion

        raise ValueError("criteriaもしくはattribute, value, operatorのセットを入力してください")

    def output(self) -> str:
        return f"{self._left.value} {self._operator.value} {self._right.output()}"


class Criteria:
    def __init__(self):
        self._previous: Criteria | Criterion | None = None
        self._prev_operator: CriteriaOperator | None = None
        self._current: Criteria | Criterion | None = None
        self._is_not: bool = False

    @classmethod
    def initialize(cls, *, operand:Criteria|Criterion, is_not:bool=False) -> Self:
        generated = cls()
        generated._current = operand
        generated._is_not = is_not
        return generated

    def and_(self, *, operand:Criteria|Criterion) -> Criteria:
        return self._generate_new_instance(operand=operand, operator=CriteriaOperator.AND)

    def or_(self, *, operand:Criteria|Criterion) -> Criteria:
        return self._generate_new_instance(operand=operand, operator=CriteriaOperator.OR)

    def output(self) -> str:
        current = self._current.output()

        if self._previous is None:
            expression = current
        else:
            previous = self._previous.output()
            expression = f"({previous} {self._prev_operator.value} {current})"

        return f"NOT ({expression})" if self._is_not else expression


    def _generate_new_instance(self, operand:Criterion | Criteria, operator:CriteriaOperator) -> Criteria:
        generated = Criteria()
        generated._previous = self
        generated._prev_operator = operator
        generated._current = operand
        return generated
