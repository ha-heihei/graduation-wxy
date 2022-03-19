import pymysql


class DBUtil:
    def __init__(self,db="wxy",exFlag=False):
        self.conn = pymysql.connect(host="localhost", port=3306, db=db, user="root", passwd="root")
        self.exFlag=exFlag

    def update(self, sql, values):
        cur = self.conn.cursor()
        try:
            cur.execute(sql, values)
            self.conn.commit()
            return True
        except Exception as e:
            if self.exFlag:
                return e
            return False
        finally:
            cur.close()

    def query(self, sql, values):
        cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            cur.execute(sql, values)
            return cur.fetchall()
        except Exception as e:
            if self.exFlag:
                return e
            return None
        finally:
            cur.close()

    def close(self):
        self.conn.close()
