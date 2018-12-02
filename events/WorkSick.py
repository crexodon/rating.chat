from event_base.event import EventBase


class WorkSick(EventBase):
    def __init__(self, chat_id: int):
        super().__init__(chat_id=chat_id, prev_event_ids=['work_audio'], event_id="work_sick",
                         message_text='Weil du spontan starke Zahnschmerzen bekommen hast, gehst du zum Arzt. Dieser stellt fest, dass du auf Grund deiner mangelnden Zahnhygiene eine aufwändige Zahnbehandlung brauchst, die die Kasse nicht übernimmmt.',
                         buttons=[{'text': 'Gabs da nicht so nigerianische Prinzen...?', 'next_event_id': 'random_positive'}])

    def set_profile_attribute(self, attribute, value):
        pass

    def set_account(self, account: str):
        pass

    @staticmethod
    def is_available(profile) -> bool:
        pass

