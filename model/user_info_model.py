import model.base_model

# inherit from leancloud model
class UserInfo(model.base_model.BaseModel):
    def __init__(self):
        attrs=['user','nickname','avatar','location','type']
        super().__init__(attrs)