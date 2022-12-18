from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

#from MySQlConnectionString import connect_string
 
Base = declarative_base()
 
class Potd(Base):
    __tablename__ = 'potd'
    # Here we define columns for the table potd
    # Notice that each column is also a normal Python instance attribute.
    potd_id = Column(Integer, primary_key=True)
    potd_fname = Column(String(512), nullable=True)
    potd_dname = Column(String(512), nullable=True)
    potd_Beschreibung = Column(String(126), nullable=True)
 
    def get_potd_fname(self):
        return self.potd_fname;
     
    def set_potd_fname(self, value):
        self.potd_fname = value.title()
    
    def get_potd_dname(self):
        return self.potd_dname;
     
    def set_potd_dname(self, value):
        self.potd_dname = value.title()

    def get_potd_Beschreibung(self):
        return self.potd_Beschreibung
     
    def set_potd_Beschreibung(self, value):
        self.potd_Beschreibung = value.title()
    
