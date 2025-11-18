# 🩺 Guia de Instalação - Vet Heart Care

Este guia irá ajudá-lo a instalar o projeto Vet Heart Care em um novo Mac.

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter instalado no Mac:

1. **Python 3.8 ou superior**
   ```bash
   # Verificar versão do Python
   python3 --version
   
   # Se não tiver Python, instale via Homebrew
   brew install python3
   ```

2. **pip (gerenciador de pacotes Python)**
   ```bash
   # Geralmente vem com Python, mas pode instalar/atualizar assim:
   python3 -m ensurepip --upgrade
   ```

3. **Git** (para clonar o repositório, se aplicável)
   ```bash
   # Verificar se tem Git
   git --version
   
   # Se não tiver, instale via Homebrew
   brew install git
   ```

## 🚀 Método 1: Instalação da Aplicação Streamlit (Recomendado)

A aplicação Streamlit é mais simples de instalar e usar. É a interface recomendada para o sistema.

### Passo 1: Obter o código do projeto

Se você tem o projeto em um repositório Git:
```bash
git clone <URL_DO_REPOSITORIO>
cd vetproject
```

Ou se você tem o projeto em um pendrive/externo, copie a pasta completa para o Mac.

### Passo 2: Criar um ambiente virtual (Recomendado)

Criar um ambiente virtual isola as dependências do projeto:

```bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar o ambiente virtual
source venv/bin/activate

# Você verá (venv) no início da linha do terminal quando estiver ativo
```

### Passo 3: Instalar dependências

```bash
# Com o ambiente virtual ativo, instale as dependências
pip install -r requirements.txt
```

### Passo 4: Verificar arquivos necessários

Certifique-se de que o template do documento existe:
```bash
# Verificar se o arquivo template existe
ls -la heartcaresite/upload_folder/Laudo\ Eco\ Modelo\ P.docx
```

Se o arquivo não existir, você precisará copiá-lo para esta pasta.

### Passo 5: Executar a aplicação

```bash
# Método mais simples (usando o script automático)
python3 run_streamlit.py

# Ou diretamente com Streamlit
streamlit run streamlit_app.py
```

A aplicação será aberta automaticamente no seu navegador em `http://localhost:8501`

### Passo 6: Usar a aplicação

- A interface abrirá no navegador
- Faça upload de um PDF com dados ecocardiográficos
- Revise e confirme os dados extraídos
- Gere o laudo em formato Word (.docx)

---

## 🏗️ Método 2: Instalação Completa (Django + Streamlit)

Se você precisar do projeto Django completo com banco de dados:

### Passo 1-2: Mesmo que o Método 1

Siga os Passos 1 e 2 do Método 1 acima.

### Passo 3: Configurar banco de dados

O projeto está configurado para usar PostgreSQL por padrão, mas você pode usar SQLite (mais simples) para desenvolvimento:

#### Opção A: Usar SQLite (Mais simples para começar)

Edite o arquivo `vetproject/settings.py` e substitua a configuração do banco de dados:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

#### Opção B: Usar PostgreSQL (Se precisar da funcionalidade completa)

1. Instalar PostgreSQL:
```bash
brew install postgresql@14
brew services start postgresql@14
```

2. Criar banco de dados:
```bash
createdb VetHeartCare
```

3. Editar `vetproject/settings.py` com suas credenciais:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'VetHeartCare',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Passo 4: Instalar dependências

```bash
pip install -r requirements.txt
```

### Passo 5: Configurar banco de dados Django

```bash
# Criar migrações
python3 manage.py makemigrations

# Aplicar migrações
python3 manage.py migrate

# Criar superusuário (opcional, para acessar o admin)
python3 manage.py createsuperuser
```

### Passo 6: Coletar arquivos estáticos

```bash
python3 manage.py collectstatic --noinput
```

### Passo 7: Executar servidor Django

```bash
python3 manage.py runserver
```

Acesse `http://localhost:8000` no navegador.

---

## 🐳 Método 3: Instalação via Docker

Se você preferir usar Docker:

### Pré-requisito: Instalar Docker Desktop

```bash
# Baixe e instale Docker Desktop para Mac de:
# https://www.docker.com/products/docker-desktop
```

### Passo 1: Construir e executar o container

```bash
# No diretório do projeto
docker compose up --build
```

A aplicação estará disponível em `http://localhost:8000`

---

## ✅ Verificação da Instalação

Para verificar se tudo está funcionando:

1. **Streamlit:**
   ```bash
   streamlit --version
   python3 -c "import streamlit; print('Streamlit OK')"
   ```

2. **Dependências principais:**
   ```bash
   python3 -c "import pdfplumber; print('pdfplumber OK')"
   python3 -c "import docx; print('python-docx OK')"
   python3 -c "import pandas; print('pandas OK')"
   ```

---

## 🆘 Solução de Problemas Comuns

### Erro: "command not found: python3"
- Instale Python via Homebrew: `brew install python3`
- Ou use `python` em vez de `python3` (verifique a versão: `python --version`)

### Erro: "pip: command not found"
```bash
python3 -m ensurepip --upgrade
```

### Erro: "Template não encontrado"
- Verifique se o arquivo `heartcaresite/upload_folder/Laudo Eco Modelo P.docx` existe
- Certifique-se de que está no diretório correto do projeto

### Erro ao instalar dependências (erros de compilação)
Algumas dependências podem precisar de bibliotecas do sistema:
```bash
# Instalar ferramentas de desenvolvimento
xcode-select --install

# Instalar dependências do sistema para algumas bibliotecas Python
brew install pkg-config
```

### Porta já em uso
Se a porta 8501 (Streamlit) ou 8000 (Django) estiver em uso:
```bash
# Para Streamlit, use outra porta:
streamlit run streamlit_app.py --server.port 8502

# Para Django, use outra porta:
python3 manage.py runserver 8001
```

### Problemas com ambiente virtual
Se tiver problemas com o ambiente virtual:
```bash
# Remover e recriar
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Erro: "Permission denied"
Alguns comandos podem precisar de permissões:
```bash
# Dar permissão de execução ao script
chmod +x run_streamlit.py
```

---

## 📝 Notas Importantes

1. **Ambiente Virtual:** É altamente recomendado usar um ambiente virtual para evitar conflitos com outros projetos Python.

2. **Template do Documento:** O arquivo `Laudo Eco Modelo P.docx` é necessário para gerar os laudos. Certifique-se de que ele está presente.

3. **Python Version:** O projeto foi desenvolvido para Python 3.8+. Versões mais antigas podem não funcionar.

4. **Primeira Execução:** Na primeira vez que executar, o Streamlit pode fazer download de alguns componentes. Isso é normal.

---

## 🎯 Recomendação

Para a maioria dos usuários, **recomendamos o Método 1 (Streamlit)** porque:
- ✅ Mais simples de instalar e usar
- ✅ Não requer configuração de banco de dados
- ✅ Interface mais moderna e intuitiva
- ✅ Funcionalidades principais disponíveis

Use o Método 2 (Django completo) apenas se precisar:
- Acesso ao painel administrativo Django
- Funcionalidades específicas do Django não disponíveis no Streamlit
- Integração com banco de dados PostgreSQL

---

## 📞 Ajuda Adicional

Se você encontrar problemas não listados aqui:

1. Verifique os logs de erro no terminal
2. Certifique-se de que todas as dependências foram instaladas: `pip list`
3. Teste com um ambiente virtual limpo
4. Verifique se está usando a versão correta do Python

---

**Boa sorte com a instalação! 🩺**
