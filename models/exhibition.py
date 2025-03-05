class Exhibition:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.artworks = []

    def add_artwork(self, artwork):
        self.artworks.append(artwork)


class Artwork:
    def __init__(self, title, image_url, description):
        self.title = title
        self.image_url = image_url
        self.description = description
