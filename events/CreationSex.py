from event_base.event import EventBase


class CreationSex(EventBase):

    def __init__(self, chat_id: int):
        super().__init__(chat_id=chat_id, prev_event_ids=['creation_age'], event_id="creation_sex",

                         message_text="Wähle dein Geschlect"
                         , buttons=[{'text': 'Männlich', 'next_event_id': 'media_start_media', 'decision_id': 1},
                                    {'text': 'Weiblich', 'next_event_id': 'media_start_media','decision_id': 2},
                                    {'text': 'divers', 'next_event_id': 'media_start_media', 'decision_id': 3}])


    @staticmethod
    def is_available(profile):
        return True

    @staticmethod
    def react(profile, decision_id):
        profile['basic']['sex'] = int(decision_id)
        return profile
