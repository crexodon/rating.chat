from event_base.event import EventBase


class PresentEngine(EventBase):
    def __init__(self, chat_id: int):
        super().__init__(chat_id=chat_id, prev_event_ids=['internet_present'], event_id="present_engine",
                         message_text="Und gehst zu...",
                         buttons=[{'text': 'Google', 'next_event_id': 'present_research'},
                                  {'text': 'Bing', 'next_event_id': 'present_research'},
                                  {'text': 'Duckduckgo', 'next_event_id': 'present_research'},
                                  {'text': 'Amazon :D', 'next_event_id': 'amazon_present'}])

    def set_profile_attribute(self, attribute, value):
        pass

    def set_account(self, account: str):
        pass

    @staticmethod
    def is_available(profile) -> bool:
        pass

