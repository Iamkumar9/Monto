from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('category/<slug:gender>/<slug:category>/', views.CategoryView.as_view(), name='category'),
    path('category/title/<str:val>/', views.CategoryTitle.as_view(), name='category-title'),
    path('productdetail/<int:pk>', views.Productdetail.as_view(), name='productdetail'),
    path('customerregistraion/',views.CustomerRegistrationView.as_view(), name='customerregistration'),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
