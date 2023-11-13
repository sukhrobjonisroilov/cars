from django.db import connection
from contextlib import closing


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row)) for row in cursor.fetchall()
    ]


def get_brend():
    with closing(connection.cursor()) as cr:
        cr.execute("""
            SELECT  * FROM core_brand 
        
        
        """)
        brand = dictfetchall(cr)
        print(brand)
        return brand
def get_car(request):
    with closing(connection.cursor()) as cr:
        cr.execute("""
                   SELECT  * FROM core_car cc              
                

                    
        """)
        cars = dictfetchall(cr)
        return cars