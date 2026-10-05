# Atividade: Desafio do Número Secreto

## Objetivo

Criar uma aplicação web em Streamlit na qual o computador sorteia um número e o usuário precisa descobri-lo.

O sistema deve informar se o palpite é:

🔼 Maior que o número secreto
🔽 Menor que o número secreto
🎯 Igual ao número secreto
Além disso, o aluno deverá desenvolver uma interface visual organizada.

## Regras

O programa deve:
- Sortear um número entre 1 e 100.
- Permitir que o usuário informe um palpite.
- Comparar o palpite com o número secreto.
- Informar uma dica:
  - "Tente um número maior!"
  - "Tente um número menor!"
  - "Parabéns! Você acertou!"
- Contar quantas tentativas o jogador utilizou.
- Possuir um botão "Novo Jogo".
- Utilizar elementos visuais do Streamlit.

## 🎨 Requisitos de Design
O aluno deverá utilizar pelo menos:
- st.title()
- st.write() ou st.markdown()
- st.number_input()
- st.button()
- st.success()
- st.warning() ou st.error()
- st.sidebar()

Pode criar um título como:
🎮 DESAFIO DO NÚMERO SECRETO

Não modularize, um único arquivo deve dar conta
O output deve ser apenas o código