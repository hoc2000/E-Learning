
from django.contrib import admin
from django.urls import path, include
from .import views, user_login
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [

    path('admin/', admin.site.urls),

    path('base', views.BASE, name='base'),

    path('404', views.PAGE_NOT_FOUND, name='404'),

    path('', views.HOME, name='home'),

    path('courses', views.COURSE_GRID, name='course_grid'),

    path('courses/filter-data', views.filter_data, name="filter-data"),

    path('course/<slug:slug>', views.COURSE_DETAILS, name='course_details'),

    path('search', views.SEARCH_COURSE, name='search_course'),

    path('contact', views.CONTACT_US, name='contact_us'),

    # Post request form user

    path('request', views.REQUEST_COURSE.as_view(), name='request_course'),

    path('about', views.ABOUT_US, name='about_us'),

    path('accounts/register', user_login.REGISTER, name='register'),

    path('accounts/', include('django.contrib.auth.urls')),

    #     path('accounts/password-reset/', auth_views.PasswordResetView.as_view(
    #         html_email_template_name='registration/password_reset_email.html'), name='password_reset'),

    path('doLogin', user_login.DO_LOGIN, name='doLogin'),

    path('accounts/profile', user_login.PROFILE, name='profile'),

    path('accounts/profile/update',
         user_login.PROFILE_UPDATE, name='profile_update'),

    path('checkout/<slug:slug>', views.CHECKOUT, name='checkout'),

    path('my-course', views.MY_COURSE, name='my-course'),

    path('course/watch-course/<slug:slug>',
         views.WATCH_COURSE, name='watch-course'),

    path('course/<slug:course_slug>/<slug:quizz_slug>', views.QUIZ, name='quiz'),

    path('course/<slug:course_slug>/<slug:quizz_slug>/data',
         views.quiz_data_view, name='quiz-data-view'),

    path('course/<slug:course_slug>/<slug:quizz_slug>/save',
         views.save_quiz_view, name='save_quiz_view'),

    #     path('download/<int:document_id>/', views.DOWNLOAD_FILE, name='download'),
    # INSTRUCTOR_URL
    path('instructor/<int:author_id>',
         views.VIEW_INSTRUCTOR.as_view(), name='single-instructor')


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
