from event_base.event import EventBase


class RandomPositive(EventBase):
    def __init__(self, chat_id: int):
        super().__init__(chat_id=chat_id, prev_event_ids=['random_spam', 'work_sick'], event_id="random_positive",
                         message_text="Warum fällst du auf diesen Spam herein??? Danke für deine Daten, hier ist die Waschmaschine.",
                         buttons=[{'text': 'Noch eine Runde?', 'next_event_id': 'media_start_media'}])

    def set_profile_attribute(self, attribute, value):
        pass

    def set_account(self, account: str):
        pass

    @staticmethod
    def is_available(profile) -> bool:
        pass

