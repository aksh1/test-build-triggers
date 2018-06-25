
from pprint import pprint

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
import os.path
import json



# Project ID for this request.
project = 'timus-199318'  
# The name of the zone where the instance group is located.
zone = 'us-east1-b'
# The name of the instance group from which you want to generate a list of included instances.
instance_group = 'instance-group-1'
 

request_body={}
new_instance={}

def  dump_in_file(filename,data):
  data=json.dumps(data)
  with open(filename,'w') as f:
    json.dump(data,f)


def parse_respose(response):
  list_of_instance=[]
  for res in response["items"]:
    split_res=res["instance"].split("/")
    index=len(split_res)-1
    list_of_instance.append(split_res[index])
  return list_of_instance
   

def get_instance_ip(service,instance):
  
  request = service.instances().get(project=project, zone=zone, instance=instance)
  response = request.execute()
  for item in response['networkInterfaces']:
    for accessConfigs in item['accessConfigs']:
      new_instance.update({instance:accessConfigs["natIP"]})


def check_new_instance(service):
  request = service.instanceGroups().listInstances(project=project, zone=zone, instanceGroup=instance_group,body=request_body)
  response = request.execute()
  parsed_respose=parse_respose(response)
  

  if os.path.isfile("list_of_instance"):
    with open("list_of_instance",'r') as r:
      files=json.load(r)

    for instance in parsed_respose:
      if instance in files:
        print instance + "is present in list"
      else:
        print "New Instance found"
        get_instance_ip(service,instance)

    no_of_instances=len(response)
    dump_in_file("list_of_instance",parsed_respose)
    return no_of_instances

  else:
    no_of_instances=len(response['items'])
    dump_in_file("list_of_instance",parsed_respose)
    return no_of_instances



def main():
  credentials = GoogleCredentials.get_application_default()
  service = discovery.build('compute', 'v1', credentials=credentials)
  # get_list_instancegroup(service)
  # check_new_instance(service)
  # print new_instance
  patch_firewall(service)



def patch_firewall(service):
  firewall="default-allow-http"
  firewall_body={
  "description": "qrefqejgnkjgnqjeknj",
  "sourceRanges": ["0.0.0.0","12.12.12.12"]
  }
  request = service.firewalls().patch(project=project, firewall=firewall, body=firewall_body)
  response = request.execute()
  pprint(response)



if __name__ == '__main__':
  main()