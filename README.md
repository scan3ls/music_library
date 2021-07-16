# music_library

## Description
A Python web application running Flask.
Serves dummy music data for use in another project [ipod_app](https://github.com/scan3ls/ipod_app)
Processes requests to serve data from a MySQL database

Hosted through Heroku [here](https://salty-oasis-19252.herokuapp.com/)

## Endpoints

- `GET /`: Pings the database for all albums
      Output:
        {
          "Albums": [
            {
                "artist": "Band Name",
                "cover": "Link to cover art",
                "id": "########-####-####-####-############",
                "name": "Album Name",
                "songs": [
                    ########-####-####-####-############,
                    ...
                ]
            },
            ...
          ]
        }

- `GET /albums`: Pings the database for all albums
      Output:
      {
        "Albums": [
          {
              "artist": "Band Name",
              "cover": "Link to cover art",
              "id": "########-####-####-####-############",
              "name": "Album Name",
              "songs": [
                  ########-####-####-####-############,
                  ...
              ]
          },
          ...
        ]
      }

- `GET /artists`: Pings the database for all artists
      Output:
      {
        "Artists": [
          {
            "albums": [
              "########-####-####-####-############",
              ...
            ],
            "id": "########-####-####-####-############",
            "name": "Artist Name",
            "songs": [
              "########-####-####-####-############",
              ...
            ]
          },
          ...
        ]
      }

- `Get /songs`: Pings the database for all songs
      Output:
      {
        "Songs": [
            {
            "album": "Album Name",
            "artist": "Artist Name",
            "id": "########-####-####-####-############",
            "name": "Song Name"
            },
            ...
        ]
      }

## Bugs
Current build is unstable.
Some request may not be able to connect to the database.
On failure the response will look like: `{"Artists":"artist"}`
Reloading the page should or retrying the request should fix this.
