from event_base.event import EventBase


class WorkAudio(EventBase):
    def __init__(self, chat_id: int):
        super().__init__(chat_id=chat_id, prev_event_ids=['phishing'], event_id="work_audio",
                         message_text='Da die Kollegen zu laut Kuchen essen, brauchst du Musik zur Konzentration. Zurück in der Playlist von gestern siehst du noch ein paar weitere passende Musikvorschläge. Jetzt bist du endgültig abgelenkt und schreibst mit deinem Partner. Mmmh, du hast hier so schöne Bilder von dir...',
                         buttons=[{'text': 'Sharing is caring', 'next_event_id': 'work_fired'},
                                  {'text': 'Doch nicht während der Arbeitszeit', 'next_event_id': 'work_sick'}])

    def set_profile_attribute(self, attribute, value):
        pass

    def set_account(self, account: str):
        pass

    @staticmethod
    def is_available(profile) -> bool:
        pass

