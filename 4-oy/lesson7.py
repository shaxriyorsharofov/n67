# import psycopg2
# conn = psycopg2.connect(
#     dbname='n67',
#     host='localhost',
#     port=5432,
#     user='postgres',
#     password='3698'
# )
# curr = conn.cursor()


# # def select_func(table_name):
# #     curr.execute(f"select *from {table_name}")
# #     return curr.fetchone()

# # print(select_func('cars'))


# # curr.execute(f"select *from cars")


# # for i in curr:
# #     print(curr.fetchone())


# # def select_data(table_name, column_name, data):
# #     curr.execute(f"select *from {table_name} where {column_name}='{data}'")
# #     return curr.fetchall()

# # print(select_data('cars', 'country', 'Brazil'))


# # def delete_data(table_name, column_name, data):
# #     query = f"DELETE FROM {table_name} WHERE {column_name} = %s"
# #     curr.execute(query, (data,))
# #     return "ochdi"

# # print(delete_data('cars','year',2003))






