import pdfplumber
from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter
import io
import os
import django
import sys
from .models import Owner
#from heartcaresite.models import Owner, Pet, CardiacData


#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vetproject.settings")  # Replace with your project's settings module
#django.setup()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python ReadPDF_WriteDB.py <file_path>")
    else:
        file_path = sys.argv[1]
        # Process the file based on the file path
        print(f"Processing file: {file_path}")
        

# Function to extract table data from a PDF
def extract_table_from_pdf(pdf_file):
    table_data = []
    
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            # Extract table data from the page, if any
            tables = page.extract_tables()
            for table in tables:
                table_data.extend(table)
                
    return table_data

# Provide the path to the PDF file you want to extract table data from
pdf_file_path = 'NENI__CAN_IZAURA__2023-10-18_09_46_49.pdf'

table_data = extract_table_from_pdf(file_path)

# Initialize variables
owner_name = animal_name = breed = sex = weight = date_of_exam = operator_name = description = report_date = None
diastole_septo_iv = ventriculo_esq = diast_diad_ve = diast_par_post_ve = None
dia_sist_ve = frac_ejecao = massa_ve = indice_massa_ve = None
diad_interno_ve_diast_norm = dia_interno_ve_sist_norm = None
espessura_relat_parede = tricuspid = tapse = doppler = None
aorta = vel_pico_va = gp_max_va = veloc_pico_mit_onda_e = veloc_pico_mit_ond_a = None
grad_pico_mit_e = grad_pico_mitral_a = mtp_mitral = taxa_mitral_e_a = None
temp_desacel_onda_e_mitral = temp_relax_isovol_mitral = temp_relax_isovol_e_mitral = None
regurgitacao_mitral = vel_reg_mit = grad_reg_mitral = dpdt = None
regurgitacao_tric = vel_reg_tric = grad_reg_tric = arteria_pulmonar = None
vel_pico_pulmonar = gradiente_pico_pulmonar = tdi_mitral = onda_e_lateral = onda_a_lateral = None
razao_ee_lat = razao_ee_lat = pressao_cap_pulmonar = vel_pico_mit_ond_e = pressao_cap_pulmonar = None
aorta_atrio_esq = diam_aortico = diam_ae = dia_esfericidade = diad_diam_ve = None

# Process the data
for row in table_data:
    print (row)
    for i in range(0, len(row), 1):
        if row[i] is not None and row[i] != '':
            key = row[i].strip()
            
            value = row[i + 1].strip() if i + 1 < len(row) and row[i + 1] is not None else None
            value2 = row[i + 2].strip() if i + 2 < len(row) and row[i + 2] is not None else None

            if key == 'Nome proprietário':
                owner_name = value
            elif key == 'Nome do animal':
                animal_name = value
            elif key == 'Raça':
                breed = value
            elif key == 'Sexo':
                sex = value
            elif key == 'Peso':
                weight = value
            elif key == 'Data do exame':
                date_of_exam = value
            elif key == 'Operador':
                operator_name = value
            elif key == 'Descrição do exame':
                description = value
            elif key == 'Data do relatório':
                report_date = value
            elif key == 'Diástole-Septo IV':
                diastole_septo_iv = value + " " + value2
            elif key == 'Ventrículo esq':
                ventriculo_esq = value
            elif key == 'Diást-diâmetro VE':
                diast_diad_ve = value + " " + value2
            elif key == 'Diástole Parede Post VE':
                diast_par_post_ve = value + " " + value2
            elif key == 'Diâmetro-síst VE':
                dia_sist_ve = value
            elif key == 'Fração Ejeção':
                frac_ejecao = value
            elif key == 'Massa VE':
                massa_ve = value
            elif key == 'Índice Massa VE':
                indice_massa_ve = value
            elif key == 'Diâmetro interno VE diást norm':
                diad_interno_ve_diast_norm = value
            elif key == 'Diâmetro interno VE sist norm':
                dia_interno_ve_sist_norm = value
            elif key == 'Espessura relativa da parede':
                espessura_relat_parede = value
            elif key == 'Tricúspid':
                tricuspid = value
            elif key == 'TAPSE':
                tapse = value
            elif key == 'Doppler':
                doppler = value
            elif key == 'Aorta':
                aorta = value
            elif key == 'Vmáx VA':
                vel_pico_va = value
            elif key == 'GP máx VA':
                gp_max_va = value
            elif key == 'Vel Pico Mitral Onda E':
                veloc_pico_mit_onda_e = value
            elif key == 'Vel Pico Mit Ond A':
                veloc_pico_mit_ond_a = value
            elif key == 'Grad Pico Mit (E)':
                grad_pico_mit_e = value
            elif key == 'Gtad Pico Mitral (A)':
                grad_pico_mitral_a = value
            elif key == 'MTP Mitral':
                mtp_mitral = value
            elif key == 'Taxa Mitral E/A':
                taxa_mitral_e_a = value
            elif key == 'Temp Desacel Onda e Mitral':
                temp_desacel_onda_e_mitral = value
            elif key == 'Temp Relax Isovol Mitral':
                temp_relax_isovol_mitral = value
            elif key == 'Temp Relax Isovol E Mitral':
                temp_relax_isovol_e_mitral = value
            elif key == 'Regurgitação Mitral':
                regurgitacao_mitral = value
            elif key == 'Velocidade Reg Mit':
                vel_reg_mit = value
            elif key == 'Gradiente Reg Mitral':
                grad_reg_mitral = value
            elif key == 'dP/dt':
                dpdt = value
            elif key == 'Regurgitação Tric':
                regurgitacao_tric = value
            elif key == 'Vel Reg Tric':
                vel_reg_tric = value
            elif key == 'Grad Reg Tric':
                grad_reg_tric = value
            elif key == 'Artéria Pulmonar':
                arteria_pulmonar = value
            elif key == 'Vel pico Pulmonar':
                vel_pico_pulmonar = value
            elif key == 'Gradiente pico Pulmonar':
                gradiente_pico_pulmonar = value
            elif key == 'TDI Mitral':
                tdi_mitral = value
            elif key == 'Onda E\' Lateral':
                onda_e_lateral = value
            elif key == 'Onda A\' Lateral':
                onda_a_lateral = value
            elif key == 'Razão E’/A\' Lat':
                razao_ee_lat = value
            elif key == 'Pressão capilar pulmonar':
                pressao_cap_pulmonar = value
            elif key == 'Vel Pico Mitral Onda E':
                vel_pico_mit_ond_e = value
            elif key == 'Pressão capilar pulmonar':
                pressao_cap_pulmonar = value
            elif key == 'Aorta/átrio esq':
                aorta_atrio_esq = value
            elif key == 'Diâmetro Aórtico':
                diam_aortico = value
            elif key == 'Diâmetro AE':
                diam_ae = value
            elif key == 'Diâm Átrio/Ao Esq':
                dia_esfericidade = value
            elif key == 'Índice de esfericidade':
                diad_diam_ve = value

