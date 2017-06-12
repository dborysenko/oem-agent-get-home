import sys
from emcli import *
from emcli.exception import VerbExecutionError
set_client_property('EMCLI_OMS_URL','{{ OEM_URL }}')
set_client_property('EMCLI_TRUSTALL','true')

agent_list = ""

for agent in sys.argv:
    agent_list += ("'" + agent + ":{{ OEM_AGENT_PORT }}',")


#agent_host = sys.argv[0] + ":3872"

count = 0
#Login to the OMS
login(username="sysman", password="{{ OEM_PASSWORD }}")



query = """
select TT.HOST_NAME, TP.PROPERTY_VALUE, OH.OH_OWNER from MGMT$TARGET_PROPERTIES TP join MGMT$TARGET TT on TP.TARGET_GUID = TT.TARGET_GUID join MGMT$OH_HOME_INFO OH on TT.HOST_NAME = OH.HOST_NAME
where TT.TARGET_TYPE = 'oracle_emd' and TT.TARGET_NAME in (%s)
and TP.PROPERTY_NAME = 'OracleHome'
and OH.TARGET_NAME like 'agent%%'
""" % agent_list[:-1]

oracle_home = list(sql=query)

if len(oracle_home.out()['data']) < 1:
    exit(1)

logout()

result_dict = {}


for res in oracle_home.out()['data']:
    # result_dict[res['HOST_NAME']] = res['PROPERTY_VALUE']
    values_dict = {}
    values_dict['home_dir'] = res['PROPERTY_VALUE']
    values_dict['owner'] = res['OH_OWNER']
    result_dict[res['HOST_NAME']] = values_dict
print result_dict