# 🔧 Troubleshooting - App não funciona no Streamlit Cloud

## ⚠️ Problemas Comuns e Soluções

### 1. ❌ Erro ao carregar a página / App não inicia

#### Sintomas:
- Página em branco
- Mensagem de erro ao acessar
- "Something went wrong"

#### Soluções:

**a) Verificar logs no Streamlit Cloud:**
1. Acesse seu app no Streamlit Cloud
2. Clique nos **"..."** (três pontos) → **"Manage app"**
3. Clique em **"Logs"** para ver os erros

**b) Verificar arquivos essenciais no repositório:**
Certifique-se de que estes arquivos estão commitados:

```bash
# Verificar arquivos no repositório
git ls-files | grep -E "(streamlit_app.py|EcoDataReferences.py|requirements.txt)"
```

Arquivos que DEVEM estar no Git:
- ✅ `streamlit_app.py` (arquivo principal)
- ✅ `EcoDataReferences.py` (funções de cálculo)
- ✅ `requirements.txt` (ou `requirements-streamlit.txt`)
- ✅ `heartcaresite/upload_folder/Laudo Eco Modelo P.docx` (template)

**c) Verificar se `EcoDataReferences.py` está no repositório:**
```bash
# Adicionar se não estiver
git add EcoDataReferences.py
git commit -m "Adicionar EcoDataReferences.py"
git push
```

**d) Verificar requirements.txt:**
Certifique-se de que está usando o arquivo otimizado:
```bash
# No seu repositório local
cp requirements-streamlit.txt requirements.txt
git add requirements.txt
git commit -m "Atualizar requirements.txt para deploy"
git push
```

---

### 2. ❌ Erro: "ModuleNotFoundError: No module named 'EcoDataReferences'"

#### Solução:
O arquivo `EcoDataReferences.py` não está no repositório Git.

```bash
# 1. Verificar se o arquivo existe localmente
ls -la EcoDataReferences.py

# 2. Adicionar ao Git
git add EcoDataReferences.py

# 3. Verificar se não está no .gitignore
grep -i EcoDataReferences .gitignore
# Se estiver listado, remova essa linha do .gitignore

# 4. Commit e push
git commit -m "Adicionar EcoDataReferences.py"
git push
```

---

### 3. ❌ Erro: "Template não encontrado"

#### Sintoma:
- App carrega mas mostra erro ao tentar gerar laudo
- Mensagem: "❌ Template não encontrado"

#### Solução:
O arquivo template não está no repositório ou está sendo ignorado pelo Git.

```bash
# 1. Verificar se o arquivo existe
ls -la "heartcaresite/upload_folder/Laudo Eco Modelo P.docx"

# 2. Verificar se está sendo ignorado pelo .gitignore
# Certifique-se de que o .gitignore permite o template:
# Deve ter: !heartcaresite/upload_folder/Laudo Eco Modelo P.docx

# 3. Forçar adição do template (mesmo se grande)
git add -f "heartcaresite/upload_folder/Laudo Eco Modelo P.docx"

# 4. Verificar tamanho (GitHub tem limite de 100MB por arquivo)
du -h "heartcaresite/upload_folder/Laudo Eco Modelo P.docx"

# 5. Commit e push
git commit -m "Adicionar template do laudo"
git push
```

**Nota:** Se o arquivo for muito grande (>50MB), considere:
- Comprimir o arquivo
- Usar Git LFS
- Ou fazer upload do template via interface da app

---

### 4. ❌ Erro: "No module named 'pdfplumber'" ou outras dependências

#### Solução:
O `requirements.txt` não está correto ou não inclui todas as dependências.

**a) Verificar requirements.txt:**
```bash
# Certifique-se de que tem todas as dependências:
cat requirements.txt
```

Deve incluir pelo menos:
```
streamlit>=1.28.0
pdfplumber>=0.10.2
python-docx>=1.0.1
pandas>=2.1.1
numpy>=1.26.1
python-dateutil>=2.8.2
Pillow>=10.1.0
```

**b) Atualizar requirements.txt:**
```bash
# Usar o arquivo otimizado
cp requirements-streamlit.txt requirements.txt
git add requirements.txt
git commit -m "Corrigir requirements.txt"
git push

# No Streamlit Cloud, clique em "⋮" → "Reboot app"
```

---

### 5. ❌ Erro: "ImportError" ou erro de sintaxe

#### Solução:
Pode haver erro de sintaxe ou problema com imports.

**a) Testar localmente primeiro:**
```bash
# Executar localmente para ver erros
python3 -m streamlit run streamlit_app.py
```

**b) Verificar Python version no Streamlit Cloud:**
- No Streamlit Cloud, certifique-se de que está usando Python 3.8+
- Isso é automático, mas você pode especificar no `packages.txt` se necessário

**c) Verificar encoding do arquivo:**
Certifique-se de que `streamlit_app.py` está em UTF-8.

---

