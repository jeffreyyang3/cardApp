from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random
import json
class intro(Page):
    def is_displayed(self):
        return self.round_number == 1
    

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
    def before_next_page(self):
        print(self.player.chosenAnswer)

class WaitForQuestion(WaitPage):
    

    def after_all_players_arrive(self):
        pass

class WaitForAnswers(WaitPage):
    def after_all_players_arrive(self):
        pass



class DisplayAnswersToCz(Page):

    form_model = 'group'
    form_fields = ['winAnswer']
    def is_displayed(self):
        return self.player.isCz


    def vars_for_template(self):
        
        answers = {}
        for player in self.group.get_players():
            if not player.isCz:
                answers[str(player.id)] = player.chosenAnswer
        return {
            'answers': answers
        }

    pass

class DisplayAnswers(WaitPage):
    def is_displayed(self):
        return not self.player.isCz


    template_name = 'cardApp/DisplayAnswers.html'
    form_model = 'group'
    form_fields = []
    
    
    
    def vars_for_template(self):
        if self.player.isCz:
            self.form_fields.append("winAnswer")
        answers = {}
        for player in self.group.get_players():
            if not player.isCz:
                answers[str(player.id)] = player.chosenAnswer
        return {
            'answers': answers
        }

class Results(Page):

    pass




page_sequence = [
    intro,
    CzDraw,
    WaitForQuestion,
    ChooseAnswer,
    WaitForAnswers,
    DisplayAnswersToCz,
    DisplayAnswers,
    Results
]
