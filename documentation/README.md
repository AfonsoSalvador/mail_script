# Instruções

## Para que serve o script?
 - O intuito deste script é automatizar o envio de emails individuais em grande demanda.
 *Por exemplo:*

 Você deseja enviar 50 emails para remetentes distintos e não deseja que o nome de todos eles apareça no corpo do email e, além disso, você deseja enviar o mesmo esqueleto do email para todos, porém com palavras específicas pra cada um (ou seja, variáveis).

## Como funciona?
 - Dentro do diretório *test* possui 2 arquivos de exemplo. O arquivo *text.txt* simula o texto a ser enviado. Para inserir as variáveis é necessário utilizar os símbolos *<>* e o número correspondente, que será explicado abaixo. 

 **Não confunda os símbolos das variáveis com as tags HTML**

 - No arquivo *params.txt* possui um exemplo de como devem ser organizados as variáveis e os emails dos remetentes. Os emails vêm sempre no início de cada linha. Logo em seguida, vêm as variáveis separadas por vírgulas. 

 **Repare que as variáveis estão na ordem dos números que estão no arquivo *text.txt*** 

### Observações
 - Para criar um email bonito e personalizado, utilize recursos do HTML no arquivo *text.txt*
