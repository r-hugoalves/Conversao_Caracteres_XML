import xml.etree.ElementTree as ET

# Importar o arquivo XML (Ele não pode estar salvo com o ".xml")

tree = ET.parse('exemploNFe')
root = tree.getroot()

# Aqui, o arquivo é convertido para a string

xmlParaConversao = ET.tostring(root) #byte
xmlString = xmlParaConversao.decode('utf-8') # str

# Depois disso, é possível utilizar o replace() para fazer a conversão dos caracteres
#& == &amp;
#< == &lt;
#>== &gt;
#' == &apos;
#" == &quot;
#| == &#124;
#remover: \

xmlConvertido1 = xmlString.replace('&', '&amp;')
xmlConvertido2 = xmlConvertido1.replace('<', '&lt;')
xmlConvertido3 = xmlConvertido2.replace('>', '&gt;')
xmlConvertido4 = xmlConvertido3.replace("'", '&apos;')
xmlConvertido5 = xmlConvertido4.replace('"', '&quot;')
xmlConvertido6 = xmlConvertido5.replace('|', '&#124;')
xmlConvertido7 = xmlConvertido6.replace('\\', ' ')
xmlConvertido8 = xmlConvertido7.replace('ns0:', '')
xmlConvertido = xmlConvertido8.replace('ns0', '')

# Exportar o arquivo XML já convertido, com outro nome, ou seja, um novo arquivo

arquivo = open('Conversão do XML da NFe.txt', 'w')
arquivo.write(xmlConvertido)
arquivo.close()