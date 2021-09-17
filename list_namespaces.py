from sys import argv, exit
from kubernetes import config, client

if len(argv) < 2:
    print(f'USAGE:     {argv[0]} NAMESPACE')
    exit(0)

config.load_kube_config()

api = client.BatchV1Api()

result = api.list_namespaced_job(namespace=argv[1], watch=False)

if not result.items:
    print('No jobs')
else:
    for item in result.items:
        print(item.status)
        print(f'{item.metadata.name}: {item.status.succeeded}')



# WHEN ACTIVE (item.status)
# {'active': 1,
#  'completion_time': None,
#  'conditions': None,
#  'failed': None,
#  'start_time': datetime.datetime(2021, 9, 16, 17, 26, 32, tzinfo=tzutc()),
#  'succeeded': None}

# ------------------------------------------

# WHEN SUCCEEDED (item.status)
# {'active': None,
#  'completion_time': datetime.datetime(2021, 9, 16, 17, 26, 37, tzinfo=tzutc()),
#  'conditions': [{'last_probe_time': datetime.datetime(2021, 9, 16, 17, 26, 37, tzinfo=tzutc()),
#                  'last_transition_time': datetime.datetime(2021, 9, 16, 17, 26, 37, tzinfo=tzutc()),
#                  'message': None,
#                  'reason': None,
#                  'status': 'True',
#                  'type': 'Complete'}],
#  'failed': None,
#  'start_time': datetime.datetime(2021, 9, 16, 17, 26, 32, tzinfo=tzutc()),
#  'succeeded': 1}
