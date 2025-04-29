from django.urls import path
from .views import (
    register_api, list_users, retrieve_user, create_user,
    delete_user, update_user, CustomLoginView
)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),               # POST username/password → token
    path('register/', register_api, name='register'),                      # POST new user
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # POST refresh token

    path('all/', list_users, name='list_users'),  # GET
    path('<int:user_id>/', retrieve_user, name='retrieve_user'),  # GET
    path('create/', create_user, name='create_user'),  # POST
    path('<int:user_id>/delete/', delete_user, name='delete_user'),  # DELETE
    path('<int:user_id>/update/', update_user, name='update_user'),  # PUT/PATCH
]
