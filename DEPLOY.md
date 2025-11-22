# 🚀 Guia de Deploy - Vet Heart Care

Este guia apresenta as melhores opções para fazer deploy da aplicação Streamlit para acesso público pela internet.

## 📊 Comparação de Opções

| Opção | Custo | Facilidade | Melhor Para |
|-------|-------|------------|-------------|
| **Streamlit Cloud** ⭐ | Grátis | ⭐⭐⭐⭐⭐ | Todos (RECOMENDADO) |
| **Render** | Grátis (com limites) | ⭐⭐⭐⭐ | Alternativa ao Streamlit Cloud |
| **Railway** | Grátis (créditos) | ⭐⭐⭐⭐ | Apps com mais recursos |
| **VPS Próprio** | $5-20/mês | ⭐⭐ | Controle total |

---

## 🌟 OPÇÃO 1: Streamlit Cloud (RECOMENDADO)

**Melhor escolha para começar!** É grátis, super fácil e feito especificamente para Streamlit.

### ✅ Vantagens:
- ✅ **100% GRÁTIS** para apps públicos
- ✅ Deploy em menos de 5 minutos
- ✅ Integração direta com GitHub
- ✅ SSL automático (HTTPS)
- ✅ URLs amigáveis
- ✅ Zero configuração de servidor
- ✅ Atualizações automáticas ao fazer push

### 📋 Pré-requisitos:
1. Conta no GitHub (grátis): https://github.com
2. Conta no Streamlit Cloud (grátis): https://streamlit.io/cloud

### 🚀 Passo a Passo:

#### 1. Preparar o Código

Primeiro, certifique-se de que seu código está pronto:

```bash
# Usar o requirements otimizado
cp requirements-streamlit.txt requirements.txt

# Verificar se o template está no lugar certo
ls heartcaresite/upload_folder/Laudo\ Eco\ Modelo\ P.docx
```

#### 2. Criar Repositório no GitHub

```bash
# Inicializar Git (se ainda não tiver)
git init

# Adicionar arquivos (certifique-se de não adicionar arquivos sensíveis)
git add .
git commit -m "Preparar para deploy no Streamlit Cloud"

# Criar repositório no GitHub e conectar
# Depois execute:
git remote add origin https://github.com/SEU_USUARIO/vet-heart-care.git
git branch -M main
git push -u origin main
```

#### 3. Deploy no Streamlit Cloud

1. Acesse: https://share.streamlit.io/
2. Faça login com sua conta GitHub
3. Clique em **"New app"**
4. Configure:
   - **Repository**: Seu repositório GitHub
   - **Branch**: `main` (ou `master`)
   - **Main file path**: `streamlit_app.py`
5. Clique em **"Deploy!"**

🎉 **Pronto!** Sua app estará online em minutos com uma URL tipo:
`https://seu-usuario-vet-heart-care.streamlit.app`

#### 4. Configurações Opcionais

Você pode adicionar um arquivo `.streamlit/config.toml` no repositório para configurações customizadas (já foi criado neste projeto).

### 🔒 Segurança

- O Streamlit Cloud oferece HTTPS automático
- Para apps privados, há planos pagos
- Não armazene dados sensíveis no código

---

## 🌐 OPÇÃO 2: Render (Alternativa Gratuita)

Render oferece deploy gratuito com algumas limitações.

### ✅ Vantagens:
- ✅ Grátis com tier gratuito
- ✅ Deploy automático via GitHub
- ✅ HTTPS automático
- ✅ Suporta múltiplas linguagens

### 📋 Deploy no Render:

1. Acesse: https://render.com
2. Crie uma conta (grátis)
3. Clique em **"New +"** → **"Web Service"**
4. Conecte seu repositório GitHub
5. Configure:
   - **Name**: `vet-heart-care`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements-streamlit.txt`
   - **Start Command**: `streamlit run streamlit_app.py --server.port $PORT --server.address 0.0.0.0`
6. Clique em **"Create Web Service"**

**Nota**: No Render, você precisa ajustar o comando de start para usar a porta `$PORT` e o endereço `0.0.0.0`.

### ⚙️ Ajustes Necessários para Render:

Crie um arquivo `render.yaml` na raiz:

```yaml
services:
  - type: web
    name: vet-heart-care
    env: python
    plan: free
    buildCommand: pip install -r requirements-streamlit.txt
    startCommand: streamlit run streamlit_app.py --server.port $PORT --server.address 0.0.0.0
    envVars:
      - key: PYTHON_VERSION
        value: 3.11.0
