from pydantic import BaseModel

class SubSection(BaseModel):
    header: str
    contentLines: list
    #def __init__(self, header, contentLines):
      #  self.header = header
      #  self.contentLines = contentLines
    
    def __str__(self):
        return f"Header={self.header} Lines={self.contentLines}"

