def add_songs(*args):
    result = ""
    song_collection = {}
    
    for song_data in args:
        title = song_data[0]
        lyrics = song_data[1]
        if title not in song_collection:
            song_collection[title] = []
        song_collection[title].extend(lyrics)
    
    for key, value in song_collection.items():
        result += f"- {key}\n"
        for line in value:
            result += f"{line}\n"

    return result
