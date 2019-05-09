from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin

from dynamic_rest.routers import DynamicRouter
from rest_framework.authtoken import views

router = DynamicRouter()

urlpatterns = [
    # Django Admin, use {% raw %}{% url 'admin:index' %}{% endraw %}
    path(settings.ADMIN_URL, admin.site.urls),
    path("api-token-auth/", views.obtain_auth_token),
    path("api/", include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG and "debug_toolbar" in settings.INSTALLED_APPS:
    import debug_toolbar

    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
