from django.urls import path
from pharma_app.views import PharmaReview

urlpatterns = [
    path('api/review-data/', PharmaReview.as_view(), name='pharma-review'),
]
