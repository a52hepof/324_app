from django.test import TestCase
import psycopg2
# Create your tests here.
print('Probando conexiones remotas')




try:
    conexion = psycopg2.connect(host="ec2-52-208-164-5.eu-west-1.compute.amazonaws.com", database="d2i565903pvam0", user="rzmdeawngownsi", password="e0f4dacf6ae38caa35190a376bd295478400b869fa5869ec4d0c33c229cd0f64")
    cur = conexion.cursor()
    print(conexion,cur)
except Exception as e:
    print(e)



try:
    conexion = psycopg2.connect(host="tommy2.heliohost.org", database="a52hepof_bp324_db", user="a52hepof_bp324_user", password="U74&a93iu")
    cur = conexion.cursor()
    print('Helios',cur)
except Exception as e:
    print(e)

import mysql.connector

try:

    cnx = mysql.connector.connect(user='a52hepof_bp324_usuario', password='U74&a93iu',
                              host='tommy2.heliohost.org',
                              database='a52hepof_bp324_mariadb')
    print(cnx)

except Exception as e:
    print(e)


try:
    conexion = psycopg2.connect(host="database-324-app.caqpfa3nnout.us-east-1.rds.amazonaws.com", database="database324app", user="postgres324", password="U74&a93iu")
    cur = conexion.cursor()
    print(conexion,cur)
except Exception as e:
    print(e)