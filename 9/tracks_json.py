import json

jstring = """
{
  "tracks": [
    {
      "album": {
        "album_type": "album",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/5l8VQNuIg0turYE1VtM9zV"
            },
            "href": "https://api.spotify.com/v1/artists/5l8VQNuIg0turYE1VtM9zV",
            "id": "5l8VQNuIg0turYE1VtM9zV",
            "name": "Leonard Cohen",
            "type": "artist",
            "uri": "spotify:artist:5l8VQNuIg0turYE1VtM9zV"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/album/6I58qJMqZHhb8jtNT3CuJB"
        },
        "href": "https://api.spotify.com/v1/albums/6I58qJMqZHhb8jtNT3CuJB",
        "id": "6I58qJMqZHhb8jtNT3CuJB",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ab67616d0000b2738c56267153920f9c0df36c5b",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/ab67616d00001e028c56267153920f9c0df36c5b",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/ab67616d000048518c56267153920f9c0df36c5b",
            "width": 64
          }
        ],
        "name": "Various Positions",
        "release_date": "1984-12-11",
        "release_date_precision": "day",
        "total_tracks": 9,
        "type": "album",
        "uri": "spotify:album:6I58qJMqZHhb8jtNT3CuJB"
      },
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/5l8VQNuIg0turYE1VtM9zV"
          },
          "href": "https://api.spotify.com/v1/artists/5l8VQNuIg0turYE1VtM9zV",
          "id": "5l8VQNuIg0turYE1VtM9zV",
          "name": "Leonard Cohen",
          "type": "artist",
          "uri": "spotify:artist:5l8VQNuIg0turYE1VtM9zV"
        }
      ],
      "disc_number": 1,
      "duration_ms": 277160,
      "explicit": false,
      "external_ids": {
        "isrc": "USSM10026643"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/track/7yzbimr8WVyAtBX3Eg6UL9"
      },
      "href": "https://api.spotify.com/v1/tracks/7yzbimr8WVyAtBX3Eg6UL9",
      "id": "7yzbimr8WVyAtBX3Eg6UL9",
      "is_local": false,
      "is_playable": true,
      "name": "Hallelujah",
      "popularity": 65,
      "preview_url": "https://p.scdn.co/mp3-preview/d26172635462cd43756f9a7bd30c1e0f68334954?cid=774b29d4f13844c495f206cafdad9c86",
      "track_number": 5,
      "type": "track",
      "uri": "spotify:track:7yzbimr8WVyAtBX3Eg6UL9"
    },
    {
      "album": {
        "album_type": "album",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/5l8VQNuIg0turYE1VtM9zV"
            },
            "href": "https://api.spotify.com/v1/artists/5l8VQNuIg0turYE1VtM9zV",
            "id": "5l8VQNuIg0turYE1VtM9zV",
            "name": "Leonard Cohen",
            "type": "artist",
            "uri": "spotify:artist:5l8VQNuIg0turYE1VtM9zV"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/album/2Aiv0ThDpFa7lqHphR6MN5"
        },
        "href": "https://api.spotify.com/v1/albums/2Aiv0ThDpFa7lqHphR6MN5",
        "id": "2Aiv0ThDpFa7lqHphR6MN5",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ab67616d0000b2730633b57b08b40f3e776e7151",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/ab67616d00001e020633b57b08b40f3e776e7151",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/ab67616d000048510633b57b08b40f3e776e7151",
            "width": 64
          }
        ],
        "name": "Songs Of Leonard Cohen",
        "release_date": "1967-12-27",
        "release_date_precision": "day",
        "total_tracks": 10,
        "type": "album",
        "uri": "spotify:album:2Aiv0ThDpFa7lqHphR6MN5"
      },
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/5l8VQNuIg0turYE1VtM9zV"
          },
          "href": "https://api.spotify.com/v1/artists/5l8VQNuIg0turYE1VtM9zV",
          "id": "5l8VQNuIg0turYE1VtM9zV",
          "name": "Leonard Cohen",
          "type": "artist",
          "uri": "spotify:artist:5l8VQNuIg0turYE1VtM9zV"
        }
      ],
      "disc_number": 1,
      "duration_ms": 229293,
      "explicit": false,
      "external_ids": {
        "isrc": "USSM16701039"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/track/2L93TdW2GMue1H2zlkt30F"
      },
      "href": "https://api.spotify.com/v1/tracks/2L93TdW2GMue1H2zlkt30F",
      "id": "2L93TdW2GMue1H2zlkt30F",
      "is_local": false,
      "is_playable": true,
      "name": "Suzanne",
      "popularity": 64,
      "preview_url": "https://p.scdn.co/mp3-preview/637b849f30d743cd55a41b0ccc3af8d143ad9380?cid=774b29d4f13844c495f206cafdad9c86",
      "track_number": 1,
      "type": "track",
      "uri": "spotify:track:2L93TdW2GMue1H2zlkt30F"
    },
    {
      "album": {
        "album_type": "album",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/5l8VQNuIg0turYE1VtM9zV"
            },
            "href": "https://api.spotify.com/v1/artists/5l8VQNuIg0turYE1VtM9zV",
            "id": "5l8VQNuIg0turYE1VtM9zV",
            "name": "Leonard Cohen",
            "type": "artist",
            "uri": "spotify:artist:5l8VQNuIg0turYE1VtM9zV"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/album/3jeTB3j3QmUs8SPIVleHtU"
        },
        "href": "https://api.spotify.com/v1/albums/3jeTB3j3QmUs8SPIVleHtU",
        "id": "3jeTB3j3QmUs8SPIVleHtU",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ab67616d0000b2738fc3f01275cae3d8ecb1c26b",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/ab67616d00001e028fc3f01275cae3d8ecb1c26b",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/ab67616d000048518fc3f01275cae3d8ecb1c26b",
            "width": 64
          }
        ],
        "name": "You Want It Darker",
        "release_date": "2016-10-21",
        "release_date_precision": "day",
        "total_tracks": 9,
        "type": "album",
        "uri": "spotify:album:3jeTB3j3QmUs8SPIVleHtU"
      },
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/5l8VQNuIg0turYE1VtM9zV"
          },
          "href": "https://api.spotify.com/v1/artists/5l8VQNuIg0turYE1VtM9zV",
          "id": "5l8VQNuIg0turYE1VtM9zV",
          "name": "Leonard Cohen",
          "type": "artist",
          "uri": "spotify:artist:5l8VQNuIg0turYE1VtM9zV"
        }
      ],
      "disc_number": 1,
      "duration_ms": 284373,
      "explicit": false,
      "external_ids": {
        "isrc": "CAC221600005"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/track/5zb7npjQqoJ7Kcpq4yD9qn"
      },
      "href": "https://api.spotify.com/v1/tracks/5zb7npjQqoJ7Kcpq4yD9qn",
      "id": "5zb7npjQqoJ7Kcpq4yD9qn",
      "is_local": false,
      "is_playable": true,
      "name": "You Want It Darker",
      "popularity": 62,
      "preview_url": "https://p.scdn.co/mp3-preview/e922198e01ae3b8bf47a641e175961de07678449?cid=774b29d4f13844c495f206cafdad9c86",
      "track_number": 1,
      "type": "track",
      "uri": "spotify:track:5zb7npjQqoJ7Kcpq4yD9qn"
    },
    {
      "album": {
        "album_type": "album",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/5l8VQNuIg0turYE1VtM9zV"
            },
            "href": "https://api.spotify.com/v1/artists/5l8VQNuIg0turYE1VtM9zV",
            "id": "5l8VQNuIg0turYE1VtM9zV",
            "name": "Leonard Cohen",
            "type": "artist",
            "uri": "spotify:artist:5l8VQNuIg0turYE1VtM9zV"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/album/6I58qJMqZHhb8jtNT3CuJB"
        },
        "href": "https://api.spotify.com/v1/albums/6I58qJMqZHhb8jtNT3CuJB",
        "id": "6I58qJMqZHhb8jtNT3CuJB",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ab67616d0000b2738c56267153920f9c0df36c5b",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/ab67616d00001e028c56267153920f9c0df36c5b",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/ab67616d000048518c56267153920f9c0df36c5b",
            "width": 64
          }
        ],
        "name": "Various Positions",
        "release_date": "1984-12-11",
        "release_date_precision": "day",
        "total_tracks": 9,
        "type": "album",
        "uri": "spotify:album:6I58qJMqZHhb8jtNT3CuJB"
      },
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/5l8VQNuIg0turYE1VtM9zV"
          },
          "href": "https://api.spotify.com/v1/artists/5l8VQNuIg0turYE1VtM9zV",
          "id": "5l8VQNuIg0turYE1VtM9zV",
          "name": "Leonard Cohen",
          "type": "artist",
          "uri": "spotify:artist:5l8VQNuIg0turYE1VtM9zV"
        }
      ],
      "disc_number": 1,
      "duration_ms": 280626,
      "explicit": false,
      "external_ids": {
        "isrc": "USSM10026189"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/track/3mFzIFFFmEXTQs6BDAK2ZZ"
      },
      "href": "https://api.spotify.com/v1/tracks/3mFzIFFFmEXTQs6BDAK2ZZ",
      "id": "3mFzIFFFmEXTQs6BDAK2ZZ",
      "is_local": false,
      "is_playable": true,
      "name": "Dance Me to the End of Love",
      "popularity": 62,
      "preview_url": "https://p.scdn.co/mp3-preview/2df9770cd2bf09efa5d55ae1fc0dd0ba1f141325?cid=774b29d4f13844c495f206cafdad9c86",
      "track_number": 1,
      "type": "track",
      "uri": "spotify:track:3mFzIFFFmEXTQs6BDAK2ZZ"
    },
    {
      "album": {
        "album_type": "album",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/5l8VQNuIg0turYE1VtM9zV"
            },
            "href": "https://api.spotify.com/v1/artists/5l8VQNuIg0turYE1VtM9zV",
            "id": "5l8VQNuIg0turYE1VtM9zV",
            "name": "Leonard Cohen",
            "type": "artist",
            "uri": "spotify:artist:5l8VQNuIg0turYE1VtM9zV"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/album/2Om4oR7plGGub1aYe5uB7B"
        },
        "href": "https://api.spotify.com/v1/albums/2Om4oR7plGGub1aYe5uB7B",
        "id": "2Om4oR7plGGub1aYe5uB7B",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ab67616d0000b2736a0b525ea5e6146f7f33369f",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/ab67616d00001e026a0b525ea5e6146f7f33369f",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/ab67616d000048516a0b525ea5e6146f7f33369f",
            "width": 64
          }
        ],
        "name": "Songs Of Love And Hate",
        "release_date": "1971-03-19",
        "release_date_precision": "day",
        "total_tracks": 8,
        "type": "album",
        "uri": "spotify:album:2Om4oR7plGGub1aYe5uB7B"
      },
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/5l8VQNuIg0turYE1VtM9zV"
          },
          "href": "https://api.spotify.com/v1/artists/5l8VQNuIg0turYE1VtM9zV",
          "id": "5l8VQNuIg0turYE1VtM9zV",
          "name": "Leonard Cohen",
          "type": "artist",
          "uri": "spotify:artist:5l8VQNuIg0turYE1VtM9zV"
        }
      ],
      "disc_number": 1,
      "duration_ms": 310773,
      "explicit": false,
      "external_ids": {
        "isrc": "USSM19919473"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/track/77K5TB5KZmDZCoJCdd1NvE"
      },
      "href": "https://api.spotify.com/v1/tracks/77K5TB5KZmDZCoJCdd1NvE",
      "id": "77K5TB5KZmDZCoJCdd1NvE",
      "is_local": false,
      "is_playable": true,
      "name": "Famous Blue Raincoat",
      "popularity": 61,
      "preview_url": "https://p.scdn.co/mp3-preview/85951977b0306650021f46b836b79d5c68522a75?cid=774b29d4f13844c495f206cafdad9c86",
      "track_number": 6,
      "type": "track",
      "uri": "spotify:track:77K5TB5KZmDZCoJCdd1NvE"
    },
    {
      "album": {
        "album_type": "album",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/5l8VQNuIg0turYE1VtM9zV"
            },
            "href": "https://api.spotify.com/v1/artists/5l8VQNuIg0turYE1VtM9zV",
            "id": "5l8VQNuIg0turYE1VtM9zV",
            "name": "Leonard Cohen",
            "type": "artist",
            "uri": "spotify:artist:5l8VQNuIg0turYE1VtM9zV"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/album/2Aiv0ThDpFa7lqHphR6MN5"
        },
        "href": "https://api.spotify.com/v1/albums/2Aiv0ThDpFa7lqHphR6MN5",
        "id": "2Aiv0ThDpFa7lqHphR6MN5",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ab67616d0000b2730633b57b08b40f3e776e7151",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/ab67616d00001e020633b57b08b40f3e776e7151",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/ab67616d000048510633b57b08b40f3e776e7151",
            "width": 64
          }
        ],
        "name": "Songs Of Leonard Cohen",
        "release_date": "1967-12-27",
        "release_date_precision": "day",
        "total_tracks": 10,
        "type": "album",
        "uri": "spotify:album:2Aiv0ThDpFa7lqHphR6MN5"
      },
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/5l8VQNuIg0turYE1VtM9zV"
          },
          "href": "https://api.spotify.com/v1/artists/5l8VQNuIg0turYE1VtM9zV",
          "id": "5l8VQNuIg0turYE1VtM9zV",
          "name": "Leonard Cohen",
          "type": "artist",
          "uri": "spotify:artist:5l8VQNuIg0turYE1VtM9zV"
        }
      ],
      "disc_number": 1,
      "duration_ms": 340560,
      "explicit": false,
      "external_ids": {
        "isrc": "USSM10013406"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/track/14CsqOaDkOkrZ49UJLtuOJ"
      },
      "href": "https://api.spotify.com/v1/tracks/14CsqOaDkOkrZ49UJLtuOJ",
      "id": "14CsqOaDkOkrZ49UJLtuOJ",
      "is_local": false,
      "is_playable": true,
      "name": "So Long, Marianne",
      "popularity": 59,
      "preview_url": "https://p.scdn.co/mp3-preview/21fca53f92d500291aeac46159763cbce789209c?cid=774b29d4f13844c495f206cafdad9c86",
      "track_number": 6,
      "type": "track",
      "uri": "spotify:track:14CsqOaDkOkrZ49UJLtuOJ"
    },
    {
      "album": {
        "album_type": "album",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/5l8VQNuIg0turYE1VtM9zV"
            },
            "href": "https://api.spotify.com/v1/artists/5l8VQNuIg0turYE1VtM9zV",
            "id": "5l8VQNuIg0turYE1VtM9zV",
            "name": "Leonard Cohen",
            "type": "artist",
            "uri": "spotify:artist:5l8VQNuIg0turYE1VtM9zV"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/album/3gUw30X6A7WEGcRdv1nFr9"
        },
        "href": "https://api.spotify.com/v1/albums/3gUw30X6A7WEGcRdv1nFr9",
        "id": "3gUw30X6A7WEGcRdv1nFr9",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ab67616d0000b27325b12e3030dcf540319f687e",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/ab67616d00001e0225b12e3030dcf540319f687e",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/ab67616d0000485125b12e3030dcf540319f687e",
            "width": 64
          }
        ],
        "name": "I'm Your Man",
        "release_date": "1988-02-02",
        "release_date_precision": "day",
        "total_tracks": 8,
        "type": "album",
        "uri": "spotify:album:3gUw30X6A7WEGcRdv1nFr9"
      },
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/5l8VQNuIg0turYE1VtM9zV"
          },
          "href": "https://api.spotify.com/v1/artists/5l8VQNuIg0turYE1VtM9zV",
          "id": "5l8VQNuIg0turYE1VtM9zV",
          "name": "Leonard Cohen",
          "type": "artist",
          "uri": "spotify:artist:5l8VQNuIg0turYE1VtM9zV"
        }
      ],
      "disc_number": 1,
      "duration_ms": 265186,
      "explicit": false,
      "external_ids": {
        "isrc": "USSM10027492"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/track/5atFAXIgMXP378op4FaxBm"
      },
      "href": "https://api.spotify.com/v1/tracks/5atFAXIgMXP378op4FaxBm",
      "id": "5atFAXIgMXP378op4FaxBm",
      "is_local": false,
      "is_playable": true,
      "name": "I'm Your Man",
      "popularity": 57,
      "preview_url": "https://p.scdn.co/mp3-preview/9ed21388ece9be71c17deb4e8199148b748d81ce?cid=774b29d4f13844c495f206cafdad9c86",
      "track_number": 4,
      "type": "track",
      "uri": "spotify:track:5atFAXIgMXP378op4FaxBm"
    },
    {
      "album": {
        "album_type": "album",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/5l8VQNuIg0turYE1VtM9zV"
            },
            "href": "https://api.spotify.com/v1/artists/5l8VQNuIg0turYE1VtM9zV",
            "id": "5l8VQNuIg0turYE1VtM9zV",
            "name": "Leonard Cohen",
            "type": "artist",
            "uri": "spotify:artist:5l8VQNuIg0turYE1VtM9zV"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/album/3gUw30X6A7WEGcRdv1nFr9"
        },
        "href": "https://api.spotify.com/v1/albums/3gUw30X6A7WEGcRdv1nFr9",
        "id": "3gUw30X6A7WEGcRdv1nFr9",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ab67616d0000b27325b12e3030dcf540319f687e",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/ab67616d00001e0225b12e3030dcf540319f687e",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/ab67616d0000485125b12e3030dcf540319f687e",
            "width": 64
          }
        ],
        "name": "I'm Your Man",
        "release_date": "1988-02-02",
        "release_date_precision": "day",
        "total_tracks": 8,
        "type": "album",
        "uri": "spotify:album:3gUw30X6A7WEGcRdv1nFr9"
      },
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/5l8VQNuIg0turYE1VtM9zV"
          },
          "href": "https://api.spotify.com/v1/artists/5l8VQNuIg0turYE1VtM9zV",
          "id": "5l8VQNuIg0turYE1VtM9zV",
          "name": "Leonard Cohen",
          "type": "artist",
          "uri": "spotify:artist:5l8VQNuIg0turYE1VtM9zV"
        }
      ],
      "disc_number": 1,
      "duration_ms": 334866,
      "explicit": false,
      "external_ids": {
        "isrc": "USSM10027491"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/track/60s0QWaOZ2UTzqdIHBCt3x"
      },
      "href": "https://api.spotify.com/v1/tracks/60s0QWaOZ2UTzqdIHBCt3x",
      "id": "60s0QWaOZ2UTzqdIHBCt3x",
      "is_local": false,
      "is_playable": true,
      "name": "Everybody Knows",
      "popularity": 56,
      "preview_url": "https://p.scdn.co/mp3-preview/13a5acdf83ddc323f6cb53e46c6508278d477a06?cid=774b29d4f13844c495f206cafdad9c86",
      "track_number": 3,
      "type": "track",
      "uri": "spotify:track:60s0QWaOZ2UTzqdIHBCt3x"
    },
    {
      "album": {
        "album_type": "album",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/5l8VQNuIg0turYE1VtM9zV"
            },
            "href": "https://api.spotify.com/v1/artists/5l8VQNuIg0turYE1VtM9zV",
            "id": "5l8VQNuIg0turYE1VtM9zV",
            "name": "Leonard Cohen",
            "type": "artist",
            "uri": "spotify:artist:5l8VQNuIg0turYE1VtM9zV"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/album/603qWApi8Q89JnkVAbixrb"
        },
        "href": "https://api.spotify.com/v1/albums/603qWApi8Q89JnkVAbixrb",
        "id": "603qWApi8Q89JnkVAbixrb",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ab67616d0000b2734921ae768a6b73150a15e16d",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/ab67616d00001e024921ae768a6b73150a15e16d",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/ab67616d000048514921ae768a6b73150a15e16d",
            "width": 64
          }
        ],
        "name": "Thanks for the Dance",
        "release_date": "2019-11-22",
        "release_date_precision": "day",
        "total_tracks": 9,
        "type": "album",
        "uri": "spotify:album:603qWApi8Q89JnkVAbixrb"
      },
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/5l8VQNuIg0turYE1VtM9zV"
          },
          "href": "https://api.spotify.com/v1/artists/5l8VQNuIg0turYE1VtM9zV",
          "id": "5l8VQNuIg0turYE1VtM9zV",
          "name": "Leonard Cohen",
          "type": "artist",
          "uri": "spotify:artist:5l8VQNuIg0turYE1VtM9zV"
        }
      ],
      "disc_number": 1,
      "duration_ms": 273093,
      "explicit": true,
      "external_ids": {
        "isrc": "CAC221900041"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/track/2DkpoHJ1h88e9dyc6SFIm2"
      },
      "href": "https://api.spotify.com/v1/tracks/2DkpoHJ1h88e9dyc6SFIm2",
      "id": "2DkpoHJ1h88e9dyc6SFIm2",
      "is_local": false,
      "is_playable": true,
      "name": "Happens to the Heart",
      "popularity": 54,
      "preview_url": "https://p.scdn.co/mp3-preview/23115042fef9e1240d05f95acf4966ebfc4d29ac?cid=774b29d4f13844c495f206cafdad9c86",
      "track_number": 1,
      "type": "track",
      "uri": "spotify:track:2DkpoHJ1h88e9dyc6SFIm2"
    },
    {
      "album": {
        "album_type": "album",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/5l8VQNuIg0turYE1VtM9zV"
            },
            "href": "https://api.spotify.com/v1/artists/5l8VQNuIg0turYE1VtM9zV",
            "id": "5l8VQNuIg0turYE1VtM9zV",
            "name": "Leonard Cohen",
            "type": "artist",
            "uri": "spotify:artist:5l8VQNuIg0turYE1VtM9zV"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/album/0AMbk6F6ZJ57OqlpB214gV"
        },
        "href": "https://api.spotify.com/v1/albums/0AMbk6F6ZJ57OqlpB214gV",
        "id": "0AMbk6F6ZJ57OqlpB214gV",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ab67616d0000b27305cbe0f78efb020ca6938646",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/ab67616d00001e0205cbe0f78efb020ca6938646",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/ab67616d0000485105cbe0f78efb020ca6938646",
            "width": 64
          }
        ],
        "name": "Ten New Songs",
        "release_date": "2001-10-09",
        "release_date_precision": "day",
        "total_tracks": 10,
        "type": "album",
        "uri": "spotify:album:0AMbk6F6ZJ57OqlpB214gV"
      },
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/5l8VQNuIg0turYE1VtM9zV"
          },
          "href": "https://api.spotify.com/v1/artists/5l8VQNuIg0turYE1VtM9zV",
          "id": "5l8VQNuIg0turYE1VtM9zV",
          "name": "Leonard Cohen",
          "type": "artist",
          "uri": "spotify:artist:5l8VQNuIg0turYE1VtM9zV"
        }
      ],
      "disc_number": 1,
      "duration_ms": 293386,
      "explicit": false,
      "external_ids": {
        "isrc": "NLB630100137"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/track/31TADh49q4s4jm6lGDeIrd"
      },
      "href": "https://api.spotify.com/v1/tracks/31TADh49q4s4jm6lGDeIrd",
      "id": "31TADh49q4s4jm6lGDeIrd",
      "is_local": false,
      "is_playable": true,
      "name": "In My Secret Life",
      "popularity": 54,
      "preview_url": "https://p.scdn.co/mp3-preview/22afac5d68811ce4788eb98a2c7ba79e9bf18ba8?cid=774b29d4f13844c495f206cafdad9c86",
      "track_number": 1,
      "type": "track",
      "uri": "spotify:track:31TADh49q4s4jm6lGDeIrd"
    }
  ]
}
  
"""

dictionary=json.loads(jstring)
#total_followers = dictionary["artists"]["items"][0]["followers"]["total"]
#name = dictionary["artists"]["items"][0]["name"]
#spotify_id = dictionary["artists"]["items"][0]["id"]
#image_url =  dictionary["artists"]["items"][0]["images"][0]["url"]

#print (spotify_id, name, image_url, total_followers)
tracks = dictionary["tracks"] #tracks array
print( "array length:", len(tracks))

tracks2 = []


for track in tracks:
    #print (track)
    #print (track["preview_url"])
    #print (track["name"])
    tracks_json={
        "name":track["name"],
        "preview_url":track["preview_url"]
    }
    tracks2.append(tracks_json)

#print (tracks2)

tracks_result = {"top_tracks":tracks2}

print (tracks_result)






#preview_url = dictionary["tracks"][0]["preview_url"]
#print (preview_url)