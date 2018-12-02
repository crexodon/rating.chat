from event_base.event import EventBase


class InternetPresent(EventBase):
    def __init__(self, chat_id: int):
        super().__init__(chat_id=chat_id, prev_event_ids=['start_present', 'manni_present'], event_id="internet_present",
                         message_text="Du öffnest schnell deinen Browser...",
                         buttons=[{'text': 'Chrome', 'next_event_id': 'present_engine'},
                                  {'text': 'Firefox', 'next_event_id': 'present_engine'},
                                  {'text': 'Internet Explorer', 'next_event_id': 'present_engine'},
                                  {'text': 'Safari', 'next_event_id': 'present_engine'}])

    def set_profile_attribute(self, attribute, value):
        pass

    def set_account(self, account: str):
        pass

    @staticmethod
    def is_available(profile) -> bool:
        pass

