from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('live_games', views.live_games, name='live_games'),
    path('download_reports', views.download_reports, name='download_reports'),
    path('game_stream/<str:stream_id>', views.game_stream, name='game_stream'),

    path('chat_gpt_prompt_select', views.chat_gpt_prompt_select, name='chat_gpt_prompt_select'),

    path('login', views.loginUser, name ='login'),
    path('register', views.registerUser, name ='register'),
    path('logout', views.logoutUser, name ='logout'),
]