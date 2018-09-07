from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random
import json


class CzDraw(Page):
    form_model = 'group'
    form_fields = ['question']

    def is_displayed(self):
        return self.player.isCz

    def vars_for_template(self):
        if 'questions' not in self.session.vars or len(self.session.vars['questions']) == 3:
            questionFile = open("cardApp/cards/questions.txt", "r")
            self.session.vars['questions'] = questionFile.readlines()
            questionFile.close()
            random.shuffle(self.session.vars['questions'])
        questionList = []
        questionList.append(self.session.vars['questions'].pop())
        questionList.append(self.session.vars['questions'].pop())
        questionList.append(self.session.vars['questions'].pop())
            
        return{
            'questionList': questionList
        }
        

class ChooseAnswer(Page):
    form_model = 'player'
    form_fields = ['chosenAnswer']
    def is_displayed(self):
        return not self.player.isCz
    
    def vars_for_template(self):
        jsonDec = json.decoder.JSONDecoder()
        newList = jsonDec.decode(self.player.providedCards)
        return{
            'question': self.group.question,
            'answerDraw': newList
        }

class WaitForQuestion(WaitPage):
    

    def after_all_players_arrive(self):
        pass

class WaitForAnswers(WaitPage):
    def after_all_players_arrive(self):
        pass

class Results(Page):
    pass


page_sequence = [
    CzDraw,
    WaitForQuestion,
    ChooseAnswer,
    WaitForAnswers,
    Results
]
