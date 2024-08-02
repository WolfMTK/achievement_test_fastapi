from dataclasses import dataclass


@dataclass
class Pagination:
    """ Пагинация. """

    limit: int
    offset: int
