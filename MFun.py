class Song:
    def __init__(self, title, artist, album, genre, duration):
        self.title = title
        self.artist = artist
        self.album = album
        self.genre = genre
        self.duration = duration

class MusicLibrary:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def get_songs_by_artist(self, artist):
        return [song for song in self.songs if song.artist == artist]

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def display_playlist(self):
        print(f"Playlist: {self.name}")
        for song in self.songs:
            print(f"{song.title} - {song.artist}")

def main_menu():
    print("Welcome to the Music Library App!")
    print("1. Manage Music Library")
    print("2. Create Playlist")
    print("3. Search for Songs")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    return choice

# Main program
library = MusicLibrary()
playlist = None

while True:
    choice = main_menu()

    if choice == "1":
        # Manage Music Library
        title = input("Enter the song title: ")
        artist = input("Enter the artist: ")
        album = input("Enter the album: ")
        genre = input("Enter the genre: ")
        duration = input("Enter the duration: ")

        new_song = Song(title, artist, album, genre, duration)
        library.add_song(new_song)
        print("Song added to the library.")
    elif choice == "2":
        # Create Playlist
        if not playlist:
            playlist_name = input("Enter playlist name: ")
            playlist = Playlist(playlist_name)
            print(f"Playlist '{playlist_name}' created.")
        else:
            print("Playlist already exists. Use option 5 to add songs to the existing playlist.")
    elif choice == "3":
        # Search for Songs
        artist_name = input("Enter artist name to search for songs: ")
        songs_by_artist = library.get_songs_by_artist(artist_name)
        print(f"Songs by {artist_name}:")
        for song in songs_by_artist:
            print(f"{song.title} - {song.album}")
    elif choice == "4":
        print("Exiting the Music Library App. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")