from UTIL.connection import DBConnection

class PropertyUtil:
    def _init_(self):
        PropertyUtil.connection=DBConnection.getConnection()

obj=PropertyUtil()