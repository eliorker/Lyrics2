from urllib.request import *

def get_song_artist_and_title():
    artist = input("Enter song artist: ")
    title = input("Enter song title: ")
    return artist, title

def get_lyrics(artist, title):
    url = 'https://api.lyrics.ovh/v1/' + artist + '/' + title
    request = Request(url)
    lyrics = urlopen(request).read().decode("utf-8")[11:-2]
    return lyrics

def get_word():
    word = input("Enter word: ")
    return word

def check_numbers_of_repeats(lyrics):
    word = get_word()
    return lyrics.lower().split().count(word)

def calculate_number_of_times_word_occurs_in_the_song():
    artist, title = get_song_artist_and_title()
    lyrics = get_lyrics(artist, title)
    return check_numbers_of_repeats(lyrics)
