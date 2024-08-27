# 🖼️🎯 ImageHunter

ImageHunter é uma ferramenta desenvolvida em Python que utiliza Selenium para buscar e baixar imagens automaticamente do site iStock. O projeto foi criado para automatizar o processo de pesquisa e download de imagens, facilitando o trabalho de quem precisa coletar um grande número de imagens para projetos de design, marketing, ou análise.

## 🛠️ Funcionalidades

- **Busca automatizada**: Realiza buscas por termos específicos no iStock e navega pelos resultados.
- **Download de imagens**: Baixa automaticamente as imagens encontradas na pesquisa e as salva em um diretório específico.
- **Armazenamento organizado**: Cria diretórios com base no termo de pesquisa para organizar as imagens baixadas.

## 📂 Estrutura do Projeto

- **`ImageHunter.py`**: Script principal que realiza a busca e o download das imagens.
- **`/imagens`**: Diretório onde as imagens baixadas são armazenadas.

## 🚀 Como Usar

1. **Clone o repositório**:
    ```bash
    git clone https://github.com/AnubisChacal/ImageHunter.git
    ```

2. **Instale as dependências**:
    ```bash
    pip install selenium requests
    ```

3. **Configure o script**:
   - Substitua a variável `pesquisa` no script com o termo de busca desejado (por exemplo, "superman").
   - Verifique o caminho do `geckodriver` para Firefox e ajuste se necessário.

4. **Execute o script**:
    ```bash
    python ImageHunter.py
    ```

5. **Resultados**:
   - As imagens serão baixadas para um diretório com o nome do termo de pesquisa.

## 🛠️ Requisitos

- **Python 3.x**
- **Selenium**
- **Requests**
- **Geckodriver** (para Firefox)

## 📝 Observações

- Certifique-se de respeitar os termos de serviço do iStock ao utilizar web scrapers para baixar imagens.
