from event_base.event import EventBase


class CreationUserName(EventBase):
    buttons = [{'text': 'Kai', 'next_event_id': 'creation_age', 'decision_id': 'Kai'},
               {'text': 'Martin', 'next_event_id': 'creation_age', 'decision_id': 'Martin'},
               {'text': 'Joni', 'next_event_id': 'creation_age', 'decision_id': 'Joni'}]

    def __init__(self, chat_id: int):
        super().__init__(chat_id=chat_id, prev_event_ids=['start'], event_id="creation_user_name",
                         message_text="Choose a name", buttons=self.buttons)

    @staticmethod
    def is_available(profile):
        return True

    @staticmethod
    def react(profile, decision_id):
        profile['basic']['name'] = decision_id
        return profile
