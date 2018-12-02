from event_base.event import EventBase


class StartDate(EventBase):
    def __init__(self, chat_id: int):
        super().__init__(chat_id=chat_id, prev_event_ids=['media_video'], event_id="start_date",
                         message_text="Da es so unterhaltsam ist schläfst du einfach ein...und schon klingelt der "
                                      "Wecker. Guten Morgen! Dein Handy erinnert dich: In zwei Tagen ist Datenight "
                                      "und du bist mit planen dran.",
                         buttons=[{'text': 'Ganz klassisch ins Kino', 'next_event_id': 'start_transport'},
                                  {'text': 'Netflix und Chill!', 'next_event_id': 'start_transport'},
                                  {'text': 'Ein kleines Barkonzert steht an', 'next_event_id': 'start_transport'}])

    @staticmethod
    def is_available(profile) -> bool:
        pass

