# 📇 Gestor de Contactos em Python

## 📖 Descrição

Este projeto consiste no desenvolvimento de um **Gestor de Contactos** utilizando a linguagem de programação **Python**.

A aplicação permite ao utilizador gerir uma lista de contactos, possibilitando adicionar, consultar, editar e eliminar informações de pessoas.

O projeto foi desenvolvido com o objetivo de aplicar conceitos fundamentais de programação em Python, como estruturas de dados, funções, classes, manipulação de ficheiros e organização de código.

---

## 🎯 Objetivos do projeto

O principal objetivo é criar uma aplicação simples e funcional para gestão de contactos.

A aplicação permite:

* ➕ Adicionar novos contactos;
* 📋 Listar contactos;
* 🔎 Pesquisar contactos;
* ✏️ Editar contactos;
* 🗑️ Eliminar contactos;

---

## 🚀 Tecnologias utilizadas

* **Python 3**
* **Programação Orientada a Objetos**
* **Ficheiros JSON** para armazenamento dos dados

---

# ⚙️ Funcionalidades

## ➕ Adicionar contacto

O utilizador pode adicionar um novo contacto fornecendo informações como:

* Nome;
* Número de telefone;
* Email;

# 📋 Listar contactos

É possível consultar todos os contactos registados.

---

# 🔎 Pesquisar contacto

O utilizador pode pesquisar um contacto através do nome ou de outras informações.

Exemplo:

```text id="wq6s2v"
Pesquisar contacto: João

Resultado:

Nome: João Silva
Telefone: 912345678
Email: joao@email.com
```

Caso nenhum contacto seja encontrado:

```text id="m0n1yk"
Nenhum contacto encontrado.
```

---

# 🗑️ Eliminar contacto

O utilizador também pode remover um contacto.

Antes da eliminação, a aplicação pode solicitar confirmação:

```text id="qnd7t8"
Deseja eliminar o contacto "João Silva"?

[S] Sim
[N] Não
```

Após a confirmação:

```text id="p2ef5k"
Contacto eliminado com sucesso!
```

---

# 💾 Armazenamento dos dados

Os contactos podem ser armazenados num ficheiro **JSON**, permitindo que os dados permaneçam disponíveis mesmo depois de fechar a aplicação.

Exemplo de estrutura:

```json id="17zhlr"
[
    {
        "nome": "João Silva",
        "telefone": "912345678",
        "email": "joao@email.com",
        "morada": "Guimarães"
    },
    {
        "nome": "Maria Santos",
        "telefone": "934567890",
        "email": "maria@email.com",
        "morada": "Braga"
    }
]
```

O ficheiro poderá ser armazenado numa pasta específica:

```text id="0qg0pq"
data/
└── contactos.json
```

---

# 🐍 Ambiente virtual

Recomenda-se utilizar um ambiente virtual `venv` para manter as dependências do projeto isoladas.

### Criar o ambiente virtual

Windows:

```bash id="98i6rm"
python -m venv venv
```

Linux/macOS:

```bash id="e3h1xk"
python3 -m venv venv
```

### Ativar o ambiente virtual

Windows:

```bash id="r8bq4z"
venv\Scripts\activate
```

Linux/macOS:

```bash id="x9r3rj"
source venv/bin/activate
```

Depois de ativado, deverá aparecer algo semelhante a:

```text id="qj5nmx"
(venv)
```

---

# 👨‍💻 Autor

**Nome:** *[Renan Straquicini]*

---

# 📜 Licença

Este projeto foi desenvolvido para fins **académicos e educacionais**.

