import os

from src.exceptions import DataBaseIsNotEmpty
from src.university import University
from src.utils import download_kaggle_dataset, extract_file, fix_json_file, load_json_file


class DataBase:
    def __init__(self, dataset, json_filename, session):
        self.dataset = dataset
        self._json_filename = json_filename
        self.session = session

    def empty(self):
        self.session.query(University).delete()
        self.session.commit()

    def fill(self):
        if not self.is_empty:
            raise DataBaseIsNotEmpty

        zip_file_name = download_kaggle_dataset(self.dataset)

        extract_file(zip_file_name, self._json_filename)
        self._load_json_file_to_db()

        os.remove(zip_file_name)
        os.remove(self._json_filename)

    def _load_json_file_to_db(self):
        fix_json_file(
            {
                "number students": "number_of_students",
                "students staff ratio": "students_staff_ratio",
                "perc intl students": "percentage_int_stud",
                "gender ratio": "gender_ratio",
            },
            self._json_filename,
        )
        json_data = load_json_file(self._json_filename)
        for university in json_data:
            self.session.add(University(**university))
        self.session.commit()

    @property
    def table(self):
        return self.session.query(University).all()

    @property
    def is_empty(self):
        return (self.session.query(University).all()) == []

