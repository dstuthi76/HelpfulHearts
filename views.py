from django.shortcuts import render,redirect
from django.views import View
from .models import Product, Doctors,DietPlan1,Hospitals,Profile,FitnessCenter,contactus,BuyNow,Doctorname1,SLOT1
from .forms import CustomerRegistrationForm,CustomerProfileForm,ContactForm,BuyNowBlock,SlotBlock
from django.contrib import messages
from django.views.generic import ListView,DetailView

class ProductView(View):

    def get(self, request):
        medicine = Product.objects.all()
        doctors = Doctors.objects.all()
        fitness = FitnessCenter.objects.all()
        hospital = Hospitals.objects.all()
        return render(request, 'app/index.html',
                      {'product': medicine, 'doctors': doctors, 'fitness': fitness, 'hospital': hospital})



class ProductDetailView(View):
    def get(self,request, pk):
        product =Product.objects.get(pk=pk)
        return render(request,'app/productdetail.html', {'product': product})


class DietPlanDetailView(View):
    def get(self,request, pk):
        product =DietPlan1.objects.get(pk=pk)
        return render(request,'app/Deit_plan_detail.html', {'product': product})



class DietPlanView(View):
    def get(self,request):
        add1 = Profile.objects.filter(user=request.user)
        product = DietPlan1.objects.filter(Primary_Diet='Anything')
        product1 = DietPlan1.objects.filter(Primary_Diet='Vegetarian')
        product2 = DietPlan1.objects.filter(Primary_Diet='Paleo')
        product3 = DietPlan1.objects.filter(Primary_Diet='Vegan')
        product4 = DietPlan1.objects.filter(Primary_Diet='Ketogenic')
        product5 = DietPlan1.objects.filter(Primary_Diet='Mediterrnean')
        return render(request, 'app/DietPlan.html', {'add1': add1, 'product': product,'product1': product1, 'product2': product2, 'product3': product3, 'product4': product4, 'product5': product5})

class HospipitalDetailView(View):
    def get(self,request,pk):
        product = Hospitals.objects.get(pk=pk)
        return render(request, 'app/Hospitaldetail.html', {'product': product})

def add_to_cart(request):
    user = request.user
    doctor_id = request.GET.get('doctor_id')
    doctor_name = Doctors.objects.get(id=doctor_id)
    messages.success(request, "Congratulations!! Your's Medical Appointment Successfully Completed ")
    Doctorname1(user=user,name=user,doctor_name=doctor_name,specialisation=user).save()
    return redirect('/appointmentDetails')

def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        slot = SLOT1.objects.filter(user=user)
        Doctornam = Doctorname1.objects.filter(user=user)
        return render(request,'app/addtocard.html',{'Doctornames':Doctornam,'slot':slot})





def profile(request):
    return render(request, 'app/profile.html')


def address(request):
    add = Profile.objects.filter(user=request.user)
    return render(request, 'app/address.html',{'add': add,'active':'btn-dark'})






class CustomerRegistrationView(View):
    def get(self,request):
       form = CustomerRegistrationForm()
       return render(request, 'app/customerregistration.html',{'form':form})

    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulations!! Successfully Registered')
            form.save()
        return render(request, 'app/customerregistration.html',{'form':form})

class DoctorProfileView(View):
    def get(self,request, pk):
        doctor = Doctors.objects.get(pk=pk)
        return render(request, 'app/doctorprofile.html', {'doctor':doctor})


class ProfileView(View):
    def get(self,request):
       form = CustomerProfileForm()
       return render(request,'app/profile.html',{'form':form,'active':'btn-primary'})

    def post(self,request):
        form=CustomerProfileForm(request.POST)
        if form.is_valid():
            User = request.user
            name=form.cleaned_data['name']
            Goal = form.cleaned_data['Goal']
            units = form.cleaned_data['units']
            gender = form.cleaned_data['gender']
            height_feet = form.cleaned_data['height_feet']
            height_inch = form.cleaned_data['height_inch']
            weight= form.cleaned_data['weight']
            Age = form.cleaned_data['Age']
            Bodyfat = form.cleaned_data['Bodyfat']
            Activity_level = form.cleaned_data['Activity_level']
            Primary_Diet = form.cleaned_data['Primary_Diet']
            reg= Profile(user=User,name=name,Goal=Goal,units=units,gender=gender,height_feet=height_feet,height_inch=height_inch,
                         weight=weight,Age=Age,Bodyfat=Bodyfat,Activity_level=Activity_level,Primary_Diet=Primary_Diet)
            reg.save()
            messages.success(request,'Congratulations!! Profile Updated Successfully ')
        return render(request,'app/profile.html',{'form':form,'active':'btn-primary'})

