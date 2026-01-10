# Mensagem - FastAPI exemplo

Projeto mínimo que expõe uma rota GET `/` retornando uma mensagem JSON.

Resumo

- Aplicação: FastAPI (em `app/main.py`) que retorna {"message": "Olá, mundo!"} na rota `/`.
- Docker: `Dockerfile` multiestágio incluído.
- Orquestração local: `docker-compose.yml` para executar o serviço rapidamente.
- Infraestrutura: arquivos Terraform em `terraform/` (ALB, ECS, VPC etc.).

Pré-requisitos

- Docker (recomendado)
- docker-compose (opcional)
- Python 3.8+ (para execução local sem container)
- Terraform (se for aplicar a infraestrutura)

Executar localmente (sem Docker)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Endpoint

GET / =>

```json
{ "message": "Olá, mundo!" }
```

Executar com Docker (recomendado)

Construir a imagem:

```bash
docker build -t mensagem_web:latest .
```

Executar a imagem:

```bash
docker run --rm -p 8000:8000 mensagem_web:latest
```

Executar com docker-compose

```bash
# Constrói a imagem e sobe o serviço (interativo)
docker compose up --build

# Em background
docker compose up --build -d

# Parar e remover

docker compose down
```

Testes

O repositório inclui testes simples em `tests/test_main.py`.

```bash
pytest -q
```

Notas sobre Terraform

Existem configurações Terraform em `terraform/` para criar VPC, ALB, ECS e recursos relacionados. Antes de aplicar em uma conta AWS, revise `terraform/variables.tf` e `terraform/terraform.tfvars.example`.

Para validar a configuração localmente (sem backend remoto):

```bash
cd terraform
terraform init -backend=false
terraform validate
```

Se quiser que eu execute o Docker Compose para subir o serviço localmente ou rode a validação do Terraform aqui, diga qual opção prefere e eu executo e mostro a saída.
