from event_base.event import EventBase


class CreationAge(EventBase):
    buttons = [{'text': '18-24', 'next_event_id': 'creation_sex', 'decision_id': 1},
               {'text': '25-60', 'next_event_id': 'creation_sex', 'decision_id': 2},
               {'text': '60+',   'next_event_id': 'creation_sex', 'decision_id': 3}]

    def __init__(self, chat_id: int):
        event_id = "creation_age"
        super().__init__(chat_id=chat_id, prev_event_ids=["creation_user_name"], event_id=event_id,
                         buttons=self.buttons,
                         message_text="Wähle dein Alter")

    @staticmethod
    def is_available(profile):
        return True

    @staticmethod
    def react(profile, decision_id):
        profile['basic']['age'] = int(decision_id)
        return profile
