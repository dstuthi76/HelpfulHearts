from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
STATE_CHOICES = (
    ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'),
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chhattisgarh', 'Chhattisgarh'),
    ('Goa', 'Goa'),
    ('Gujarat', 'Gujarat'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jammu and Kashmir', 'Jammu and Kashmir'),
    ('Jharkhand', 'Jharkhand'),
    ('Karnataka', 'Karnataka'),
    ('Kerala', 'Kerala'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Telangana', 'Telangana'),
    ('Tripura', 'Tripura'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('Uttarakhand', 'Uttarakhand'),
    ('West Bengal', 'West Bengal'),
)


CATEGORY_CHOICES = (
    ('drops', 'Drops'),
    ('Capsules', 'Capsules'),
    ('injections', 'injections'),
    ('general medicine', 'General medicine'),

)


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=100)
    product_photo = models.ImageField(upload_to='product-img')

    def __str__(self):
        return str(self.id)


CATEGORY1_CHOICES = (
    ('cardiologist', 'cardiologist'),
    ('General Physician', 'General Physician'),
    ('allergist', 'allergist'),
    ('anesthesiologist', 'anesthesiologist'),
    ('dentist', 'dentist'),
    ('dermatologist', 'dermatologist'),
    ('fertility specialist', 'fertility specialist'),
    ('massage therapist', 'massage therapist'),
    ('neurologist', 'neurologist'),
    ('pediatrician', 'pediatrician'),
    ('radiologist', 'radiologist'),
)


class Doctors(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor_name = models.CharField(max_length=100)
    consultant_fee = models.FloatField()
    description = models.TextField()
    Location = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=50)
    specialisation = models.CharField(choices=CATEGORY1_CHOICES, max_length=35)
    Google_meet = models.TextField(default='')
    doctor_photo = models.ImageField(upload_to='doctor-img')

    def __str__(self):
        return str(self.id)




STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('on the way', 'on the way'),
    ('Cancel', 'Cancel')
)


STATUS1_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('on the way', 'on the way'),
    ('Cancel', 'Cancel')
)
STATUS10_CHOICES = (
    ('Gym','Gym'),
    ('Hospital','Hospital'),
    ('Yoga Center','Yoga Center'),
    ('Fitness Studios','Fitness Studios'),
    ('Wellness Center','Wellness Center'),
    ('Nutritionists','Nutritionists'),
    ('Physiotherapy Center','Physiotherapy Center'),
)


class Hospitals(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    Phone = models.IntegerField()
    City = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    Location = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=STATUS10_CHOICES)
    Hospital_photo = models.ImageField(upload_to='Hospital-img')


    def __str__(self):
        return str(self.id)


STATUS2_CHOICES = (
    ('Lose Weight','Lose Weight'),
    ('Maintain','Maintain'),
    ('Build Muscle','Build Muscle')
)

STATUS3_CHOICES = (
    ('Low','Low'),
    ('Medium','Medium'),
    ('High','High')
)

STATUS4_CHOICES = (
    ('Lightly Active','Lightly Active'),
    ('Moderately Active','Moderately Active'),
    ('Highly Active','Highly Active'),
    ('Extremely Active','Extremely Active'),
)

STATUS5_CHOICES = (
    ('Anything','Anything'),
    ('Paleo','Paleo'),
    ('Vegetarian','Vegetarian'),
    ('Vegan','Vegan'),
    ('Ketogenic','Ketogenic'),
    ('Mediterranean','Mediterranean'),
)


class DietPlan1(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    Age = models.IntegerField()
    Goal = models.CharField(choices=STATUS2_CHOICES, max_length=50)
    Bodyfat = models.CharField(choices=STATUS3_CHOICES, max_length=50)
    Activity_level = models.CharField(choices=STATUS4_CHOICES, max_length=50)
    Primary_Diet = models.CharField(choices=STATUS5_CHOICES, max_length=50)
    Diet_photo = models.ImageField(upload_to='Diet-img')



    def __str__(self):
        return str(self.id)

STATUS22_CHOICES = (
    ('U.S.Stanndard','U.S.Stanndard'),
    ('Metric','Metric'),
)

STATUS33_CHOICES = (
    ('Male','Male'),
    ('Female','Female'),
)


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    Goal = models.CharField(choices=STATUS2_CHOICES, max_length=50)
    units =models.CharField(choices=STATUS22_CHOICES, max_length=50)
    gender = models.CharField(choices=STATUS33_CHOICES, max_length=50)
    height_feet = models.IntegerField()
    height_inch = models.IntegerField()
    weight =models.FloatField()
    Age =models.IntegerField()
    Bodyfat = models.CharField(choices=STATUS3_CHOICES, max_length=50)
    Activity_level = models.CharField(choices=STATUS4_CHOICES, max_length=50)
    Primary_Diet = models.CharField(choices=STATUS5_CHOICES, max_length=50)



    def __str__(self):
        return str(self.id)


class FitnessCenter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    City = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    Location = models.CharField(max_length=900)
    type = models.CharField(max_length=50, choices=STATUS10_CHOICES)
    Fitness_photo = models.ImageField(upload_to='Fitness-img')


    def __str__(self):
        return str(self.id)

class contactus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField()
    Answer = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return str(self.id)


class BuyNow(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Full_Name=models.CharField(max_length=200)
    Email=models.EmailField()
    Address=models.TextField()
    City=models.CharField(max_length=200)
    State=models.CharField(choices=STATE_CHOICES, max_length=50)
    Zipcode=models.IntegerField(max_length=6)
    Name_on_Card=models.CharField(max_length=200)
    Card_Number=models.IntegerField(max_length=16)
    Exp_Month=models.CharField(max_length=12)
    Exp_Year=models.IntegerField(max_length=4)
    Cvv=models.IntegerField(max_length=3)

    def __str__(self):
        return str(self.id)


class Doctorname1(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    doctor_name = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    specialisation = models.CharField(choices=CATEGORY1_CHOICES, max_length=35)
    #Slot = models.ForeignKey(SLOT1,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


SLOT_CHOICES = (
    ('9Am to 12Pm','9Am to 12Pm'),
    ('12Pm to 3Pm','12Pm to 3Pm'),
    ('3Pm to 6Pm','3Pm to 6Pm'),
    ('6Pm to 9Pm','6Pm to 9Pm'),
)

class SLOT1(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slot = models.CharField(choices=SLOT_CHOICES, max_length=35)
    date = models.DateField()
    phone = models.IntegerField()
    Doctor_specialization = models.CharField(choices=CATEGORY1_CHOICES, max_length=35)

    def __str__(self):
        return str(self.id)

