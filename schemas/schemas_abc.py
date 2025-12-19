from pydantic import BaseModel, Field


class AbcModel(BaseModel):
    abc: str = Field(
        Ellipsis,
        min_length=2,
        max_length=40,
        deprecated=False,
    )
    
#--------------------------------------------------------------------------

class AbcDisplay(BaseModel):
    id: int
    abc: str
    
    class ConfigDict:
        from_attributes = True
