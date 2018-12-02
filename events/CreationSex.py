from event_base.event import EventBase


class CreationSex(EventBase):

    def __init__(self, chat_id: int):
        super().__init__(chat_id=chat_id, prev_event_ids=['hello', 'hello'], event_id="creation_sex",

                         message_text="hello", buttons=[{'text': 'Männlich', 'next_event_id': 'creation_age', 'decision_id': 1},
                                                        {'text': 'Weiblich', 'next_event_id': 'creation_age','decision_id': 2},
                                                        {'text': 'divers', 'next_event_id': 'creation_age', 'decision_id': 3}}])


    @staticmethod
    def is_available(profile):
        return True

    @staticmethod
    def react(profile, decision_id):
        profile['basic']['sex'] = int(decision_id)
        return profile
