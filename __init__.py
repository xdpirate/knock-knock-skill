from mycroft import MycroftSkill, intent_file_handler

class KnockKnock(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('knock.knock.intent')
    def handle_knock_knock(self, message):
        who = self.get_response('knock.knock')
        punchline = self.get_response(who + ' who?')
        self.speak_dialog('gratification')

    
def create_skill():
    return KnockKnock()
