import os

if 'DYNO' not in os.environ:
    import pymysql
    pymysql.install_as_MySQLdb()