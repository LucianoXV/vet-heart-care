#!/bin/bash
# Iniciar_Aplicacao.command
# Execute este arquivo para iniciar a aplicação

# Obter o diretório do script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"

clear
echo "🩺 Vet Heart Care - Sistema de Laudos"
echo "======================================"
echo ""

# Verificar se o ambiente virtual existe
if [ ! -d "venv" ]; then
    echo "❌ Ambiente virtual não encontrado!"
    echo ""
    echo "Por favor, execute primeiro o instalador:"
    echo "  - 'instalar.py' (interface gráfica)"
    echo "  - ou 'Iniciar_Instalacao.command'"
    echo ""
    read -p "Pressione ENTER para sair..."
    exit 1
fi

# Ativar ambiente virtual
echo "🔧 Ativando ambiente..."
source venv/bin/activate

# Verificar Streamlit
echo "📋 Verificando dependências..."
if ! python3 -c "import streamlit" 2>/dev/null; then
    echo "❌ Streamlit não encontrado!"
    echo ""
    echo "Por favor, execute primeiro o instalador:"
    echo "  - 'instalar.py' (interface gráfica)"
    echo "  - ou 'Iniciar_Instalacao.command'"
    echo ""
    read -p "Pressione ENTER para sair..."
    exit 1
fi

echo "✅ Tudo pronto!"
echo ""
echo "🚀 Abrindo aplicação no navegador..."
echo ""
echo "   A aplicação será aberta automaticamente."
echo "   Para parar a aplicação, feche esta janela"
echo "   ou pressione Ctrl+C"
echo ""
echo "======================================"
echo ""

# Verificar template
TEMPLATE_PATH="heartcaresite/upload_folder/Laudo Eco Modelo P.docx"
if [ ! -f "$TEMPLATE_PATH" ]; then
    echo "⚠️  AVISO: Template não encontrado em:"
    echo "   $TEMPLATE_PATH"
    echo ""
    echo "   A aplicação funcionará, mas você não poderá"
    echo "   gerar laudos até adicionar o template."
    echo ""
    sleep 3
fi

# Iniciar aplicação
python3 run_streamlit.py

# Mensagem ao sair
echo ""
echo "👋 Aplicação encerrada."
read -p "Pressione ENTER para fechar..."
