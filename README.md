# K8S Full Stack

Projeto de estudo utilizando Kubernetes local com Kind para executar uma aplicação Full Stack composta por:

- Front-end HTML, CSS e JavaScript
- API Python com FastAPI
- Banco de dados PostgreSQL

## Arquitetura

```text
┌───────────────┐
│   Front-end   │
│ HTML/CSS/JS   │
└───────┬───────┘
        │ HTTP
        ▼
┌───────────────┐
│    FastAPI    │
│ Python API    │
└───────┬───────┘
        │ SQL
        ▼
┌───────────────┐
│ PostgreSQL 17 │
└───────────────┘
```

Todos os componentes são executados dentro de um cluster Kubernetes criado com Kind.

---

# Tecnologias

- Kubernetes
- Kind
- Docker
- FastAPI
- PostgreSQL 17
- Nginx
- HTML
- CSS
- JavaScript

---

# Estrutura do Projeto

```text
K8S-Full-Stack
│
├── api
│   ├── app
│   │   └── main.py
│   │
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend
│   ├── index.html
│   ├── style.css
│   ├── script.js
│   └── Dockerfile
│
├── sql
│   └── init.sql
│
└── k8s
    ├── namespace.yaml
    │
    ├── api
    │   ├── deployment.yaml
    │   ├── secret.yaml
    │   └── service.yaml
    │
    ├── frontend
    │   ├── deployment.yaml
    │   └── service.yaml
    │
    └── postgres
        ├── configmap.yaml
        ├── deployment.yaml
        ├── secret.yaml
        └── service.yaml
```

---

# Criando o Cluster

```powershell
kind create cluster --name estudos
```

Verificar:

```powershell
kubectl get nodes
```

---

# Build das Imagens

## API

```powershell
cd api

docker build -t produtos-api:v1 .
```

Carregar imagem no Kind:

```powershell
kind load docker-image produtos-api:v1 --name estudos
```

---

## Front-end

```powershell
cd frontend

docker build -t produtos-frontend:v1 .
```

Carregar imagem no Kind:

```powershell
kind load docker-image produtos-frontend:v1 --name estudos
```

---

# Deploy da Aplicação

Aplicar todos os manifests:

```powershell
kubectl apply -R -f k8s/
```

Verificar os recursos:

```powershell
kubectl get all -n estudos
```

---

# Banco de Dados

O banco é inicializado automaticamente