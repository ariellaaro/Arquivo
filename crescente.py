# input: 3 números inteiros
# output: em ordem crescente

primeiro = int(input())
segundo  = int(input())
terceiro = int(input())

if(terceiro > segundo):
    aux = terceiro
    terceiro = segundo
    segundo = aux

if(segundo > primeiro):
    aux = segundo
    segundo = primeiro
    primeiro = aux

if(terceiro > segundo):
    aux = terceiro
    terceiro = segundo
    segundo = aux

print(terceiro)
print(segundo)
print(primeiro)
