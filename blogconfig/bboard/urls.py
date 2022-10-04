from django.urls import path
from .views import index, by_rubric, BbCreateView, PostEditor

urlpatterns = [
    path("add/", BbCreateView.as_view(), name='add'),
    path("<int:rubric_id>/",by_rubric, name='by_rubric'),
    path("", index, name='index'),
    path("post_edit/<int:pk>/", PostEditor.post_edit, name='post_edit'),
]
