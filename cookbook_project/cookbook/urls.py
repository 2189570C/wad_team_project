from django.conf.urls import url
from cookbook import views

app_name = 'cookbook'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    url(r'^sign-up/$', views.signup, name='signup'),
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^logout/$', views.user_logout, name='user_logout'),
    url(r'^myprofile/$', views.myprofile, name='myprofile'),
    url(r'^myprofile/account-settings/$', views.account_settings, name='account_settings'),
    url(r'^myprofile/account-settings/delete-account/$', views.delete_account, name='delete_account'),
    url(r'^myprofile/account-settings/change-password/$', views.change_password, name='change_password'),
    url(r'^myprofile/saved-recipes/$', views.savedrecipes, name='saved-recipes'),
    url(r'^myprofile/upload-recipe/$', views.uploadrecipe, name='upload-recipe'),
    url(r'^user/(?P<user>[\w\-]+)/$', views.view_user, name='view_user'),
    url(r'^user/(?P<user>[\w\-]+)/(?P<recipe_slug>[\w\-]+)/$', views.view_recipe, name='view_recipe'),
    url(r'^user/(?P<user>[\w\-]+)/(?P<recipe_slug>[\w\-]+)/edit/$', views.editrecipe, name='editrecipe'),    
    url(r'^best-rated/$', views.bestrated, name='best-rated'),
    url(r'^newest-recipes/$', views.newestrecipes, name='newest-recipes'),
    url(r'^search/$', views.search, name='search'),
    url(r'^categories/$', views.categories, name='categories'),
    url(r'^categories/(?P<category_name>[\w\-]+)/', views.view_category, name='view_category'),
    url(r'^help/$', views.about, name='help'),
    url(r'^help/faq/$', views.faq, name='faq'),
    url(r'^help/conversion-charts/$', views.conversioncharts, name='conversion-charts'),
    url(r'^help/recipe-writing-guidelines/$', views.recipeguide, name='recipe-writing-guidelines'),
    url(r'^help/commenting-rules/$', views.commentingrules, name='commenting-rules'),    

    # Ajax urls
    url(r'^save_recipe/$', views.save_recipe, name='save_recipe'),
    url(r'^delete_comment/$', views.delete_comment, name='delete_comment'),
    url(r'^delete_recipe/$', views.delete_recipe, name='delete_recipe'),
    url(r'^rate_recipe/$', views.rate_recipe, name='rate_recipe'),
    url(r'^username_check/$', views.username_check, name='username_check'),
]
