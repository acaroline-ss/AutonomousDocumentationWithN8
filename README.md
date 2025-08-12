
# Funcionalidades

# Como correr o arquivo na sua maquina 
### Precisa ter o docker instalado na sua maquina para correr o n8n localmente
### Criar o containeu  no docker com o seguinte formato docker run -it --name n8n-docflow-new -v C:\Users\AnaSilva\n8n_checkpoint:/data -p 5679:5678 -e N8N_BASIC_AUTH_ACTIVE=true -e N8N_BASIC_AUTH_USER=admin -e N8N_BASIC_AUTH_PASSWORD=senha123 n8nio/n8n
### entrar na porta no docker 
### Baixar e importar o arquivo "workflow.json" dentro do n8n
### configurar o reposirotio do github que voce deseja clonar no node "clonar repositorio" ex https://github.com/acaroline-ss/AutonomousDocumentationWithN8N.git
### integrar com algum modelo d eia do lm studio com a url "http://host.docker.internal:<PORTA>" e escolha o seu modelo local, ou use uma api externa como a do grok ou da open ai

# Dependencias 
### docker 
### lm studio 
### api de alguma ia (local, groq ou open ai)

# Como configurar o ambiente 

#


