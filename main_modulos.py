from modulos import variavel1	#caso 1: impoortando apenas a variavel1
import modulos					#caso 2: importando toda a biblioteca porem com o prefixo "modulos."
from modulos import *			#caso 3: importando toda a bilioteca e suas variaveis
	
print(variavel1)		#caso 1:  
print(modulos.variavel2)#caso 2: 
print(variavel3)		#caso 3: 