# Print the extracted values
print(f"Owner Name: {owner_name}")
print(f"Animal Name: {animal_name}")
print(f"Breed: {breed}")
print(f"Sex: {sex}")
print(f"Weight: {weight}")
print(f"Date of Exam: {date_of_exam}")
print(f"Operator Name: {operator_name}")
print(f"Description of Exam: {description}")
print(f"Report Date: {report_date}")
print(f"Diástole-Septo IV: {diastole_septo_iv}")
print(f"Ventrículo esq: {ventriculo_esq}")
print(f"Diást-diâmetro VE: {diast_diad_ve}")
print(f"Diástole Parede Post VE: {diast_par_post_ve}")
print(f"Diâmetro-síst VE: {dia_sist_ve}")
print(f"Fração Ejeção: {frac_ejecao}")
print(f"Massa VE: {massa_ve}")
print(f"Índice Massa VE: {indice_massa_ve}")
print(f"Diâmetro interno VE diást norm: {diad_interno_ve_diast_norm}")
print(f"Diâmetro interno VE sist norm: {dia_interno_ve_sist_norm}")
print(f"Espessura relativa da parede: {espessura_relat_parede}")
print(f"Tricúspid: {tricuspid}")
print(f"TAPSE: {tapse}")
print(f"Doppler: {doppler}")
print(f"Aorta: {aorta}")
print(f"Vmáx VA: {vel_pico_va}")
print(f"GP máx VA: {gp_max_va}")
print(f"Vel Pico Mitral Onda E: {veloc_pico_mit_onda_e}")
print(f"Vel Pico Mit Ond A: {veloc_pico_mit_ond_a}")
print(f"Grad Pico Mit (E): {grad_pico_mit_e}")
print(f"Gtad Pico Mitral (A): {grad_pico_mitral_a}")
print(f"MTP Mitral: {mtp_mitral}")
print(f"Taxa Mitral E/A: {taxa_mitral_e_a}")
print(f"Temp Desacel Onda e Mitral: {temp_desacel_onda_e_mitral}")
print(f"Temp Relax Isovol Mitral: {temp_relax_isovol_mitral}")
print(f"Temp Relax Isovol E Mitral: {temp_relax_isovol_e_mitral}")
print(f"Regurgitação Mitral: {regurgitacao_mitral}")
print(f"Velocidade Reg Mit: {vel_reg_mit}")
print(f"Gradiente Reg Mitral: {grad_reg_mitral}")
print(f"dP/dt: {dpdt}")
print(f"Regurgitação Tric: {regurgitacao_tric}")
print(f"Vel Reg Tric: {vel_reg_tric}")
print(f"Grad Reg Tric: {grad_reg_tric}")
print(f"Arteria Pulmonar: {arteria_pulmonar}")
print(f"Vel pico Pulmonar: {vel_pico_pulmonar}")
print(f"Gradiente pico Pulmonar: {gradiente_pico_pulmonar}")
print(f"TDI Mitral: {tdi_mitral}")
print(f"Onda E' Lateral: {onda_e_lateral}")
print(f"Onda A' Lateral: {onda_a_lateral}")
print(f"Razão E’/A' Lat: {razao_ee_lat}")
print(f"Razão E/E' Lat: {razao_ee_lat}")
print(f"Pressão capilar pulmonar: {pressao_cap_pulmonar}")
print(f"Vel Pico Mitral Onda E: {vel_pico_mit_ond_e}")
print(f"Pressão capilar pulmonar: {pressao_cap_pulmonar}")
print(f"Aorta/átrio esq: {aorta_atrio_esq}")
print(f"Diâmetro Aórtico: {diam_aortico}")
print(f"Diâmetro AE: {diam_ae}")
print(f"Diâm Átrio/Ao Esq: {dia_esfericidade}")
print(f"Índice de esfericidade: {diad_diam_ve}")

# Writing the new Formatting file
