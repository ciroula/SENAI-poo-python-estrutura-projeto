import pytest
from meu_projeto_1.models.pessoa import Pessoa
from meu_projeto_1.models.enums.sexo import Sexo
from meu_projeto_1.models.endereco import Endereco
from meu_projeto_1.models.enums.unidade_federativas import UnidadeFederativa

@pytest.fixture
def Criar_pessoa():
    pessoa_1 = Pessoa(80526, "Michel", "24/11/24", "71987072195", "mychellb2002@", Sexo.MASCULINO,
                Endereco("Tancredo", "4", "1°Andar", "41207", "Salvador", UnidadeFederativa.SAO_PAULO))
    return pessoa_1

def test_pessoa_atributo_nome(Criar_pessoa):
    assert Criar_pessoa.nome == "Michel"