from typing import Iterable


def transpose_2d[T](iterable: Iterable[Iterable[T]]):
    """
    Transpose (swap) rows and columns of a 2D iterable, e.g.

    ```
    [*transpose_2d([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])] == [
        (1, 4, 7),
        (2, 5, 8),
        (3, 6, 9)
    ]
    ```
    """

    return zip(*iterable)


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    print(f"{[*transpose_2d(matrix)]=}")
