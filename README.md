# 📦 Mini ERP - Controle de Estoque Industrial

> Sistema em Python desenvolvido para gerenciar o fluxo de materiais na indústria, focando em rastreabilidade de lotes, status de aprovação, persistência local em arquivos de texto e modularização.

---

## 🚀 Sobre o Projeto

Este projeto nasceu da união entre a minha **experiência prática no setor industrial** e o **desenvolvimento de software**. O objetivo é simular um mini ERP voltado para o controle de estoque de chão de fábrica, permitindo o gerenciamento de entradas, saídas (Stock Check), posições físicas, lotes e o **status de qualidade** dos insumos.

Além da regra de negócio voltada para logística, o projeto foi construído para praticar conceitos avançados de engenharia de software, como **organização em pacotes**, **modularização** e **tratamento robusto de exceções**.

---

## 🛠️ Tecnologias e Ferramentas Utilizadas

* **Linguagem:** Python 3.x
* **Persistência de Dados:** Arquivos de Texto (`.txt`) com codificação `UTF-8`
* **Módulos Nativos:** `datetime` (carimbo automático de data e hora)
* **IDE:** PyCharm

---

## ⚙️ Funcionalidades do Sistema

1. **Cadastro de Materiais:** Registro completo contendo Código, Nome, Lote, Status (ex: Aprovado/Reprovado), Local de Armazenamento e Data/Hora automática de entrada.
2. **Visualização de Estoque:** Listagem formatada em colunas de todos os insumos armazenados.
3. **Stock Check (Saída/Baixa):** Realiza a baixa automatizada de materiais do estoque com base na busca pelo código do produto.
4. **Persistência Local:** Dados salvos em arquivo texto (`materiais.txt`), garantindo a retenção das informações.
5. **Tratamento de Exceções:** Validação de entradas no menu e proteção contra interrupções de teclado (`Ctrl+C`).

---

## 📂 Estrutura do Projeto

```text
📦 sistema_erp/
│
├── 📂 lib/
│   ├── 📂 arquivo/
│   │   └── __init__.py      # Lógica de manipulação, leitura, cadastro e baixa (TXT)
│   └── 📂 interface/
│       └── __init__.py      # Menus dinâmicos, cabeçalhos, cores e validações de input
│
├── materiais.txt            # Banco de dados local em formato texto (gerado automaticamente)
└── sistema.py               # Script principal (Entry Point) que controla o fluxo do ERP
