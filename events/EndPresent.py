from event_base.event import EventBase


class EndPresent(EventBase):
    def __init__(self, chat_id: int):
        super().__init__(chat_id=chat_id, prev_event_ids=['present_inspiration', 'amazon_buy_present'], event_id="end_present",
                         message_text="Du gehst nochmal aufs Klo und machst dann Feierabend nach diesem anstrengenden Arbeitstag.",
                         buttons=[{'text': 'Next', 'next_event_id': 'start_schufa'}])

    def set_profile_attribute(self, attribute, value):
        pass

    def set_account(self, account: str):
        pass

    @staticmethod
    def is_available(profile) -> bool:
        pass

