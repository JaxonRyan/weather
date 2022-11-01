from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Results(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    location = db.Column(db.Text(), nullable=False)
    temp = db.Column(db.Text(), nullable=False)
    dt_obj = db.Column(db.Text(), nullable=False)
    feels_like = db.Column(db.Text(), nullable=False)
    weather = db.Column(db.Text(), nullable=False)
    location = db.Column(db.Text(), nullable=False)
    icon = db.Column(db.Text(), nullable=False)
    icon_url = db.Column(db.Text(), nullable=False)

    def to_dict(self):
        return {
            'id': self.first,
            'location': self.location,
            'temp': self.temp,
            'dt_obj': self.dt_obj,
            'feels_like': self.feels_like,
            'weather': self.weather,
            'location': self.location,
            'icon': self.icon,
            'icon_url': self.icon_url
        }