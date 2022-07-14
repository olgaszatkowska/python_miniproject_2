from sqlalchemy.orm import scoped_session
from dataclasses import dataclass

from src.university import University
from src.utils import parse_percent, parse_ratio

@dataclass
class Analizator:
    session: scoped_session

    @property
    def aggregation(self):
        gender_ratio_query = (
            self.session.query().with_entities(University.gender_ratio).all()
        )
        gender_ratios = [parse_ratio(ratio) for ratio, in gender_ratio_query]
        return sum(filter(None, gender_ratios)) / len(gender_ratios)

    @property
    def chart_data(self):
        query = (
            self.session.query()
            .with_entities(University.ranking, University.percentage_int_stud)
            .all()
        )
        data = [
            [ranking, parse_percent(percentage_int_stud)]
            for ranking, percentage_int_stud in query
            if None not in [ranking, parse_percent(percentage_int_stud)]
        ]
        return [elem for elem, _ in data], [elem for _, elem in data]

