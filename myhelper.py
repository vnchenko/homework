from dao.db import OracleDb
import cx_Oracle


class Helper:

    def init(self):
        self.db = OracleDb()

    def Get_phone(self, phone_id=None):

        if phone_id:
            phone_id = "'{0}'".format(phone_id)
        else:
            phone_id = 'null'

        query = "select * from table(pkg_hr.get_phone({0}))".format(phone_id)
        result = self.db.execute(query)

        return result.fetchall()

    def Update_phone(self, phone_id, phone_model, phone_vendor, phone_price, phone_date):

        cursor = self.db.cursor
        status = cursor.var(cx_Oracle.STRING)

        cursor.callproc("pkg_hr.update_phone", [phone_id, phone_model, phone_vendor, phone_price,  phone_date, status])

        return status.getvalue()


if __name__ == "main":
    helper = Helper()
