# Projeto 01 de Inteligência Artificial - IA25_P01_G05

## Repositório
[Link do repositório GitHub](https://github.com/HugoSpecial/IA25_P01_G05)  

---

## Equipa de Desenvolvimento (Grupo 5)
- Duarte Pereira — Nº 27959
- Hugo Especial — Nº 27963
- Paulo Gonçalves — Nº 27966 
- Marco Cardoso — Nº 27969 
- Hugo Pereira — Nº 27970

---

## Introdução
Todos os anos letivos, a equipa administrativa do **IPCA** enfrenta dificuldades na criação dos horários das aulas.  
É necessário garantir que todas as restrições relacionadas com **professores, cursos, salas e disponibilidade** sejam cumpridas, o que torna o processo demorado e complexo.

Este projeto tem como objetivo desenvolver uma **ferramenta automática de geração de horários** para os cursos de licenciatura, facilitando o trabalho administrativo e garantindo horários equilibrados e eficientes.

---

## Objetivo
O principal objetivo é criar um sistema que produza horários válidos e otimizados, tendo em conta um conjunto de ***hard** e **soft constraints***.

### *Hard Constraints*
- Cada aula dura **2 horas**.  
- Todas as turmas têm **10 aulas semanais**.  
- Cada curso pode ter **1 ou 2 aulas por semana**.  
- Uma turma **não pode ter mais de 3 aulas por dia**.  
- O horário deve respeitar a **disponibilidade dos professores**.  
- **Aulas online (máx. 3)** devem ser realizadas **no mesmo dia**.  
- Algumas aulas são obrigatoriamente atribuídas a **salas específicas**.

### *Soft Constraints*
- Aulas da mesma unidade curricular devem ocorrer em **dias distintos**.  
- Cada turma deve ter, se possível, **apenas 4 dias de aulas por semana**.  
- As aulas de cada dia devem ser **consecutivas**.  
- O número de **salas diferentes por turma** deve ser minimizado.

---

## Descrição do Projeto
O projeto consiste no desenvolvimento de um **agente inteligente** capaz de gerar horários automaticamente com base nas restrições definidas.  
O processo inclui:
- Definição de **dados sobre cursos, professores e salas**.
- Aplicação das ***hard*** e ***soft constraints***.  
- Avaliação de **possíveis soluções**.  
- Seleção do **melhor horário encontrado**.

### Implementação Técnica:
O projeto deve ser **implementado em Python**, recorrendo a um **Jupyter Notebook** e a **biblioteca *Constraint***.

---


## Como Executar

- Ter o **Python 3.10+** instalado.  
- Ter a biblioteca **python-constraint** instalada:
  ```bash
  pip install python-constraint
  ```
- Entrar na pasta src/:
  ```bash
  cd src/
  ```
- Executar o main.py:
  ```bash
  python main.py
  ```
  

---

## Resultados Esperados
- **Horários completos e válidos** para todos os cursos.  
- **Cumprimento total** das restrições obrigatórias.  
- **Otimização** das preferências.
- **Facilidade de ajuste** e análise de resultados.

---
