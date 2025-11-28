#!/bin/bash
# Script para corrigir problemas comuns de deploy

echo "🔧 Corrigindo problemas de deploy..."
echo ""

# 1. Garantir que requirements.txt está correto
echo "1️⃣  Verificando requirements.txt..."
if [ ! -f "requirements.txt" ] && [ -f "requirements-streamlit.txt" ]; then
    echo "   📝 Copiando requirements-streamlit.txt para requirements.txt..."
    cp requirements-streamlit.txt requirements.txt
    echo "   ✅ requirements.txt criado"
fi

# 2. Garantir que EcoDataReferences.py está no Git
echo ""
echo "2️⃣  Verificando EcoDataReferences.py..."
if [ -f "EcoDataReferences.py" ]; then
    if ! git ls-files | grep -q "EcoDataReferences.py"; then
        echo "   ➕ Adicionando EcoDataReferences.py ao Git..."
        git add EcoDataReferences.py
        echo "   ✅ EcoDataReferences.py adicionado"
    else
        echo "   ✅ EcoDataReferences.py já está no Git"
    fi
else
    echo "   ❌ EcoDataReferences.py não encontrado!"
    echo "   Você precisa ter este arquivo para o app funcionar."
    exit 1
fi

# 3. Garantir que streamlit_app.py está no Git
echo ""
echo "3️⃣  Verificando streamlit_app.py..."
if [ -f "streamlit_app.py" ]; then
    if ! git ls-files | grep -q "streamlit_app.py"; then
        echo "   ➕ Adicionando streamlit_app.py ao Git..."
        git add streamlit_app.py
        echo "   ✅ streamlit_app.py adicionado"
    else
        echo "   ✅ streamlit_app.py já está no Git"
    fi
else
    echo "   ❌ streamlit_app.py não encontrado!"
    exit 1
fi

# 4. Garantir que requirements.txt está no Git
echo ""
echo "4️⃣  Verificando requirements.txt..."
if [ -f "requirements.txt" ]; then
    if ! git ls-files | grep -q "requirements.txt"; then
        echo "   ➕ Adicionando requirements.txt ao Git..."
        git add requirements.txt
        echo "   ✅ requirements.txt adicionado"
    else
        echo "   ✅ requirements.txt já está no Git"
    fi
else
    echo "   ❌ requirements.txt não encontrado!"
    exit 1
fi

# 5. Garantir que template está no Git (mesmo que grande)
echo ""
echo "5️⃣  Verificando template..."
TEMPLATE="heartcaresite/upload_folder/Laudo Eco Modelo P.docx"
if [ -f "$TEMPLATE" ]; then
    # Verificar se está sendo ignorado
    if grep -q "^heartcaresite/upload_folder/.*\.docx" .gitignore 2>/dev/null && ! grep -q "!Laudo Eco Modelo P.docx" .gitignore 2>/dev/null; then
        echo "   ⚠️  Template pode estar sendo ignorado pelo .gitignore"
        echo "   📝 Adicionando exceção no .gitignore..."
        
        # Adicionar exceção no final do .gitignore
        if ! grep -q "!heartcaresite/upload_folder/Laudo Eco Modelo P.docx" .gitignore 2>/dev/null; then
            echo "" >> .gitignore
            echo "# Exceção: Template necessário para o app" >> .gitignore
            echo "!heartcaresite/upload_folder/Laudo Eco Modelo P.docx" >> .gitignore
            echo "   ✅ Exceção adicionada no .gitignore"
        fi
    fi
    
    # Forçar adição do template
    if ! git ls-files | grep -q "Laudo Eco Modelo P.docx"; then
        echo "   ➕ Adicionando template ao Git (forçar)..."
        git add -f "$TEMPLATE"
        echo "   ✅ Template adicionado"
    else
        echo "   ✅ Template já está no Git"
    fi
    
    # Verificar tamanho
    SIZE=$(du -h "$TEMPLATE" | cut -f1)
    echo "   📦 Tamanho do template: $SIZE"
    if [ $(du -m "$TEMPLATE" | cut -f1) -gt 50 ]; then
        echo "   ⚠️  AVISO: Template é maior que 50MB, pode demorar para fazer push"
    fi
else
    echo "   ⚠️  AVISO: Template não encontrado em:"
    echo "      $TEMPLATE"
    echo "   O app funcionará, mas não será possível gerar laudos sem o template."
fi

# 6. Verificar .streamlit/config.toml (opcional mas recomendado)
echo ""
echo "6️⃣  Verificando configurações..."
if [ -d ".streamlit" ] && [ -f ".streamlit/config.toml" ]; then
    if ! git ls-files | grep -q ".streamlit/config.toml"; then
        echo "   ➕ Adicionando .streamlit/config.toml ao Git..."
        git add .streamlit/config.toml
        echo "   ✅ Config adicionada"
    else
        echo "   ✅ .streamlit/config.toml já está no Git"
    fi
else
    echo "   ℹ️  .streamlit/config.toml não encontrado (opcional)"
fi

# 7. Status do Git
echo ""
echo "📋 Status do Git:"
echo "=================="
git status --short | head -20

# 8. Verificar se tem mudanças para commit
echo ""
echo "📦 Preparando commit..."
MUDANCAS=$(git status --porcelain | wc -l | tr -d ' ')
if [ "$MUDANCAS" -gt 0 ]; then
    echo "   ✅ $MUDANCAS arquivo(s) para adicionar/commitar"
    echo ""
    read -p "   Deseja fazer commit e push agora? (s/N): " CONFIRMAR
    if [ "$CONFIRMAR" = "s" ] || [ "$CONFIRMAR" = "S" ]; then
        git add .
        git commit -m "Corrigir deploy - garantir todos arquivos essenciais"
        echo ""
        echo "   ✅ Commit criado!"
        echo ""
        read -p "   Deseja fazer push agora? (s/N): " PUSH_CONFIRMAR
        if [ "$PUSH_CONFIRMAR" = "s" ] || [ "$PUSH_CONFIRMAR" = "S" ]; then
            git push
            echo ""
            echo "   ✅ Push realizado!"
            echo ""
            echo "🎉 Agora vá no Streamlit Cloud e:"
            echo "   1. Clique em '⋮' (três pontos)"
            echo "   2. Selecione 'Reboot app'"
            echo "   3. Aguarde o redeploy"
        else
            echo ""
            echo "   ℹ️  Para fazer push manualmente:"
            echo "      git push"
        fi
    else
        echo ""
        echo "   ℹ️  Para fazer commit manualmente:"
        echo "      git add ."
        echo "      git commit -m 'Corrigir deploy'"
        echo "      git push"
    fi
else
    echo "   ✅ Nenhuma mudança pendente"
fi

echo ""
echo "=========================================="
echo "✅ Verificação completa!"
echo "=========================================="
echo ""
echo "📝 Próximos passos:"
echo "   1. Se fez push, reinicie o app no Streamlit Cloud"
echo "   2. Verifique os logs no Streamlit Cloud se ainda houver problemas"
echo "   3. Execute './verificar_deploy.sh' para verificar novamente"
echo ""


