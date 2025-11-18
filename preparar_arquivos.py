#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para preparar arquivos para execução no Mac
Torna os arquivos .command e .py executáveis
"""

import os
import stat

def tornar_executavel(arquivo):
    """Torna um arquivo executável"""
    if not os.path.exists(arquivo):
        print(f"⚠️  Arquivo não encontrado: {arquivo}")
        return False
    
    try:
        st = os.stat(arquivo)
        os.chmod(arquivo, st.st_mode | stat.S_IEXEC)
        print(f"✅ {arquivo} agora é executável")
        return True
    except Exception as e:
        print(f"❌ Erro ao tornar {arquivo} executável: {e}")
        return False

def main():
    print("🔧 Preparando arquivos para execução no Mac...")
    print("=" * 50)
    print("")
    
    arquivos = [
        "Iniciar_Instalacao.command",
        "Iniciar_Aplicacao.command",
        "instalar.py",
        "run_streamlit.py"
    ]
    
    sucesso = 0
    total = len(arquivos)
    
    for arquivo in arquivos:
        if tornar_executavel(arquivo):
            sucesso += 1
    
    print("")
    print("=" * 50)
    if sucesso == total:
        print(f"✅ Todos os {total} arquivos estão prontos!")
    else:
        print(f"⚠️  {sucesso} de {total} arquivos preparados")
    
    print("")
    print("📝 Próximos passos:")
    print("   1. Para instalar: execute 'instalar.py' ou 'Iniciar_Instalacao.command'")
    print("   2. Para iniciar: execute 'Iniciar_Aplicacao.command'")
    print("")

if __name__ == "__main__":
    main()
