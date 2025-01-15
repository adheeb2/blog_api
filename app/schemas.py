from pydantic import BaseModel

class GreetingBase(BaseModel):
    message: str

class GreetingCreate(GreetingBase):
    pass
class Greeting(GreetingBase):
    id : int

