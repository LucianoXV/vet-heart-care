# Instruções para Atualizar o Template Word

## 📝 Novos Campos Adicionados

Para que os novos campos funcionem corretamente no documento gerado, você precisa adicionar os seguintes placeholders no arquivo `Laudo Eco Modelo P.docx`:

### Novos Placeholders para Adicionar:

```
<frequencia_cardiaca>
<ritmo>
<description>
<report_date>
```

### Onde Adicionar no Template:

1. **Seção de Parâmetros Básicos** - Adicione próximo aos outros dados do animal:
   - `<frequencia_cardiaca>` - para a frequência cardíaca
   - `<ritmo>` - para o tipo de ritmo cardíaco

2. **Formato Sugerido no Template:**
   ```
   Frequência Cardíaca: <frequencia_cardiaca> bpm
   Ritmo: <ritmo>
   Descrição do Exame: <description>
   Data do Relatório: <report_date>
   ```

### 📋 Lista Completa de Placeholders Disponíveis:

```
<exam_date>          - Data do exame
<owner_name>         - Nome do proprietário
<species>            - Espécie do animal
<sex>                - Sexo do animal
<age>                - Idade
<weight>             - Peso
<ficha>              - Número da ficha
<breed>              - Raça
<animal_name>        - Nome do animal
<frequencia_cardiaca> - Frequência cardíaca (NOVO)
<ritmo>              - Ritmo cardíaco (NOVO)

<!-- Medidas Ecocardiográficas -->
<diastole_septo_IV>           - Diástole-Septo IV
<diastole_parede_post_VE>     - Diástole Parede Post VE
<diast_diametro_VE>           - Diást-diâmetro VE
<diametro_sist_VE>            - Diâmetro-síst VE
<encurtamento_fracional_VE>   - Encurtamento Fracional VE
<fracao_ejecao>               - Fração Ejeção
<diametro_interno_VE_diast_norm> - Diâmetro interno VE diást norm
<diametro_aortico>            - Diâmetro Aórtico
<diametro_AE>                 - Diâmetro AE
<diam_atrio_ao_esq>           - Diâm Átrio/Ao Esq
<vmax_va>                     - Vmáx VA
<gp_max_va>                   - GP máx VA
<vel_pico_pulmonar>           - Vel pico Pulmonar
<gradiente_pico_pulmonar>     - Gradiente pico Pulmonar
<vel_pico_mitral_e>           - Vel Pico Mitral Onda E
<vel_pico_mit_ond_a>          - Vel Pico Mit Ond A
<taxa_mitral_ea>              - Taxa Mitral E/A
<temp_desacel_onda_e_mitral>  - Temp Desacel Onda e Mitral
<temp_relax_isovol_mitral>    - Temp Relax Isovol Mitral
<temp_relax_isovol_e_mitral>  - Temp Relax Isovol E Mitral
<onda_e_lateral>              - Onda E' Lateral
<onda_a_lateral>              - Onda A' Lateral
<razao_e_a_lat>               - Razão E'/A' Lat
<tapse>                       - TAPSE
<tapse_resultado>             - Resultado TAPSE (Normal/Diminuido/Aumentado)
<mapse>                       - MAPSE

<!-- Resultados de Referência -->
<diam_aortico_result>         - Resultado Diâmetro Aórtico
<diastole_septo_iv_result>    - Resultado Diástole-Septo IV
<diam_ae_result>              - Resultado Diâmetro AE
<diast_par_post_ve_result>    - Resultado Diástole Parede Post VE
<diast_diametro_VE_result>    - Resultado Diást-diâmetro VE
<dia_sist_ve_result>          - Resultado Diâmetro-síst VE

<!-- Observações -->
<notes>                       - Observações
<conclusion>                  - Conclusões
```

## 🔧 Como Atualizar o Template:

1. Abra o arquivo `heartcaresite/upload_folder/Laudo Eco Modelo P.docx`
2. Adicione os novos campos onde desejar no documento
3. Use os placeholders `<frequencia_cardiaca>` e `<ritmo>`
4. Salve o arquivo
5. Teste a geração de um novo laudo

## 📊 Seção de Referências Calculadas

Os resultados das referências médicas são calculados automaticamente e substituídos nos placeholders correspondentes. Eles aparecem como:
- "Normal" - quando dentro dos valores de referência
- "Diminuido" - quando abaixo dos valores de referência  
- "Aumentado" - quando acima dos valores de referência

## ✅ Teste a Atualização:

1. Execute o Streamlit app: `python3 run_streamlit.py`
2. Faça upload de um PDF
3. Preencha os novos campos na confirmação
4. Gere o documento e verifique se os novos campos aparecem corretamente
