import pytest
from meu_projeto.models.pessoa import Pessoa #Caminho relativo
from meu_projeto.models.endereco import Endereco #Caminho absoluto
from meu_projeto.models.enums.sexo import Sexo

#Modelo.
@pytest.fixture
def Criar_pessoa():
    Pessoa_1 = Pessoa("Michel", 21, Sexo.MASCULINO,
                  Endereco("dwq",12)
                    )
    return Pessoa_1

def test_pessoa_atributo_nome(Criar_pessoa):
    assert Criar_pessoa.nome == "Michel"

def test_pessoa_atributo_idade(Criar_pessoa):
    assert Criar_pessoa.idade == 21

def