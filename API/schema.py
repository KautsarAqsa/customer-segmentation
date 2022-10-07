from pydantic import BaseModel


# Clustering API request data model
class Item(BaseModel):
    sex: int
    marital_status: int
    age: int
    education: int
    income: int
    occupation: int
    settlement_size: int	