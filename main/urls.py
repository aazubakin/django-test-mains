from django.urls import path

from main import views


app_name = 'main'

urlpatterns = (
    path(
        '',
        views.home,
        name='home'
    ),
    path(
        'bills/',
        views.BillsView.as_view(),
        name='bill'
    ),
    path(
        'form-bills/',
        views.form_bill,
        name='form-bill'
    ),
    path(
        'client-org/',
        views.ClientsView.as_view(),
        name='client'
    ),
    path(
        'api/bills/',
        views.BillsApiView.as_view(),
        name='api-bills'
    ),
    path(
        'api/upload-bills/',
        views.BillFileUpload.as_view(),
        name = 'api-upload-bills'
    ),
    path(
        'api/upload-clients/',
        views.ClientFileUploadView.as_view(),
        name = 'api-upload-clients'
    )
)
