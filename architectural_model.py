from dbmanager import iccAPI
import json

#Data format accepted by Visualization tool
nodes = []   #onenode per app component
links = []   #connections among components
groups = []  #components per app and permissions

#connect to db
icc = iccAPI()

#Get architectural model
applications = icc.getApplications()

for app in applications:

    id = app['id']
    app_name = app['name']
    print(app_name)

    #get app permissions 
    app_permissions = icc.getApplicationPermissions( id)

    #get components
    leaves = []
    app_components = icc.getApplicationComponents(id)
    for app_component in app_components:

        #get components permissions
        component_name = app_component['name'].split('.')[-1]
        component_permissions = icc.getComponentPermissions(app_component['id'])  
        nodes.append({'name': component_name, 'permissions': component_permissions, 'width':120, 'height':50}) #for visualization tool
        leaves.append(len(nodes)-1)

        #get links
        clinks = icc.getComponentLinks(app_component['id'])
        for clink in clinks:
            color = "black"
            if clink['covert'] and clink['didfail']:
               color = "red"
            elif clink['covert']:
                 color = "blue"
            elif clink['didfail']:
                 color = "purple"

            links.append({'source': app_component['id']-1 , 'target': clink['target']-1, 'method': clink['method'],'action': clink['action'], 'color':color})

    groups.append({'name':app_name,'permissions': app_permissions, 'leaves':leaves})

# disconnect from db
icc.close()

#export data to json file
data = {'nodes':nodes, 'groups':groups, 'links':links}
json.dump(data, open('data.json', 'wb'))