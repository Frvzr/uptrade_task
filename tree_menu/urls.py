from django.urls import path
from tree_menu.apps import TreeMenuConfig
from tree_menu import views
from django.conf.urls.static import static
from django.conf import settings



app_name = TreeMenuConfig.name

urlpatterns = [
    path('<path:url>?<str:selected>', views.TreeMenuView.as_view(), name='select'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
