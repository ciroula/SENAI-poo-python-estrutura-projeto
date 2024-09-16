import os

from meu_projeto.models.pessoa import Pessoa 
from meu_projeto.models.enums.sexo import Sexo
from meu_projeto.models.endereco import Endereco

os.system("cls || clear")

#Instanciando classes.
pessoa_1 = Pessoa("Michel", 21, Sexo.MASCULINO,
                  Endereco("dwq",12)
                  )

print(pessoa_1)