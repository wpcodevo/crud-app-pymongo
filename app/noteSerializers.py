def noteEntity(note) -> dict:
    return {
        "id": str(note["_id"]),
        "title": note["title"],
        "category": note["category"],
        "content": note["content"],
        "published": note["published"],
        "createdAt": note["createdAt"],
        "updatedAt": note["updatedAt"]
    }


def populatednoteEntity(note) -> dict:
    return {
        "id": str(note["_id"]),
        "title": note["title"],
        "category": note["category"],
        "content": note["content"],
        "published": note["published"],
        "createdAt": note["createdAt"],
        "updatedAt": note["updatedAt"]
    }


def noteListEntity(notes) -> list:
    return [populatednoteEntity(note) for note in notes]
