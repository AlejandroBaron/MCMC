#!/usr/bin/env python
# -*- coding: utf-8 -*-


import PyPDF2
import pandas as pd
import numpy as np

def removeAccents(string):
    s=list(string)
    dic={"á":"a","é":"e","í":"i","ó":"o","ú":"u"}
    keys=list(dic.keys())
    for i in range(len(page)):
        if s[i] in keys :
            s[i] = dic.get(s[i])
        return "".join(s)

books=["GoT.pdf","El_Hereje.pdf","CienAnosDeSoledad.pdf","DivinaComedia.pdf","SantosInocentes.pdf"]


matrix=np.zeros((28,28))
np.vectorize(int)(matrix)
for book in books:

    text=open("Source_Books/"+book,"rb")
    pdfReader = PyPDF2.PdfFileReader(text,strict=False)


    index={"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"ñ":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26," ":27}
    alphabet=[u"a",u"b",u"c",u"d",u"e",u"f",u"g",u"h",u"i",u"j",u"k",u"l",u"m",u"n",u"ñ",u"o",u"p",u"q",u"r",u"s",u"t",u"u",u"v",u"w",u"x",u"y",u"z",u" "]
    npages=pdfReader.numPages
    print(book)

    for i in range(npages):
        page=pdfReader.getPage(i).extractText()
        page=removeAccents(page)
        print("Pages left",npages-i)
        for x in alphabet:
            for y in alphabet:
                matrix[index[x],index[y]]+=page.count(x+y)



with open('matrix.txt','wb') as f:
    for line in matrix:
        np.savetxt(f, line, fmt='%.2f')

dataframe = pd.DataFrame(matrix,columns=alphabet,index=alphabet).astype(int)
print(dataframe)
dataframe.to_csv('outfile.csv', sep=' ', header=True, index=True)
