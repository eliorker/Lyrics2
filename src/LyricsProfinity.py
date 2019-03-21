from urllib.request import *

profinity = ['fuck', 'shit', 'whore', 'gun']

def add_profinity(new_profinity):
    profinity.append(new_profinity)

def get_song_artist_and_title():
    artist = input("Enter song artist: ")
    title = input("Enter song title: ")
    return artist, title

def get_lyrics(artist, title):
    url = 'https://api.lyrics.ovh/v1/' + artist + '/' + title
    request = Request(url)
    print(type(request))
    lyrics = urlopen(request).read().decode("utf-8")[11:-2]
    return lyrics

def check_lyrics_for_profinity(lyrics):
    if any(word in lyrics for word in profinity):
        return True
    return False

def does_song_contains_profinity():
    artist, title = get_song_artist_and_title()
    lyrics = get_lyrics(artist, title)
    return check_lyrics_for_profinity(lyrics)
