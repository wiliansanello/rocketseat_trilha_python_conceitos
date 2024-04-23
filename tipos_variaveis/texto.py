# Declaração
nome_completo = "Wilian Ansanello"
print("Nome completo na primeira forma:", nome_completo)
print("Nome completo na segunda forma:" + nome_completo)
print("Nome completo na terceira forma:" + "Wilian" + "Ansanello")
print("Nome completo na quarta forma:" , "Wilian" , "Ansanello")

nome_completo_aspas = """Já chegou
o disco voador"""
print("Quinta forma: ", nome_completo_aspas)

nome_completo_quebra = " Wilian \
    Ansanello"
print("Sexta forma:", nome_completo_quebra)

nome = "Wilian"
sobrenome = "Ansanello"

print("Sétima forma: %s" % nome_completo)
print("Oitava forma: %s %s" % (nome, sobrenome))
print(f"Nona forma: {nome} {sobrenome}")
print("Décima forma: {} {}".format(nome, sobrenome))
print("Décima primeira forma: {} {}".format(sobrenome, nome))

