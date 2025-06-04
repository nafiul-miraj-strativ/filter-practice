from django.urls import path,include

urlpatterns = [
    path('api/v1/filterApp/', include(f"apps.filterApp.api.v1.urls"),),
]
