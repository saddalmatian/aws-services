from models.domains import message as message_domain


class MessageIn(message_domain.Message):
    pass

class MessageResp(message_domain.MessageInDB):
    pass