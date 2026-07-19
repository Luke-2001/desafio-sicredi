# 

# Desafio Sicredi - Automação de Compras no SauceDemo

Este projeto implementa uma automação de compras no site de demonstração SauceDemo, utilizando Selenium WebDriver e Python. O objetivo é simular o fluxo de login, adição de produtos ao carrinho, checkout e geração de um relatório de compras.

## Contexto de Desenvolvimento

Este projeto foi desenvolvido como parte de um desafio técnico de automação. Como desenvolvedor com **5 anos de experiência em Java**, possuo uma base sólida em lógica de programação, arquitetura de software e padrões de projeto (como o Page Object Model aplicado aqui).

Embora este tenha sido meu primeiro projeto desenvolvido em Python, utilizei minha experiência prévia em desenvolvimento de software para estruturar a solução seguindo boas práticas, como a aplicação do padrão Page Object Model, separação de responsabilidades e organização modular do código. A Inteligência Artificial foi utilizada como apoio ao aprendizado da linguagem e das bibliotecas, acelerando a implementação sem substituir o entendimento das soluções adotadas.

## Funcionalidades

- **Login Automatizado:** Realiza o login no SauceDemo com credenciais pré-definidas.
- **Leitura de Produtos:** Lê uma lista de produtos e suas quantidades de um arquivo CSV.
- **Adição ao Carrinho:** Adiciona os produtos especificados ao carrinho de compras.
- **Checkout:** Preenche as informações do cliente e finaliza a compra.
- **Geração de Relatório:** Cria um arquivo de texto (`relatorio_compras.txt`) com o resumo da compra, incluindo produtos bem-sucedidos e falhas.
- **Capturas de Tela:** Salva capturas de tela do carrinho e da confirmação da compra.
- **Logout:** Realiza o logout da aplicação após a conclusão do fluxo.

## Ambiente de Desenvolvimento e Versões

A automação foi desenvolvida e validada no seguinte ambiente:

| Ferramenta / Biblioteca | Versão                      |
| --- |-----------------------------|
| **Python** | 3.14.6                      |
| **Selenium** | 4.46.0                      |
| **WebDriver Manager** | 4.1.2                       |
| **Microsoft Edge** | Versão estável mais recente |

## Pré-requisitos

Para executar este projeto, você precisará ter instalado:

- **Python 3.x**
- **Navegador Edge:** O projeto utiliza o Microsoft Edge por uma escolha estratégica de estabilidade. Durante o desenvolvimento, observou-se que outros navegadores baseados em Chromium (como o Google Chrome) exibem alertas nativos de segurança ("Mude sua senha") ao utilizar as credenciais públicas do SauceDemo, o que pode bloquear a execução do Selenium. O Edge mostrou-se mais resiliente a esses popups nativos, garantindo um fluxo de automação contínuo.
- **WebDriver para Edge:** O `webdriver-manager` cuidará do download automático do WebDriver compatível com sua versão do Edge. No entanto, é fundamental que o navegador Edge esteja presente.

## Instalação

1. **Clone o repositório** (ou descompacte o arquivo do projeto):

    ```bash
    git clone https://github.com/Luke-2001/desafio-sicredi.git
    cd desafio-sicredi
    ```

2. **Crie e ative um ambiente virtual** (recomendado ):

    ```bash
    python -m venv .venv
    # No Windows
    .venv\Scripts\activate
    # No macOS/Linux
    source .venv/bin/activate
    ```

3. **Instale as dependências**:

    ```bash
    pip install -r requirements.txt
    ```


## Como Executar

1. **Prepare o arquivo de entrada:** Certifique-se de que o arquivo `data/produtos_compra.csv` exista e contenha os produtos que você deseja comprar, no formato:

    ```
    Produto,Quantidade
    Sauce Labs Backpack,2
    Sauce Labs Bike Light,1
    Sauce Labs Bolt T-Shirt,3
    ```

   > **Observação Importante:** O SauceDemo não possui suporte para múltiplas unidades do mesmo produto. O campo Quantidade foi mantido no CSV para atender ao requisito do desafio, porém, ao utilizar o SauceDemo, cada produto é adicionado apenas uma vez devido à limitação da aplicação.

2. **Execute o script principal**:

    ```bash
    python main.py
    ```

   A automação abrirá o navegador Edge, realizará o fluxo de compra e gerará os arquivos de log e relatório.

## Estrutura do Projeto

