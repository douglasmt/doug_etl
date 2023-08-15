from airflow.plugins_manager import AirflowPlugin
from airflow.hooks.base import BaseHook

from elasticsearch import Elasticsearch

# In order to connect Elastic Search with Airflow
class ElasticHook(BaseHook):

    def __init__(self, conn_id='elastic_default', *args, **kwargs):

        super().__init__( *args,**kwargs)
        conn = self.get_connection(conn_id) # get connection on airflow connections

        conn_config = {}
        hosts = []

        if conn.host: # get the variables
            hosts = conn.host.split(',')
        if conn.port:
            conn_config['port'] = int(conn.port)
        if conn.login:
            conn_config['http_auth'] = (conn.login, conn.password)

        self.es = Elasticsearch(hosts, **conn_config)  
        self.index = conn.schema # data in elastic in schema we define on connections

    def info(self):
        return self.es.info()

    def set_index(self, index):
        self.index = index

    def add_doc(self, index, doc_type, doc):
        self.set_index(index)
        res = self.es.index(index=index, doc_type=doc_type, doc=doc)
        return res

class AirflowElasticPlugin(AirflowPlugin):
    name = 'elastic'
    hooks = [ElasticHook] # system plugin manager

'''
  FutureWarning,
name    | source                                        | hooks
========+===============================================+=========================
elastic | $PLUGINS_FOLDER/hooks/elastic/elastic_hook.py | elastic_hook.ElasticHook
'''    