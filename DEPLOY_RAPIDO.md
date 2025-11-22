# ⚡ Deploy Rápido - 5 Minutos

## 🎯 Método Mais Rápido: Streamlit Cloud

### Passo 1: Preparar Projeto (2 minutos)

```bash
# Executar script preparador
./setup-streamlit-cloud.sh

# Ou manualmente:
cp requirements-streamlit.txt requirements.txt
```

### Passo 2: Criar Repositório no GitHub (1 minuto)

1. Vá para https://github.com/new
2. Nome do repositório: `vet-heart-care`
3. Clique em **"Create repository"**

### Passo 3: Enviar Código (1 minuto)

```bash
# Se ainda não tiver Git inicializado:
git init
git add .
git commit -m "Preparar para deploy"

# Conectar ao GitHub (substitua SEU_USUARIO):
git remote add origin https://github.com/SEU_USUARIO/vet-heart-care.git
git branch -M main
git push -u origin main
```

### Passo 4: Deploy no Streamlit Cloud (1 minuto)

1. Acesse: https://share.streamlit.io/
2. Faça login com GitHub
3. Clique em **"New app"**
4. Configure:
   - Repository: `SEU_USUARIO/vet-heart-care`
   - Branch: `main`
   - Main file: `streamlit_app.py`
5. Clique em **"Deploy!"**

✅ **Pronto!** Sua app estará online em ~2-3 minutos!

URL será tipo: `https://seu-usuario-vet-heart-care.streamlit.app`

---

## 📋 Checklist Antes do Deploy

- [ ] Template `Laudo Eco Modelo P.docx` está na pasta `heartcaresite/upload_folder/`
- [ ] Arquivo foi commitado no Git (verifique com `git status`)
- [ ] Testou localmente que funciona
- [ ] Executou `./setup-streamlit-cloud.sh` para preparar

---

## 🆘 Problemas?

### "Template não encontrado" em produção
**Solução:** Certifique-se de que o arquivo está commitado:
```bash
git add heartcaresite/upload_folder/Laudo\ Eco\ Modelo\ P.docx
git commit -m "Adicionar template"
git push
```

### App não inicia
**Solução:** Verifique os logs no Streamlit Cloud e certifique-se de que:
- `requirements.txt` está usando o otimizado
- Todos os arquivos necessários estão no repositório

---

**Mais detalhes? Veja DEPLOY.md completo!**

