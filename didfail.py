from bs4 import BeautifulSoup
from dbmanager import iccAPI

#connect to db
icc = iccAPI()

#get applications id and name in the format [{id:"", name = ""},{...}]
apps = icc.getApplications()

#inverse the key and value of application dict
inv_apps = {}
for app in apps:
    inv_apps[app["name"]] = app["id"]


#Location of didfail output .out file
path = 'flows.out' 

output_file = open(path, 'r')
lines = output_file.readlines()

idx = 0

#start index of useful section
startIdx = 0

#end index of useful section
endIdx = 0

#useful section
flows = []

#only get the flows with 1 intents part
for line in lines:
    if 'Flows with 1 intent(s)' in line:
        startIdx = idx
    if 'Flows with 2 intent(s)' in line:
        endIdx = idx
    idx += 1

#assign the flow with 1 intent part to a new matrix, startIdx+1 to avoid "flow with 1 intent(s)" line
flows = lines[startIdx+1: endIdx]

#store all unique pairs of link source and target in links matrix
links = []
source = ""
target = ""

for flow in flows:
    for sub_flow in flow.split(','):
        #tx is the source
        if "tx=" in sub_flow:
            for k,v in inv_apps.items():
                if str(k) in sub_flow:
                    source = str(k)

        #rx is the target
        elif "rx=" in sub_flow:
	    for k,v in inv_apps.items():
                if str(k) in sub_flow:
                    target = str(k)

    #if both source and target exist
    if len(source)>0 and len(target)>0:
        link_map = {"source":source,"target":target}

        # check duplicate link, only add unique link
        if link_map not in links:
            links.append(link_map)

    #if source isn't exist
    elif len(source)==0:
        print("ERROR: source isn't exist")

    #if target isn't exist
    elif len(target)==0:
        print("ERROR: target isn't exist")

#get all links id between source and target and set didfail as 1 in the link table
for link in links:
    link_ids = []
    source_app = link["source"]
    target_app = link["target"]


    #get all the possible links id between source and target app
    link_ids = icc.findVulnerableLinks(source_app, target_app)

    #set didfail = 1 for each link in link table
    if len(link_ids)>0:
        for link_id in link_ids:
            icc.setDidfailVulnerableLink(link_id)
         


     
# disconnect from db
icc.close()    
