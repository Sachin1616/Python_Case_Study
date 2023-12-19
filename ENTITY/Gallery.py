from DAO.implementation import DbConnection

class Gallery(DbConnection):
    def _init_(self):
        self.GalleryID=''
        self.Name=''
        self.Description=''
        self.Location=''
        self.Curator=''
        self.OpeningHours=''
        self.ArtistID=''

    def create(self):
        create_str = '''create  table  if not exists Gallery
        (
        GalleryID INT  PRIMARY KEY,
        Name VARCHAR(255),
        Description TEXT,
        Location VARCHAR(255),
        Curator VARCHAR(255),
        OpeningHours VARCHAR(255),
        ArtistID INT
        )'''
        self.open()
        self.s.execute(create_str)
        self.s.close()
        print('Table created successfully------:')
obj=Gallery()
obj.create()