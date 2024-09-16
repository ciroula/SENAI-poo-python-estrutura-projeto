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
            f"\nLogradouro: {self.logradouro}"
            f"\nnumero: {self.numero}"
            f"\ncomplemento: {self.complemento}"
            f"\ncep: {self.cep}"
            f"\ncidade: {self.cidade}"
            f"\nUf: {self.unidadefederativa.texto}"
            f"\nUf: {self.unidadefederativa.sigla}"
        )