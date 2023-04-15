from django.contrib import admin
from django.urls import path, include
from orders import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('booking.urls')),
    path('order/', include('orders.urls')),
    path('checkout', views.checkout, name='checkout'),
    path('mark_order_as_delivered', views.mark_order_as_delivered, name='mark_order_as_delivered'),
    path('garbage/', include('dashboard.urls')),
    path('parking/', include('parking_zones.urls')),
]
