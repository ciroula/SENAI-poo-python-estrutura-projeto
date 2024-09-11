import os

from models.pessoa import Pessoa
from models.enums.sexo import Sexo
from models.endereco import Endereco
from models.enums.unidade_federativas import UnidadeFederativa
from models.enums.siglas import Siglas

os.system ("cls || clear")

pessoa_1 = Pessoa(80526, "Michel", "24/11/24", "71987072195", "mychellb2002@", Sexo.MASCULINO,
                Endereco("Tancredo", "4", "1°Andar", "41207", "Salvador", UnidadeFederativa.SAO_PAULO, Siglas.SAO_PAULO))

vini_jr = Pessoa(56, "Vinicius jr", "25/12/1830","71987250369", "vinijr@gmail.com", Sexo.MASCULINO,
                 Endereco("arere", "3", "jogatina joga facil", "33333", "Salvador", UnidadeFederativa.BAHIA, Siglas.BAHIA))

print(pessoa_1)
print(vini_jr)
