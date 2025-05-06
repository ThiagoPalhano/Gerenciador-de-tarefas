
dicionario = {'chave':'valor', 'ano':'idade', 'pais':'cidade'}

try:
    var = dicionario['pc']
    print(var)
except KeyError:
    print("chave não encontrada")

finally:
    print("!")