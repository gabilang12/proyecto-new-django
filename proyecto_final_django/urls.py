# """
# URL configuration for proyecto_final_django project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/4.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path
# from django.urls import include, path
# from rest_framework import routers
# #from app_final.views import MiVistaAPI
# from app_final.views import mi_vista

# #router = routers.DefaultRouter()

# #router.register('mi_ruta', MiVistaAPI)

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

# # urlpatterns = [
# #     path('api/', include(router.urls)),
# #     path('mi_ruta/', mi_vista),
# # ]

# from django.urls import include, path
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'mi_ruta', mi_vista)

# urlpatterns = [
#     path('api/', include(router.urls)),
# ]

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app_final.views import mi_vista

#router = routers.DefaultRouter()
#router.register(r'mi_ruta', mi_vista)

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('api/', include(router.urls)),
    path('api/mi_ruta/', mi_vista, name='mi_ruta'),
]