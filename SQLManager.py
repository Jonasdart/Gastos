__author__ = 'pedro'


class SQLManager (object):
    def __init__(self):
        """
        :return:
        """
        self.query = ""

    def order_with_separator(self, array, bet="`", sep=","):
        """
        Order array as a string with the selected separator
        :param array:
        :return:
        """
        string = ""
        for i in range(len(array)):
            if i != len(array) - 1:
                string += bet + str(array[i]) + bet + sep + " "
            else:
                string += bet + str(array[i]) + bet
        return string

    def query_where(self, where):
        """
        Create a query for the where statement
        :param where: list with the where statement
        :return:
        """
        query = "WHERE"

        # We go throw the where statement
        for data in where:
            # We add the data column
            query += " `" + data[0] + "`"

            # We add the comparison
            query += " " + data[1]

            # We add the value
            if data[2] == "NULL":
                query += " " + data[2]
            else:
                query += " '" + str(data[2]) + "'"

            # Then we add link between statement
            #query += " " + data[3]

        # We return the query
        return query

    def query_insert(self, table, columns, values):
        """
        Insert a new data into the table
        :param table: string table name
        :param columns:
        :param values:
        :return:
        """
        # First we add the insert into statement
        self.query = "INSERT INTO `" + table + "`"

        # Then we go throw each column and add the column name
        self.query += "(" + self.order_with_separator(columns) + ")"

        # Then we go throw the values and add then
        self.query += " VALUES (" + self.order_with_separator(values, bet="'") + ")"

    def query_update(self, table, columns, values, where):
        """
        Update the table query
        :param table: string with table name
        :param columns: string/list with columns values
        :param values: string/list with values
        :param where: list with where statement
        :return:
        """
        # We create the new query
        self.query = "UPDATE `" + table + "`"

        # We connect the columns and the values into one list
        concat = ["`"+columns[i]+"`='"+values[i]+"'" for i in range(len(columns))]

        # Then we add to the query this values
        self.query += " SET " + self.order_with_separator(concat, bet="")

        # Finally we add the where
        self.query += " " + self.query_where(where)

    def query_delete(self, table, where):
        """
        Delete query constructor
        :param table: string table
        :param where: list of where
        :return:
        """
        # Start the new query
        self.query += "DELETE FROM `" + table + "`"

        # Add the where statement
        self.query += " " + self.query_where(where)

    def query_select(self, table, columns, where=None, order=None, desc=True):
        """
        Create the select query
        :param table: string with table name
        :param columns: string/list with columns to be queried
        :param where: list with conditions for where
        :param order: string with the column name to order
        :param desc: boolean if the data should asc or desc
        :return:
        """
        # We start the query as select
        self.query = "SELECT"

        # Then we should check the columns to see what we should run
        if columns == "*":
            self.query += " *"
        else:
            # If it is a list we add each column to the query
            self.query += " " + self.order_with_separator(columns)

        # Then we add the statement from table
        self.query += " FROM `" + table + "`"

        # If the where is not none we add the where query
        if where is not None:
            self.query += " " + self.query_where(where)

        # If the order is not empty we add the order
        if order is not None:
            self.query += "ORDER BY " + order

            # If the desc is true
            if desc:
                self.query += " DESC"
            else:
                self.query += " ASC"

    def query_columns(self, table):
        """
        Get the query for the columns of the table
        :param table:
        :return:
        """
        self.query = "DESCRIBE `" + table + "`"

    def custom_query(self, query):
        """
        Set a custom query
        :param query: string custom query
        :return:
        """
        self.query = query

    def create_table(self, name, bd = '`dados_brutos`'):
        self.query = "CREATE TABLE "
        self.query += f"{bd}.`{name}`"
        self.query += "( `1` FLOAT NOT NULL ) ENGINE = InnoDB;"
