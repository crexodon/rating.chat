from event_base.event import EventBase


class AmazonBuyPresent(EventBase):
    def __init__(self, chat_id: int):
        super().__init__(chat_id=chat_id, prev_event_ids=['present_inspiration'], event_id="amazon_buy_present",
                         message_text="Das Geschenk ist im Warenkorb und nun zum Checkout.",
                         buttons=[{'text': 'Kreditkarte', 'next_event_id': 'end_present'},
                                  {'text': 'Paypal', 'next_event_id': 'end_present'},
                                  {'text': 'Sofort-Überweisung', 'next_event_id': 'end_present'}])

    def set_profile_attribute(self, attribute, value):
        pass

    def set_account(self, account: str):
        pass

    @staticmethod
    def is_available(profile) -> bool:
        pass

