from dbmanager import iccAPI

#connect to db
icc = iccAPI()

#Get architectural model
applications = icc.getApplications()

for app in applications:

    id = app['id']

    #get components
    app_components = icc.getApplicationComponents(id)
    for app_component in app_components:

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
                    icc.addLink(app_component['id'], match, intent['method'], action)

            #explicit intents
            else:
                target = icc.getIntentComponent(intent['id'])
                if(target != None):
                   action = icc.getIntentAction(intent['id'])
                   icc.addLink(app_component['id'], target, intent['method'], action)

# disconnect from db
icc.close()