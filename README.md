# CALCULADORA TK
🎈CALCULADORA BÁSICA COM INTERFACE GRÁFICA.

<img src="FOTO.png" align="center" width="400"> <br>

## DESCRIÇÃO:
A calculadora desenvolvida é uma aplicação gráfica simples, criada em **Python** utilizando a biblioteca **Tkinter**. Ela possui uma interface moderna com **tema escuro**, funcionalidades básicas de cálculo e um layout responsivo com interface amigável.

1. **Interface Gráfica:**
   * A interface utiliza a biblioteca padrão Tkinter para criação de GUIs.
   * Apresenta um **tema escuro** com cores contrastantes para facilitar a visualização.

2. **Layout da Calculadora:**
   * Um campo de entrada no topo exibe a expressão e o resultado.
   * Os botões numéricos (0–9), operadores (`+`, `-`, `*`, `/`), ponto (`.`) e igual (`=`) estão organizados em uma grade.
   * O botão **"APAGAR"** está posicionado na última linha e ocupa toda a largura da janela, facilitando o acesso rápido para limpar a expressão.

3. **Entrada e Exibição:**
   * O campo de entrada aceita expressões matemáticas diretamente dos botões.
   * Os resultados e expressões são exibidos no estilo padrão do Python (ex: multiplicação com `*`, divisão com `/`).

4. **Ações dos Botões:**
   * Botões numéricos e operadores inserem seus valores no campo de entrada.
   * O botão `=` avalia a expressão digitada e exibe o resultado.
   * O botão **"APAGAR"** limpa completamente a entrada, permitindo ao usuário começar uma nova operação.

5. **Lógica de Execução:**
   * A função `on_button_click` gerencia os eventos de clique.
   * Quando o botão `=` é pressionado, a expressão é avaliada com `eval()` e o resultado substitui a entrada.
   * Caso contrário, o caractere do botão é simplesmente adicionado à expressão existente.

6. **Manuseio de Erros:**
   * Caso ocorra um erro (ex: divisão por zero ou expressão inválida), o campo de entrada exibirá a palavra **"Erro"**.

7. **Design Responsivo e Restrição de Tamanho:**
   * A interface é configurada para distribuir os elementos proporcionalmente.
   * A janela da calculadora tem **tamanho fixo**, ou seja, **não pode ser redimensionada** pelo usuário.

## EXECUTANDO O PROJETO:
1. Acesse o diretório onde o código está salvo: `cd ./CODIGO`. Execute o script Python:

```bash
python CODIGO.py
```

2. A interface da calculadora será aberta automaticamente.

3. Utilize os botões da interface para montar expressões matemáticas.

4. Clique em `=` para calcular o resultado, que será exibido no campo superior.

5. Clique em **"APAGAR"** para limpar a entrada.

6. Para encerrar o programa, simplesmente feche a janela da aplicação.

## SOBRE O EXECUTAVEL:
### 1. EXECUTANDO:
   * O executável gerado está disponível apenas para sistemas **Windows x64** e pode ser encontrado no diretório `./APP`.
   * Para executá-lo, basta dar dois cliques. Ele é especialmente útil em máquinas onde o **Python não está instalado**.
   * Trata-se da **mesma aplicação contida no arquivo `./CODIGO/CODIGO.py`**, porém empacotada de forma independente.
   * Se necessário, você pode recompilar o executável a qualquer momento.

### 2. GERANDO:
> **IMPORTANTE:** Antes de gerar o novo `executável`, certifique-se de excluir o arquivo `./APP/CALCULADORA TK.exe`.

   **1. Instalação do [PyInstaller:](https://pyinstaller.org/en/stable/)**
   - Certifique-se de ter o PyInstaller instalado. Se não tiver, instale usando o comando abaixo:
   ```bash
   pip install pyinstaller
   ```

   **2. Gerando o Executável:**
   - No diretório `./CODIGO`, execute o comando abaixo para gerar o executável a partir do arquivo `.spec`:

   ```bash
   pyinstaller EXECUTAVEL.spec
   ```

   - O arquivo `CALCULADORA TK.exe` será criado dentro da pasta `./CODIGO/dist`.

   - Após a geração, você pode mover o executável para `./APP` e remover as pastas temporárias `./CODIGO/build` e `./CODIGO/dist`.

   - Para executar o aplicativo, basta dar dois cliques no arquivo `.exe`.

## NÃO SABE?
- Entendemos que para manipular arquivos em muitas linguagens e tecnologias, é necessário possuir conhecimento nessas áreas. Para auxiliar nesse aprendizado, oferecemos cursos gratuitos disponíveis:
* [CURSO DE PYTHON](https://github.com/VILHALVA/CURSO-DE-PYTHON)
* [CURSO DE TKINTER](https://github.com/VILHALVA/CURSO-DE-TKINTER)
* [CONFIRA MAIS CURSOS](https://github.com/VILHALVA?tab=repositories&q=+topic:CURSO)

## CREDITOS:
- [PROJETO CRIADO PELO VILHALVA](https://github.com/VILHALVA)


