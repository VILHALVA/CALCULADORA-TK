# CALCULADORA
🎈CALCULADORA BÁSICA COM INTERFACE GRÁFICA.

<img src="FOTO.png" align="center" width="400"> <br>

## DESCRIÇÃO:
A calculadora desenvolvida é uma aplicação gráfica simples implementada em Python usando a biblioteca Tkinter. Aqui está uma descrição de como ela funciona e quais são suas funcionalidades:

1. **Interface Gráfica:**
   - A interface é construída usando a biblioteca Tkinter, que é uma ferramenta padrão para criar GUIs (Interfaces Gráficas do Usuário) em Python.

2. **Layout da Calculadora:**
   - A calculadora tem uma entrada de texto na parte superior que exibe as entradas e resultados.
   - Os botões numéricos (0-9) estão dispostos em uma grade, juntamente com botões para operações aritméticas (+, -, *, /), ponto decimal, igual (=), e a tecla 'C' para apagar a entrada.

3. **Entrada e Exibição:**
   - O campo de entrada aceita a digitação de expressões matemáticas.
   - As entradas e os resultados são exibidos no formato da entrada padrão da linguagem Python. Por exemplo, a multiplicação é representada por '*', a divisão por '/', e assim por diante.

4. **Ações dos Botões:**
   - Os botões numéricos e operadores aritméticos inserem os respectivos caracteres na entrada.
   - O botão '=' realiza a avaliação da expressão na entrada e exibe o resultado.
   - O botão 'C' limpa a entrada, permitindo ao usuário recomeçar.

5. **Lógica de Execução:**
   - A lógica de execução está centralizada na função `on_button_click`, que é chamada quando um botão é pressionado.
   - Se o botão pressionado for '=', a expressão na entrada é avaliada e o resultado é exibido.
   - Caso contrário, o valor do botão é anexado à entrada existente.

6. **Manuseio de Erros:**
   - A aplicação tenta avaliar a expressão inserida, e caso haja um erro durante a avaliação (por exemplo, uma divisão por zero), o resultado exibido é "Erro".

## COMO USAR?
### BAIXANDO O PROJETO:
**Passo 1:** Clone o repositório para o seu sistema local.

```bash
git clone https://github.com/VILHALVA/CALCULADORA-TK.git
```

**Passo 2:** Navegue até o diretório do projeto.

```bash
cd CALCULADORA-TK
```

**Passo 3:** Descompacte o arquivo ZIP (se você baixou manualmente):

```bash
unzip CALCULADORA-TK.zip
```

### EXECUTANDO O EXECUTAVEL:
1. **Localize o Arquivo:** Após o download, localize o arquivo executável no seu sistema. Geralmente, os downloads são salvos na pasta "Downloads" do seu computador, mas você pode tê-lo salvo em outro local.

2. **Duplo Clique:** Para executar o arquivo, basta dar um duplo clique sobre ele. Isso abrirá o programa associado ao arquivo. Se o arquivo for um instalador, ele iniciará o processo de instalação. Se for um programa independente, ele será iniciado.

3. **Permissões de Administrador:** Dependendo do programa e das configurações do seu computador, você pode precisar de permissões de administrador para executá-lo. Se solicitado, clique com o botão direito do mouse no arquivo executável e selecione "Executar como administrador".

4. **Compatibilidade:** Certifique-se de que o executável seja compatível com a versão do seu sistema operacional. Se você estiver usando um sistema operacional Windows x64, o executável deve ser compilado para x64 para funcionar corretamente. Isso é importante porque o sistema operacional x64 não pode executar aplicativos compilados apenas para x86 (32 bits).

5. **Dependências:** Verifique se o executável depende de algum software adicional ou bibliotecas para funcionar corretamente. Às vezes, você pode precisar instalar outras ferramentas ou componentes antes de executar o executável.

6. **Configurações de Segurança:** Se o seu sistema operacional estiver configurado para bloquear a execução de aplicativos de fontes desconhecidas ou não confiáveis, você pode precisar ajustar as configurações de segurança para permitir a execução do executável.

7. **Atualizações e Patches:** Por fim, verifique se há atualizações ou patches para o executável, especialmente se for um software de terceiros. As atualizações podem corrigir problemas conhecidos ou adicionar novos recursos ao programa.

### EXECUTANDO O SCRIPT PYTHON:
- Para executar o código Python `(CODIGO.py)` em um PC zerado, ou seja, em um computador onde o Python não está instalado, você precisará seguir alguns passos adicionais para configurar o ambiente de execução. Aqui está um guia básico para isso:

1. **Baixe e Instale o Python:**
   - A primeira etapa é baixar o instalador do Python para o seu sistema operacional. Você pode encontrar o instalador oficial em [python.org](https://www.python.org/downloads/).
   - Se você estiver usando o Windows, certifique-se de baixar a versão adequada para o seu sistema operacional (32 bits ou 64 bits).
   - Siga as instruções do instalador para instalar o Python no seu PC.

2. **Configuração das Variáveis de Ambiente (opcional):**
   - No Windows, é uma boa prática adicionar o diretório de instalação do Python ao PATH do sistema. Isso permite que você execute comandos Python de qualquer diretório no prompt de comando.
   - Para fazer isso, após a instalação, procure "Variáveis de Ambiente" nas configurações do sistema, e adicione o caminho para o diretório de instalação do Python (normalmente algo como C:\PythonXX, onde XX é a versão do Python).

3. **Transferindo o Script para o PC:**
   - Transfira o arquivo `nome-do-arquivo.py` para o PC. Isso pode ser feito por meio de um pen drive, rede local, ou qualquer outro método de transferência de arquivo.

4. **Executando o Script:**
   - Abra um prompt de comando (no Windows, pressione `Win + R`, digite "cmd" e pressione Enter).
   - Navegue até o diretório onde o `nome-do-arquivo.py` está localizado usando o comando `cd` (por exemplo, `cd C:\Caminho\Para\O\nome-do-arquivo.py`).
   - Execute o script digitando `python nome-do-arquivo.py` e pressionando Enter.

5. **Instalando Dependências (se necessário):**
   - Se o seu script Python depende de pacotes ou módulos externos, você precisará instalá-los manualmente.
   - Use o comando `pip install nome-do-pacote` para instalar os pacotes necessários. Certifique-se de estar conectado à internet para que o pip possa baixar e instalar os pacotes.

Seguindo esses passos, você poderá executar o seu script Python em um PC zerado, mesmo sem ter o Python instalado anteriormente. Certifique-se de que todas as dependências do script estejam instaladas e que o Python esteja configurado corretamente no seu sistema. Se você não estiver familiarizado com esses passos, confira nosso [curso completo sobre o Python](https://github.com/VILHALVA/CURSO-DE-PYTHON) para obter orientações detalhadas.

## SAIBA MAIS:
- [PROJETO CRIADO PELO VILHALVA](https://github.com/VILHALVA)
- [FAÇA OS NOSSOS CURSOS](https://github.com/VILHALVA?tab=repositories&q=+topic:CURSO)


