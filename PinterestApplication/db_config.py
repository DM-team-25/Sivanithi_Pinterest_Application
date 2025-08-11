import pymysql


# Function to connect to database

def getConnection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="Aspire@123",
        database="pinterest_app"
    )
