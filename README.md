# Mensagem - FastAPI exemplo

Projeto mínimo que expõe uma rota GET `/` retornando uma mensagem JSON.

Pré-requisitos

- Python 3.8+
- Docker (opcional, para containerização)
- docker-compose (opcional)

Instalação rápida (desenvolvimento local)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Executar servidor localmente

```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Testes (local)

```bash
pytest -q
```

Resposta esperada na rota `/`:

```json
{ "message": "Olá, mundo!" }
```

---

Uso com Docker

O projeto inclui um `Dockerfile` multiestágio e um `docker-compose.yml` para facilitar a execução em containers.

Construir a imagem Docker:

```bash
docker build -t mensagem_web:latest .
```

Executar o container:

```bash
docker run --rm -p 8000:8000 mensagem_web:latest
```

Ou usando docker-compose (recomendado para desenvolvimento/integração rápida):

```bash
# Constrói a imagem e sobe o serviço
docker compose up --build

# Para rodar em background
docker compose up --build -d

# Parar e remover
docker compose down
```

Executar testes dentro do container

```bash
# Executa pytest no serviço definido no docker-compose
docker compose run --rm web pytest -q
```

Desenvolvimento com hot-reload (opção)

O `docker-compose.yml` padrão monta o diretório do projeto como somente leitura por segurança. Para desenvolvimento com hot-reload, você tem duas opções rápidas:

1) Ajustar `docker-compose.yml` trocando o volume para leitura/escrita e habilitar o reload no comando:

```yaml
# volumes:
#   - ./:/app:rw
# command: uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

2) Ou executar temporariamente o serviço com montagem de volume e `--reload`:

```bash
docker compose run --service-ports --rm -v "$(pwd)":/app web \
  uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

Notas de produção

- Para produção, considere usar um servidor de aplicação como Gunicorn com workers Uvicorn (`gunicorn -k uvicorn.workers.UvicornWorker`) e ajustar o número de workers conforme CPU/ram.
- Evite usar `--reload` em ambiente de produção.

Dicas / Troubleshooting

- Se a porta 8000 estiver em uso, altere o mapeamento de portas (`-p 8001:8000`) ou configure outra porta no `uvicorn`.
- Se instalar localmente, ative o virtualenv antes de instalar dependências para evitar conflitos com pacotes do sistema.
- Permissões em volumes: em alguns sistemas, pode ser necessário ajustar permissões do diretório para que o processo Python no container consiga ler/editar arquivos quando o volume é montado como `rw`.

Se quiser, eu posso:
- Rodar `docker compose up --build` aqui para construir e subir o serviço e mostrar a saída, ou
- Gerar um `docker-compose.override.yml` pronto para desenvolvimento com `:rw` e `--reload`.
