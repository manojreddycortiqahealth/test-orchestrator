from pydantic import BaseModel

class Settings(BaseModel):
    model: str = "fake-model"

class SuggestionContext(BaseModel):
    record_id: str
    text: str

class Suggestion(BaseModel):
    title: str
    score: float

class SuggestionPayload(BaseModel):
    record_id: str
    suggestions: list[Suggestion]
    orchestrator_version: str
