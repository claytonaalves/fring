from datetime import datetime
from core.database import db


class Device(db.Model):

    device_id = db.Column(db.String(36), primary_key=True)
    last_query = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())


    def __init__(self, device_id=''):
        if device_id:
            self.device_id = device_id
            # set date to the year beginning for new devices
            self.last_query = datetime(2017, 1, 1) 
