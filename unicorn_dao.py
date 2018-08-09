import db_tool

db = db_tool.SQLHelper()


def add_unicorn(unicorn):
    sql = 'insert into unicorn(unicorn_name, unicorn_age, number_id) VALUES (%s, %s, %s)'
    db.save(sql, (unicorn.get_unicorn_name(), unicorn.get_unicorn_age(), unicorn.get_number_id()))


def show_all():
    sql = 'select * from unicorn'
    unicorns = db.show_all(sql)
    return unicorns


def search(number_id):
    sql = 'select * from unicorn where number_id = %s'
    unicorn = db.search(sql, number_id)
    return unicorn


def delete(number_id):
    sql = 'delete * from unicorn where number_id = %s'
    db.delete(sql, number_id)
