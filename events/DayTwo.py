from event_base.event import EventBase


class DayTwo(EventBase):
    def __init__(self, chat_id: int):
        super().__init__(chat_id=chat_id, prev_event_ids=['start_schufa', 'random_spam'], event_id="day_two",
                         message_text="Du gehst wieder zur Arbeit und schaust in deine Mails.",
                         buttons=[{'text': 'Oh, ein nigerianischer Prinz', 'next_event_id': 'random_spam'},
                                  {'text': 'Hmm, was ist das denn?', 'next_event_id': 'phishing'}])

    def set_profile_attribute(self, attribute, value):
        pass

    def set_account(self, account: str):
        pass

    @staticmethod
    def is_available(profile) -> bool:
        pass

