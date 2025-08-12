# Auto Documentation with n8n + LLM

Gera documentação em **Markdown** a partir de arquivos **.py** de um repositório Git, usando um fluxo no **n8n** conectado a um **LLM** (Groq ou LM Studio).  

## 📌 Visão geral
- Clona um repositório  
- Lê todos os arquivos indicados no nó **Ler arquivos de código**
- Converte binários → texto  
- Envia cada arquivo ao LLM com um prompt de documentação  
- Junta as respostas  
- Gera a documentação e salva na pasta indicada no último nó
> Workflow principal: `workflow.json`.

## 🔧 Funcionalidades
- Executa localmente via **Docker**
- Importação do `workflow.json` direto no n8n
- Uso do **LM Studio** (modelo de IA local via `host.docker.internal:<PORTA>`)
- Geração de documentação em Markdown (títulos, listas, trechos de código)

## ✅ Pré-requisitos
- **Docker** instalado
- **Git dentro do container do n8n** (para `git clone`)
- **LM Studio**
---

# 🛠️ Como correr na sua máquina (Windows)

### 1) Instalar o docker e criar o container do n8n (windows)
- Baixar e instalar o Docker Desktop
- Página oficial (download): https://www.docker.com/ 
- Guia oficial de uso: https://docs.docker.com/
- A seguir, crie o container no terminal no seguinte formato: 
`docker run -it --name <CONTAINER_NAME> ^
  -v <HOST_PATH_TO_DATA>:/data ^
  -p <HOST_PORT>:5678 ^
  -e N8N_BASIC_AUTH_ACTIVE=true ^
  -e N8N_BASIC_AUTH_USER=<BASIC_AUTH_USER> ^
  -e N8N_BASIC_AUTH_PASSWORD=<BASIC_AUTH_PASSWORD> ^
  <IMAGE_NAME>`

### 2) Baixe o arquivo **workflow.json** que está neste repositório

### 3) Acesse o n8n 

Abra: http://localhost:5679
  
### 4) Importar o workflow

No n8n, vá em: **Create wokflow → Import from file → Selecione o** `workflow.json`.

# ⚙️ Como configurar os nós do fluxo do n8n

## 1) **Clonar repositório** 

`rm -rf <TARGET_DIR> && git clone <REPO_URL> <TARGET_DIR>`

`<TARGET_DIR>`: a pasta de destino local onde o repositório será clonado.
Ex.: no container do n8n normalmente é /data/repos.

`<REPO_URL>`: a URL do repositório Git (HTTPS ou SSH).

Exemplo Completo:
`rm -rf /data/repos && git clone https://github.com/usuario/meu-repo.git /data/repos`

## 2) **Ler Arquivos do código**

Percorre os arquivos na pasta indicada e pega os arquivos na linguagem escolhida.

Exemplo:
`/data/repos/**/*.py`

- `/data/repos/` → pasta base onde a busca começa.
- `**/` → percorre recursivamente zero ou mais subpastas.
- `*.py` → pega arquivos cujo nome termina em `py`

## 3) **AI Agent**

Neste nó podem ser usados dois tipos de APIs:

### **API Externa**: 
Utiliza uma chave de API da OpenAI ou da Groq, obtida nas respetivas contas oficiais, para integrar o provedor externo ao teu fluxo conforme necessário.
### **API Local**: 
### 📥 Instalar o LM Studio

Baixe e instale para **Windows/macOS/Linux**:
- **LM Studio — Download:** https://lmstudio.ai/download

### ⬇️ Baixar um modelo

No app, abra a aba de modelos (“Discover”), pesquise um modelo (ex.: llama-3.2-3b-instruct) clique em **Load**.  

### 🔌 Iniciar API local (OpenAI-compatible)

1. No LM Studio, vá em **Developer / Start Server** (ou “Local Server”).  

### 🔗 Conectar no n8n

Use o nó **OpenAI Chat Model** (ou **OpenAI Compatible Chat**) e crie uma credencial com:
- **API Key:** `lm-studio`
- **Base URL:** `http://localhost:1234/v1` (ou `http://host.docker.internal:1234/v1` se o n8n estiver correndo em um container no Docker)
- **Model:** exatamente o nome exibido no LM Studio (ex.: `llama-3.2-3b-instruct`)

### 4) Após isto, basta clicar em *Execute workflow* no n8n e a documentação será gerada e guardada na pasta indicada no nó **Salvar DOCUMENTATION** 







