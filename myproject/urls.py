from django.urls import path, include
from myproject import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
#from django.conf.urls import url
from django.urls import re_path as url
urlpatterns = [
    #     path('ERROR', views.error, name="error"),
    path("subjects/<slug:MaMH>/", views.MonHoc_show, name=""),
    path("subjects/<slug:MaMH>/<slug:LoaiTL>/",
         views.MonHoc_LoaiTL_show, name="MonHoc_LoaiTL_show"),
    path('category/<slug:NhomMH>/<slug:Khoa>/', views.MonHocList_view),
    path('document/<slug:slug>/', views.one_document_view),
    path('alert/<slug:slug>/read', views.Doc_Thong_Bao),
    path('download/<slug:slug>/', views.TaiLieu_download, name='TaiLieu_download'),
    path('dashboard/', views.dashboard_view, name='dashboard_view'),
    path('dashboard/DuyetTL/', views.DuyetTL_view, name='DuyetTL_view'),
    path('dashboard/DuyetTL/Preview/<slug:MaTL>',
         views.TaiLieu_Preview, name='TaiLieu_Preview'),
    path('dashboard/DuyetTL/XetDuyet/<slug:slug>',
         views.TaiLieu_Duyet, name='TaiLieu_Duyet'),
    path('dashboard/DongGopTL/', views.DongGopTL_view, name='DongGopTL_view'), path(
        'dashboard/TaiLieu/', views.TaiLieu_view, name='TaiLieu_view'),
    path('dashboard/TaiLieu/delete/<slug:slug>',
         views.TaiLieu_delete, name='TaiLieu_delete'),
    path('dashboard/ThanhVien/', views.ThanhVien_view, name='ThanhVien_view'),
    path('dashboard/ThanhVien/active/<slug:username>',
         views.ThanhVien_Active, name='ThanhVien_Active'),
    path('dashboard/ThanhVien/staff/<slug:username>',
         views.ThanhVien_Staff, name='ThanhVien_Staff'),
    path('dashboard/BinhLuan/', views.BinhLuan_view, name='BinhLuan_view'),
    path('dashboard/profile/', views.ThongTinCaNhan_view,
         name='ThongTinCaNhan_view'),
    path('profile/<slug:username>/',
         views.show_profile_public, name='show_profile'),
    path('DangKy/', views.DangKy_view, name='DangKy_view'),
    path('', views.home_view, name='home_view'),
    path('DangNhap/', auth_views.LoginView.as_view(
        template_name='global_DangNhap.html'), name='DangNhap_view'),
    path('DangXuat/', auth_views.LogoutView.as_view(next_page='/'),
         name='DangXuat_view'),
    path('search/', views.search_view, name='search'),
    url(r'^media/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT}),
    # url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password/password_reset_complete.html'), name='password_reset_complete'),
    path('password_reset/', views.password_reset_request, name="password_reset"),
]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
handler404 = views.error404
# print(urlpatterns)
# print(settings.MEDIA_URL, settings.MEDIA_ROOT)
# print(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
# print(settings.STATIC_URL, settings.STATIC_ROOT)
# print(static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
