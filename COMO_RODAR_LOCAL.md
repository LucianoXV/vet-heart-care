# 🖥️ Como Rodar Localmente

## Opção 1: Método Mais Simples (Recomendado) ⭐

### Se você já instalou antes:
```bash
python3 run_streamlit.py
```

Ou no Mac, dê um duplo clique em:
- `Iniciar_Aplicacao.command`

---

## Opção 2: Se é a primeira vez instalando

### Passo 1: Instalar dependências

**Opção A - Com interface gráfica (Mais fácil):**
```bash
python3 instalar.py
```
Ou dê duplo clique em `instalar.py` no Finder

**Opção B - Pela linha de comando:**
```bash
# No Mac
./Iniciar_Instalacao.command
```

**Opção C - Manualmente:**
```bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente virtual
source venv/bin/activate

# Instalar dependências
pip install -r requirements-streamlit.txt
```

### Passo 2: Rodar a aplicação

```bash
# Se ativou o ambiente virtual, já está ativo
# Se não, ative novamente:
source venv/bin/activate

# Rodar a aplicação
python3 run_streamlit.py
```

---

## Opção 3: Método Direto (Sem ambiente virtual)

Se você não quer usar ambiente virtual:

```bash
# Instalar Streamlit e dependências
pip3 install -r requirements-streamlit.txt

# Rodar diretamente
streamlit run streamlit_app.py
```

---

## 📋 Checklist Rápido

Antes de rodar, certifique-se de que:

- [ ] ✅ Python 3.8+ instalado (`python3 --version`)
- [ ] ✅ Dependências instaladas
- [ ] ✅ Template existe: `heartcaresite/upload_folder/Laudo Eco Modelo P.docx`

---

## 🚀 Depois de Rodar

A aplicação abrirá automaticamente no navegador em:
```
http://localhost:8501
```

Se não abrir automaticamente, acesse manualmente essa URL.

---

## 🛑 Para Parar a Aplicação

Pressione `Ctrl+C` no terminal onde está rodando.

---

## ⚠️ Problemas Comuns

### "Python não encontrado"
```bash
# Verificar se Python está instalado
python3 --version

# Se não estiver, instale via Homebrew:
brew install python3
```

### "Streamlit não encontrado"
```bash
pip3 install streamlit
```

### "Template não encontrado"
- A aplicação funcionará, mas não poderá gerar laudos
- Verifique se o arquivo `Laudo Eco Modelo P.docx` está em:
  `heartcaresite/upload_folder/`

### "Porta 8501 já em uso"
```bash
# Rodar em outra porta
streamlit run streamlit_app.py --server.port 8502
```

---

## 💡 Dica

Se você usa Mac e quer facilitar:
1. Execute `preparar_arquivos.py` uma vez
2. Depois pode dar duplo clique em `Iniciar_Aplicacao.command` sempre que quiser rodar

---

## 📝 Resumo dos Comandos

```bash
# Primeira vez (instalar):
python3 instalar.py

# Depois (rodar):
python3 run_streamlit.py

# Ou simplesmente:
streamlit run streamlit_app.py
```

---

**Pronto! A aplicação estará rodando localmente! 🎉**

