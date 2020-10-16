# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3


class QuotesPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def process_item(self, item, spider):
        self.db_store(item)
        return item

    def create_connection(self):
        self.conn = sqlite3.connect("quotes.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS quote_table""")
        self.curr.execute("""create table quote_table( title text, author text)""")

    def db_store(self, item):
        self.curr.execute("""insert into quote_table values(?,?)""", (
            item["title"],
            item["author"]
        ))
        self.conn.commit()
