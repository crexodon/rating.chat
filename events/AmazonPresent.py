from event_base.event import EventBase


class AmazonPresent(EventBase):
    def __init__(self, chat_id: int):
        super().__init__(chat_id=chat_id, prev_event_ids=['start_present', 'manni_present', 'present_engine'], event_id="amazon_present",
                         message_text="Auf der Arbeit ist es langweilig und du denkst über ein Geschenk für deinen "
                                      "Partner nach.",
                         buttons=[{'text': 'Frag ich mal Manni', 'next_event_id': 'manni_present'},
                                  {'text': 'Das Internet weiß Rat', 'next_event_id': 'internet_present'},
                                  {'text': 'Direkt zu Amazon', 'next_event_id': 'amazon_present'}])

    def set_profile_attribute(self, attribute, value):
        pass

    def set_account(self, account: str):
        pass

    @staticmethod
    def is_available(profile) -> bool:
        pass

