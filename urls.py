from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm,MyPasswordChangeForm,MyPasswordResetForm,MySetPasswordForm

urlpatterns = [
    #HomePage
    path('',views.ProductView.as_view(),name='home'),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),


    #doctorsAppointment
    path('appointments/', views.add_to_cart, name='appointment'),
    path('appointmentDetails/',views.show_cart,name='appointmentDetails'),
    path('appointmentform/',views.DocView.as_view(),name='appointment-form'),
    path('Doctors/',views.DoctorsSpec.as_view(),name='doctors'),
    path('doctors/<int:pk>', views.DoctorProfileView.as_view(), name='doctor-profile'),


    #medicinesPayment
    path('buy/', views.BuynowView.as_view(), name='buy-now'),


    #DietPlan
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('dietplan/',views.DietPlanView.as_view(),name='dietplan'),
    path('deitplandetail/<int:pk>',views.DietPlanDetailView.as_view(),name='detaildeitplan'),


    #HospitalDetails
    path('hospitaldetail/<int:pk>',views.HospipitalDetailView.as_view(),name='hospitaldetail'),

    #staticPages
    path('AboutUs/',views.AboutUs,name='aboutus'),
    path('ContactUs/',views.ContactView.as_view(),name='contactus'),
    path('service/',views.Service,name='service'),

    #FitnessCenters
    path('FitnessCenter/<int:pk>',views.Fitness.as_view(),name='fitness-center'),


    #authentication
    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html',form_class=MyPasswordChangeForm,success_url='/passwordchangedone/'),name='passwordchange'),
    path('passwordchangedone/',auth_views.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'),name='passwordchangedone'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm), name='login'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html',form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'),name='password_reset_complete'),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)