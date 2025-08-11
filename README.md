## Como correr o arquivo na sua maquina 
1 Precisa ter o docker instalado na sua maquina para correr o n8n localmente
2 Criar o containeu  no docker com o seguinte formato docker run -it --name n8n-docflow-new -v C:\Users\AnaSilva\n8n_checkpoint:/data -p 5679:5678 -e N8N_BASIC_AUTH_ACTIVE=true -e N8N_BASIC_AUTH_USER=admin -e N8N_BASIC_AUTH_PASSWORD=senha123 n8nio/n8n
3 entrar na porta no docker 
4 Baixar e importar o arquivo "workflow.json"
5 configurar o reposirotio do github que voce deseja clonar no node "cloar repositorio" 
