import pyunicore.client as unicore_client
from base64 import b64encode

if __name__ == "__main__":
    base_url = "https://draco-nginx:8080/DEMO-SITE/rest/core"

    # authenticate with username/password
    username = ''
    password = ''
    token = b64encode(f"{username}:{password}".encode('utf-8')).decode("ascii")
    transport = unicore_client.Transport(token, oidc=False)

    transport = unicore_client.Transport(token, oidc=False)
    all_sites = unicore_client.get_sites(transport)
    print(all_sites)

    client = unicore_client.Client(transport, base_url)
    # client.properties

    my_job = {'Executable': 'sleep 100'}

    job = client.new_job(job_description=my_job, inputs=[])
    # job.properties
    # job.working_dir.properties
    # job.working_dir.listdir()

    jobs = client.get_jobs()
    print(jobs[0].is_running())
