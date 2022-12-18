from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import load_only
from Potd import Potd
from MySQlConnectSQLAlchemy import connect_string


class utilities(object):
    @staticmethod
    def createSession():
        # connect to database
        engine = create_engine(connect_string, echo=False)
        # create a Session
        Session = sessionmaker(bind=engine)
        return Session()

    @staticmethod
    def closeSessionCommit(session):
        """Close and Commit session"""
        session.commit()
        session.close()
        return None

    @staticmethod
    def closeSessionRollback(session):
        """Close and Rollback session"""
        session.rollback()
        session.close()
        return None

    @staticmethod
    def get_potd_name(icon_id):
        # read database
        engine = create_engine(connect_string, echo=False)
        # create a Session
        Session = sessionmaker(bind=engine)

        session = Session()
        potd = session.query(Potd).filter(Potd.potd_id == icon_id).options(
            load_only("potd_fname", "potd_dname")).first()
        # print("Dateiname: ", potd.potd_dname+potd.potd_fname)
        session.close()
        # print("Utilities: ", potd.potd_dname+potd.potd_fname)
        return potd.potd_dname + potd.potd_fname
