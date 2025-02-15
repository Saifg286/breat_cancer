# breast_cancer/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView  # To handle redirection

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/prediction/', permanent=True)),  # Redirect root to /prediction
    path('prediction/', include('prediction.urls')),  # Include the prediction URLs
]
