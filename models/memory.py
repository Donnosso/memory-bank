class Memory:

    def __init__(self, title, date, mood, journal):
        self.title = title
        self.date = date
        self.mood = mood
        self.journal = journal

    def to_dict(self):
        return {
            "title": self.title,
            "date": self.date,
            "mood": self.mood,
            "journal": self.journal
        }
    @classmethod
    def from_dict(cls, data):
        return cls(data['title'], data['date'], data['mood'], data['journal'])
