from src.database.models import Performance as Model
from src.server.resolves.type_of_play import dbmanager


def get(id_: int) -> Model | None:
    res = dbmanager.execute_query(
        query=f'select * from {Model.__name__} where id=(?)',
        args=(id_,))

    return None if not res else Model(
        id=res[0],
        datetime_start=res[1],
        play_id=res[2],
        hall_id=res[3]
    )


def get_all() -> list[Model] | dict:
    l = dbmanager.execute_query(
        query=f"select * from {Model.__name__}",
        fetchone=False)

    res = []

    if l:
        for res in l:
            res.append(Model(
                id=res[0],
                datetime_start=res[1],
                play_id=res[2],
                hall_id=res[3]
            ))

    return res


def delete(id_: int) -> None:
    return dbmanager.execute_query(
        query=f'delete from {Model.__name__} where id=(?)',
        args=(id_,))


def create(new: Model) -> int | dict:
    res = dbmanager.execute_query(
        query=f"insert into {Model.__name__} (datetime_start, playID, hallID) values(?,?,?) returning id",
        args=(new.datetime_start, new.play_id, new.hall_id))

    if type(res) != dict:
        res = get(res[0])

    return res


def update(id_: int, new: Model) -> None:
    return dbmanager.execute_query(
        query=f"update {Model.__name__} set (datetime_start, playID, hallID) = (?,?,?) where id=(?)",
        args=(new.datetime_start, new.play_id, new.hall_id, id_))
