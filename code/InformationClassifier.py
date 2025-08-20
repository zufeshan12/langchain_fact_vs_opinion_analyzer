from pydantic import BaseModel,Field
from typing import Optional,Literal

class InfoClassifier(BaseModel):
    # class attributes
    statement: str = Field(description="statement made by user")
    classifier_output: Literal['fact','opinion','ambiguous'] = Field(description="Given the user statement, classify the statement as fact, opinion or ambiguous")
