from django.urls import path
from .views import DashboardsView
from. import views


urlpatterns = [
    path('', DashboardsView.as_view(), name='dashboards'),
   
    # path('sign-in/', views.sign_in, name='sign-in'),
    # path('sign-out/', views.sign_out, name='sign-out'),   

]