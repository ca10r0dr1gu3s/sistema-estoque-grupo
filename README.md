# 📋 Sistema de Gerenciamento de Tarefas (To-Do List)

> **Universidade Positivo**  
> **Disciplina:** Design Profissional  
> **Trabalho Prático:** Desenvolvimento Colaborativo com Git e GitHub  

---

## 👥 Integrantes da Equipe

| Nome Completo | Usuário GitHub | Responsabilidade Principal |
| :--- | :--- | :--- |
| **Caio Rodrigues** | [@ca10r0dr1gu3s](https://github.com/ca10r0dr1gu3s) | Estrutura inicial, Menu interativo, Conclusão de Tarefas e Gestão do Repositório |
| **Lauro Manoel** | [@lauromanoel-hub](https://github.com/lauromanoel-hub) | Módulo de Validações, Cadastro, Edição e Exclusão de Tarefas |
| **Luan** | [@naskjz](https://github.com/naskjz) | Módulo de Listagem Formatada, Filtros e Relatórios Estatísticos |

---

## 🎯 Objetivo do Projeto
Desenvolver um sistema em Python para terminal com menu interativo, aplicando boas práticas de desenvolvimento colaborativo, organização em branches temáticas, revisões de código via Pull Requests e resolução de conflitos de merge.

---

## ⚙️ Funcionalidades do Sistema
- [x] **Menu Interativo**: Navegação intuitiva no terminal.
- [x] **Cadastro de Tarefas**: Título, descrição, prioridade (Baixa, Média, Alta) e ID incremental.
- [x] **Validação de Entradas**: Prevenção de campos em branco e validação de tipos de dados.
- [x] **Edição de Tarefas**: Atualização granular de campos com preservação dos dados atuais.
- [x] **Exclusão com Confirmação**: Proteção contra exclusões acidentais.
- [x] **Conclusão de Tarefas**: Gestão do status (`Pendente` / `Concluída`).
- [x] **Listagem e Relatórios**: Visualização formatada e métricas de produtividade.

---

## 🚀 Como Executar o Programa

### Pré-requisitos
- Python 3.10 ou superior instalado.
- Git instalado na máquina.

### Executando localmente:
```bash
# 1. Clone o repositório
git clone https://github.com/ca10r0dr1gu3s/sistema-estoque-grupo.git

# 2. Acesse a pasta do projeto
cd sistema-estoque-grupo

# 3. Execute o programa
python app.py
```

---

## 🌿 Organização de Branches
Para manter a estabilidade da branch principal (`main`), todas as alterações foram desenvolvidas em branches isoladas:

- `main`: Versão estável em produção.
- `feature/menu-e-conclusao`: Implementação do fluxo principal e status (Caio).
- `feature/cadastro-edicao-exclusao`: Módulo CRUD e validações (Lauro).
- `feature/listagem-e-relatorios`: Listagem e estatísticas (naskjz).
- `fix/conflito-menu`: Branch utilizada para o exercício prático de resolução de conflitos.
