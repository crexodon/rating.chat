from event_base.event import EventBase


class CreationSex(EventBase):
    buttons = [{'text': 'test_1', 'next_event_id': 'creation_age', 'decision_id': 1},
               {'text': 'test_2', 'next_event_id': 'creation_age', 'decision_id': 2},
               {'text': 'test_3', 'next_event_id': 'creation_age', 'decision_id': 3}]

    def __init__(self, chat_id: int):
        super().__init__(chat_id=chat_id, prev_event_ids=['hello', 'hello'], event_id="creation_sex",
                         message_text="hello", buttons=self.buttons)

    @staticmethod
    def is_available(profile):
        return True

    @staticmethod
    def react(profile, decision_id):
        profile['basic']['sex'] = int(decision_id)
        return profile
