from event_base.event import EventBase


class MediaVideo(EventBase):
    def __init__(self, chat_id: int):
        event_id = "creation_age"
        super().__init__(chat_id=chat_id, prev_event_ids=["media_start_media"],
                         event_id="media_start_media" ,
                         buttons=[{'text': 'Ich schaue mir meine DVDs im Regal an.', 'next_event_id': 'video'},
                                  {'text': 'Netflix und Chill!', 'next_event_id': 'video'},
                                  {'text': 'Ab zu youtube', 'next_event_id': 'video'},
                                  {'text': 'Mal den Fernseher anschmeißen', 'next_event_id': 'video'}],
                         message_text="Nach der ganzen Musik möchtest du was gucken. Was tust du",)

    def is_available(profile):
        return True
