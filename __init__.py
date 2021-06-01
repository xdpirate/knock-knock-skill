from mycroft import MycroftSkill, intent_file_handler


class KnockKnock(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('knock.knock.intent')
    def handle_knock_knock(self, message):
        self.speak_dialog('knock.knock')


def create_skill():
    return KnockKnock()

