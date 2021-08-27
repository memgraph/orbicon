def memberGraph():
    return {
        "nodes": [
            {
                "id": 1,
                "label": "mbudiselicbuda",
                "shape": "circularImage",
                "image": "https://avatars.githubusercontent.com/u/4950251?s=88&v=4",
                "title": "Ovo je njonjo",
                "size": 100,
                "borderWidth": 10,
                "color": {"border": "green"},
            },
            {"id": 2, "label": "mbudiselicbuda", "shape": "ellipse", "borderWidth": 5, "color": {"border": "green"}},
            {"id": 3, "label": "mbudiselicbuda", "shape": "database"},
            {"id": 4, "label": "mbudiselicbuda", "image": "https://avatars.githubusercontent.com/u/4950251?s=88&v=4"},
            {"id": 5, "label": "mbudiselicbuda", "shape": "diamond"},
            {"id": 6, "label": "mbudiselicbuda", "shape": "dot"},
            {"id": 7, "label": "mbudiselicbuda", "shape": "square"},
            {"id": 8, "label": "mbudiselicbuda", "shape": "triangle"},
        ],
        "edges": [
            {"from": 1, "to": 2},
            {"from": 2, "to": 3, 2: "to"},
            {"from": 3, "to": 2, "arrows": "to"},
            {"from": 2, "to": 4},
            {"from": 2, "to": 5},
            {"from": 5, "to": 6},
            {"from": 5, "to": 7},
            {"from": 6, "to": 8},
        ],
    }


def usernames():
    return {
        "usernames": [
            {
                "username": "Gitbuda",
            },
            {
                "username": "afico",
            },
            {
                "username": "jmrden",
            },
            {
                "username": "jmatak",
            },
            {
                "username": "cofi",
            },
        ]
    }


def userDetails():
    return {
        "username": "Gitbuda",
        "firstName": "Marko",
        "lastName": "Budiselic",
        "love": 10.2,
        "avatar": "https://avatars.githubusercontent.com/u/4950251?s=88&v=4",
        "community": "Feature, not bug",
        "importance": 50.5,
        "company": "Memgraph",
        "githubAccount": "https://github.com/gitbuda",
        "twitterAccount": "https://twitter.com/mbudiselicbuda",
        "twitterUsername": "twitterBuda",
        "githubUsername": "gitBuda",
    }


def activities():
    return {
        "activities": [
            {
                "username": "Gitbuda",
                "action": "PR_MAKE",
                "description": "This guy made a PR!",
                "date": "2020-01-01T08:00:00",
            },
            {
                "username": "Gitbuda2",
                "action": "PR_MAKE2",
                "description": "This guy made a PR!",
                "date": "2020-01-01T08:00:00",
            },
            {
                "username": "Gitbuda3",
                "action": "PR_MAKE3",
                "description": "This guy made a PR!",
                "date": "2020-01-01T08:00:00",
            },
            {
                "username": "Gitbuda",
                "action": "PR_MAKE",
                "description": "This guy made a PR!",
                "date": "2020-01-01T08:00:00",
            },
            {
                "username": "Gitbuda2",
                "action": "PR_MAKE2",
                "description": "This guy made a PR!",
                "date": "2020-01-01T08:00:00",
            },
            {
                "username": "Gitbuda3",
                "action": "PR_MAKE3",
                "description": "This guy made a PR!",
                "date": "2020-01-01T08:00:00",
            },
            {
                "username": "Gitbuda",
                "action": "PR_MAKE",
                "description": "This guy made a PR!",
                "date": "2020-01-01T08:00:00",
            },
            {
                "username": "Gitbuda2",
                "action": "PR_MAKE2",
                "description": "This guy made a PR!",
                "date": "2020-01-01T08:00:00",
            },
            {
                "username": "Gitbuda3",
                "action": "PR_MAKE3",
                "description": "This guy made a PR!",
                "date": "2020-01-01T08:00:00",
            },
            {
                "username": "Gitbuda",
                "action": "PR_MAKE",
                "description": "This guy made a PR!",
                "date": "2020-01-01T08:00:00",
            },
            {
                "username": "Gitbuda2",
                "action": "PR_MAKE2",
                "description": "This guy made a PR!",
                "date": "2020-01-01T08:00:00",
            },
            {
                "username": "Gitbuda3",
                "action": "PR_MAKE3",
                "description": "This guy made a PR!",
                "date": "2020-01-01T08:00:00",
            },
        ]
    }
