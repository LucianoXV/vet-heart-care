from django import forms
from django.core.validators import FileExtensionValidator

class CustomTextInput(forms.TextInput):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('attrs', {}).update({'class': 'uk-input uk-form-width-medium uk-form-small'})
        super().__init__(*args, **kwargs)

class CustomTextAreaInput(forms.Textarea):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('attrs', {}).update({'class': 'uk-textarea uk-form-width-large uk-form-small'})
        super().__init__(*args, **kwargs)

class CustomEmailInput(forms.EmailInput):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('attrs', {}).update({'class': 'uk-input uk-form-width-large uk-form-small'})
        super().__init__(*args, **kwargs)

class CustomDateInput(forms.DateInput):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('attrs', {}).update({'class': 'uk-input uk-form-width-medium uk-form-small'})
        self.input_type = 'date'  # Set the input type as 'date'
        super().__init__(*args, **kwargs)


class PDFUploadForm(forms.Form):
    pdf_file = forms.FileField(label='Selecione o arquivo PDF', validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    def clean_pdf_file(self):
        file = self.cleaned_data['pdf_file']
        if file:
            # Check if the uploaded file's format is not PDF
            if not file.name.endswith('.pdf'):
                raise forms.ValidationError('Please upload a PDF file.')
        return file

class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)

class DataConfirmationForm(forms.Form):
    date_of_exam = forms.DateField(label='Data do Exame', input_formats=['%d/%m/%Y'],required=False, widget=CustomTextInput())

    owner_name = forms.CharField(label="Tutor", max_length=100, required=False, widget=CustomTextInput())
    email = forms.EmailField(label="Email", required=False, widget=CustomEmailInput())
    phone = forms.CharField(label="Phone", required=False, widget=CustomTextInput())
    address = forms.CharField(label="Address", required=False, widget=CustomTextInput())

    animal_name = forms.CharField(label="Nome do animal", max_length=100, required=False, widget=CustomTextInput())
    sex = forms.CharField(label="Sexo", max_length=100, required=False, widget=CustomTextInput()) 
    species = forms.CharField(label="Especie", max_length=100, required=False, widget=CustomTextInput())
    age = forms.CharField(label="Idade", max_length=100, required=False, widget=CustomTextInput())
    breed = forms.CharField(label="Raça", max_length=100, required=False, widget=CustomTextInput())
    
    weight = forms.CharField(label="Peso", max_length=100, required=False, widget=CustomTextInput())
    record_number = forms.IntegerField(label="Ficha n", required=False, widget=CustomTextInput())
    place = forms.CharField(label="Local", max_length=100, required=False, widget=CustomTextInput())

    #tapse = forms.DecimalField(label="Tapse", max_digits=5, decimal_places=2, required=False)
    #tapse_resultado = forms.CharField(label="Tapse resultado", max_length=100, required=False)
    fup_date = forms.DateField(label='Data de Acompanhamento', input_formats=['%d/%m/%Y'],required=False, widget=CustomTextInput())
    notes = forms.CharField(label="Observações", widget=CustomTextAreaInput(), required=False)
    conclusion = forms.CharField(label="Conclusões", widget=CustomTextAreaInput(), required=False)

