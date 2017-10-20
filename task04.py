import requests

#import json library
import json
controller='sandboxapic.cisco.com'
def getTicket():

    #controller='devnetapi.cisco.com/sandbox/apic_em'


    # put the ip address or dns of your apic-em controller in this url
    url = "https://" + controller + "/api/v1/ticket"

    #the username and password to access the APIC-EM Controller
    payload = {"username":"devnetuser","password":"Cisco123!"}

    #Content type must be included in the header
    header = {"content-type": "application/json"}

    #Performs a POST on the specified url to get the service ticket
    response= requests.post(url,data=json.dumps(payload), headers=header, verify=False)

    #convert response to json format
    r_json=response.json()

    #print(r_json)
    #parse the json to get the service ticket
    ticket = r_json["response"]["serviceTicket"]

    return ticket
def get_count(ticket):
    url = "https://" + controller + "/api/v1/network-device/count"

    # Content type must be included in the header as well as the ticket
    header = {"content-type": "application/json", "X-Auth-Token": ticket}

    # this statement performs a GET on the specified host url
    response = requests.get(url, headers=header, verify=False)

    # json.dumps serializes the json into a string and allows us to
    # print the response in a 'pretty' format with indentation etc.
    # print ("Hosts = ")
    # print (json.dumps(response.json(), indent=4, separators=(',', ': ')))
    r_resp = response.json()

    print("Number of Network Devices available:  ",r_resp["response"])


ticket=getTicket()

get_count(ticket)
