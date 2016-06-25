# !usr/bin/env python
# coding: utf-8

from __future__ import unicode_literals, print_function

from MyDB import MyDB

__author__ = 'David Ji'

'''MyDB Example'''


def main():
    # 创建数据库实例
    test_db = MyDB(user='root', passwd='0516', db='test_py')

    # Create
    c_params = (('Benzema', 28, 'M'), ('Bale', 26, 'M'), ('Ronaldo', 31, 'M'))
    last_row_id = test_db.insert('person', c_params,
                                 field_list=['name', 'age', 'gender'],
                                 is_many=True)
    print(last_row_id)  # 1

    # Retrieve
    result_set = test_db.select('SELECT * FROM person WHERE age<28;')
    print(result_set)  # ((2L, u'Bale', 26L, u'M'),)

    # Update
    update_sql = 'UPDATE person SET age=%s WHERE name=%s;'
    u_params = (29, 'Benzema')
    update_rows_cnt = test_db.update(update_sql, u_params)
    print(update_rows_cnt)  # 1

    # Delete
    delete_rows_cnt = test_db.delete("DELETE FROM person WHERE age>30;")
    print(delete_rows_cnt)  # 1


if __name__ == '__main__':
    main()
