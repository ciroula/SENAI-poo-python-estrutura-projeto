import pytest
from meu_projeto_2.models_2.pessoa_2 import Pessoa

@pytest.fixture

def pessoa_valida():
    pessoa = Pessoa("Michel", 21)

    return pessoa

def test_pessoa_alterar_nome_valida(pessoa_valida):
    pessoa_valida.nome = "Felipe"
    assert pessoa_valida.nome == "Felipe"

def test_pessoa_nome_valida(pessoa_valida):
    assert pessoa_valida.nome == "Michel"

def test_pessoa_idade_valida(pessoa_valida):
    assert pessoa_valida.idade == 21

def test_pessoa_idade_negativa_retorna_messagem_excecao(pessoa_valida):
    with pytest.raises(ValueError, match="Idade nao pode ser negativa."):
        #assert pessoa_valida.nome == "Michel"
        Pessoa("Michel", -1)