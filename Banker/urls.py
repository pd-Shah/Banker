from django.contrib import admin
from django.urls import path, include, re_path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)
from rest_framework.authtoken import views
# from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

# from django.conf.urls.static import static
from Banker import settings
from account.urls import router as account_router
from branch.urls import router as branch_router
from transaction.urls import router as transaction_router
from user.urls import router as users_router

schema = get_swagger_view(title="APIs")

urlpatterns = [
    path("site-admin/", admin.site.urls),
    path('api/v1/token/', views.obtain_auth_token),
    path('api/v1/branch/', include((branch_router.urls, 'branch'))),
    path('api/v1/user/', include((users_router.urls, 'user'))),
    path('api/v1/transaction/', include((transaction_router.urls, 'transaction'))),
    path('api/v1/account/', include((account_router.urls, 'account'))),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        re_path(r"^__debug__/", include(debug_toolbar.urls)),
        # swagger Schema routes, Display all APIs
        path("v1/schema/", SpectacularAPIView.as_view(), name="schema"),
        path(
            "",
            SpectacularSwaggerView.as_view(url_name="schema"),
            name="swagger-ui",
        ),
    ]
