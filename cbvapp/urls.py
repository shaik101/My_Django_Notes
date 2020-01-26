from django.urls import path

from django.views.generic import TemplateView

from .views import PostView, PostListView, PostDetailView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('',TemplateView.as_view(template_name="cbv.html")),
    path('test/',PostView.as_view()),
    path('list/',PostListView.as_view(), name="post_list"),
    path('detail/<int:pk>', PostDetailView.as_view(), name="post_detail"),
    path('update/<int:pk>',PostUpdateView.as_view(),name="post_update"),
    path('delete/<int:pk>',PostDeleteView.as_view(),name="post_delete"),
]
