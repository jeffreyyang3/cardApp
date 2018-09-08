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
    num_rounds = 3


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()
        print('creating subsession called')
        if('answers' not in self.session.vars or 
        len(self.session.vars['answers']) < (10 * (len(self.get_players()) - 1))):
            answerFile = open("cardApp/cards/answers.txt", "r")
            self.session.vars['answers'] = answerFile.readlines()
            answerFile.close()
            random.shuffle(self.session.vars['answers'])

        


        

  

        
        numPlayers = len(self.get_players())
        for i in range(numPlayers):
            if(i == 0):
                self.get_players()[i].isCz = True
                
            else:
                answerDraw = []
                for x in range(10):
                    answerDraw.append(self.session.vars['answers'].pop())
                self.get_players()[i].providedCards = json.dumps(answerDraw)
                

                self.get_players()[i].isCz = False
                
        
        

            
            
    pass


class Group(BaseGroup):
    
    question = models.TextField()
    winAnswer = models.TextField()
    winner = models.IntegerField()
    pass


class Player(BasePlayer):
    username = models.CharField()
    isCz = models.BooleanField()
    providedCards = models.TextField()
    question = models.TextField()
    chosenAnswer = models.TextField()
    def chat_nickname(self):
        return self.player.username
