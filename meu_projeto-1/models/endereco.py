from models.enums.unidade_federativas import UnidadeFederativa
from models.enums.siglas import Siglas


class Endereco:
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str, unidadefederativa: UnidadeFederativa, siglas: Siglas) -> None:
        
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade
        self.unidadefederativa = unidadefederativa
        self.siglas = siglas
    
    
    def __str__(self) -> str:
        return (
            f"\nLogradouro: {self.logradouro}"
            f"\nnumero: {self.numero}"
            f"\ncomplemento: {self.complemento}"
            f"\ncep: {self.cep}"
            f"\ncidade: {self.cidade}"
            f"\nUf: {self.unidadefederativa.value}"
            f"\nSiglas: {self.siglas.value}"
        )