class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artist_count()

    # class method that helps count the songs
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    # class function to help add genre to our empty genre class attribute
    def add_to_genres(self):
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)

    # class    funcion to add artists to artist class attribut  
    def add_to_artists(self):
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)

    # class function to count genres added ensuring we don't double add
    def add_to_genre_count(self):
        if self.genre in Song.genre_count:
            Song.genre_count[self.genre] += 1
        else:
            Song.genre_count[self.genre] = 1

    # class function to count artists added ensuring we don't double add
    def add_to_artist_count(self):
        if self.artist in Song.artist_count:
            Song.artist_count[self.artist] += 1
        else:
            Song.artist_count[self.artist] = 1

    # classmethod to show our program list as we continue to add
    @classmethod
    def show_song(cls):
        print(f"Total Songs Created: {cls.count}")
        print(f"Genres: {cls.genres}")
        print(f"Artists: {cls.artists}")
        print(f"Genre Count: {cls.genre_count}")
        print(f"Artist Count: {cls.artist_count}")

