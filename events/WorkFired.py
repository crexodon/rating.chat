from event_base.event import EventBase


class WorkFired(EventBase):
    def __init__(self, chat_id: int):
        super().__init__(chat_id=chat_id, prev_event_ids=['work_audio'], event_id="work_fired",
                         message_text='Wer hätte geahnt, dass dein Partner alle Bilder in die Cloud synct. Mit den Nacktbildern nimmt dich jetzt erstmal keiner auf der Arbeit ernst, sorry ^^',
                         buttons=[{'text': 'Noch eine Runde?', 'next_event_id': 'media_start_media'}])

    def set_profile_attribute(self, attribute, value):
        pass

    def set_account(self, account: str):
        pass

    @staticmethod
    def is_available(profile) -> bool:
        pass

