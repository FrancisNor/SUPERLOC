""" This module is used to define model to be used exclusively by the views. These models
are not expected to correspond to any database table """


class Reservation(object):
    """ This class represents the intermediary model once the reservation form has been
    completed. It will be further used for selecting the vehicle among the ones available."""

    def __init__(self, departure_agency, return_agency, category, departure_date, return_date):
        self.departure_agency = departure_agency
        self.return_agency = return_agency
        self.category = category
        self.departure_date = departure_date
        self.return_date = return_date
