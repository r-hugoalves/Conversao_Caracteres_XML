# Conversao de Caracteres de um arquivo XML 

O programa tem como objetivo realizar a conversão de caracteres especiais em um arquivo XML. 
A intenção é facilitar a importação de arquivos de NF-e, CF-e, e NFC-e em sistemas ERP por API, onde é necessário a conversão do XML.

O programa faz a seguinte conversão:

& == &amp;

< == &lt;

> == &gt;

' == &apos;

" == &quot;

| == &#124;

E por fim, remove: \
 
A conversão se dá por meio de múltiplos arquivos que são salvos e convertidos, um a um, salvado em um arquivo final que é exportado em ".txt"

Por se tratar de um programa simples e curto, o fato de salvar diversos arquivos um após o outro não interfere no funcionamento e nem na performance do programa. Afinal, os arquivos de conversão são salvos apenas enquanto dura a execução do programa.

A conversão é feita utilizando o método replace(), nativo do python. Porém, ele só pode ser utilizando em strings, por isso que é feita a conversão utilizando "ET.tostring()" de um arquivo byte (que foi o XML importado).
Por conta disso, são feitas algumas conversões a mais no arquivo para tratar alguns caracteres específicos da conversão byte > string, sendo eles:
=> ns0
=> ns0:
