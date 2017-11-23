from model.base_model import BaseModel


# inherit from leancloud model
class UserInfo(BaseModel):
    def __init__(self):
        attrs = ['user', 'nickname', 'avatar', 'location', 'type']
        super().__init__(attrs)
