from event_base.event import EventBase


class Restmusik(EventBase):
    def __init__(self, chat_id: int):
        event_id = "restmusik"
        super().__init__(chat_id=chat_id, prev_event_ids=["creation_sex<<w"],
                         event_id="media_start_media" ,
                         buttons=[{'text' :'Ich mache das Radio an', 'next_event_id': 'restmusic'},
                                  {'text': 'Ich öffne Spotify', 'next_event_id': 'restmusic'},
                                  {'text': 'Hey, Alexa...', 'next_event_id': 'restmusic'},
                                  {'text': 'Ich gehe zu youtube', 'next_event_id': 'video'}],
                         message_text="Du hast Feierabend und bist zu Hause. Da es etwas ruhig ist, möchtest du Musik hören. Wie machst du das?",)


    def is_available(profile):
        return True
