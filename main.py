import utils.client as uc

def main():
    client = uc.login()

    # creates list of all releases of the personal user collection
    release_ids = [
        release.id for release in client.identity().collection_folders[0].releases
    ]

    # albums
    csv_string = "id,title,artist,comment,duration,genre,track,year,album,label\n"
    for id in release_ids:
        release = client.release(id)

        year = str(release.year)
        album = release.title
        artist = release.artists[0].name
        label = release.labels[0].name
        genre = release.genres[0]

        tracklist = release.tracklist

        # tracks
        for track in tracklist:
            duration = duration_to_ms(duration_raw=track.duration)
            csv_string += f"{str(id)},{track.title},{artist},Vinyl,{duration},{genre},{track.position},{year},{album},{label}\n"

    open("tracks.csv", "w").write(csv_string)

def duration_to_ms(duration_raw:str) -> str:
    if not duration_raw: return "2000"
    durations = duration_raw.split(":")
    ms = int(durations[0]) * 60000 + int(durations[1]) * 1000 
    return ms if len(durations)==2 else ms + int(durations[2])

if __name__ == "__main__":
    main()