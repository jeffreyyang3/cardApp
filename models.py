from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import json
import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'cardApp'
    players_per_group = None
    num_rounds = 100


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    
    question = models.TextField()
    winAnswer = models.TextField()
    winner = models.StringField()
    wins = models.IntegerField()
    pass


class Player(BasePlayer):
    username = models.CharField()
    isCz = models.BooleanField()
    providedCards = models.TextField()
    question = models.TextField()
    chosenAnswer = models.TextField()
    def chat_nickname(self):
        return self.player.username
