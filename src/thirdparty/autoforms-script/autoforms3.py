import json

# Opening JSON file
jf = open('dados.json',encoding='utf-8')
# returns JSON object as a dictionary
data = json.load(jf)
# Closing file
jf.close()

# Mapping json to html data
mapeador1 = {}
mapeador1["chave_01"] = data["Nome"]
mapeador1["chave_02"] = data["SIAPE"]
mapeador1["chave_03"] = data["Cargo"]
mapeador1["chave_04"] = data["Telefone"]
mapeador1["chave_05"] = data["email"]
mapeador1["chave_06"] = data["InstituicaoDestino"]
mapeador1["chave_21"] = data["Evento"]
mapeador1["chave_07"] = data["CidadeDestino"]
mapeador1["chave_08"] = data["EstadoDestino"]
mapeador1["chave_09"] = data["DataInicioEvento"]
mapeador1["chave_10"] = data["DataTerminoEvento"]
mapeador1["chave_11"] = data["DataInicioAfastamento"]
mapeador1["chave_12"] = data["DataTerminoAfastamento"]
form1Tab1 = data["Form1Tab1"]
print("NaturezaAfastamento:" , form1Tab1["NaturezaAfastamento"])
form1Tab2 = data["Form1Tab2"]
print("TipoAfastamento:", form1Tab2["TipoAfastamento"])
mapeador1["chave_13"] = ""
mapeador1["chave_14"] = ""
mapeador1["chave_15"] = ""
mapeador1["chave_16"] = ""
mapeador1["chave_17"] = ""
mapeador1["chave_18"] = "[digite aqui o nome do programa de pós-graduação ou unidade da UFF que concederá bolsa de estudos ou pagamento do curso/mensalidades ou passagens e/ou diárias]"
mapeador1["chave_19"] = "[digite aqui o nome da agência de fomento ou instituição brasileira federal que concederá bolsa de estudos ou pagamento do curso/mensalidades ou passagens e/ou diárias]"
mapeador1["chave_20"] = "[digite aqui o nome da agência de fomento ou instituição brasileira não federal que concederá bolsa de estudos ou pagamento do curso/mensalidades ou passagens e/ou diárias]"
if form1Tab1["NaturezaAfastamento"] == "CASO_1":
     mapeador1["chave_13"] = "X"
     mapeador1["chave_18"] = form1Tab1["NomeFinanciador"]
elif form1Tab1["NaturezaAfastamento"] == "CASO_2":
     mapeador1["chave_14"] = "X"
     mapeador1["chave_19"] = form1Tab1["NomeFinanciador"]
elif form1Tab1["NaturezaAfastamento"] == "CASO_3":
     mapeador1["chave_15"] = "X"
elif form1Tab1["NaturezaAfastamento"] == "CASO_4":
     mapeador1["chave_16"] = "X"
     mapeador1["chave_20"] = form1Tab1["NomeFinanciador"]
elif form1Tab1["NaturezaAfastamento"] == "CASO_5":
     mapeador1["chave_17"] = "X"

mapeador1["chave_tipo_1"] = ""
mapeador1["chave_tipo_2"] = ""
mapeador1["chave_tipo_3"] = ""
mapeador1["chave_tipo_4"] = ""
mapeador1["chave_tipo_5"] = ""
mapeador1["chave_tipo_6"] = ""
mapeador1["chave_tipo_7"] = ""
mapeador1["chave_tipo_8"] = ""
mapeador1["chave_tipo_9"] = ""
mapeador1["chave_22"] = "" # outro
if form1Tab2["TipoAfastamento"] == "TIPO_1":
     mapeador1["chave_tipo_1"] = "X"
elif form1Tab2["TipoAfastamento"] == "TIPO_2":
     mapeador1["chave_tipo_2"] = "X"
elif form1Tab2["TipoAfastamento"] == "TIPO_3":
     mapeador1["chave_tipo_3"] = "X"
elif form1Tab2["TipoAfastamento"] == "TIPO_4":
     mapeador1["chave_tipo_4"] = "X"
elif form1Tab2["TipoAfastamento"] == "TIPO_5":
     mapeador1["chave_tipo_5"] = "X"
elif form1Tab2["TipoAfastamento"] == "TIPO_6":
     mapeador1["chave_tipo_6"] = "X"
elif form1Tab2["TipoAfastamento"] == "TIPO_7":
     mapeador1["chave_tipo_7"] = "X"
elif form1Tab2["TipoAfastamento"] == "TIPO_8":
     mapeador1["chave_tipo_8"] = "X"
     mapeador1["chave_22"] = form1Tab2["Outro"]
elif form1Tab2["TipoAfastamento"] == "TIPO_9": # Banca Examinadora
     mapeador1["chave_tipo_8"] = "X"
     mapeador1["chave_tipo_9"] = "X"
     mapeador1["chave_22"] = "Banca Examinadora"

