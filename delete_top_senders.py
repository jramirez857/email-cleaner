from deleter import Deleter
from top_senders import TopSenders


class DeleteTopSenders(Deleter):
    def __init__(self, **kwargs):
        self.top_senders = TopSenders()

    def delete(self):
        senders = self.top_senders.get(num_emails=100)
        print(senders)
        Deleter(top_n_senders=senders, num_emails=100).delete_emails()


if __name__ == "__main__":
    DeleteTopSenders().delete()
