from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('diversity/', views.DiversityView.as_view(), name='diversity'),
    path('diversity/<int:diversity_id>/update/', views.UpdateDiversityView.as_view(), name='update_diversity'),
    path('diversity/<int:diversity_id>/delete/', views.DeleteDiversityView.as_view(), name='delete_diversity'),
    path('diversity/create_diversity/', views.CreateDiversityView.as_view(), name='create_diversity'),
    path('module/', views.ModuleListView.as_view(), name='module_list'),
    path('module/create/', views.ModuleCreateView.as_view(), name='create_modules'),
    path('module/<int:module_id>/update/', views.ModuleUpdateView.as_view(), name='update_module'),
    path('module/<int:module_id>/delete/', views.DeleteModuleView.as_view(), name='delete_module'),
]