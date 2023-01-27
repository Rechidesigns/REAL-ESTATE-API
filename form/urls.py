from django.urls import path
from .import views

urlpatterns = [
    path('book-inspection/', views.BookInspectionView().as_view(), name="book_appointment_for_inspection"),
    path('book-inspection/<int:booking_id>/', views.BookInspectionDetailView().as_view(), name="book_inspection"),
]
