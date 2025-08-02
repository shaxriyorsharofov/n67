# import psycopg2
# from prettytable import PrettyTable

# conn = psycopg2.connect(
#             dbname='apteka',
#             user='postgres',
#             password='3698',
#             host='localhost',
#             port=5432
#         )
# curr = conn.cursor()


# class Mijoz:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
# m = Mijoz('Anvar', 56)

# class Dori:
#     def __init__(self, nomi, narxi, firma, count):
#         self.nomi = nomi
#         self.narxi = narxi
#         self.count = count

#     def get_info(self):
#         return f"nomi:{self.nomi} narxi:{self.narxi} firma:{self.firma}"
    
# # d1 = Dori('parasetamol', 5000, 50)
# # d2 = Dori('teraflyu', 10000, "shayana farm")
# # d3 = Dori('taylolfenhot', 14000, "firma")


# class Apteka:
#     def dorilar(self):
#         table = PrettyTable()
#         curr.execute('select *from dori')
#         fields = [i[0] for i in curr.description]
#         table.field_names = fields
#         table.add_rows([list(i) for i in curr.fetchall()])
#         print(table)        
    
#     def detail(seld, dori_nomi):
#         try:
#             table = PrettyTable()
#             curr.execute(f"select *from dori where name='{dori_nomi}'")
#             fields = [i[0] for i in curr.description]
#             table.field_names = fields
#             table.add_rows([list(i) for i in curr.fetchall()])
#             print(table) 
#         except:
#             print("Bunday dori topilmadi")
        
        
    
#     def dori_qoshish(self):
#         name = input('Dori nomini kiriting: ')
#         narxi = int(input('Dori narxini kiriting: '))
#         count = int(input('Dori sonini kiriting: '))
#         curr.execute(f"select *from dori where name='{name}'")
#         dori  = curr.fetchone()
#         if dori:
#             curr.execute(f"update dori set price={narxi}, count={dori[3]+count} where name='{name}'")
#         else:
#             curr.execute(f"insert into dori(name, price, count) values('{name}', {narxi}, {count})")
        
#         conn.commit()
#         print("Dori qoshildi")
    
#     def sotish(self):
#         name = input("Ismingizni kiriting: ")
#         curr.execute(f"select *from mijoz where name='{name}'")
#         mijoz  = curr.fetchone()
#         if mijoz:
#             dori_nomi = input("Dorini nomini kiriting")
#             curr.execute(f"select *from dori where name='{dori_nomi}'")
#             dori  = curr.fetchone()
#             if dori:
#                 print(f"{dori_nomi} dan {dori[3]} ta bor")
#                 dori_soni = int(input('Dori sonini kiriting'))
#                 curr.execute(f"update dori set count={dori[3]-dori_soni} where name='{dori_nomi}'")
#                 conn.commit()
#                 curr.execute(f"insert into apteka(user_id, dori_id, count, total_summ) values({mijoz[0]}, {dori[0]}, {dori_soni}, {dori_soni*dori[2]})")
#                 conn.commit()
#             else:
#                 print('Bunaqa dori mavjud emas!')
                
#         else:
#             print('Siz roxatdan otishingiz kerak')

        
    
#     def mijoz_qoshish(self):
#         name = input("Ismingizni kiriting: ")
#         age = int(input("Yoshingizni kiriting: "))
        
#         curr.execute(f"insert into mijoz(name, age) values('{name}', {age})")
#         print("Siz muvaffaqqiyatli roxatdan otdingiz.")
#         conn.commit()
    
# p = Apteka()


# a = True
# while a:
#     d = int(input("0 chiqish\n1 dorilar\n2 dorini qidirish\n3 dori qoshish\n4 dori sotib olish\n5 roxatdan otish\nTepadan birini tanlang : "))
#     if d == 1:
#         p.dorilar()
#     elif d == 2:
#         dori_nomi = input('Dorini nomini kiriting: ')
#         p.detail(dori_nomi)
#     elif d == 3:
#         p.dori_qoshish()
#     elif d == 4:
#         p.sotish()
#     elif d == 5:
#         p.mijoz_qoshish()
#     elif d == 0:
#         a = False 
        
    
    
    
    
    
    


# # a1 = Apteka("DORIXONA")
# # a1.create(d1)
# # a1.create(d2)
# # a1.create(d3)
# # a1.all_dori()



# # class DB:
# #     def __init__(self, dbname):
# #         self.conn = psycopg2.connect(
# #             dbname=dbname,
# #             user='postgres',
# #             password='3698',
# #             host='localhost',
# #             port=5432
# #         )
# #         self.curr = self.conn.cursor()
        
# #     def products(self, table_name):
# #         self.curr.execute(f"select *from {table_name}")
# #         print(self.curr.fetchall())
        
# #     def insert_func(self, table_name):
# #         self.curr.execute(f'select *from {table_name}')
# #         columns = {i[0]: i[1] for i in self.curr.description}
# #         d = {}
# #         for i, j in columns.items():
# #             if i != 'id':
# #                 if j == 23:
# #                     a = int(input(f'{i} ni kiriting: '))
# #                 else:
# #                     a = input(f'{i} ni kiriting: ')
# #                 d[i]=a
        
# #         k = ','.join([f"{i}" for i, j in d.items()]) 
# #         k_ = [j for i, j in d.items()]
    
# #         self.curr.execute(f"insert into {table_name}({k}) values{tuple(k_)};")
# #         print('Malumot qoshildi')
# #         self.conn.commit()
        
    
# # n67 = DB('n67')
# # # n67.insert_func('person')
# # n67.products('person')


        
        
print('GIT')