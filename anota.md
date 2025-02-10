# Estruturas de dados

- `Homogêno` -> Aceita apenas dados de um único tipo
- `Heterogêneo` -> Aceita dados de tipos diferentes
- As estruturas de dados são declaradas com o case **`snake_case`**
- `print()` -> Termina com () é um método. 

## Listas 
- `list` -> Ordenada, mutável e heterogênea.

**1. Declaração da estrutura de dados list**
```py
sabores = ["mussarela", "calabresa", "Frango com catupiry", "portuguesa"]
dados_pizza = ["mussarela", 26.90, sabores]
print("Sabores disponíveis: " , sabores) 
print("Informações da Pizza: " , dados_pizza)
```
**2. Operações com Listas**

a. `append()` -> Adiciona um novo valor ao final da lista.
```py
sabores.append("margherita")
print("Sabores disponíveis: " , sabores) 
```

b. `remove()` -> Remove um elemento da lista.
```py
sabores.remove("calabresa")
print("Sabores disponíveis: " , sabores) 
```

c. Acessando itens:
```py
print(sabores[0])
print(sabores[1])
print(sabores[2])
print(sabores[3])
print(sabores[-1])
```
## tuplas()
**1. Declaração de tuplas ()**
```py
tamanhos = ("pequena", "média", "grande")
print("Tamanhos disponíveis: " , tamanhos)
```

**2. Operações com tuplas**
```py
print("Tamanho: ", tamanhos[-1] )
```

- Verificar itens:
```py
print("Existe tamanho grande ?", "grande" in tamanhos)
```
<br><br>

# Métodos
- `lower()` -> Transforma a string em minúscula
- `print()` -> Usado para saida de dados
- `input()` -> Usado para entrada de dados
- `range(inclusivo,exclusivo)` -> Cria uma quantidade de números
  - Inclusivo -> O número aparece na iteração
  - exclusivo -> O número não aparece
- `enumerate()` -> Para obter um índice numérico
- `float()` -> Conversão explicita de um valor para número decimal

<br><br>

## Funções
- `def` -> Palavra chave que define uma função.
- `nome_da_funcao` -> Nome da função em si. Padrão snake_case.
- `()` -> Pode conter ou não parâmetros.
- `:` -> Indica o bloco da função.
- `return` -> Opcional, usado para retornar um valor da função.
- `parâmetro` -> É uma variável temporária
- `argumento` -> É o valor que você irá passar no parâmetro.
- `invocação` -> É o ato de chamar ou usar a função.

<br><br>

## Palavras reservadas
`break` -> Encerra o loop


