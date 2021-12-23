# -*- coding: utf-8 -*-

import sqlite3

def selectOperation():
    
    connection = sqlite3.connect("chinook.db")
    
    #komutlarda harf duyarlılığı yoktur ama değerlerde vardır!
    
    #cursor = connection.execute("""select firstname,lastname 
    #                            from customers 
    #                            where city='Prague' or city='Berlin'
    #                            order by firstname desc""")
    #
    #for row in cursor:
    #    print("FirsName:",row[0])
    #    print("LastName:",row[1])
    #    print("*****************")
    #desc ters çevirir. order by sıralama için kullanılır.
    
    
    #  
    #cursor = connection.execute("""select city,count(*)
    #                               from customers
    #                               group by city having count(*)>1
    #                               order by count(*)""")
    #for row in cursor:
    #    print("city:",row[0])
    #    print("count:",row[1])
    #    print("**************")
    
        
    cursor = connection.execute("""select firstname,lastname
                                   from customers
                                   where firstname like 'a%' """)
    for row in cursor:
        print("firstname:",row[0])
        print("lastname:",row[1])
        print("**************")
        
    connection.close()

#selectOperation()

def insertOperation():
    connection = sqlite3.connect("chinook.db")
    connection.execute("""insert into customers
                          (firstname,lastname,city,email)
                          values('Mert','Simsek','İzmir','mertsmsk70@gmail.com')
                          """)
    connection.commit() #db ye göndermek için.
    connection.close()

#insertOperation()

def updateOperation():
    connection = sqlite3.connect("chinook.db")
    connection.execute("""update customers set city='İstanbul'
                          where city='İzmir' """)
    connection.commit()
    connection.close()

#updateOperation()

def deleteOperation():
    connection = sqlite3.connect("chinook.db")
    connection.execute("""delete from customers
                          where city='İstanbul' """)
    connection.commit()
    connection.close()

#deleteOperation()

def joinOperation():
    connection = sqlite3.connect("chinook.db")
    cursor = connection.execute("""SELECT albums.Title,artists.Name 
                                   FROM artists INNER JOIN albums
                                   on artists.ArtistId = albums.ArtistId""")
    for row in cursor:
        print("Title:",row[0]," Name:",row[1])
    
    connection.close()
    
#joinOperation()
    
    
    