import pytest
from meu_projeto_1.models_1.pessoa_1 import Pessoa
from meu_projeto_1.models_1.enums_1.sexo_1 import Sexo
from meu_projeto_1.models_1.endereco_1 import Endereco
from meu_projeto_1.models_1.enums_1.unidade_federativas_1 import UnidadeFederativa

@pytest.fixture
def Criar_pessoa():
    pessoa_1 = Pessoa(80526, "Michel", "24/11/24", "71987072195", "mychellb2002@", Sexo.MASCULINO,
                Endereco("Tancredo", "4", "1°Andar", "41207", "Salvador", UnidadeFederativa.SAO_PAULO))
    return pessoa_1

def test_pessoa_atributo_nome(Criar_pessoa):
    assert Criar_pessoa.nome == "Michel"