from django.contrib import admin
from .models import (
    Product,
    Doctors,
    DietPlan1,
    Hospitals,
    Profile,
    FitnessCenter,
    contactus,
    BuyNow,
    Doctorname1,
    SLOT1,
)


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'selling_price', 'discounted_price', 'description', 'brand', 'category',
                    'product_photo']


@admin.register(Doctors)
class DoctorModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'doctor_name', 'consultant_fee', 'description', 'Location', 'city', 'zipcode',
                    'state',
                    'specialisation',
                    'Google_meet',
                    'doctor_photo']


@admin.register(Hospitals)
class HospitalsModelAdmin(admin.ModelAdmin):
    list_display =['id','user','name','description','Phone','City','zipcode','Location','type','Hospital_photo']


@admin.register(DietPlan1)
class DietPlanModelAdmin(admin.ModelAdmin):
    list_display =['id','user','name','description','Age','Goal','Bodyfat','Activity_level','Primary_Diet','Diet_photo']



@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','Goal','units','gender','height_feet','height_inch','weight','Age','Bodyfat','Activity_level','Primary_Diet']

@admin.register(FitnessCenter)
class FitnessModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','description','City','zipcode','Location','type','Fitness_photo']

@admin.register(contactus)
class ContactUsModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','Answer','email']


@admin.register(BuyNow)
class BuyNowModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','Full_Name','Email','Address','City','State','Zipcode','Name_on_Card','Card_Number','Exp_Month','Exp_Year','Cvv']


@admin.register(Doctorname1)
class DoctorNameModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','doctor_name','specialisation']



@admin.register(SLOT1)
class SlotModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','slot','date','phone','Doctor_specialization']