### 6. ❌ App carrega mas não faz nada / Botões não funcionam

#### Possível causa:
Problema com session state ou com a função `main()`.

**Solução:**
Verificar se o código termina com:

```python
if __name__ == "__main__":
    main()
```

Verificar o final do `streamlit_app.py`:
```bash
tail -20 streamlit_app.py
```

Deve terminar com:
```python
if __name__ == "__main__":
    main()
```

---

### 7. ❌ Erro ao fazer upload de PDF

#### Possível causa:
Problema com tempfile ou permissões.

**Solução:**
O código já usa `tempfile`, que funciona no Streamlit Cloud. Verifique se:
- O tamanho do PDF não excede 50MB (configurado no `.streamlit/config.toml`)
- O PDF não está corrompido

---

## 🔍 Checklist de Diagnóstico

Antes de reportar problemas, verifique:

- [ ] ✅ `streamlit_app.py` está na raiz do repositório
- [ ] ✅ `EcoDataReferences.py` está na raiz e commitado
- [ ] ✅ `requirements.txt` contém todas as dependências necessárias
- [ ] ✅ Template `Laudo Eco Modelo P.docx` está commitado
- [ ] ✅ Arquivo `.streamlit/config.toml` existe (opcional)
- [ ] ✅ `.gitignore` não está ignorando arquivos essenciais
- [ ] ✅ Código funciona localmente (`streamlit run streamlit_app.py`)
- [ ] ✅ Último commit foi feito com push para GitHub
- [ ] ✅ App foi reiniciado no Streamlit Cloud após push

---

## 🛠️ Script de Verificação

Execute este script localmente antes de fazer push:

```bash
#!/bin/bash
echo "🔍 Verificando arquivos necessários..."

# Verificar arquivo principal
if [ ! -f "streamlit_app.py" ]; then
    echo "❌ streamlit_app.py não encontrado!"
    exit 1
fi

# Verificar EcoDataReferences
if [ ! -f "EcoDataReferences.py" ]; then
    echo "❌ EcoDataReferences.py não encontrado!"
    exit 1
fi

# Verificar requirements
if [ ! -f "requirements.txt" ] && [ ! -f "requirements-streamlit.txt" ]; then
    echo "❌ requirements.txt não encontrado!"
    exit 1
fi

# Verificar template
TEMPLATE="heartcaresite/upload_folder/Laudo Eco Modelo P.docx"
if [ ! -f "$TEMPLATE" ]; then
    echo "⚠️  Template não encontrado: $TEMPLATE"
fi

# Verificar se main() existe
if ! grep -q "if __name__ == \"__main__\":" streamlit_app.py; then
    echo "⚠️  main() não encontrada no final do arquivo"
fi

echo "✅ Verificação completa!"
```

---

## 📞 Como Obter Ajuda

1. **Ver logs no Streamlit Cloud:**
   - App → "..." → "Manage app" → "Logs"

2. **Testar localmente:**
   ```bash
   streamlit run streamlit_app.py
   ```

3. **Verificar repositório Git:**
   ```bash
   git status
   git log --oneline -5
   ```

4. **Verificar arquivos commitados:**
   ```bash
   git ls-files | grep -E "(streamlit_app|EcoDataReferences|requirements|Laudo)"
   ```

---

## 🚀 Passos para Re-deploy Correto

Se nada funcionar, tente fazer deploy limpo:

1. **Limpar e reconfigurar:**
   ```bash
   # Usar requirements otimizado
   cp requirements-streamlit.txt requirements.txt
   
   # Verificar arquivos essenciais
   git add streamlit_app.py EcoDataReferences.py requirements.txt
   git add -f "heartcaresite/upload_folder/Laudo Eco Modelo P.docx"
   
   # Commit
   git commit -m "Corrigir deploy - adicionar arquivos faltantes"
   git push
   ```

2. **No Streamlit Cloud:**
   - Delete o app antigo
   - Crie um novo app
   - Selecione o repositório atualizado

3. **Aguardar deploy:**
   - Primeira vez pode demorar 3-5 minutos
   - Verifique os logs para ver progresso

---

## ⚡ Solução Rápida Mais Comum

O problema mais comum é **arquivos faltando no repositório**. 

Execute isso e tente novamente:

```bash
# Garantir que todos os arquivos essenciais estão commitados
git add streamlit_app.py
git add EcoDataReferences.py  
git add requirements-streamlit.txt
git mv requirements-streamlit.txt requirements.txt 2>/dev/null || cp requirements-streamlit.txt requirements.txt
git add requirements.txt
git add -f "heartcaresite/upload_folder/Laudo Eco Modelo P.docx"
git commit -m "Corrigir deploy - garantir todos arquivos essenciais"
git push

# No Streamlit Cloud, reinicie o app (⋮ → Reboot app)
```

---

**Ainda não funciona?** Verifique os logs detalhados no Streamlit Cloud e compartilhe a mensagem de erro exata!


