#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from utils.client import login

# import csv

if __name__ == "__main__":
    client = login()

    print("--- successfully logged in ---")

    release_ids = [
        release.id for release in client.identity().collection_folders[0].releases
    ]

    for id in release_ids:
        release = client.release(id)

        year = str(release.year)
        album = release.title
        artist = release.artists[0].name
        label = release.labels[0].name
        genre = release.genres[0]

        tracklist = release.tracklist

        for track in tracklist:
            print("id: " + str(id))
            print("title: " + track.title)
            print("artist: " + artist)
            # print("comment: \"Vinyl\"")
            print("duration: " + track.duration)  # todo: to millisec & empty values?
            # print("bpm: " + bpm)
            print("genre: " + genre)
            print("track: " + track.position)
            print("year: " + year)  # release year
            print("album: " + album)
            print("label: " + label)

            print("-------------------------------------")

# def write_csv(id):
#     header = ['Titel', 'Artist', 'Genre', 'Track', 'Year', 'Album', 'Duration']
#     release = get_release(id)
#     artist = release.artists[0].name
#     year = release.year
#     album = release.title
#     genre = release.genres[0]
#     with open('../resources/file.csv', 'w', encoding='UTF8') as file:
#         writer = csv.writer(file)
#         writer.writerow(header)
#         for track in release.tracklist:
#             data = [track.title, artist, genre, track.position, year, album, track.duration]
#             writer.writerow(data)
