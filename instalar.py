#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Instalador Automático - Vet Heart Care
Interface gráfica para instalação sem linha de comando
"""

import subprocess
import sys
import os
import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading

class InstaladorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🩺 Instalador Vet Heart Care")
        self.root.geometry("700x600")
        self.root.configure(bg="#f0f0f0")
        
        # Criar interface
        self.criar_interface()
        
    def criar_interface(self):
        # Título
        titulo = tk.Label(
            self.root,
            text="🩺 Vet Heart Care - Instalador",
            font=("Arial", 20, "bold"),
            bg="#f0f0f0",
            fg="#1f77b4"
        )
        titulo.pack(pady=20)
        
        # Instruções
        instrucoes = tk.Label(
            self.root,
            text="Este instalador irá configurar automaticamente o Vet Heart Care.\nClique em 'Instalar' para começar.",
            font=("Arial", 11),
            bg="#f0f0f0",
            justify="center"
        )
        instrucoes.pack(pady=10)
        
        # Área de log
        log_label = tk.Label(
            self.root,
            text="Log de Instalação:",
            font=("Arial", 10, "bold"),
            bg="#f0f0f0"
        )
        log_label.pack(pady=(20, 5), anchor="w", padx=20)
        
        self.log_text = scrolledtext.ScrolledText(
            self.root,
            height=20,
            width=80,
            font=("Courier", 9),
            bg="#ffffff",
            fg="#000000"
        )
        self.log_text.pack(pady=5, padx=20, fill="both", expand=True)
        
        # Botões
        botoes_frame = tk.Frame(self.root, bg="#f0f0f0")
        botoes_frame.pack(pady=20)
        
        self.btn_instalar = tk.Button(
            botoes_frame,
            text="▶ Instalar Agora",
            command=self.iniciar_instalacao,
            bg="#28a745",
            fg="white",
            font=("Arial", 12, "bold"),
            padx=20,
            pady=10,
            cursor="hand2"
        )
        self.btn_instalar.pack(side="left", padx=10)
        
        self.btn_fechar = tk.Button(
            botoes_frame,
            text="✖ Fechar",
            command=self.root.quit,
            bg="#dc3545",
            fg="white",
            font=("Arial", 12),
            padx=20,
            pady=10,
            cursor="hand2"
        )
        self.btn_fechar.pack(side="left", padx=10)
        
    def log(self, mensagem):
        """Adiciona mensagem ao log"""
        self.log_text.insert("end", mensagem + "\n")
        self.log_text.see("end")
        self.root.update()
        
    def verificar_python(self):
        """Verifica se Python está instalado"""
        try:
            resultado = subprocess.run(
                [sys.executable, "--version"],
                capture_output=True,
                text=True
            )
            versao = resultado.stdout.strip()
            self.log(f"✅ Python encontrado: {versao}")
            return True
        except Exception as e:
            self.log(f"❌ Erro ao verificar Python: {e}")
            messagebox.showerror("Erro", "Python não encontrado!\nPor favor, instale Python 3.8 ou superior.")
            return False
    
    def verificar_template(self):
        """Verifica se o template existe"""
        template_path = os.path.join(
            os.path.dirname(__file__),
            'heartcaresite',
            'upload_folder',
            'Laudo Eco Modelo P.docx'
        )
        if os.path.exists(template_path):
            self.log("✅ Template encontrado")
            return True
        else:
            self.log("⚠️  AVISO: Template não encontrado")
            self.log(f"   Caminho esperado: {template_path}")
            self.log("   A aplicação funcionará, mas não será possível gerar laudos até o template ser adicionado.")
            return False
    
    def criar_venv(self):
        """Cria ambiente virtual"""
        try:
            self.log("\n📦 Criando ambiente virtual...")
            subprocess.run(
                [sys.executable, "-m", "venv", "venv"],
                check=True,
                capture_output=True
            )
            self.log("✅ Ambiente virtual criado com sucesso")
            return True
        except subprocess.CalledProcessError as e:
            self.log(f"❌ Erro ao criar ambiente virtual: {e}")
            return False
    
    def instalar_dependencias(self):
        """Instala dependências"""
        try:
            self.log("\n📥 Instalando dependências...")
            self.log("   Isso pode levar alguns minutos...")
            
            # Determinar pip correto (dentro do venv se existir)
            if os.path.exists("venv/bin/pip"):
                pip_cmd = os.path.join(os.getcwd(), "venv", "bin", "pip")
            else:
                pip_cmd = [sys.executable, "-m", "pip"]
            
            # Usar pip do sistema ou do venv
            if isinstance(pip_cmd, str):
                cmd = [pip_cmd, "install", "-r", "requirements.txt"]
            else:
                cmd = pip_cmd + ["install", "-r", "requirements.txt"]
            
            processo = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
                universal_newlines=True
            )
            
            # Mostrar progresso
            for linha in processo.stdout:
                linha_limpa = linha.strip()
                if linha_limpa and ("Installing" in linha_limpa or "Collecting" in linha_limpa or "Successfully installed" in linha_limpa or "Requirement already satisfied" in linha_limpa):
                    self.log(f"   {linha_limpa[:70]}")  # Limitar tamanho da linha
            
            processo.wait()
            
            if processo.returncode == 0:
                self.log("✅ Dependências instaladas com sucesso")
                return True
            else:
                self.log("❌ Erro ao instalar dependências")
                return False
                
        except Exception as e:
            self.log(f"❌ Erro: {e}")
            return False
    
    def iniciar_instalacao(self):
        """Inicia processo de instalação em thread separada"""
        self.btn_instalar.config(state="disabled")
        self.log_text.delete(1.0, "end")
        
        thread = threading.Thread(target=self.executar_instalacao)
        thread.daemon = True
        thread.start()
    
    def executar_instalacao(self):
        """Executa instalação completa"""
        self.log("=" * 60)
        self.log("🩺 INSTALADOR VET HEART CARE")
        self.log("=" * 60)
        
        # Passo 1: Verificar Python
        self.log("\n📋 Passo 1: Verificando Python...")
        if not self.verificar_python():
            self.btn_instalar.config(state="normal")
            return
        
        # Passo 2: Verificar template
        self.log("\n📋 Passo 2: Verificando arquivos necessários...")
        self.verificar_template()
        
        # Passo 3: Criar ambiente virtual
        self.log("\n📋 Passo 3: Configurando ambiente...")
        if not os.path.exists("venv"):
            if not self.criar_venv():
                self.btn_instalar.config(state="normal")
                messagebox.showerror("Erro", "Não foi possível criar o ambiente virtual.")
                return
        
        # Passo 4: Instalar dependências
        self.log("\n📋 Passo 4: Instalando dependências Python...")
        if not self.instalar_dependencias():
            self.btn_instalar.config(state="normal")
            messagebox.showerror("Erro", "Erro ao instalar dependências.\nVerifique o log acima.")
            return
        
        # Instalação concluída
        self.log("\n" + "=" * 60)
        self.log("✅ INSTALAÇÃO CONCLUÍDA COM SUCESSO!")
        self.log("=" * 60)
        self.log("\n📝 Próximos passos:")
        self.log("   1. Para iniciar a aplicação, execute:")
        self.log("      python3 run_streamlit.py")
        self.log("\n   2. Ou use o script 'Iniciar_Aplicacao.command'")
        self.log("\n   3. A aplicação abrirá automaticamente no navegador")
        
        self.btn_instalar.config(state="normal")
        self.btn_instalar.config(text="✅ Instalação Concluída", state="disabled")
        
        messagebox.showinfo(
            "Instalação Concluída!",
            "Instalação realizada com sucesso!\n\n"
            "Para iniciar a aplicação, execute:\n"
            "python3 run_streamlit.py\n\n"
            "Ou use o arquivo 'Iniciar_Aplicacao.command'"
        )

def main():
    # Verificar se estamos no diretório correto
    if not os.path.exists("requirements.txt"):
        messagebox.showerror(
            "Erro",
            "Arquivo requirements.txt não encontrado!\n\n"
            "Certifique-se de executar este script na pasta raiz do projeto."
        )
        return
    
    root = tk.Tk()
    app = InstaladorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
