# Vet Heart Care - Sistema de Laudos (Streamlit)

Este é uma interface moderna e intuitiva para o sistema de geração de laudos ecocardiográficos veterinários, desenvolvida com Streamlit.

## 🚀 Como Executar

### Método 1: Script Automático (Recomendado)
```bash
python run_streamlit.py
```

### Método 2: Comando Direto
```bash
streamlit run streamlit_app.py
```

### Método 3: Instalação Manual
```bash
# Instalar Streamlit se necessário
pip install streamlit>=1.28.0

# Executar a aplicação
streamlit run streamlit_app.py --server.port 8501
```

## 📋 Funcionalidades

### 1. Upload de PDF
- Interface drag-and-drop para upload de relatórios ecocardiográficos
- Extração automática de dados de tabelas PDF usando pdfplumber
- Prévia dos dados extraídos antes da confirmação

### 2. Confirmação de Dados
- Interface intuitiva para revisão e edição dos dados extraídos
- Campos organizados por categoria (informações do animal, proprietário, dados ecocardiográficos)
- Cálculo automático de referências médicas baseadas no peso do animal

### 3. Geração de Laudo
- Criação automática de documento Word (.docx) usando template
- Substituição de placeholders com dados do exame
- Download direto do laudo gerado
- Opção de gerar novo laudo

## 🏗️ Arquitetura

### Componentes Principais
- **streamlit_app.py**: Aplicação principal Streamlit
- **EcoDataReferences.py**: Cálculos de referências médicas (mantido do Django)
- **run_streamlit.py**: Script de inicialização
- **heartcaresite/upload_folder/Laudo Eco Modelo P.docx**: Template do documento

### Fluxo de Dados
1. **Upload**: PDF → Extração com pdfplumber → Processamento de dados
2. **Confirmação**: Interface de edição → Validação → Cálculo de referências
3. **Geração**: Template Word → Substituição de placeholders → Download

## 🔧 Dependências

As principais dependências são:
- `streamlit>=1.28.0`: Framework web
- `pdfplumber`: Extração de dados de PDF
- `python-docx`: Manipulação de documentos Word
- `pandas`: Processamento de dados
- `numpy`: Cálculos numéricos

Todas as dependências estão listadas em `requirements.txt`.

## 📁 Estrutura de Arquivos

```
vetproject/
├── streamlit_app.py              # Aplicação principal Streamlit
├── run_streamlit.py              # Script de inicialização
├── README_STREAMLIT.md           # Este arquivo
├── requirements.txt              # Dependências Python
├── EcoDataReferences.py          # Cálculos de referências médicas
└── heartcaresite/
    └── upload_folder/
        └── Laudo Eco Modelo P.docx  # Template do documento
```

## 🎯 Vantagens da Interface Streamlit

### Comparado ao Django Original:
- ✅ **Interface mais intuitiva**: Drag-and-drop, navegação por etapas
- ✅ **Visual moderno**: Design responsivo e profissional
- ✅ **Feedback visual**: Spinners, barras de progresso, notificações
- ✅ **Menos complexidade**: Sem necessidade de configuração de banco de dados
- ✅ **Deploy fácil**: Execução simples com um comando
- ✅ **Desenvolvimento rápido**: Iteração mais rápida

### Mantém Funcionalidades Originais:
- ✅ **Lógica de negócio**: Todos os cálculos de referência médica preservados
- ✅ **Extração de PDF**: Mesmo processo de extração de dados
- ✅ **Geração de documento**: Mesmo template e processo de substituição
- ✅ **Validações**: Mesmas validações de dados

## 🚨 Importante

### Template Necessário
Certifique-se de que o arquivo `Laudo Eco Modelo P.docx` existe em:
```
heartcaresite/upload_folder/Laudo Eco Modelo P.docx
```

### Porta Padrão
A aplicação roda na porta 8501 por padrão. Se estiver em uso, use:
```bash
streamlit run streamlit_app.py --server.port 8502
```

### Dados de Referência
O sistema usa cálculos simplificados para TAPSE (não conecta ao PostgreSQL como no Django original). Para produção, considere implementar a conexão com banco de dados se necessário.

## 🆘 Solução de Problemas

### Erro: "Template não encontrado"
- Verifique se o arquivo `Laudo Eco Modelo P.docx` está na pasta correta
- Certifique-se de que o arquivo não está corrompido

### Erro: "Streamlit não encontrado"
```bash
pip install streamlit>=1.28.0
```

### Erro: "PDF não pode ser processado"
- Verifique se o PDF contém tabelas com dados
- Teste com um PDF diferente
- Certifique-se de que o PDF não está protegido por senha

### Porta em uso
```bash
streamlit run streamlit_app.py --server.port 8502
```

## 📞 Suporte

Para dúvidas ou problemas:
1. Verifique este README
2. Consulte os logs de erro no terminal
3. Teste com arquivos PDF diferentes
4. Verifique se todas as dependências estão instaladas

