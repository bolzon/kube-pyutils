from sys import argv, exit
from kubernetes import config, client

if len(argv) < 2:
    print(f'USAGE:     {argv[0]} NAMESPACE')
    exit(0)

CONTAINER_NAME = 'test-pod'
CONTAINER_IMAGE = 'docker/whalesay'
NAMESPACE = argv[1]

config.load_kube_config()

container = client.V1Container(name=CONTAINER_NAME,
                               image=CONTAINER_IMAGE,
                               image_pull_policy='Always')

pod_template = client.V1PodTemplate()
pod_template = template = client.V1PodTemplateSpec()

template = client.V1PodTemplateSpec()
template.spec = client.V1PodSpec(containers=[container],
                                 restart_policy='OnFailure')

body = client.V1Job()
body.metadata = client.V1ObjectMeta(namespace=NAMESPACE, name='test-job')
body.spec = client.V1JobSpec(template=template)

api = client.BatchV1Api()

result = api.create_namespaced_job(namespace=NAMESPACE, body=body)

print(result)