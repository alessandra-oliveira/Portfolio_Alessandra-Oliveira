# Portfolio Alessandra Oliveira

Projeto de portfolio pessoal desenvolvido com Django, Django REST Framework e integração com microserviço de notificações.

---

## Repositórios

| Projeto | Link |
|--------|------|
| Portfolio (este projeto) | https://github.com/alessandra-oliveira/Portfolio_Alessandra-Oliveira |
| Microserviço de Notificações | https://github.com/alessandra-oliveira/notificacao-ms |

---

## Pré-requisitos

- Python 3.12+
- Git

---

## Como executar os dois projetos

Você precisará de **dois terminais abertos ao mesmo tempo** — um para cada projeto.

---

## 1. Microserviço de Notificações (porta 8001)

### 1.1 Clonar o repositório

```bash
git clone https://github.com/alessandra-oliveira/notificacao-ms.git
cd notificacao-ms
```

### 1.2 Criar e ativar o ambiente virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

### 1.3 Instalar as dependências

```bash
pip install -r requirements.txt
```

### 1.4 Aplicar as migrações

```bash
python manage.py migrate
```

### 1.5 Criar o superusuário

```bash
python manage.py createsuperuser
```

### 1.6 Iniciar o servidor na porta 8001

```bash
python manage.py runserver 8001
```

### 1.7 Configurar dados no Admin

Acesse http://127.0.0.1:8001/admin/ e:

1. Crie uma **Empresa**: nome = `Portfolio Alessandra`. Anote o **hash** gerado automaticamente.
2. Crie um **Target**: empresa = `Portfolio Alessandra`, user_id = `1`.
3. Crie algumas **Notificações** para esse target.

---

## 2. Portfolio (porta 8000)

### 2.1 Clonar o repositório

Abra um **novo terminal** e clone o portfolio:

```bash
git clone https://github.com/alessandra-oliveira/Portfolio_Alessandra-Oliveira.git
cd Portfolio_Alessandra-Oliveira
```

### 2.2 Criar e ativar o ambiente virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

### 2.3 Instalar as dependências

```bash
pip install -r requirements.txt
```

### 2.4 Configurar o microserviço no settings.py

Abra `portfolio_pessoal/settings.py` e atualize as configurações do microserviço com o hash gerado no passo 1.7:

```python
NOTIFICACAO_MS_URL = 'http://127.0.0.1:8001'
NOTIFICACAO_MS_API_KEY = 'SEU_HASH_AQUI'
```

### 2.5 Aplicar as migrações

```bash
python manage.py migrate
```

### 2.6 Criar o superusuário

```bash
python manage.py createsuperuser
```

### 2.7 Iniciar o servidor na porta 8000

```bash
python manage.py runserver
```

---

## 3. Testar

Com os **dois servidores rodando**:

1. Acesse http://127.0.0.1:8000/admin/ e faça login
2. Acesse http://127.0.0.1:8000/portfolio/
3. O **sino 🔔** deve aparecer no menu com o número de notificações não lidas
4. Clique no sino para ver as notificações
5. Clique em uma notificação para marcá-la como lida — o contador diminui automaticamente
6. Para testar **sem conexão**: pare o servidor do microserviço (Ctrl+C). O badge deve mudar para **X** cinza na próxima atualização (a cada 5 segundos)

### Criar notificações via API (simulando outro sistema)

```bash
# Windows (PowerShell)
Invoke-RestMethod -Uri "http://127.0.0.1:8001/api/notificacoes/criar/" `
  -Method POST `
  -Headers @{"X-Api-Key"="SEU_HASH_AQUI"; "Content-Type"="application/json"} `
  -Body '{"user_id": 1, "mensagem": "Nova notificacao de teste!"}'
```

---

## Estrutura dos projetos

```
# Microserviço
notificacao-ms/
├── notificacao_ms/        ← configurações Django
├── notificacoes/          ← app principal
│   ├── models.py          ← Empresa, Target, Notification
│   ├── views.py           ← endpoints da API
│   ├── serializers.py
│   ├── authentication.py  ← validação X-Api-Key e X-User-Id
│   └── urls.py
└── requirements.txt

# Portfolio
Portfolio_Alessandra-Oliveira/
├── portfolio_pessoal/     ← configurações Django
├── core/
│   ├── context_processors.py  ← passa configs do MS para templates
│   └── templates/core/
│       └── base.html          ← sino de notificações + JavaScript
├── portfolio/             ← app do portfolio
└── requirements.txt
```
