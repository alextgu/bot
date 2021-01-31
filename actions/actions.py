from rasa_sdk import Action


question_mapper = {
    'how old is alex?': '14',
    'what is alex?': 'ikea table stand',
    "who is alex's friend?": 'sexmon',
    'can edward beat a no hand tennis player?': 'can AQ build a chatbot?',
    'can ducks code?': 'we know one that does',
    'why can simon tell the future?': 'because jojolito tells him',
    'rock, paper or scissors?' : 'fak',
    'how big is simon pp?': ':-',
    'how big is alex pp?': '.',
    'how many people can edward beat in tennis?': 'about 3..... in the world',
    'what is edwards ideal basketball position?': 'maple story a'
}


class ActionAnswerQuestion(Action):
    def name(self):
        return 'action_answer_question'

    def run(self, dispatcher, tracker, domain):
        intent = tracker.latest_message['intent'].get('name')
        
        if intent == 'question':
            message = tracker.latest_message.get('text')
            if message.lower() in question_mapper.keys():
                dispatcher.utter_message(text=question_mapper[message.lower()])
            else:
                dispatcher.utter_message(text='I do not know the answer. Ask me another question.')
        return []
