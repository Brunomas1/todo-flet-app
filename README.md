# 📝 Todo List App com Flet

Este é um aplicativo de lista de tarefas (To-Do List) moderno e responsivo, desenvolvido com [Flet](https://flet.dev). Ele permite adicionar, editar, concluir, excluir e limpar tarefas com animações suaves e suporte a tema claro/escuro.

---

## ✨ Funcionalidades

- ✅ Adicionar tarefas
- 🖊️ Editar tarefas com campo inline
- ❌ Excluir tarefas
- ☑️ Marcar tarefas como concluídas com **animação de riscado e cor vermelha**
- 🧹 Limpar tarefas concluídas
- 🌗 Alternar entre tema claro e escuro
- 🎨 Cores adaptadas ao tema
- 📱 Layout responsivo e visual moderno

---

## 📦 Tecnologias utilizadas

- [Python 3.10+](https://www.python.org/)
- [Flet](https://flet.dev): Framework para apps frontend com Python

---

## 🚀 Como rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/Brunomas1/todo-flet-app.git
cd todo-flet-app
```

### 2. Crie e ative um ambiente virtual (opcional mas recomendado)

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install flet
```

### 4. Execute o app

```bash
flet run main.py
```

Ou, se estiver na pasta `src`:

```bash
flet run src/main.py
```

---

## 🧠 Organização do código

- `main.py`: Código principal do aplicativo
- Estilização e lógica de interface organizadas por funções
- Uso de `AnimatedSwitcher` para transições suaves
- Separação clara entre UI e ações (eventos)

---

## 🙌 Contribuições

Contribuições são bem-vindas!  
Sinta-se à vontade para abrir issues ou enviar pull requests.

---
#
