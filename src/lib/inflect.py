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


if __name__ == "__main__":
    p = inflect.engine()

    print(possessive_pronoun("masculine"))
    print(possessive_pronoun("feminine"))
