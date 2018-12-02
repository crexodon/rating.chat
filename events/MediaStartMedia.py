from event_base.event import EventBase


class MediaStartMedia(EventBase):
    def __init__(self, chat_id: int):

        super().__init__(chat_id=chat_id, prev_event_ids=["creation_sex"],
                         event_id="media_start_media",
                         buttons=[{'text':'Ich mache das Radio an', 'next_event_id': 'restmusic', 'decision_id': None},
                                  {'text': 'Ich öffne Spotify', 'next_event_id': 'restmusic', 'decision_id': 'Spotify'},
                                  {'text': 'Hey, Alexa...', 'next_event_id': 'restmusic', 'decision_id': 'Amazon'},
                                  {'text': 'Ich gehe zu youtube', 'next_event_id': 'video', 'decision_id': 'Youtube'}],
                         message_text="Du hast Feierabend und bist zu Hause. Da es etwas ruhig ist, möchtest du Musik hören. Wie machst du das?",)


    def is_available(profile):
        return True

    @staticmethod
    def react(profile, decision_id):
        if decision_id is not None:
            profile['account'] = str(decision_id)
            return profile
        return None
