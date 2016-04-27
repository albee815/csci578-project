from dbmanager import iccAPI
import MySQLdb
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

        #get intents
        intents = icc.getComponentIntents(app_component['id'])
        for intent in intents:
            #implicit intents
            if (intent['implicit']):

                action = icc.getIntentAction(intent['id'])
                mimetype = icc.getIntentMimeType(intent['id'])

                #find matches
                matches = icc.getIntentMatches(action,mimetype);
                matches;
                for match in matches:
                    links.append({'source': len(nodes)-1 , 'target': match-1, 'method': intent['method'], 'action': action})
            #explicit intents
            else:
                target = icc.getIntentComponent(intent['id'])
                if(target != None):
                   action = icc.getIntentAction(intent['id'])
                   links.append({'source': len(nodes)-1 , 'target': target-1, 'method': intent['method'], 'action': action})


    groups.append({'name':app_name,'permissions': app_permissions, 'leaves':leaves})

# disconnect from db
icc.close()

#export data to json file
data = {'nodes':nodes, 'groups':groups, 'links':links}
json.dump(data, open('data.json', 'wb'))