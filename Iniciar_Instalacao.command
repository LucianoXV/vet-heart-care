#!/bin/bash
# Iniciar_Instalacao.command
# Este arquivo pode ser executado clicando duas vezes no Mac

# Obter o diretório do script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"

# Mensagem inicial
echo "🩺 Vet Heart Care - Instalador Automático"
echo "=========================================="
echo ""
echo "Este script irá instalar automaticamente todas as dependências."
echo "Por favor, aguarde..."
echo ""

# Verificar Python
echo "📋 Verificando Python..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 não encontrado!"
    echo "Por favor, instale Python 3.8 ou superior."
    echo ""
    echo "Você pode instalar via Homebrew:"
    echo "  brew install python3"
    echo ""
    read -p "Pressione ENTER para sair..."
    exit 1
fi

PYTHON_VERSION=$(python3 --version)
echo "✅ $PYTHON_VERSION encontrado"
echo ""

# Verificar se está no diretório correto
if [ ! -f "requirements.txt" ]; then
    echo "❌ Arquivo requirements.txt não encontrado!"
    echo "Certifique-se de executar este script na pasta raiz do projeto."
    read -p "Pressione ENTER para sair..."
    exit 1
fi

# Criar ambiente virtual se não existir
echo "📦 Configurando ambiente virtual..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    if [ $? -eq 0 ]; then
        echo "✅ Ambiente virtual criado"
    else
        echo "❌ Erro ao criar ambiente virtual"
        read -p "Pressione ENTER para sair..."
        exit 1
    fi
else
    echo "✅ Ambiente virtual já existe"
fi
echo ""

# Ativar ambiente virtual
echo "🔧 Ativando ambiente virtual..."
source venv/bin/activate
echo ""

# Atualizar pip
echo "📥 Atualizando pip..."
pip install --upgrade pip --quiet
echo "✅ pip atualizado"
echo ""

# Instalar dependências
echo "📥 Instalando dependências..."
echo "   Isso pode levar alguns minutos..."
echo ""
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo ""
    echo "=========================================="
    echo "✅ INSTALAÇÃO CONCLUÍDA COM SUCESSO!"
    echo "=========================================="
    echo ""
    echo "📝 Para iniciar a aplicação:"
    echo "   1. Execute: python3 run_streamlit.py"
    echo "   2. Ou use o arquivo 'Iniciar_Aplicacao.command'"
    echo ""
    echo "💡 Dica: Você pode dar um duplo clique em"
    echo "   'Iniciar_Aplicacao.command' para iniciar a aplicação."
    echo ""
else
    echo ""
    echo "❌ Erro durante a instalação"
    echo "Verifique as mensagens acima para mais detalhes"
fi

echo ""
read -p "Pressione ENTER para fechar..."
