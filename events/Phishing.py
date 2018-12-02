from event_base.event import EventBase


class Phishing(EventBase):
    def __init__(self, chat_id: int):
        super().__init__(chat_id=chat_id, prev_event_ids=['day_two'], event_id="phishing",
                         message_text='Das würde doch sehr gut zum Geschenk gestern passen! Woher wissen die das...',
                         buttons=[{'text': 'Passt ja super, direkt mitgekauft', 'next_event_id': 'work_audio'},
                                  {'text': 'Nee, das reicht erstmal', 'next_event_id': 'work_audio'}])

    def set_profile_attribute(self, attribute, value):
        pass

    def set_account(self, account: str):
        pass

    @staticmethod
    def is_available(profile) -> bool:
        pass