mapeador2 = {}
mapeador2["chave_01"] = data["Nome"]
mapeador2["chave_02"] = data["SIAPE"]
mapeador4 = {}
mapeador4["chave_01"] = data["Nome"]
mapeador4["chave_02"] = data["SIAPE"]
mapeador4["chave_03"] = data["Cargo"]
mapeador4["chave_04"] = data["RG"]
mapeador4["chave_05"] = data["CPF"]
mapeador4["chave_06"] = data["Evento"]
mapeador4["chave_07"] = data["CidadeDestino"]
mapeador4["chave_08"] = data["DataInicioAfastamento"]  #data["DataInicioEvento"]
mapeador4["chave_09"] = data["DataTerminoAfastamento"] #data["DataTerminoEvento"]
mapeador4["chave_10"] = data["MotivoRenuncia"]
mapeador4["chave_11"] = data["DataDaSolicitacaoSEI"]
mapeador4["chave_12"] = data["Nome"]
mapeador3 = {}
mapeador3["chave_01"] = data["DataDaSolicitacaoSEI"]
mapeador3["chave_02"] = data["Nome"]
mapeador3["chave_03"] = data["DataDeNascimento"]
mapeador3["chave_04"] = data["CPF"]
mapeador3["chave_05"] = data["RG"]
mapeador3["chave_06"] = data["OrgaoEmisorRG"]
mapeador3["chave_07"] = data["SIAPE"]
mapeador3["chave_08"] = data["Cargo"]
mapeador3["chave_09"] = data["Escolaridade"]
mapeador3["chave_10"] = data["Telefone"]
mapeador3["chave_11"] = data["Telefone"]
mapeador3["chave_12"] = data["email"]
mapeador3["chave_13"] = data["NomeENumeroDoBanco"]
mapeador3["chave_14"] = data["Agencia"]
mapeador3["chave_15"] = data["ContaCorrente"]
mapeador3["chave_16"] = data["DV"]
mapeador3["chave_17"] = data["LocalOrigem"]
mapeador3["chave_18"] = data["DataInicioAfastamento"]
mapeador3["chave_19"] = data["CidadeDestino"]
mapeador3["chave_20"] = data["MeioDeTransporteIda"]
mapeador3["chave_21"] = data["CidadeDestino"]
mapeador3["chave_22"] = data["DataVoltaEvento"]
mapeador3["chave_23"] = data["LocalOrigem"]
mapeador3["chave_24"] = data["MeioDeTransporteVolta"]
mapeador3["chave_25"] = data["DataInicioEvento"]
mapeador3["chave_26"] = data["HoraInicioEvento"]
mapeador3["chave_27"] = data["DataTerminoEvento"]
mapeador3["chave_28"] = data["HoraTerminoEvento"]
mapeador3["chave_29"] = data["DescricaoMotivoViagem"]
mapeador3["chave_30"] = data["NumeroProcessoSEI"]
mapeador3["chave_31"] = data["JustificativaDiariasPassagens"]
mapeador3["chave_32"] = data["DataDaSolicitacaoSEI"]
mapeador3["chave_33"] = data["Nome"]
mapeador3["chave_tipo_6"] = mapeador1["chave_tipo_6"]
mapeador3["chave_tipo_7"] = mapeador1["chave_tipo_7"]
mapeador3["chave_tipo_8"] = mapeador1["chave_tipo_8"]
mapeador3["chave_tipo_9"] = mapeador1["chave_tipo_9"]
mapeador3["chave_34"] = mapeador1["chave_22"]     # Outro
if form1Tab2["TipoAfastamento"] == "TIPO_9":
     # Se banca examinadora, tirar do 'outro' no form3
     mapeador3["chave_tipo_8"] = ""
     mapeador3["chave_34"] = ""

omapeador = [mapeador1,mapeador2,mapeador3,mapeador4]
oformhtml = ['oform-1.htm','oform-2.htm','oform-3.htm','oform-4.htm']
nformhtml = ['nform-1.htm','nform-2.htm','nform-3.htm','nform-4.htm']

import platform

# ============== CHECK IF ENCODING IS CORRECT FOR LINUX ==============

if platform.system() == 'Linux':
     print("LINUX! lembre-se de instalar pacote magic: pip install python-magic")
     # pip install python-magic
     import magic
     blob = open(oformhtml[0], 'rb').read()
     m = magic.open(magic.MAGIC_MIME_ENCODING)
     m.load()
     encoding = m.buffer(blob)  # "utf-8" "us-ascii" etc
     print("Codificação dos arquivos de entrada:", encoding)
     if encoding != 'iso-8859-1':
          print("ERRO: o script no linux exige arquivo oform-1.htm na codificacao iso-8859-1")
     assert(encoding == 'iso-8859-1')

# ============== BEGIN PROCESSING FILES ==============

for i in range(4):
     # Loading data in the html forms
     contents = None
     with open(oformhtml[i], encoding='latin-1') as f:
          contents = f.read()
          # Replacing data
          for key, value in omapeador[i].items():
               contents = contents.replace(key,value)
          # Creating and writing data in a new html file
          nf = open(nformhtml[i], "w", encoding='latin-1')
          nf.write(contents)
          nf.close()

print("Finalizado!")
