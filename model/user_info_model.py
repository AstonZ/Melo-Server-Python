from model.base_model import BaseModel


# inherit from leancloud model
class UserInfo(BaseModel):
    def __init__(self):
        super().__init__(['user', 'nickname', 'avatar', 'location', 'type'])
