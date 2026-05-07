# 🐍 Snake Game
Um jogo clássico da Snake recriado em Python usando o módulo **turtle**, com classes separadas para organização: **Snake**, **Food** e **Scoreboard**.  
O objetivo é simples: comer comida, crescer e evitar bater nas paredes ou na própria cauda.

---

## 🎯 Objetivo  
Criar uma versão modular e orientada a objetos do jogo Snake, com animações suaves, deteção de colisões e sistema de pontuação.

---

## 🧩 Estrutura do Projeto  
- **Snake** – controla o movimento, direção e crescimento da cobra  
- **Food** – gera comida em posições aleatórias  
- **Scoreboard** – mostra e atualiza a pontuação  
- **main.py** – contém o loop principal do jogo e a lógica de colisões

---

## 🚀 Funcionalidades  
- Movimento suave da cobra com animação controlada por `screen.tracer(0)`  
- Comida gerada em posições aleatórias  
- Sistema de pontuação com atualização dinâmica  
- Crescimento da cobra ao comer  
- Deteção de colisão com paredes  
- Deteção de colisão com a própria cauda  
- Fim de jogo com mensagem personalizada

---

## 🎮 Controlo do Jogo  
- **Seta ↑** → mover para cima  
- **Seta ↓** → mover para baixo  
- **Seta ←** → mover para a esquerda  
- **Seta →** → mover para a direita  

---

## 🧠 Conceitos Praticados  
- Programação orientada a objetos (OOP)  
- Herança de classes (`Food` e `Scoreboard` herdam de `Turtle`)  
- Animação com `screen.tracer()`  
- Deteção de colisões  
- Listas e manipulação de coordenadas  
- Loops de jogo  
- Modularização de código