def AboutUs(request):
    return render(request, 'app/aboutus.html')


def Service(request):
    return render(request, 'app/service.html')

class Fitness(View):
    def get(self,request,pk):
        product = FitnessCenter.objects.get(pk=pk)
        return render(request, 'app/FitnessDetail.html', {'product': product})

class ContactView(View):
    def get(self,request):
        form=ContactForm()
        return render(request,'app/contactus.html',{'form':form})
    def post(self,request):
        form = ContactForm(request.POST)
        if form.is_valid():
            User = request.user
            name = form.cleaned_data['name']
            Answer= form.cleaned_data['Answer']
            email = form.cleaned_data['email']
            reg =contactus(user=User,name=name,Answer=Answer,email=email)
            reg.save()
            messages.success(request, 'Congratulations!! Your Answer Successfully Submitted ')
        return render(request, 'app/contactus.html', {'form': form})


class BuynowView(View):
    def get(self,request):
        form=BuyNowBlock()
        return render(request,'app/buynow.html',{'form':form})
    def post(self,request):
        form = BuyNowBlock(request.POST)
        if form.is_valid():
            user = request.user
            Full_Name = form.cleaned_data['Full_Name']
            Email = form.cleaned_data['Email']
            Address = form.cleaned_data['Address']
            City = form.cleaned_data['City']
            State = form.cleaned_data['State']
            Zipcode= form.cleaned_data['Zipcode']
            Name_on_Card = form.cleaned_data['Name_on_Card']
            Card_Number = form.cleaned_data['Card_Number']
            Exp_Month = form.cleaned_data['Exp_Month']
            Exp_Year = form.cleaned_data['Exp_Year']
            Cvv = form.cleaned_data['Cvv']

            reg =BuyNow(user=user,Full_Name=Full_Name,Email=Email,Address=Address,City=City,State=State,
                           Zipcode=Zipcode,Name_on_Card=Name_on_Card,Card_Number=Card_Number,Exp_Month=Exp_Month,
                           Exp_Year=Exp_Year,Cvv=Cvv)
            reg.save()
            messages.success(request," Congratulations!! Your Transaction Successfully Completed You Can get Your order within 2 days " )
        return render(request, 'app/buynow.html', {'form': form})


class DocView(View):
    def get(self,request):
       form = SlotBlock()
       return render(request,'app/appointmentform.html',{'form':form,'active':'btn-dark'})

    def post(self,request):
        form = SlotBlock(request.POST)
        if form.is_valid():
            user = request.user
            name=form.cleaned_data['name']
            slot = form.cleaned_data['slot']
            date = form.cleaned_data['date']
            phone = form.cleaned_data['phone']
            Doctor_specialization = form.cleaned_data['Doctor_specialization']
            reg = SLOT1(user=user,name=name,slot=slot,date=date,phone=phone,Doctor_specialization=Doctor_specialization)
            reg.save()
            messages.success(request,'Your Data saved please have a look at Doctors')
        return render(request,'app/appointmentform.html',{'form':form,'active':'btn-dark'})


class DoctorsSpec(View):
    def get(self,request):
        add1 = SLOT1.objects.filter(user=request.user)
        product = Doctors.objects.filter(specialisation='cardiologist')
        product1 = Doctors.objects.filter(specialisation='General Physician')
        product2 = Doctors.objects.filter(specialisation='allergist')
        product3 = Doctors.objects.filter(specialisation='anesthesiologist')
        product4 = Doctors.objects.filter(specialisation='dentist')
        product5 = Doctors.objects.filter(specialisation='dermatologist')
        product6 = Doctors.objects.filter(specialisation='fertility specialist')
        product7 = Doctors.objects.filter(specialisation='massage therapist')
        product8 = Doctors.objects.filter(specialisation='neurologist')
        product9 = Doctors.objects.filter(specialisation='pediatrician')
        product10 = Doctors.objects.filter(specialisation='radiologist')
        return render(request, 'app/doctors.html', {'add1': add1, 'product': product,'product1': product1, 'product2': product2, 'product3': product3, 'product4': product4, 'product5': product5 , 'product6': product6 , 'product7': product7, 'product8': product8, 'product9': product9, 'product10': product10 })
