from event_base.event import EventBase


class RandomSpam(EventBase):
    def __init__(self, chat_id: int):
        super().__init__(chat_id=chat_id, prev_event_ids=['day_two'], event_id="random_spam",
                         message_text="I'm a Nigerian prince and need your help to save 9 mill $. If you can give me your bank account I will give you 30%. Please contact me so we can start our business.",
                         buttons=[{'text': 'Wow, das klingt gut!', 'next_event_id': 'random_positive'},
                                  {'text': 'Weg damit', 'next_event_id': 'day_two'}])

    def set_profile_attribute(self, attribute, value):
        pass

    def set_account(self, account: str):
        pass

    @staticmethod
    def is_available(profile) -> bool:
        pass

