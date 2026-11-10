# 📄 Relatório Técnico de Desenvolvimento Colaborativo
**Disciplina:** Design Profissional  
**Instituição:** Universidade Positivo  
**Projeto:** Sistema de Gerenciamento de Tarefas (To-Do List)  
**Repositório:** [https://github.com/ca10r0dr1gu3s/sistema-estoque-grupo](https://github.com/ca10r0dr1gu3s/sistema-estoque-grupo)  

---

## 👥 1. Identificação da Equipe e Divisão de Tarefas

| Integrante | GitHub | Papel no Projeto | Contribuições Técnicas |
| :--- | :--- | :--- | :--- |
| **Caio Rodrigues** | [@ca10r0dr1gu3s](https://github.com/ca10r0dr1gu3s) | Líder Técnico & Repositório | Criação do repositório público, elaboração do `README.md`, menu principal iterativo (`main`), função de concluir tarefas (`concluir_tarefa`) e mediação da resolução de conflitos de merge. |
| **Lauro Manoel** | [@lauromanoel-hub](https://github.com/lauromanoel-hub) | Desenvolvedor Backend (CRUD) | Validações de entrada (`validar_texto`, `validar_prioridade`, `validar_id`), funções de busca (`buscar_tarefa`), cadastro com geração incremental de IDs, edição de dados e exclusão com confirmação. |
| **Luan dos Santos** | [@naskjz](https://github.com/naskjz) | Desenvolvedor de Interface & Métricas | Formatação tabular da listagem de tarefas (`listar_tarefas`) e módulo estatístico de produtividade (`exibir_relatorio`), calculando percentuais de conclusão e métricas por prioridade. |

---

## 🌿 2. Organização e Ciclo de Vida de Branches
Para evitar alterações concorrentes desordenadas na branch principal (`main`), adotamos um fluxo baseado em **Feature Branches**:

1. `main`: Mantida exclusivamente com código funcional e testado.
2. `feature/menu-e-conclusao`: Implementação do fluxo inicial e status de conclusão (PR #1).
3. `feature/listagem-e-relatorios`: Implementação do módulo visual e analítico de dados (PR #2).
4. `feature/cadastro-edicao-exclusao`: Implementação do núcleo de manipulação de dados (PR #3).

Cada branch foi integrada via **Pull Request**, permitindo revisão de código (*Code Review*) antes da mesclagem.

---

## ⚠️ 3. Identificação e Resolução do Conflito de Merge (Etapa 5)

### A. Origem do Conflito
O conflito de merge ocorreu durante a integração do **Pull Request #3** (`feature/cadastro-edicao-exclusao`).  
Enquanto a branch do integrante Lauro continha a implementação das funções de cadastro substituindo o arquivo base `app.py`, as branches anteriores já haviam introduzido na `main` o menu expansivo e as funções de relatórios.  
Ao tentar mesclar o PR #3 na `main`, o Git identificou que a mesma região de linhas do arquivo `app.py` havia sido modificada com conteúdos divergentes em ambas as ramificações, impedindo o merge automático:
```text
Auto-merging app.py
CONFLICT (content): Merge conflict in app.py
Automatic merge failed; fix conflicts and then commit the result.
```

### B. Evidências Capturadas
1. **GitHub Pull Request #3**: Bloqueio de merge automático com o status:  
   *"This branch has conflicts that must be resolved (app.py)"*.
2. **VS Code / Git CLI**: Exibição dos marcadores de conflito (`<<<<<<< HEAD`, `=======`, `>>>>>>> origin/feature/cadastro-edicao-exclusao`).

### C. Solução Técnica Adotada
A equipe reuniu as modificações e aplicou a resolução manual:
1. **Preservação das Validações e CRUD:** As funções desenvolvidas pelo Lauro foram mantidas integralmente no início do módulo.
2. **Integração das Métricas:** As funções de listagem e estatísticas desenvolvidas pelo Luan foram acopladas sem perda de dados.
3. **Unificação do Menu:** O laço interativo principal do Caio foi configurado para endereçar todas as 6 opções operacionais do sistema.
4. **Commit de Resolução:** As alterações unificadas foram testadas, confirmadas sem erros de sintaxe e consolidadas através do commit de merge:
   `fix: resolve conflito de merge integrando CRUD do Lauro ao menu e relatorios`.

---

## 💡 4. Dificuldades Encontradas e Aprendizados
- **Comunicação e Sincronização:** Compreensão prática de que o comando `git pull` antes de iniciar novas branches previne retrabalho e descompasso entre repositórios remotos e locais.
- **Resolução Construtiva de Conflitos:** O conflito de código não foi tratado como erro individual, mas sim como um estágio natural da colaboração técnica, exigindo diálogo para unificar o melhor de cada entrega.
- **Rastreabilidade:** A disciplina no uso de commits descritivos permitiu mapear com clareza a evolução semanal de cada funcionalidade.
