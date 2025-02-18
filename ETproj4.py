# Writing a program that prompts for songs, asking for the title and the artist
# Starting with a blank dictionary
songs = {}

# Prompting the user for songs, getting the title and the artist
print('Help create a music collection!')
print()
song_entries = int(input('How many songs and artists would you like to add: '))
print()
for i in range(song_entries):
    title = input('Enter a song title: ').lower()
    artist = input('Enter the artists name: ').lower()
    songs[title] = artist

# Asking user for song title and displaying corresponding artist
print()
def find_artist(title):
    x = input('Enter a song title to see the artist: ').lower()
    if x in songs.keys():
        return songs.get(x)

print(f'The artist is {find_artist(title)}')
print()
# Prompting the user to enter a song and then updating the artist information
a = ''
b = ''
def update_song(a,b):
    a = input('Enter the name of a song in the collection: ').lower()
    if a in songs.keys():
        b = input('Update artist name: ').lower()
        if b not in songs.values():
            songs.update({a: b})
            return 'Song updated.'
        elif b in songs.values():
            return 'Artist name unchanged.'

print(update_song(a, b))
print()

# removing a song from the music collection by user input

def remove_song(title):
    song = input('Enter the name of a song to remove it from the collection: ').lower()
    if song in songs:
        del songs[song]
    return f'Song {song} removed'

print(remove_song(title))
print()
# Displaying the songs in the dictionary
print('All the songs in the collection are:')
for key in songs:
    print(key)