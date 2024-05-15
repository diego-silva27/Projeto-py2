Definição da função calcular_preço_total:

A função aceita dois parâmetros: produto (nome do produto) e quantidade (quantidade necessária).
Nesta função, verifique se o produto está na tabela de preços (tabela). Nesse caso, calcule o preço total multiplicando o preço do produto pela quantidade necessária. Caso contrário, será exibida a mensagem “Produto não encontrado na tabela”. é exibido e o preço total é definido como 0.
Esta função retorna o preço total.
Definição da tabela de preços:

Crie um dicionário chamado tabela que contenha nomes de produtos como chaves e preços como valores.
Inicialização da variável Total_value:

A variável total_value é inicializada com o valor 0. Esta variável será utilizada para acompanhar o custo total da compra.
Loop quando verdadeiro:

Use while True para iniciar um loop infinito. Isso significa que o código dentro do loop será executado repetidamente até que uma instrução break seja encontrada.
Entrada do usuário para o produto:

O programa exige que o usuário insira o nome do produto desejado usando a função input(). Use .capitalize() para converter nomes de produtos em letras maiúsculas.
Verifique para concluir a compra:

Se o usuário entrar em “checkout”, o programa exibe a mensagem “Purchase Complete!” e usa break para sair do loop.
Requisitos de quantidade do produto:

Caso o usuário não conclua a compra, o programa utilizará input() para solicitar a quantidade do produto desejado e converter o input para um número inteiro.
Cálculo do preço total do produto:

O programa chama a função calcula_preco_total com os parâmetros de produto e quantidade informados pelo usuário. Calcule o preço total do produto com base nesta função.
Atualizar valor total da compra:

Use o operador += para adicionar o preço total do produto a total_value.

Exibição do preço total do produto:
   - O programa exibe o preço total do produto no formato de duas casas decimais.

Exibição do total de compras:
   - Após o término do loop (quando o usuário finaliza a compra), o programa exibe o valor total da compra formatado com duas casas decimais.