```json
# Raiz do projeto
├── config/
│   └── settings.py         # Configurações globais do projeto (ex: modo DEBUG)
├── data/
│   └── produtos_compra.csv # Arquivo CSV com a lista de produtos para compra
├── logs/
│   └── automacao.log       # Arquivo de log da execução da automação
├── pages/
│   ├── pagina_carrinho.py        # Page Object para a página do carrinho
│   ├── pagina_checkout.py    # Page Object para as etapas de checkout
│   ├── pagina_login.py       # Page Object para a página de login
│   ├── pagina_menu.py        # Page Object para o menu lateral
│   └── pagina_produtos.py    # Page Object para a página de produtos
├── services/
│   ├── leitor_csv.py       # Serviço para leitura do arquivo CSV de produtos
│   └── servico_relatorio.py   # Serviço para geração do relatório de compras
├── screenshots/
│   ├── cart.png            # Captura de tela do carrinho
│   └── confirmation.png    # Captura de tela da confirmação de compra
├── utils/
│   ├── criador_driver.py   # Utilitário para criação e configuração do WebDriver
│   └── util_elementos.py    # Utilitário para interações com elementos (ex: highlight)
├── main.py                 # Ponto de entrada principal da automação
├── requirements.txt        # Lista de dependências do projeto
└── README.md               # Este arquivo de documentação
```

## Considerações e Melhorias Futuras

Durante a análise do projeto, foram identificados alguns pontos que podem ser aprimorados para aumentar a robustez, a manutenibilidade e a aderência a boas práticas:

- **Geração de PDF:** A funcionalidade de clicar no botão "Generate PDF Order" (`BOTAO_GERAR_PDF_PEDIDO`) no `checkout_page.py` pode não estar presente em todas as versões do SauceDemo ou ser um elemento customizado. Recomenda-se tratar essa etapa como opcional ou validar sua existência de forma mais robusta para evitar falhas inesperadas no fluxo principal.
- **Tratamento de Quantidades:** O projeto lê a quantidade de produtos do CSV, mas o SauceDemo permite adicionar apenas uma unidade por item. O código atual não reflete essa diferença no relatório. Uma melhoria seria ajustar o relatório para indicar a quantidade solicitada vs. a quantidade efetivamente adicionada, ou adaptar a lógica para lidar com a limitação de forma mais explícita.
- **Validação do Carrinho:** Embora haja uma verificação de produtos ausentes no carrinho, o fluxo prossegue para o checkout mesmo que alguns itens não tenham sido adicionados. A função `validar_produtos()` em `pagina_carrinho.py` poderia ser utilizada para interromper o processo se o carrinho não estiver conforme o esperado.
- **Caminhos Relativos:** O projeto utiliza caminhos relativos para logs, screenshots e o arquivo CSV. Para maior portabilidade e execução em diferentes ambientes, é recomendável usar caminhos absolutos baseados na raiz do projeto e garantir que os diretórios de saída (`logs/`, `screenshots/`) sejam criados programaticamente, se não existirem.
- **Tratamento de Exceções:** Algumas exceções são relançadas sem preservar a cadeia de causa (`raise Exception(...)` dentro de `except`). Utilizar `raise ... from exc` melhoraria a rastreabilidade de erros.
- **Configuração de Credenciais e Dados:** Credenciais de login e dados de checkout estão fixos no código (`main.py`). Para ambientes de produção, é essencial externalizar esses dados para variáveis de ambiente, arquivos de configuração seguros ou sistemas de gerenciamento de segredos.
- **Dependências:** O arquivo `requirements.txt` pode conter dependências não utilizadas diretamente pelo projeto. Recomenda-se revisar e manter apenas as dependências essenciais e fixar suas versões para garantir a reprodutibilidade.
- **Testes Automatizados:** A adição de testes unitários e de integração seria fundamental para garantir a qualidade e a estabilidade da automação, especialmente em cenários de mudanças na aplicação alvo.

## Tecnologias Utilizadas

- **Python 3.x**
- **Selenium WebDriver:** Para automação do navegador.
- **`webdriver-manager`***:** Para gerenciamento automático do WebDriver.
- **Edge WebDriver:** Para automação do navegador Edge.
- **`logging`***:** Para registro de eventos e depuração.
- **`csv`***:** Para leitura e escrita de arquivos CSV.

## Autor

- **Lucas Bassanesi**
- GitHub: https://github.com/Luke-2001
