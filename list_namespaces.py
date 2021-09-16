from kubernetes import config, client

config.load_kube_config()

api = client.BatchV1Api()

result = api.list_namespaced_job(namespace='gdpr-anonymizer', watch=False)

if not result.items:
    print('No jobs')
else:
    for item in result.items:
        print(item.metadata.name)
