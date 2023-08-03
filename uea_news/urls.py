
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('autenticacao/', include('autenticacao.urls')),
    path('publico/', include('publico.urls'))
]
