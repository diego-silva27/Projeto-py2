1. Definição da função calcular_preco_total:
   - Esta função recebe dois argumentos: produto (o nome do produto) e quantidade (a quantidade desejada).
   - Dentro da função, é verificado se o produto está na tabela de preços (tabela). Se estiver, o preço total é calculado multiplicando o preço do produto pela quantidade desejada. Caso contrário, uma mensagem de "Produto não encontrado na tabela." é exibida e o preço total é definido como 0.
   - O preço total é retornado pela função.

2. Definição da tabela de preços:
   - É criado um dicionário chamado tabela que contém os nomes dos produtos como chaves e seus preços como valores.

3. Inicialização da variável valor_total:
   - A variável valor_total é inicializada com o valor 0. Esta variável será usada para acompanhar o custo total da compra.

4. Loop while True:
   - Um loop infinito é iniciado usando while True. Isso significa que o código dentro do loop será executado repetidamente até que a instrução break seja encontrada.

5. Entrada do usuário para o produto:
   - O programa solicita ao usuário que insira o nome do produto desejado usando a função input(). O nome do produto é convertido para maiúsculas usando .capitalize().

6. Verificação para finalizar a compra:
   - Se o usuário inserir "Finalizar compra", o programa exibe uma mensagem "Compra finalizada!" e sai do loop usando break.

7. Solicitação da quantidade do produto:
   - Se o usuário não finalizar a compra, o programa solicita a quantidade do produto desejado usando input() e converte a entrada para um número inteiro.

8. Cálculo do preço total do produto:
   - O programa chama a função calcular_preco_total com os argumentos produto e quantidade inseridos pelo usuário. O preço total do produto é calculado com base na função.

9. Atualização do valor total da compra:
   - O preço total do produto é adicionado ao valor_total usando o operador +=.

10. Exibição do preço total do produto:
   - O programa exibe o preço total do produto formatado com duas casas decimais.

11. Exibição do valor total da compra:
   - Após o loop terminar (quando o usuário finalizar a compra), o programa exibe o valor total da compra formatado com duas casas decimais.
