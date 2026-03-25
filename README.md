# API Health Check

Projeto simples em Flask para expor endpoints de health check e servir como base de demonstracao de pipeline CI/CD.

## Objetivo

O objetivo principal deste projeto e rodar uma pipeline de CI/CD com GitHub Actions, incluindo:
- execucao de testes automatizados;
- build da imagem Docker;
- publicacao da imagem no Docker Hub.

## Endpoints

- `GET /health` retorna status da aplicacao.
- `GET /liveness` retorna status de liveness.
- `GET /` retorna uma mensagem simples da API.

## Executar localmente

1. Instale as dependencias:
   - `pip install -r requirements.txt`
2. Inicie a API:
   - `python app/main.py`
3. Acesse:
   - `http://localhost:5000/health`

## Testes

- Executar testes: `python -m pytest -q`

## CI/CD

O workflow esta em `/.github/workflows/ci-cd.yml` e atualmente:
- roda testes em Python 3.11;
- realiza build e push da imagem Docker com tags `latest` e `github.sha`.