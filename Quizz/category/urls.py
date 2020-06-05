from django.urls import path
from .views import*

urlpatterns = [
    path('categories/', categories),
    path('questions/', questions),
     path('end/', end),
    path('quiz/geography/', quiz_geography),
    path('quiz/entertainment/', quiz_entertainment),
    path('quiz/history/', quiz_history),
    path('quiz/literature/', quiz_literature),
    path('quiz/science/', quiz_science),
    path('quiz/sport/', quiz_sport),
]
