from event_base.event import EventBase


class ManniPresent(EventBase):
    def __init__(self, chat_id: int):
        super().__init__(chat_id=chat_id, prev_event_ids=['start_present'], event_id="manni_present",
                         message_text="Manni hat keinen Bock auf dich und sagt du sollst weiter arbeiten. Hmmm, "
                                      "was jetzt?",
                         buttons=[{'text': 'Doch das Internet. Da sind sie wenigstens nett zu mir', 'next_event_id': 'internet_present'},
                                  {'text': 'Ich hab Amazon Prime!', 'next_event_id': 'amazon_present'}])

    def set_profile_attribute(self, attribute, value):
        pass

    def set_account(self, account: str):
        pass

    @staticmethod
    def is_available(profile) -> bool:
        pass

