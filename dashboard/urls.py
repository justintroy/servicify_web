from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings



from . import views
from .forms import UserLoginForm


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('home/', views.dashboard, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='includes/login.html', next_page='/',
                                                authentication_form=UserLoginForm), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('custom_logout', views.custom_logout, name='custom_logout'),
    path('register/', views.register, name='register'),

    #services
    path('service/<slug:service_id>', views.service_details, name='service_details'),
    path('service-marketplace/', views.service_marketplace, name='service_marketplace'),
    path('createservice/', views.createservice, name='createservice'),
    path('service/<slug:service_id>/service_requests', views.service_requests, name='service_requests'),
    path('service-request/view/', views.view_service, name='view_service'),

    # work offers
    path('createworkoffer/', views.createworkoffer, name='createworkoffer'),
    path('workoffer/', views.work_offer_list, name='work_offer_list'),
    path('biddings/<slug:work_offer_id>', views.work_offer_bidding, name='work_offer_bidding'),
    path('biddings/<slug:work_offer_id>/view/<slug:bidding_id>', views.view_bidding_details, name='view_bidding_details'),
    
    path('register/success', views.register_success, name='register_success'),
    path('activate/<slug:uidb64>/<slug:token>/',
         views.activate, name='activate'),
    path('profile/<slug:user_id>', views.profile_page, name='profile'),
    path('profile/client', views.profile_client, name='profile_client'),
    path('contact/', views.contactus, name='contact_us'),
    path('about/', views.aboutus, name='about_us'),
    path('search/', views.search_results, name='search_results'),

    # unused
    path('workoffer/view', views.workoffer, name='workoffer_view'),
    path('workoffer2/', views.workoffer2, name='workoffer2'),
    path('acquireservice/', views.acquireservice, name='acquireservice'),
    path('acquireservice2/', views.acquireservice2, name='acquireservice2'),


    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


