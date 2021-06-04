# https://mypy.readthedocs.io/en/stable/kinds_of_types.html


# * Uinon Types : 타입을 선택적으로 가능하도록 한다.
from typing import Union

x: Union[int, str] = 3  # ok
# x: Union[int, str] = None # fail!


def foo3(x: Union[int, str]) -> None:
    print(x)


foo3(x)

# * Optional types : Optional[X] == Union[X, None]
from typing import Optional

y: Optional[int] = None