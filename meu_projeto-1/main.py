import os

from models.pessoa import Pessoa
from models.enums.sexo import Sexo
from models.endereco import Endereco
from models.enums.unidade_federativas import UnidadeFederativa

os.system ("cls || clear")

pessoa_1 Pessoa(15, "Michel", "24/11/24", "71987072195", "mychellb2002@", Sexo.MASCULINO,
                Endereco("Tancredo", "4", "1°Andar", "41207", "Salvador", UnidadeFederativa.RIO_DE_JANEIRO))

print(essoa_1)