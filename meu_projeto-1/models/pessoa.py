from models.enums.sexo import Sexo
from models.endereco import Endereco
from models.enums.unidade_federativas import UnidadeFederativa
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
            f"ID: {self.id}"
            f"nome: {self.nome}"
            f"data_nascimento: {self.data_nascimento}"
            f"telefone: {self.telefone}"
            f"emai: {self.emai}"
            f"sexo: {self.sexo.value}"
            f"endereco: {self.endereco}"
        )