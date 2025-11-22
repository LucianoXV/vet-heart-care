#!/bin/bash
# Script para preparar projeto para deploy no Streamlit Cloud

echo "🚀 Preparando projeto para Streamlit Cloud..."
echo ""

# Verificar se requirements-streamlit.txt existe
if [ ! -f "requirements-streamlit.txt" ]; then
    echo "❌ Arquivo requirements-streamlit.txt não encontrado!"
    exit 1
fi

# Fazer backup do requirements.txt original
if [ -f "requirements.txt" ] && [ ! -f "requirements-original.txt" ]; then
    echo "📦 Fazendo backup do requirements.txt original..."
    cp requirements.txt requirements-original.txt
fi

# Copiar requirements otimizado
echo "📝 Copiando requirements otimizado..."
cp requirements-streamlit.txt requirements.txt

# Verificar se o template existe
TEMPLATE_PATH="heartcaresite/upload_folder/Laudo Eco Modelo P.docx"
if [ ! -f "$TEMPLATE_PATH" ]; then
    echo "⚠️  AVISO: Template não encontrado em:"
    echo "   $TEMPLATE_PATH"
    echo ""
    echo "   Certifique-se de adicionar o template antes de fazer deploy!"
else
    echo "✅ Template encontrado"
fi

# Verificar se streamlit_app.py existe
if [ ! -f "streamlit_app.py" ]; then
    echo "❌ streamlit_app.py não encontrado!"
    exit 1
fi

echo ""
echo "✅ Projeto preparado para Streamlit Cloud!"
echo ""
echo "📝 Próximos passos:"
echo "   1. git add ."
echo "   2. git commit -m 'Preparar para deploy no Streamlit Cloud'"
echo "   3. git push"
echo "   4. Acesse https://share.streamlit.io/ e faça deploy"
echo ""

