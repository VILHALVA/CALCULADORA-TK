# CALCULADORA
🎈CALCULADORA BÁSICA COM INTERFACE GRÁFICA.

[![GitHub Repo stars](https://img.shields.io/badge/VILHALVA-GITHUB-03A9F4?logo=github)](https://github.com/VILHALVA)
[![GitHub Repo stars](https://img.shields.io/badge/MEUS-CURSOS-03A9F4?logo=github)](https://github.com/VILHALVA?tab=repositories&q=CURSO&type=public&language=&sort=)

<img src="https://drmarcellolopes.site.med.br/fmfiles/index.asp/::XPR1MAIP::/Calculadora.png" align="center" width="280"> <br>

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

Essa calculadora simples é uma demonstração básica de como criar uma interface gráfica para realizar operações matemáticas simples em Python. Ela oferece uma interação amigável com o usuário e é capaz de realizar cálculos básicos de maneira eficaz.