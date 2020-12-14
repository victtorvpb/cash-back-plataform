def to_camel_case(string: str) -> str:
    output = ''.join(x for x in string.title() if x.isalnum())
    return f'{output[0].lower()}{output[1:]}'


def format_cpf(cpf: str) -> str:
    return cpf.replace('-', '').replace('.', '')
