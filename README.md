# CPF Generator

Pacote Python leve para **geração** e **validação** de números de CPF brasileiros por meio de uma interface de linha de comando (CLI).

---

## Funcionalidades Principais

* **Gerar CPF**: Produz CPFs válidos, nos formatos:
    * Formatado: `000.000.000-00`
    * Sem formatação: `00000000000`
* **Validar CPF**: Verifica a validade de CPFs, tanto formatados quanto sem formatação.
* **CLI Amigável**: Comandos simples e intuitivos construídos com `argparse`.
* **Qualidade de Código**: O código é formatado com `blue` e `isort` para garantir consistência e legibilidade.
* **Testes Automatizados**: Cobertura completa de testes com `pytest` para assegurar a confiabilidade.

---

## Instalação

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/pycodebr/cpf_generator_test.git
    cd cpf_generator
    ```

2.  **Instale em modo editável:**
    ```bash
    pip install -e .
    ```
    A instalação em **modo editável** (com a flag `-e`) é um passo crucial para o desenvolvimento. Este comando "linka" seu projeto ao ambiente Python, fazendo com que o pacote `cpf` (dentro da pasta `src`) seja reconhecido e possa ser importado de qualquer lugar do projeto.

    Isso **facilita enormemente as importações**, permitindo o uso de caminhos absolutos (ex: `from cpf.generator import generate`) em vez de caminhos relativos complexos. O resultado é um código mais limpo, robusto e fácil de manter.

---

## Uso da CLI

Execute os comandos a partir do diretório raiz do projeto.

| Ação | Comando |
| :--- | :--- |
| **Gerar CPF formatado** (padrão) | `python -m cli generate` |
| **Gerar CPF sem formatação** | `python -m cli generate --raw` |
| **Validar CPF formatado** | `python -m cli validate 529.982.247-25` |
| **Validar CPF sem formatação**| `python -m cli validate 52998224725` |

> **Dica:** Se ocorrer um erro de importação, verifique se você está na raiz do projeto e se o ambiente virtual ativo é o mesmo onde o pacote foi instalado com `pip install -e .`.

---

## Ferramentas de Desenvolvimento e Qualidade

Este projeto utiliza um conjunto de ferramentas para garantir a qualidade, consistência e manutenibilidade do código.

### 🧪 Testes com `pytest`

`pytest` é um framework que torna a criação de testes simples e escaláveis.

* **Por que é importante?** Testes automatizados garantem que as funcionalidades (`gerar` e `validar` CPF) funcionem como esperado e que novas alterações não quebrem o código existente. Isso é fundamental para a estabilidade do projeto.

* **Como usar:**
    1.  Instale o `pytest`:
        ```bash
        pip install pytest
        ```
    2.  Rode a suíte de testes:
        ```bash
        pytest -v
        ```

### 💅 Formatação de Código com `blue`

`blue` é um formatador de código Python que reformata todo o seu código para seguir um estilo consistente, baseado no formatador `black`.

* **Por que é importante?** Um estilo de código uniforme em todo o projeto melhora drasticamente a legibilidade. Isso facilita a manutenção e a colaboração, pois todos os desenvolvedores escrevem e leem código no mesmo formato.

* **Como usar:**
    1.  Instale o `blue`:
        ```bash
        pip install blue
        ```
    2.  Formate um arquivo ou diretório:
        ```bash
        blue src/cli.py
        ```

### ✨ Organização de Importações com `isort`

`isort` é um utilitário Python que organiza as importações (`import`) em ordem alfabética e as separa por tipo.

* **Por que é importante?** Manter as importações organizadas torna o código mais limpo e evita conflitos de merge (`merge conflicts`) quando diferentes desenvolvedores adicionam novas importações aos arquivos.

* **Como usar:**
    1.  Instale o `isort`:
        ```bash
        pip install isort
        ```
    2.  Organize as importações em todo o projeto:
        ```bash
        isort .
        ```

### 📖 Documentação com `MkDocs`

`MkDocs` é um gerador de sites estáticos rápido e simples, voltado para a criação de documentação de projetos.

* **Por que é importante?** Uma boa documentação é essencial para que outros possam entender, usar e contribuir com o seu projeto. `MkDocs` facilita a criação de uma documentação bonita e funcional a partir de arquivos Markdown.

* **Como usar:**
    1.  Instale o `MkDocs`:
        ```bash
        pip install mkdocs
        ```
    2.  Inicie um novo projeto de documentação (se necessário):
        ```bash
        mkdocs new .
        ```
    3.  Inicie um servidor local para visualizar a documentação:
        ```bash
        mkdocs serve
        ```

---

## Estrutura do Projeto

```
cpf_generator/
├── src/
│   ├── cpf/
│   │   ├── generator.py      # Lógica de geração de CPF
│   │   └── validator.py      # Lógica de validação de CPF
│   └── cli.py               # Ponto de entrada da CLI
├── tests/
│   ├── test_generator.py    # Testes do gerador de CPF
│   └── test_validator.py    # Testes do validador de CPF
└── setup.py                 # Configuração do pacote
```

---

## Contribuindo

1.  Faça um **Fork** deste repositório.
2.  Crie uma **branch** de feature:
    ```bash
    git checkout -b feature/NomeDaFuncionalidade
    ```
3.  Faça seus **commits**:
    ```bash
    git commit -m "Descrição da mudança"
    ```
4.  Envie para a sua branch:
    ```bash
    git push origin feature/NomeDaFuncionalidade
    ```
5.  Abra um **Pull Request**.

> Siga o guia de estilo PEP 8, utilize as ferramentas de formatação e inclua testes para novas funcionalidades.

---

## Licença

Este projeto está sob a **Licença MIT**.