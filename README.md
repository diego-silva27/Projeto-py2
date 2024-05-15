A função calcular_preço_total calcula o custo total de um produto com base na quantidade desejada. Com apenas dois parâmetros, produto e quantidade, essa função realiza verificações importantes.

Primeiro, ela confere se o produto está na tabela de preços, uma espécie de catálogo onde os produtos e seus preços são listados. Se o produto estiver na tabela, o sistema multiplica o preço unitário pela quantidade desejada para obter o preço total. Mas se o produto não estiver na tabela, uma mensagem avisa que o produto não foi encontrado e o preço total é definido como zero.

Depois de todos esses passos, a função retorna o preço total, que é crucial para a conclusão da compra.

Além disso, o sistema mantém uma variável chamada total_value, que é atualizada com o custo total da compra. Ela começa com zero e é incrementada à medida que novos produtos são selecionados.

Para tornar a experiência do usuário mais intuitiva, o sistema utiliza um loop infinito que permite navegar pelo catálogo de produtos e escolher as quantidades desejadas. A cada ciclo do loop, o usuário é solicitado a fornecer o nome do produto desejado, facilitando a correspondência com os itens na tabela de preços.

E para finalizar a compra a qualquer momento, basta digitar "checkout", o que encerra o loop e confirma a conclusão da compra.

Durante todo o processo, o sistema mantém o usuário informado sobre o custo total da compra, exibindo-o formatado com duas casas decimais, garantindo assim uma experiência de compra transparente e acessível.
