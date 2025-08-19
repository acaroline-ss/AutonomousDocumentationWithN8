# Auto Documentation with n8n + LLM

Generates documentation in **Markdown** from files in a GitHub repository using an **n8n** workflow connected to an **LLM**.  

## 📌 Overview
- Clones a repository  
- Reads all files specified in the **Read code files** node
- Converts binaries → text  
- Sends each file to the LLM with a documentation prompt  
- Merges the responses  
- Generates the documentation and saves it in the folder specified in the last node  
> Main workflow: `workflow.json`.

## 🔧 Features
- Runs locally via **Docker**
- Imports `workflow.json` directly into n8n
- Uses **LM Studio** (local AI model via `host.docker.internal:<PORT>`)
- Generates documentation in Markdown (headings, lists, code snippets)

## ✅ Requirements
- **Docker** installed
- **Git inside the n8n container** (for `git clone`)
- **LM Studio**
---

# 🛠️ How to Run on Your Machine (Windows)

### 1) Install Docker and Create the n8n Container (Windows)
- Download and install Docker Desktop
- Official download page: https://www.docker.com/ 
- Official usage guide: https://docs.docker.com/
- Then, create the container in the terminal in the following format: 
`docker run -it --name <CONTAINER_NAME> ^
  -v <HOST_PATH_TO_DATA>:/data ^
  -p <HOST_PORT>:5678 ^
  -e N8N_BASIC_AUTH_ACTIVE=true ^
  -e N8N_BASIC_AUTH_USER=<BASIC_AUTH_USER> ^
  -e N8N_BASIC_AUTH_PASSWORD=<BASIC_AUTH_PASSWORD> ^
  <IMAGE_NAME>`

### 2) Download the `workflow.json` file from this repository

### 3) Access n8n 

Open: http://localhost:5679
  
### 4) Import the workflow

In n8n, go to: **Create workflow → Import from file → Select** `workflow.json`.

# ⚙️ How to Configure the n8n Workflow Nodes

## 1) **Clone Repository** 

`rm -rf <TARGET_DIR> && git clone <REPO_URL> <TARGET_DIR>`

`<TARGET_DIR>`: the local destination folder where the repository will be cloned.
Example: in the n8n container it’s usually /data/repos.

`<REPO_URL>`: the Git repository URL (HTTPS or SSH).

Full example:
`rm -rf /data/repos && git clone https://github.com/user/my-repo.git /data/repos`

## 2) **Read Code Files**

Traverses the files in the specified folder and retrieves files in the chosen language.

Example:
`/data/repos/**/*.py`

- `/data/repos/` → base folder where the search starts.
- `**/` → recursively traverses zero or more subfolders.
- `*.py` → gets files whose names end with `.py`

💡 For testing purposes, you can also use the folder `codigo` included in this repository as an example input. It contains sample files that allow you to quickly validate the auto-documentation workflow in n8n.

## 3) **AI Agent**

This node can use two types of APIs:

### **External API**: 
Uses an API key from OpenAI or Groq, obtained from their respective official accounts, to integrate the external provider into your workflow as needed.

### **Local API**: 
### 📥 Install LM Studio

Download and install for **Windows/macOS/Linux**:
- **LM Studio — Download:** https://lmstudio.ai/download

### ⬇️ Download a Model

In the app, open the “Discover” tab, search for a model (e.g., llama-3.2-3b-instruct) and click **Load**.  

### 🔌 Start Local API (OpenAI-compatible)

1. In LM Studio, go to **Developer / Start Server** (or “Local Server”).  

### 🔗 Connect in n8n

Use the **OpenAI Chat Model** (or **OpenAI Compatible Chat**) node and create a credential with:
- **API Key:** `lm-studio`
- **Base URL:** `http://localhost:1234/v1` (or `http://host.docker.internal:1234/v1` if n8n is running inside a Docker container)
- **Model:** exactly the name displayed in LM Studio (e.g., `llama-3.2-3b-instruct`)

### 4) After this, simply click *Execute workflow* in n8n and the documentation will be generated and saved in the folder specified in the `Save DOCUMENTATION` node.
