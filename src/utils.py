from config import app_config


class Utils:

    def __init__(self, event):
        self.event = event

    def process_data(self):
        queries = []
        for record in self.event:
            table_name = self.select_table_name(record["body"])
            query = self.create_query(record["body"], table_name)
            queries.append(query)

    def select_table_name(self):
        prompt = app_config.prompt_select_table
        # implement IA API to select table name
        pass

    def create_query(self):
        prompt = app_config.prompt_create_query
        # implement IA API to create query
        pass

    def create_connection(self):
        conn_string = self.create_conn_string()
        pass

    def create_conn_string(self):
        pass

    def update_db(self, queries):
        conn = self.create_connection()
        for query in queries:
            pass
