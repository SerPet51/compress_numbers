from typing import List, Sequence, TypeVar
 
T = TypeVar("T")
 
 
def compress_numbers(numbers: Sequence[T]) -> List[T]:
    result: List[T] = []
    for value in numbers:
        if not result or value != result[-1]:
            result.append(value)
    return result