from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import DateTime, func
from sqlalchemy.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DECIMAL

#from MySQlConnectionString import connect_string
 
Base = declarative_base()
 
class Art(Base):
    __tablename__ = 'art'
    # Here we define columns for the table art
    # Notice that each column is also a normal Python instance attribute.
    id_art = Column(Integer, primary_key=True)
    e_a = Column(String(255), nullable=True)
    aname = Column(String(255), nullable=True)
    create_time = Column(DateTime, server_default=func.sysdate())
      
class Quelle(Base):
    __tablename__ = 'quelle'
    # Here we define columns for the table art
    # Notice that each column is also a normal Python instance attribute.
    id_quelle = Column(Integer, primary_key=True)
    qname = Column(String(255), nullable=True)
    create_time = Column(DateTime, server_default=func.sysdate())
 
class Anrede(Base):
    __tablename__ = 'anrede'
    id_anrede = Column(Integer, primary_key=True)
    anrede = Column(String(255), nullable=True)
    create_time = Column(DateTime, server_default=func.sysdate())
    
class Zahlung(Base):
    __tablename__ = 'zahlung'
    id_zahlung = Column(Integer, primary_key=True)
    zname = Column(String(255), nullable=True)
    create_time = Column(DateTime, server_default=func.sysdate())
 
class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table art
    # Notice that each column is also a normal Python instance attribute.
    id_person = Column(Integer, primary_key=True)
    id_anrede = Column(Integer, ForeignKey('anrede.id_anrede', ondelete='CASCADE'))
    nachname = Column(String(255), nullable=True)
    vorname = Column(String(255), nullable=True)
    create_time = Column(DateTime, server_default=func.sysdate())
 
class Kontakt(Base):
    __tablename__ = 'kontakt'
    # Here we define columns for the table art
    # Notice that each column is also a normal Python instance attribute.
    id_kontakt = Column(Integer, primary_key=True)
    id_person = Column(Integer, ForeignKey('person.id_person', ondelete='CASCADE'))
    email = Column(String(255), nullable=True)
    strasse = Column(String(255), nullable=True)
    hausnr = Column(String(255), nullable=True)
    plz = Column(String(255), nullable=True)
    ort = Column(String(255), nullable=True)
    telefon = Column(String(255), nullable=True)
    mobil = Column(String(255), nullable=True)
    create_time = Column(DateTime, server_default=func.sysdate())
    
class Betrag(Base):
    __tablename__ = 'betrag'
    # Here we define columns for the table art
    # Notice that each column is also a normal Python instance attribute.
    id_betrag = Column(Integer, primary_key=True)
    id_person = Column(Integer, ForeignKey('person.id_person', ondelete='CASCADE'))
    id_zahlung = Column(Integer, ForeignKey('zahlung.id_zahlung', ondelete='CASCADE'))
    id_quelle = Column(Integer, ForeignKey('quelle.id_quelle', ondelete='CASCADE'))
    e_a = Column(String(255), nullable=False)
    betrag_total = Column(DECIMAL(7,2), nullable=False)
    bemerkung = Column(String(255), nullable=True)
    datum = Column(DateTime, nullable=True)
    create_time = Column(DateTime, server_default=func.sysdate())

class Eingang(Base):
    __tablename__ = 'eingang'
    # Here we define columns for the table art
    # Notice that each column is also a normal Python instance attribute.
    id_eingang = Column(Integer, primary_key=True)
    id_person = Column(Integer, ForeignKey('person.id_person', ondelete='CASCADE'))
    id_zahlung = Column(Integer, ForeignKey('zahlung.id_zahlung', ondelete='CASCADE'))
    id_quelle = Column(Integer, ForeignKey('quelle.id_quelle', ondelete='CASCADE'))
    betrag_total = Column(DECIMAL(7,2), nullable=False)
    bemerkung = Column(String(255), nullable=True)
    datum = Column(DateTime, nullable=True)
    create_time = Column(DateTime, server_default=func.sysdate())


class Position(Base):
    __tablename__ = 'position'
    # Here we define columns for the table art
    # Notice that each column is also a normal Python instance attribute.
    id_pos = Column(Integer, primary_key=True)
    id_betrag = Column(Integer, ForeignKey('betrag.id_betrag', ondelete='CASCADE'))
    id_art = Column(Integer, ForeignKey('art.id_art', ondelete='CASCADE'))
    pos_name = Column(String(255), nullable=True)
    pos_betrag = Column(DECIMAL(7,2), nullable=False)
    bemerkung = Column(String(255), nullable=True)
    create_time = Column(DateTime, server_default=func.sysdate())    
    
class View_person_liste(Base):
    __tablename__ = 'view_person_liste'
    # Here we define columns for the table art
    # Notice that each column is also a normal Python instance attribute.
    id_person = Column(Integer, primary_key=True)
    anrede = Column(String(255), nullable=True)
    Name = Column(String(255), nullable=True)
     
class View_kontakt_liste(Base):
    __tablename__ = 'view_kontakt_liste'
    # Here we define columns for the table art
    # Notice that each column is also a normal Python instance attribute.
    id_kontakt = Column(Integer, primary_key=True)
    anrede = Column(String(255), nullable=True)
    Name = Column(String(255), nullable=True)
    plz = Column(String(255), nullable=True)
    strasse = Column(String(255), nullable=True)
    ort = Column(String(255), nullable=True)
    email = Column(String(255), nullable=True)
    telefon = Column(String(255), nullable=True)
    mobil = Column(String(255), nullable=True)

class View_betrag_liste(Base):
    __tablename__ = 'view_betrag_liste'
    # Here we define columns for the table art
    # Notice that each column is also a normal Python instance attribute.
    id_betrag = Column(Integer, primary_key=True)
    EA = Column(String(255), nullable=True)
    anrede = Column(String(255), nullable=True)
    Name = Column(String(255), nullable=True)
    betrag = Column(DECIMAL(7,2), nullable=True)
    datum = Column(String(255), nullable=True)
    bemerkung = Column(String(255), nullable=True)
    zname = Column(String(255), nullable=True)
    qname = Column(String(255), nullable=True)
    z_id = Column(Integer, nullable=True)
    q_id = Column(Integer, nullable=True)

class View_eingang_liste(Base):
    __tablename__ = 'view_eingang_liste'
    # Here we define columns for the table art
    # Notice that each column is also a normal Python instance attribute.
    id_betrag = Column(Integer, primary_key=True)
    EA = Column(String(255), nullable=True)
    anrede = Column(String(255), nullable=True)
    Name = Column(String(255), nullable=True)
    betrag = Column(DECIMAL(7,2), nullable=True)
    datum = Column(String(255), nullable=True)
    bemerkung = Column(String(255), nullable=True)
    zname = Column(String(255), nullable=True)
    qname = Column(String(255), nullable=True)


class View_pos_liste(Base):
    __tablename__ = 'view_pos_liste'
    # Here we define columns for the table art
    # Notice that each column is also a normal Python instance attribute.
    id_pos = Column(Integer, primary_key=True)
    id_betrag = Column(Integer, nullable=True)
    art = Column(String(255), nullable=True)
    betrag = Column(DECIMAL(7,2), nullable=True)
    bemerkung = Column(String(255), nullable=True)

