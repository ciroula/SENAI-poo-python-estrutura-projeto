from meu_projeto_1.models.enums.sexo import Sexo
from meu_projeto_1.models.endereco import Endereco
#from models.enums.unidade_federativas import UnidadeFederativa

class Pessoa ():
    def __init__(self, id: int, nome: str, data_nascimento: str, telefone: str, email: str, sexo: Sexo, endereco: Endereco) -> None:
        self.id = id
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.telefone = telefone
        self.email = email
        self.sexo = sexo
        self.endereco = endereco

    def __str__(self) -> str:
        return(
            f"\nID: {self.id}"
            f"\nnome: {self.nome}"
            f"\ndata_nascimento: {self.data_nascimento}"
            f"\ntelefone: {self.telefone}"
            f"\nemai: {self.email}"
            f"\nsexo: {self.sexo.texto}"
            f"\nsexo: {self.sexo.caracter}"
            f"\nendereco: {self.endereco}"
        )