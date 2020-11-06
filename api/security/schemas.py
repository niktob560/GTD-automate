import security.models
from ninja import Schema
from pydantic_django import PydanticDjangoModel

class TokenIn(PydanticDjangoModel):
    def get_object(self):
        o = security.models.LongToken()
        o.token = self.token
        return o
    class Config:
        model = security.models.LongToken
        orm_mode = True
        exclude = ('id', 'expiringtoken')


class TokenOut(PydanticDjangoModel):
    def get_object(self):
        o = security.models.ExpiringToken()
        o.token = self.token
        o.expire_at = self.expire_at
        o.owner_token = self.owner_token
        return o
    class Config:
        model = security.models.ExpiringToken
        orm_mode = True
