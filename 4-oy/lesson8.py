import psycopg2

conn = psycopg2.connect(
    dbname='n67',
    user='postgres',
    host='localhost',
    port=5432,
    password=3698
)

curr = conn.cursor()


# def create_table():
#     tablle_name = input('Jadval nomini kiriting: ')
#     a = True
#     c = {}
#     while a:
#         column_name = input('Column nomini kiriting: ')
#         column_type = input('Column type ni kiriting: ')

#         c[column_name] = column_type
        
#         b = input('Siz yana column qoshmoqchimisiz(Ha\Yoq)').lower()
#         if b == 'yoq':
#             a = False
      
#     k = ','.join([f"{i} {j}" for i, j in c.items()])   
#     curr.execute(f"create table {tablle_name} ({k});")
#     print('Table yaratildi')
           
            
# create_table()    
# conn.commit()

# def insert_func(table_name):
#     curr.execute(f'select *from {table_name}')
#     columns = {i[0]: i[1] for i in curr.description}
#     d = {}
#     for i, j in columns.items():
#         if i != 'id':
#             if j == 23:
#                 a = int(input(f'{i} ni kiriting: '))
#             else:
#                 a = input(f'{i} ni kiriting: ')
#             d[i]=a
    
#     k = ','.join([f"{i}" for i, j in d.items()]) 
#     k_ = [j for i, j in d.items()]
  
#     curr.execute(f"insert into {table_name}({k}) values{tuple(k_)};")
#     print('Malumot qoshildi')
    

# insert_func('person')
# conn.commit()

# a = {3:4, 6:7}
# d = [i for i in a.items()]
# f = [f"{i[0]} {i[1]}" for i in d]
# k = ','.join(f)
# print(f)





from prettytable import PrettyTable
table = PrettyTable()

def pretty_func(table_name):
    curr.execute(f'select *from {table_name};')
    for i in curr.fetchall():
        if i[4].strip() == 'Male':
            print(i)
    # fields = [i[0] for i in curr.description]
    # table.field_names = fields
    # table.add_rows([list(i) for i in curr.fetchall()])
    # print(table)

pretty_func('person')

# table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]

# table.add_row(["Adelaide", 1295, 1158259, 600.5])
# table.add_row(["Brisbane", 5905, 1857594, 1146.4])
# table.add_row(["Darwin", 112, 120900, 1714.7])
# table.add_row(["Hobart", 1357, 205556, 619.5])
# table.add_row(["Sydney", 2058, 4336374, 1214.8])
# table.add_row(["Melbourne", 1566, 3806092, 646.9])
# table.add_row(["Perth", 5386, 1554769, 869.4])
# table.add_rows(
#     [
#         ["Adelaide", 1295, 1158259, 600.5],
#         ["Brisbane", 5905, 1857594, 1146.4],
#         ["Darwin", 112, 120900, 1714.7],
#         ["Hobart", 1357, 205556, 619.5],
#         ["Sydney", 2058, 4336374, 1214.8],
#         ["Melbourne", 1566, 3806092, 646.9],
#         ["Perth", 5386, 1554769, 869.4],
#     ]
# )

# print(table)


