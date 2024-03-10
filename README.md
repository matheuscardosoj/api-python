# Documentação do projeto de API em Python

<img src="https://files.realpython.com/media/Consuming-APIs-in-Python_Watermarked.718777293942.jpg" alt="drawing" width="100%"/>

## Como utilizar

1. Deve ser instalado o Docker usando este [link](https://www.docker.com/get-started/).
2. Após a instalação faça o download do diretório no GitHub [aqui](https://github.com/matheuscardosoj/api-python/archive/refs/heads/main.zip).
3. Baixado o diretório, descompacte-o em uma pasta de sua preferência e abra essa mesma pasta pelo CMD.
4. Em seguida, execute o seguinte comando no cmd `docker build -t api-python .` ele será responsável por gerar a imagem da API.
5. Posteriormente, com a execução do comando finalizada execute este comando `docker run -p 80:80 --name container_api_python api-python` ele será responsável por criar um container e executá-lo. para pausar basta usar o nome que escolheu (container_api_python) no comando `docker stop container_api_python`. Caso queira iniciá-lo novamente execute o comando `docker start container_api_python`.
6. Com o container rodando você conseguirá acessar a API no localhost porta 80 e realizar testes, através de apps como curl, Postman ou Insomnia, nos seguintes endpoints:
    * `GET /users`: Retorna a lista completa de usuários.
    * `GET /users/{id}`: Retorna os detalhes do usuário com o ID especificado.
    * `POST /users`: Adiciona um novo usuário à lista.
    * `PUT /users/{id}`: Atualiza os dados do usuário com o ID especificado.
    * `DELETE /users/{id}`: Remove o usuário com o ID especificado.
