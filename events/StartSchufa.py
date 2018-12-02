from event_base.event import EventBase


class StartSchufa(EventBase):
    def __init__(self, chat_id: int):
        super().__init__(chat_id=chat_id, prev_event_ids=['end_present'], event_id="start_schufa",
                         message_text="Du hast einen Brief bekommen.",
                         buttons=[{'text': 'Oh nee, Rundfunkgebühren Gebühren! Zahle ich...später.', 'next_event_id': 'day_two'},
                                  {'text': 'G...E....ach weg damit', 'next_event_id': 'day_two'}])

    def set_profile_attribute(self, attribute, value):
        pass

    def set_account(self, account: str):
        pass

    @staticmethod
    def is_available(profile) -> bool:
        pass

