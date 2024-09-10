from models.enums.unidade_federativas import UnidadeFederativa


class Endereco:
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str, unidadefederativa: UnidadeFederativa) -> None:
        
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade
        self.unidadefederativa = unidadefederativa
    
    def __str__(self) -> str:
        return (
            f"Logradouro: {self.logradouro}"
            f"numero: {self.numero}"
            f"complemento: {self.complemento}"
            f"cep: {self.cep}"
            f"cidade: {self.cidade}"
            f"Uf: {self.unidadefederativa.value}"
        )