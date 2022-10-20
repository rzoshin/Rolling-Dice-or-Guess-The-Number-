from django.urls import path
from .views import loginUser, gamePage, gtnGame, gtnGameRule, rdGame, rdGameRules, registerPage, logoutUser


urlpatterns = [

    path('', gamePage, name='game-page'),
    path('guess-the-number', gtnGame, name='gtn-page'),
    path('guess-the-number-rules', gtnGameRule, name='gtn-rules-page'),

    path('rolling-dice', rdGame, name='rd-page'),
    path('rolling-dice-rules', rdGameRules, name='rd-rules'),

    path('login/', loginUser, name='login-user'),
    path('signup/', registerPage, name='signup-user'),
    path('logout/', logoutUser, name='logout-user'),
]
