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
