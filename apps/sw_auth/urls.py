from django.conf.urls.defaults import *
from django.contrib.auth import views as auth_views
from django.views.generic.simple import direct_to_template

from . import views

urlpatterns = patterns('',
    
    # From registration.backends.default.urls
    url(r'^activate/complete/$',
        direct_to_template,
        { 'template': 'sw_auth/activation_complete.html' },
        name='registration_activation_complete'),
    
    # Activation keys get matched by \w+ instead of the more specific
    # [a-fA-F0-9]{40} because a bad activation key should still get to the view;
    # that way it can return a sensible "invalid key" message instead of a
    # confusing 404.
    url(r'^activate/(?P<activation_key>.+)/$',
        views.activate_user,
        name='registration_activate'),
    
    url(r'^register/$',
        views.register_user,
        name='registration_register'),
    
    url(r'^register/complete/$',
        direct_to_template,
        { 'template': 'sw_auth/registration_complete.html' },
        name='registration_complete'),
    
    url(r'^register/closed/$',
        direct_to_template,
        { 'template': 'sw_auth/registration_closed.html' },
        name='registration_disallowed'),
    
    # From registration.auth_urls
    url(r'^login/$',
        auth_views.login,
        {'template_name': 'sw_auth/login.html'},
        name='auth_login'),
    
    url(r'^logout/$',
        auth_views.logout,
        {'template_name': 'sw_auth/logout.html'},
        name='auth_logout'),
    
    url(r'^password/change/$',
        views.password_reset,
        name='auth_password_change'),
    
    url(r'^password/change/done/$',
        auth_views.password_change_done,
        {'template_name': 'sw_auth/password_change_done.html'},
        name='auth_password_change_done'),
    
    url(r'^password/reset/$',
        views.password_reset,
        name='auth_password_reset'),
    
    url(r'^password/reset/confirm/(?P<token>.+)/$',
        views.password_confirm,
        name='auth_password_reset_confirm',       
        ),
    
    url(r'^password/reset/complete/$',
        auth_views.password_reset_complete,
        {'template_name': 'sw_auth/password_reset_complete.html'},
        name='auth_password_reset_complete'),
    
    url(r'^password/reset/done/$',
        auth_views.password_reset_done,
        {'template_name': 'sw_auth/password_reset_done.html'},
        name='auth_password_reset_done'),

    url(r'^settings/$', views.my_settings),

    # Additional URLs
    url(r'^$', views.index),
)

