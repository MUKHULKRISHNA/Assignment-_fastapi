from configparser import ConfigParser
import os


conf_path = os.getcwd() + '\\configuration\\application.conf'
config = ConfigParser()
config.read(conf_path)

host = config.get('PortDetails', 'host', fallback='127.0.0.1')
port = config.get('PortDetails', 'port', fallback='8000')

# my_db = config.get('MongoDetails', 'db_intern', fallback='my database')
# student_base = config.get('MongoDetails', 'db-my')
#
# # get_const = config.get('Apis', 'get')
# post_const = config.get('Apis', 'post')
# get_const_2 = config.get('Apis', 'get_2')
# put_cons = config.get('Apis', 'put')
# del_cons = config.get('Apis', 'del')
# email_cons = config.get('Apis', 'email_apis')
# pipline_cons = config.get('Apis', 'pipeline_ap')
