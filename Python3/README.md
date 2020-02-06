# Gerador de CPF em Python3
  
<p align="center">
  <img src="https://i.imgur.com/4Ds4MDc.png" alt="CPF Gen redesenhado"/>

Um gerador de CPFs válidos, escrito em Python3, com auxílio da biblioteca PySimpleGUI.
Escrito por Pedro Lemos numa tarde do dia 12 de Outubro de 2019.

Escrevi uma versão desse projeto em C, que você pode ver [clicando aqui](https://github.com/pedrolemoz/cpfgen-c), e uma versão em Java, que você pode ver [clicando aqui](https://github.com/pedrolemoz/cpfgen-java).

### Como usar
Instale o Python3. Ele virá com todas as bibliotecas padrão, e o pip. Após isso, abra o prompt de comando no diretório do projeto, e digite:

```
pip3 install -r requeriments.txt
```
Isso irá instalar todas as coisas necessárias para que a aplicação funcione corretamente.

Um duplo clique é suficiente para executar o programa.

Para gerar CPFs válidos, especifique a quantidade, e clique em gerar.
O destino padrão do arquivo é o diretório atual.
Se desejar alterar, poderá clicar no botão procurar, ou especificar o diretório manualmente.

#### Usar sem interface gráfica:
Caso deseje usar o algoritmo em outro projeto, use o arquivo ```GeneratorAlgorithm.py``` e sua classe principal para o seu código.
```python3
from GeneratorAlgorithm import Generator
```
Você deverá instanciar a classe ```Generator```. A classe contém o método ```generate_CPF()```, que é público. Veja um exemplo:

```python3
CPF = Generator() # Instanciando a classe
CPF.generate_CPF() # Este é o CPF que foi gerado
```

Note que o algoritmo gera apenas um CPF. Para gerar mais, você deverá usar um laço de repetição for, como no exemplo abaixo:

```python3
# Gerando e exibindo 10 CPFs

CPF = Generator()
for i in range(10):
    print(CPF.generate_CPF())
```

### Contribua com este projeto!

Caso deseje melhorar ou adicionar novas funcionalidades, faça um fork do projeto e mande um pull request.
Apreciarei a sua colaboração.
