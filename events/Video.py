from event_base.event import EventBase


class Video(EventBase):
    def __init__(self, chat_id: int):
        super().__init__(chat_id=chat_id, prev_event_ids=["media_start_media"],
                         event_id="video",
                         buttons=[{'text': 'Ich schaue mir meine DVDs im Regal an.', 'next_event_id': 'video', 'decision_id': None},
                                  {'text': 'Netflix und Chill!', 'next_event_id': 'video', 'decision_id': 'Netflix' },
                                  {'text': 'Ab zu youtube', 'next_event_id': 'video' , 'decision_id': 'Youtube'},
                                  {'text': 'Mal den Fernseher anschmeißen', 'next_event_id': 'video', 'decision_id': None}],
                         message_text="Nach der ganzen Musik möchtest du was gucken. Was tust du",)

    def is_available(profile):
        return True

    @staticmethod
    def react(profile, decision_id):
        if decision_id is not None:
            profile['account'] = str(decision_id)
            return profile
        return None
