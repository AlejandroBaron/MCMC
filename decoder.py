import numpy as np
import pandas as pd


mensaje="there are three kinds of lies lies damn lies and statistics mark twain i could not claim that i was smarter than sixty five other guys but the average of sixty five other guys certainly feynman a single death is a tragedy a million deaths is a statistic joseph stalin coincidences in general are great stumbling blocks in the way of that class of thinkers who have been educated to know nothing of the theory of probabilities that theory to which the most glorious objects of human research are indebted for the most glorious of illustrations edgar allen poe morgue morpheus this is your last chance after this there is no turning back you take the blue pill the story ends you wake up in your bed and believe whatever you want to believe you take the red pill you stay in wonderland and i show you how deep the rabbit hole goes "


ocurrencias = pd.read_csv("AustenCount.txt",sep='\t',header=None).values

"Tomamos logaritmos para reducir el tamaño de los números (al calcular productorios serán demasiado grandes)"
logocurrencias=np.log(ocurrencias+1)

print(pd.DataFrame(ocurrencias))

abc="abcdefghijklmnopqrstuvwxyz"

#charIndex={"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"ñ":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26," ":27}
charIndex={"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25," ":26}
to_Char=list(charIndex.keys())


def score(m):

	p=0

	'''Para cada par de letras en el mensaje m, ver qué score obtenemos según las ocurrencias
	   Sin embargo, como los números son muy grandes, vamos a tomar logaritmos (en vez de
	   productorio de ocurrencias, tomaremos la suma de los logaritmos)'''
	for i in range(len(m)-1):
		ic1=charIndex[m[i]]
		ic2=charIndex[m[i+1]]
		p+=logocurrencias[ic1,ic2]

	return p



def desencriptar(mensaje,func):

	desencriptared=list(mensaje)
	func=list(func)

	"Para cada caracter del mensaje, lo desencripta a tenor de la funcion que se le indique"
	for i in range(len(desencriptared)):
		value=charIndex[desencriptared[i]]

		if value<26:
			newchar=func[value]
			desencriptared[i]=to_Char[newchar]

	return "".join(desencriptared)

def permutar2(f):

	fperm=[i for i in f]


	swap=np.random.choice(26,size=2,replace=False)


	fperm[swap[0]]=f[swap[1]]
	fperm[swap[1]]=f[swap[0]]

	return fperm


#####################################################
'''
BANCO DE PRUEBAS: los siguientes valores indican un ejemplo válido de encriptado y desencriptado correspondiente

encriptadora=[i-1 for i in [23,5,6,18,22,26,9,3,25,1,4,17,7,2,19,8,12,14,16,15,11,10,21,13,24,20]]
desencriptadora=[i-1 for i in [10,14,8,11,2,3,13,16,7,22,21,24,26,18,20,19,12,4,15,17,23,5,1,25,9,6,27]]

encriptado=desencriptar(mensaje,encriptadora)
print(encriptado)
print(desencriptar(encriptadito,desencriptadora))
exit()
'''
###################################################


funcAleatoria=list(np.random.choice(26,size=26,replace=False))


"Encripto el mensaje con una func Aleatoria"
encriptado=desencriptar(mensaje,funcAleatoria)

funcActual=list(range(27))
funcPropuesta=None
scoreActual = score(desencriptar(encriptado,funcActual))

iteraciones=300000
for i in range(iteraciones):



	"Nueva funcion propuesta tras permutar"
	funcPropuesta=permutar2(funcActual)
	scorePropuesta=score(desencriptar(encriptado,funcPropuesta))


	"Si Uniforme< a(i,j)=scoreProopuesta/scoreActual (recordemos que los scores están en logaritmos, por eso hacemos la exponencial) "
	"aceptaremos la funcion (actualizando el scoreActual)"
	if np.random.uniform() <= np.exp(scorePropuesta-scoreActual):
		funcActual=funcPropuesta
		scoreActual=scorePropuesta


	if(i%100==0):
		print(i,desencriptar(encriptado,funcActual))


print("FIN")
