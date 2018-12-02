from event_base.event import EventBase


class PresentInspiration(EventBase):
    def __init__(self, chat_id: int):
        super().__init__(chat_id=chat_id, prev_event_ids=['present_research'], event_id="present_inspiration",
                         message_text="Du findest großartige Inspiration und willst es gleich bestellen.",
                         buttons=[{'text': 'Ab ins Geschäft nachher', 'next_event_id': 'end_present'},
                                  {'text': 'Nämlich auf Amazon', 'next_event_id': 'amazon_buy_present'}])

    def set_profile_attribute(self, attribute, value):
        pass

    def set_account(self, account: str):
        pass

    @staticmethod
    def is_available(profile) -> bool:
        pass

