#!/bin/bash
# Script para verificar se o projeto está pronto para deploy

echo "🔍 Verificando preparação para deploy..."
echo ""

ERROS=0
AVISOS=0

# Verificar arquivo principal
echo -n "Verificando streamlit_app.py... "
if [ -f "streamlit_app.py" ]; then
    echo "✅"
    
    # Verificar se tem main()
    if grep -q "if __name__ == \"__main__\":" streamlit_app.py; then
        echo "   ✅ main() encontrada"
    else
        echo "   ⚠️  AVISO: main() não encontrada no final do arquivo"
        AVISOS=$((AVISOS + 1))
    fi
else
    echo "❌ NÃO ENCONTRADO!"
    ERROS=$((ERROS + 1))
fi

# Verificar EcoDataReferences
echo -n "Verificando EcoDataReferences.py... "
if [ -f "EcoDataReferences.py" ]; then
    echo "✅"
    
    # Verificar se está no git
    if git ls-files | grep -q "EcoDataReferences.py"; then
        echo "   ✅ Está no repositório Git"
    else
        echo "   ⚠️  AVISO: Arquivo existe mas não está no Git"
        echo "      Execute: git add EcoDataReferences.py"
        AVISOS=$((AVISOS + 1))
    fi
else
    echo "❌ NÃO ENCONTRADO!"
    ERROS=$((ERROS + 1))
fi

# Verificar requirements
echo -n "Verificando requirements.txt... "
if [ -f "requirements.txt" ]; then
    echo "✅"
    
    # Verificar dependências essenciais
    ESSENCIAIS=("streamlit" "pdfplumber" "python-docx" "pandas" "numpy")
    for dep in "${ESSENCIAIS[@]}"; do
        if grep -qi "$dep" requirements.txt; then
            echo "   ✅ $dep encontrado"
        else
            echo "   ⚠️  $dep não encontrado em requirements.txt"
            AVISOS=$((AVISOS + 1))
        fi
    done
    
    # Verificar se está no git
    if git ls-files | grep -q "requirements.txt"; then
        echo "   ✅ Está no repositório Git"
    else
        echo "   ⚠️  AVISO: requirements.txt não está no Git"
        AVISOS=$((AVISOS + 1))
    fi
elif [ -f "requirements-streamlit.txt" ]; then
    echo "⚠️  requirements.txt não encontrado, mas requirements-streamlit.txt existe"
    echo "   💡 Execute: cp requirements-streamlit.txt requirements.txt"
    AVISOS=$((AVISOS + 1))
else
    echo "❌ NÃO ENCONTRADO!"
    ERROS=$((ERROS + 1))
fi

# Verificar template
echo -n "Verificando template... "
TEMPLATE="heartcaresite/upload_folder/Laudo Eco Modelo P.docx"
if [ -f "$TEMPLATE" ]; then
    echo "✅"
    
    # Verificar tamanho
    SIZE=$(du -h "$TEMPLATE" | cut -f1)
    echo "   📦 Tamanho: $SIZE"
    
    # Verificar se está no git
    if git ls-files | grep -q "Laudo Eco Modelo P.docx"; then
        echo "   ✅ Está no repositório Git"
    else
        echo "   ⚠️  AVISO: Template não está no Git"
        echo "      Execute: git add -f \"$TEMPLATE\""
        AVISOS=$((AVISOS + 1))
    fi
    
    # Verificar se não está sendo ignorado
    if grep -q "Laudo Eco Modelo P.docx" .gitignore 2>/dev/null; then
        echo "   ⚠️  AVISO: Template pode estar no .gitignore"
        AVISOS=$((AVISOS + 1))
    fi
else
    echo "❌ NÃO ENCONTRADO!"
    echo "   Caminho esperado: $TEMPLATE"
    ERROS=$((ERROS + 1))
fi

# Verificar .gitignore
echo -n "Verificando .gitignore... "
if [ -f ".gitignore" ]; then
    echo "✅"
    
    # Verificar se template está sendo ignorado incorretamente
    if grep -q "^heartcaresite/upload_folder/.*\.docx" .gitignore && ! grep -q "!Laudo Eco Modelo P.docx" .gitignore; then
        echo "   ⚠️  AVISO: .gitignore pode estar ignorando o template"
        AVISOS=$((AVISOS + 1))
    fi
else
    echo "⚠️  .gitignore não encontrado (opcional mas recomendado)"
    AVISOS=$((AVISOS + 1))
fi

# Verificar estrutura de diretórios
echo ""
echo "📁 Verificando estrutura..."
if [ -d "heartcaresite" ]; then
    echo "   ✅ Diretório heartcaresite existe"
    if [ -d "heartcaresite/upload_folder" ]; then
        echo "   ✅ Diretório upload_folder existe"
    else
        echo "   ⚠️  Diretório upload_folder não encontrado"
        AVISOS=$((AVISOS + 1))
    fi
else
    echo "   ⚠️  Diretório heartcaresite não encontrado"
    AVISOS=$((AVISOS + 1))
fi

# Verificar imports no streamlit_app.py
echo ""
echo "🔍 Verificando imports..."
if [ -f "streamlit_app.py" ]; then
    if grep -q "from EcoDataReferences import" streamlit_app.py; then
        echo "   ✅ Import de EcoDataReferences OK"
    else
        echo "   ⚠️  Import de EcoDataReferences não encontrado"
        AVISOS=$((AVISOS + 1))
    fi
    
    if grep -q "import streamlit" streamlit_app.py; then
        echo "   ✅ Import do Streamlit OK"
    else
        echo "   ❌ Import do Streamlit não encontrado!"
        ERROS=$((ERROS + 1))
    fi
fi

# Resumo
echo ""
echo "=========================================="
if [ $ERROS -eq 0 ] && [ $AVISOS -eq 0 ]; then
    echo "✅ PROJETO PRONTO PARA DEPLOY!"
    echo "=========================================="
    echo ""
    echo "Próximos passos:"
    echo "1. git add ."
    echo "2. git commit -m 'Preparar para deploy'"
    echo "3. git push"
    echo "4. Fazer deploy no Streamlit Cloud"
    exit 0
elif [ $ERROS -eq 0 ]; then
    echo "⚠️  PROJETO QUASE PRONTO - $AVISOS AVISO(S)"
    echo "=========================================="
    echo ""
    echo "Corrija os avisos acima antes de fazer deploy."
    exit 0
else
    echo "❌ ERROS ENCONTRADOS: $ERROS"
    echo "⚠️  AVISOS: $AVISOS"
    echo "=========================================="
    echo ""
    echo "Corrija os erros acima antes de fazer deploy!"
    exit 1
fi


