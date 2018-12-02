from event_base.event import EventBase


class StartTransport(EventBase):
    def __init__(self, chat_id: int):
        super().__init__(chat_id=chat_id, prev_event_ids=['start_date'], event_id="start_transport",
                         message_text="Nachdem das geregelt ist, geht's ab zur Arbeit.",
                         buttons=[{'text': 'Bloß nicht zu spät für die S-Bahn', 'next_event_id': 'start_present'},
                                  {'text': 'Wo stand mein Auto noch gleich?', 'next_event_id': 'start_present'},
                                  {'text': 'Fahrradhelm auf und los gehts', 'next_event_id': 'start_present'}])

    def set_profile_attribute(self, attribute, value):
        pass

    def set_account(self, account: str):
        pass

    @staticmethod
    def is_available(profile) -> bool:
        pass

