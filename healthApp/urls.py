from django.urls import path

from . import views, PredictionViews, PostViews

app_name = 'healthApp'
urlpatterns = [
    path('', views.home, name='home'),

    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),

    path('user/profile/', views.user_profile, name='user_profile'),
    path('user/edit_save/<int:id>', views.user_edit_save, name='user_edit_save'),
    path('user/my_posts/<int:id>', views.list_post_by_user_id, name='list_post_by_user_id'),

    path('post/detail/<int:id>', PostViews.post_detail, name='post_detail'),
    path('post/create/', PostViews.post_create, name='post_create'),
    path('post/create_save/', PostViews.post_create_save, name='post_create_save'),
    path('post/edit_save/<int:id>', PostViews.post_edit_save, name='post_edit_save'),
    path('post/delete/<int:id>', PostViews.post_delete, name='post_delete'),

    path('predict/heart/', PredictionViews.heart, name='heart'),
    path('predict/heart_predict/', PredictionViews.heart_predict, name='heart_predict'),
    path('predict/kidney/', PredictionViews.kidney, name='kidney'),
    path('predict/kidney_predict/', PredictionViews.kidney_predict, name='kidney_predict'),
    path('predict/diabetes/', PredictionViews.diabetes, name='diabetes'),
    path('predict/diabetes_predict/', PredictionViews.diabetes_predict, name='diabetes_predict'),
    path('predict/liver/', PredictionViews.liver, name='liver'),
    path('predict/liver_predict/', PredictionViews.liver_predict, name='liver_predict'),
    path('predict/cancer/', PredictionViews.cancer, name='cancer'),
    path('predict/cancer_predict/', PredictionViews.cancer_predict, name='cancer_predict'),
    path('predict/result/', PredictionViews.result, name='result'),
]
