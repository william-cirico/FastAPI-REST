from typing import Union
import re


def clear_cpf(cpf: str) -> str:
    """
    Limpa o CPF (remove todos os caracteres que não são numéricos).

    Args:
        cpf: CPF. Ex.: 103.287.321-12.
    Returns:
        CPF limpo.
    """
    cpf = re.sub(r'\D', '', cpf)

    return cpf


def generate_check_digits(cpf: str) -> str:
    """
    Gera os dígitos verificadores de um CPF.

    Args:
        cpf: CPF sem os dígitos verificadores. Ex.: 103287321.
    Returns:
        Uma string com os dois dígitos verificadores gerados a partir do CPF recebido.
    """
    accumulator = 0
    for digit, i in zip(cpf, range(10, 1, -1)):
        accumulator += int(digit) * i

    digit1 = 11 - (accumulator % 11)

    if digit1 > 9:
        digit1 = 0

    cpf = f'{cpf}{digit1}'

    accumulator = 0
    for digit, i in zip(cpf, range(11, 1, -1)):
        accumulator += int(digit) * i

    digit2 = 11 - (accumulator % 11)
    if digit2 > 9:
        digit2 = 0

    return f'{digit1}{digit2}'


def is_cpf_valid(cpf) -> Union[str, bool]:
    """
    Verifica de o CPF informado é válido.

    Args:
        cpf: CPF limpo (somente dígitos). Ex.: 10328732112.
    Returns:
        Retorna True se o CPF for válido, False em caso contrário.
    """
    if len(cpf) != 11:
        return False

    cpf_without_check_digits = cpf[:-2]
    validator_cpf = cpf_without_check_digits + generate_check_digits(cpf_without_check_digits)
    sequency = validator_cpf == validator_cpf[0] * len(validator_cpf)

    return cpf == validator_cpf and not sequency
