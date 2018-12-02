
from event_base.event import EventBase


class Restmusik(EventBase):
    def __init__(self, chat_id: int):
        super().__init__(chat_id=chat_id, prev_event_ids=["media_start_media"],
                         event_id="restmusik" ,
                         buttons=[{'text': 'Per Whatsapp mit Manni teilen', 'next_event_id': 'video'},
                                  {'text': 'Ab auf facebook damit', 'next_event_id': 'video'},
                                  {'text': 'Ab zu youtube', 'next_event_id': 'video'}],
                         message_text='Du entdeckst ein super cooles Lied...',)

    def is_available(profile):
        return True
