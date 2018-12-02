from event_base.event import EventBase


class PresentResearch(EventBase):
    def __init__(self, chat_id: int):
        super().__init__(chat_id=chat_id, prev_event_ids=['present_engine'], event_id="present_research",
                         message_text="Geschenkinspiration...",
                         buttons=[{'text': 'Folgende Pinterests könnten dir gefallen', 'next_event_id': 'present_inspiration'},
                                  {'text': 'Spiegel Online: Die beliebtesten Geschenke der Deutschen', 'next_event_id': 'present_inspiration'},
                                  {'text': 'Gutefrage.net hat gute Antworten', 'next_event_id': 'present_inspiration'}])

    def set_profile_attribute(self, attribute, value):
        pass

    def set_account(self, account: str):
        pass

    @staticmethod
    def is_available(profile) -> bool:
        pass

