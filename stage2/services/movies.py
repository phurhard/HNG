async def get_movies(
    data: dict
):
    # building the response
    response = {
        "jsonrpc": "2.0",
        "id": data.get("id"),
        "result": {
            "id": data.get("id"),
            "contextId": "generated-context-id",
            "status": "success",
            "message": "Movies fetched successfully",
        },
        "artifacts": [
                {
                    "artifactId": "artifact-uuid1",
                    "name": "The Shawshank Redemption",
                    "parts": [
                        {
                            "kind": "text",
                            "text": "Some kind of text"
                        }
                    ]
                },
                {
                    "artifactId": "artifact-uuid2",
                    "name": "The Dark Knight",
                    "parts": [
                        {
                            "kind": "data",
                            "data": {
                                "year": 2008,
                                "rating": 9.0
                            }
                        }
                    ]
                },
                {
                    "artifactId": "artifact-uuid3",
                    "name": "The Dark Knight Rises",
                    "parts": [
                        {
                            "kind": "data",
                            "data": {
                                "year": 2012,
                                "rating": 8.5
                            }
                        }
                    ]
                }
            ]
    }

    # response = {
    #     "jsonrpc": "2.0",
    #     "id": "test-001",
    #     "result": {
    #         "id": "task-001",
    #         "contextId": "generated-context-id",
    #         "status": {
    #             "state": "input-required",
    #             "timestamp": "2025-10-26T10:30:00.000Z",
    #             "message": {
    #                 "messageId": "msg-uuid",
    #                 "role": "agent",
    #                 "parts": [
    #                     {
    #                         "kind": "text",
    #                         "text": "I played e5"
    #                     }
    #                 ],
    #                 "kind": "message",
    #                 "taskId": "task-001"
    #             }
    #         },
    #         "artifacts": [
    #             {
    #                 "artifactId": "artifact-uuid",
    #                 "name": "move",
    #                 "parts": [
    #                     {
    #                         "kind": "text",
    #                         "text": "e5"
    #                     }
    #                 ]
    #             },
    #             {
    #                 "artifactId": "artifact-uuid-2",
    #                 "name": "board",
    #                 "parts": [
    #                     {
    #                         "kind": "file",
    #                         "file_url": "http://localhost:9000/chess-boards/context-id/task-001.png"
    #                     }
    #                 ]
    #             }
    #         ],
    #         "history": [""],
    #         "kind": "task"
    #     }
    # }
    return response
