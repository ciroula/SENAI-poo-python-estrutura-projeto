import os

from models.pessoa import Pessoa 
from models.enums.sexo import Sexo
from models.endereco import Endereco

os.system("cls || clear")

#Instanciando classes.
pessoa_1 = Pessoa("Michel", 21, Sexo.MASCULINO,
                  Endereco("dwq",12)
                  )

print(pessoa_1)