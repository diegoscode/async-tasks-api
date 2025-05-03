# async-tasks-api

### Descrição:

O **async-tasks-api** é um projeto minimalista que integra **FastAPI**, **Celery**, **RabbitMQ** e **Redis** para realizar o processamento assíncrono de tarefas. Ele oferece uma API simples para enfileirar tarefas e consultar seus resultados, com Celery gerenciando o processamento de tarefas em segundo plano e Redis armazenando os resultados.

Além disso, o projeto utiliza **Docker** para containerizar os serviços, garantindo fácil escalabilidade e isolamento entre os componentes (FastAPI, Celery, RabbitMQ e Redis), facilitando a implantação e o gerenciamento do ambiente de desenvolvimento e produção.

---

# 🚀 Instruções para Rodar o Projeto

1. Após clonar o projeto, no Windows, primeiramente iniciar o Docker Desktop.

2. Abrir o terminal na pasta do projeto.

3. No terminal, iniciar o WSL:
    >  wsl.exe -d Ubuntu

4. Construir e iniciar os containers:
    > docker-compose up --build

5. Testar a API:
- Abrir outro terminal na pasta do projeto e iniciar o WSL (Ver tópico 3)

- No terminal, enviar uma tarefa. Exemplo:
    > curl -X POST "http://localhost:8000/add?x=10&y=20"

- Exemplo de resposta esperada:

    ```

    {"task_id":"fb65efc3-9f60-48e3-9a50-f726a64036a8"}

    ```

- Ainda no terminal, verificar o resultado:

    ```

    curl http://localhost:8000/result/fb65efc3-9f60-48e3-9a50-f726a64036a8

    ```

- Resposta esperada:

    ```
    {
        "task_id":"fb65efc3-9f60-48e3-9a50-f726a64036a8",
        "status":"SUCCESS",
        "result":30
    }

    ```