# Docker - Text Summarizer API

Este documento explica como executar a aplicação usando Docker.

## Pré-requisitos

- Docker instalado
- Docker Compose instalado
- Chave da API OpenAI configurada

## Configuração

1. **Configure a variável de ambiente:**

   ```bash
   export OPENAI_API_KEY="sua-chave-da-openai-aqui"
   ```

2. **Ou crie um arquivo `.env` na raiz do projeto:**
   ```bash
   echo "OPENAI_API_KEY=sua-chave-da-openai-aqui" > .env
   ```

## Executando com Docker Compose

### 1. Build e execução

```bash
# Build das imagens e execução
docker-compose up --build

# Executar em background
docker-compose up -d --build
```

### 2. Verificar logs

```bash
# Ver logs em tempo real
docker-compose logs -f backend

# Ver logs de todos os serviços
docker-compose logs
```

### 3. Parar os serviços

```bash
docker-compose down
```

## Executando apenas com Docker

### 1. Build da imagem

```bash
cd backend
docker build -t text-summarizer-api .
```

### 2. Executar container

```bash
docker run -p 8000:8000 -e OPENAI_API_KEY="sua-chave" text-summarizer-api
```

## Verificando se está funcionando

1. **Health Check:**

   ```bash
   curl http://localhost:8000/api/v1/health
   ```

2. **Documentação da API:**

   - Swagger: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

3. **Teste de resumo:**
   ```bash
   curl -X POST "http://localhost:8000/api/v1/summarize" \
        -H "Content-Type: application/json" \
        -d '{
          "text": "Este é um texto de exemplo para testar a API de resumo. Ele deve ter pelo menos 10 caracteres para ser válido.",
          "summary_type": "medio"
        }'
   ```

## Comandos úteis

```bash
# Ver containers em execução
docker ps

# Entrar no container
docker exec -it text-summarizer-llm-backend-1 bash

# Ver logs específicos
docker logs text-summarizer-llm-backend-1

# Rebuild sem cache
docker-compose build --no-cache

# Limpar containers e imagens não utilizadas
docker system prune -a
```

## Troubleshooting

### Erro de permissão

```bash
# Se houver problemas de permissão no Linux
sudo docker-compose up --build
```

### Porta já em uso

```bash
# Verificar o que está usando a porta 8000
lsof -i :8000

# Ou mudar a porta no docker-compose.yml
ports:
  - "8001:8000"  # Mapeia porta 8001 do host para 8000 do container
```

### Problemas de memória

```bash
# Aumentar memória disponível para Docker
# (no Docker Desktop: Settings > Resources > Memory)
```

## Desenvolvimento

Para desenvolvimento com hot-reload:

```bash
# Executar com volume montado para desenvolvimento
docker-compose up --build

# O código será recarregado automaticamente quando alterado
```

## Produção

Para produção, considere:

1. **Remover volumes de desenvolvimento**
2. **Usar variáveis de ambiente seguras**
3. **Configurar logs apropriados**
4. **Implementar health checks robustos**
5. **Usar reverse proxy (nginx)**
6. **Configurar SSL/TLS**
