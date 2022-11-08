from datetime import datetime
from typing import List
from pydantic import BaseModel
from bson.objectid import ObjectId


class NoteBaseSchema(BaseModel):
    id: str | None = None
    title: str
    content: str
    category: str | None = None
    published: bool = False
    createdAt: datetime | None = None
    updatedAt: datetime | None = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class UpdateNoteSchema(BaseModel):
    title: str | None = None
    content: str | None = None
    category: str | None = None
    published: bool | None = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class ListNoteResponse(BaseModel):
    status: str
    results: int
    notes: List[NoteBaseSchema]
