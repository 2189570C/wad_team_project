from django.conf.urls import url
from cookbook import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    url(r'^sign-up/$', views.signup, name='signup'),
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^logout/$', views.user_logout, name='user_logout'),
    url(r'^myprofile/$', views.myprofile, name='myprofile'),
    url(r'^myprofile/saved-recipes/$', views.savedrecipes, name='savedrecipes'),
    url(r'^myprofile/upload-recipe/$', views.uploadrecipe, name='uploadrecipe'),
    url(r'^user/(?P<user>[\w\-]+)/$', views.view_user, name='userprofile'),
    url(r'^user/(?P<user>[\w\-]+)/(?P<name>[\w\-]+)/$', views.view_recipe, name='viewrecipe'),
    url(r'^best-rated/$', views.bestrated, name='best-rated'),
    url(r'^search/$', views.search, name='search'),
    url(r'^categories/$', views.categories, name='categories'),
    url(r'^categories/(?P<category>[\w\-]+)/', views.view_category, name='viewcategory'),
    url(r'^help/$', views.about, name='help'),
    url(r'^help/faq/$', views.faq, name='faq'),
    url(r'^help/conversion-charts/$', views.conversioncharts, name='conversion-charts'),
    url(r'^help/recipe-writing-guidelines/$', views.recipeguide, name='recipe-writing-guidelines'),
    url(r'^help/commenting-rules/$', views.commentingrules, name='commenting-rules'),    

]
