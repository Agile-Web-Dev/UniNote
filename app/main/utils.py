def get_default_links(class_id):
    links = [
        {
            "name": "Chat",
            "icon": "bi-chat-text",
            "url": f"/{class_id}/chatroom",
        },
        {
            "name": "Notes",
            "icon": "bi-pencil-square",
            "url": f"/{class_id}/notes",
        },
    ]

    return links
