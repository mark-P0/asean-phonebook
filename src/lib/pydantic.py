from enum import IntEnum
import typing as T
from pydantic import ValidationError, create_model
from src.lib.python.enum import EnumValues


def typed_input[TType](
    *,
    model_name="TypedInput",
    _type: type[TType],
    message: str | None = None,
    invalid_input_message: str | None = None,
) -> TType:
    model = create_model(model_name, value=_type)

    if message is None:
        message = f"Enter value (of type {_type.__name__!r}): "

    if invalid_input_message is None:
        invalid_input_message = (
            f"Invalid input — please enter a value of type {_type.__name__!r}"
        )

    while True:
        try:
            value = input(message)
            inst = T.cast(
                T.Any,  # Dynamic model creation does not provide "correct" type hints
                model.model_validate(dict(value=value)),
            )

            return T.cast(TType, inst.value)
        except ValidationError:
            print(invalid_input_message)
            print()


def enum_input[TEnum: EnumValues](
    *,
    enum: type[TEnum],
    message: str | None = None,
    invalid_input_message: str | None = None,
):
    model_name = enum.__name__ + "Input"

    if message is None:
        message = f"Enter one of {enum.values()}: "

    if invalid_input_message is None:
        invalid_input_message = f"Invalid input — please enter one of: {enum.values()}"

    return typed_input(
        model_name=model_name,
        _type=enum,
        message=message,
        invalid_input_message=invalid_input_message,
    )


if __name__ == "__main__":

    class Example(EnumValues, IntEnum):
        SOMETHING = 1
        ANOTHER = 2

    example = enum_input(message="Enter example: ", enum=Example)
    print(f"{example=} {type(example)=}")

    typed = typed_input(_type=int)
    print(f"{typed=} {type(typed)=}")
