from datetime import datetime
from criteria import Criteria, Criterion
from leaf import Attribute, Value, LeafOperators



query_str = Criteria.initialize(
    operand=Criterion.initialize(
        attribute=Attribute(value="A"),
        value=Value(value=1),
        operator=LeafOperators.EQUALS
    )
).and_(
    operand=Criterion.initialize(
        attribute=Attribute(value="B"),
        value=Value(value=2),
        operator=LeafOperators.NOT_EQUALS
    )
).and_(
    operand=Criterion.initialize(
        attribute=Attribute(value="C"),
        value=Value(value=2),
        operator=LeafOperators.LT
    )
).or_(
    operand=Criteria.initialize(
        operand=Criterion.initialize(
            attribute=Attribute(value="A"),
            value=Value(value=1),
            operator=LeafOperators.EQUALS
        ),
        is_not=True
    ).and_(
        operand=Criterion.initialize(
            attribute=Attribute(value="B"),
            value=Value(value=datetime.now()),
            operator=LeafOperators.NOT_EQUALS
        )
    ).and_(
        operand=Criterion.initialize(
            attribute=Attribute(value="C"),
            value=Value(value="2"),
            operator=LeafOperators.LT
        )
    )
).output()

print(query_str)