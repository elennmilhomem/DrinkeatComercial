from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings 


urlpatterns = [
    path("", views.FeedView.as_view(), name="dashboard_feed"),
    path("register/post", views.register_post, name="register_post")

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
