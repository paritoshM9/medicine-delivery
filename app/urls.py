from django.urls import path,include
from .views import ListOrdersView, AddOrderView, UserView, ListMedicinesView, AddMedicineView, OrderView, upload_file, sign_in
from .views import ListOrdersView, AddOrderView, UserView, ListMedicinesView, AddMedicineView, OrderView, upload_file, ChatView
from django.urls import path, include
from .views import (
    ListOrdersView,
    AddOrderView,
    UserView,
    ListMedicinesView,
    AddMedicineView,
    OrderView,
    ChatView
)
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
router = routers.DefaultRouter()


urlpatterns = [
    #path('orders/', ListOrdersView.as_view(), name="orders-all"),
    path('user/', UserView.as_view(), name="user"),
    path('order/', OrderView.as_view()),
    path('medicine/', AddMedicineView),
    path('upload/', upload_file, name="upload"),
    path('sign/', sign_in)

    path('chat/', ChatView.as_view())
    # path('upload/', upload_file, name="upload")
    path('chat/', ChatView.as_view()),
]
