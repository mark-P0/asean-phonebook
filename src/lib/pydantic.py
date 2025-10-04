import typing as T
from pydantic import ValidationError, create_model
from src.lib.python.enum import EnumValues


def enum_input[TEnum: EnumValues](*, message: str | None = None, enum: type[TEnum]):
    model_name = enum.__name__ + "Input"
    model = create_model(model_name, value=enum)

    if message is None:
        message = f"Enter one of {enum.values()}: "

    while True:
        try:
            value = input(message)
            inst = T.cast(
                T.Any,  # Dynamic model creation does not provide "correct" type hints
                model.model_validate(dict(value=value)),
            )

            return T.cast(
                TEnum,
                inst.value,
            )
        except ValidationError:
            print(f"Invalid input — please enter one of: {enum.values()}")
            print()
