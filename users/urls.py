from django.urls import path
from .views import (
    login_api, logout_api, register_api,
    list_users, retrieve_user, create_user, delete_user, update_user
)

urlpatterns = [
    path('login/', login_api, name='login_api'), # POST
    path('logout/', logout_api, name='logout_api'), # DELETE
    path('register/', register_api, name='register_api'), # POST

    path('all/', list_users, name='list_users'),  # GET
    path('<int:user_id>/', retrieve_user, name='retrieve_user'),  # GET
    path('create/', create_user, name='create_user'),  # POST
    path('<int:user_id>/delete/', delete_user, name='delete_user'),  # DELETE
    path('<int:user_id>/update/', update_user, name='update_user'),  # PUT/PATCH
]
