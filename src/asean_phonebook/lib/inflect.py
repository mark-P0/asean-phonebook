from typing import Literal
import inflect


def with_indefinite_article(word: str):
    p = inflect.engine()

    return p.a(word)


def possessive_pronoun(gender: Literal["masculine"] | Literal["feminine"]):
    p = inflect.engine()

    p.gender(gender)

    pronoun = (
        p.singular_noun("theirs")
        if gender == "masculine"
        else p.singular_noun("them")
        if gender == "feminine"
        else False
    )
    if pronoun is False:
        raise ValueError("Unsupported gender...?")

    return pronoun


def oxford_join(words: list[str]):
    p = inflect.engine()

    return p.join(words)


if __name__ == "__main__":
    print(possessive_pronoun("masculine"))
    print(possessive_pronoun("feminine"))

    print(f"{oxford_join(list("abcde"))=}")
    print(f"{oxford_join(list("abc"))=}")
    print(f"{oxford_join(list("ab"))=}")
    print(f"{oxford_join(list("a"))=}")
    print(f"{oxford_join(list(""))=}")
