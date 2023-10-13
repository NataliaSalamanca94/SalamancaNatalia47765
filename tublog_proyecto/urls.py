from django.contrib.auth import views as auth_views  # Import Django's built-in auth views

# Your other imports remain the same
from tublog import views
from django.urls import path
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # ... Other URL patterns ...
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Use auth_views.LoginView
    path('logout/', views.user_logout, name='user_logout'),
    path('blogposts/', views.BlogPostListView.as_view(), name='blogpost_list'),
    path('blogposts/create/', login_required(views.BlogPostCreateView.as_view()), name='blogpost_create'),
    path('blogposts/update/<int:pk>/', login_required(views.BlogPostUpdateView.as_view()), name='blogpost_update'),
    path('blogposts/delete/<int:pk>/', login_required(views.BlogPostDeleteView.as_view()), name='blogpost_delete'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('', views.home, name='home'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/', views.category_list, name='category_list'),
    path('tags/create/', views.tag_create, name='tag_create'),
    path('tags/', views.tag_list, name='tag_list'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
]