```

---

## 🚂 OPÇÃO 3: Railway (Alternativa Moderna)

Railway oferece créditos gratuitos mensais.

### ✅ Vantagens:
- ✅ $5 em créditos grátis por mês
- ✅ Deploy super rápido
- ✅ Excelente para desenvolvimento

### 📋 Deploy no Railway:

1. Acesse: https://railway.app
2. Crie conta (pode usar GitHub)
3. Clique em **"New Project"** → **"Deploy from GitHub repo"**
4. Selecione seu repositório
5. Railway detecta automaticamente que é Streamlit
6. Configure as variáveis de ambiente se necessário

Railway geralmente detecta Streamlit automaticamente e configura tudo!

---

## 💻 OPÇÃO 4: VPS Próprio (Controle Total)

Para mais controle, você pode usar um VPS como DigitalOcean, Linode, ou AWS Lightsail.

### ✅ Vantagens:
- ✅ Controle total
- ✅ Sem limites de recursos
- ✅ Pode customizar tudo

### 📋 Setup Básico (Ubuntu/Debian):

```bash
# 1. Atualizar sistema
sudo apt update && sudo apt upgrade -y

# 2. Instalar Python e pip
sudo apt install python3 python3-pip python3-venv -y

# 3. Clonar repositório
git clone https://github.com/SEU_USUARIO/vet-heart-care.git
cd vet-heart-care

# 4. Criar ambiente virtual
python3 -m venv venv
source venv/bin/activate

# 5. Instalar dependências
pip install -r requirements-streamlit.txt

# 6. Configurar firewall
sudo ufw allow 8501/tcp

# 7. Executar com nohup (ou usar systemd)
nohup streamlit run streamlit_app.py --server.port 8501 --server.address 0.0.0.0 &
```

### 🔒 Configurar Nginx (Recomendado para produção):

```nginx
# /etc/nginx/sites-available/vet-heart-care
server {
    listen 80;
    server_name seu-dominio.com;

    location / {
        proxy_pass http://127.0.0.1:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Depois configure SSL com Let's Encrypt (grátis):
```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d seu-dominio.com
```

---

## 📝 Checklist de Preparação

Antes de fazer deploy, certifique-se de:

- [ ] ✅ Usar `requirements-streamlit.txt` (otimizado)
- [ ] ✅ Template Word está no repositório (`heartcaresite/upload_folder/`)
- [ ] ✅ Arquivos sensíveis estão no `.gitignore`
- [ ] ✅ Código funciona localmente
- [ ] ✅ Testou upload de PDF e geração de laudo
- [ ] ✅ Não há credenciais hardcoded no código

---

## 🔧 Ajustes Necessários no Código

### Para Deploy em Cloud (Streamlit Cloud, Render, Railway):

O código atual já deve funcionar! Apenas certifique-se de:

1. **Paths relativos**: O código já usa `os.path.join(os.path.dirname(__file__), ...)` que funciona em cloud ✅

2. **Template deve estar no repositório**: 
   - O arquivo `heartcaresite/upload_folder/Laudo Eco Modelo P.docx` deve estar commitado no Git

3. **Upload de arquivos**: Já usa `tempfile`, que funciona perfeitamente em cloud ✅

### Para Render/Railway (porta dinâmica):

Se usar Render ou Railway, você pode precisar criar um `Procfile` ou ajustar o start command (já incluído nas instruções acima).

---

## 💰 Custos Comparados

| Serviço | Tier Gratuito | Limitações |
|---------|---------------|------------|
| **Streamlit Cloud** | ✅ Grátis | Apps públicos ilimitados |
| **Render** | ✅ Grátis | Sleep após 15min inativo |
| **Railway** | ✅ $5 créditos/mês | ~500 horas de uso |
| **VPS (DO/Linode)** | ❌ | ~$5-20/mês |

---

## 🎯 Recomendação Final

**Para começar:** Use **Streamlit Cloud** - é grátis, super fácil e perfeito para Streamlit.

**Se precisar de mais recursos:** Considere **Railway** ou **Render**.

**Para produção crítica:** Use **VPS próprio** com Nginx + SSL.

---

## 🆘 Problemas Comuns

### "Template não encontrado" em produção
- Certifique-se de que o arquivo `Laudo Eco Modelo P.docx` está commitado no Git
- Verifique o caminho relativo no código

### "Timeout" ou app demora para carregar
- Primeira execução pode demorar (instalação de dependências)
- Verifique se não há dependências muito pesadas

### Erro de porta
- Certifique-se de usar `$PORT` em Render/Railway
- No Streamlit Cloud, isso é automático

---

## 📞 Próximos Passos

1. Escolha uma opção (recomendamos Streamlit Cloud)
2. Prepare o repositório GitHub
3. Siga os passos da opção escolhida
4. Teste tudo funcionando
5. Compartilhe a URL! 🎉

**Boa sorte com o deploy! 🚀**

