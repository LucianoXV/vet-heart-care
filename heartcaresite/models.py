from django.db import models

class Owner(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    rec_date = models.DateTimeField("record date published", null=True, blank=True)
    
    def __str__(self):
        return self.name

class Pet(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    breed = models.CharField(max_length=255, null=True, blank=True)
    species = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=255, null=True, blank=True)
    weight = models.CharField(max_length=255, null=True, blank=True)
    fup_date = models.DateTimeField("follow up date", null=True, blank=True)
    # Add other fields as needed
    rec_date = models.DateTimeField("record date published")

    def __str__(self):
        return self.name

class CardiacData(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)  # Assuming you have a Pet model defined
    weight = models.CharField(max_length=255, null=True, blank=True)
    exam_date = models.DateField(null=True, blank=True)
    operator = models.CharField(max_length=255, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    conclusion = models.TextField(null=True, blank=True)
    doctor_name = models.CharField(max_length=255, null=True, blank=True)

    diastole_septo_iv = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    diast_par_post_ve = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    diast_diad_ve = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    dia_sist_ve = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    encurtamento_frac_VE = models.DecimalField(max_digits=3, decimal_places=0, null=True, blank=True)
    frac_ejecao = models.DecimalField(max_digits=3, decimal_places=0, null=True, blank=True)
    diad_interno_ve_diast_norm = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    diam_aortico = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    diam_ae = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    diam_atrio_ao_esq = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    vel_pico_va = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    gp_max_va = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    vel_pico_pulmonar = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    gradiente_pico_pulmonar = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    veloc_pico_mit_onda_e = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    veloc_pico_mit_ond_a = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    taxa_mitral_e_a = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    temp_desacel_onda_e_mitral = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    temp_relax_isovol_mitral = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    temp_relax_isovol_e_mitral = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    onda_e_lateral = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    onda_a_lateral = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    razao_ee_lat= models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    tapse = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    tapse_resultado = models.CharField(max_length=255, null=True, blank=True)
    
    # Add other fields as needed
    rec_date = models.DateTimeField("record date published")
    
    def __str__(self):
        return f"Cardiac Data for {self.pet.name}"

class Tapse(models.Model):
    species = models.CharField(max_length=255)
    weight = models.DecimalField(max_digits=10,decimal_places=1)
    weight_metric = models.CharField(max_length=255)
    min = models.DecimalField(max_digits=3, decimal_places=1)
    max = models.DecimalField(max_digits=3, decimal_places=1)
    def __str__(self):
        return self.name