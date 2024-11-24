from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('wardrobe', views.wardrobe, name='wardrobe'),
    path('wardrobe/<str:name>', views.wardrobe_items, name='wardrobe_items'),
    path('wardrobe/delete/<int:item_id>', views.delete, name='delete'),
    path('wardrobe/add/add-item', views.add, name='add'),
    path('contact', views.contact, name='contact')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)