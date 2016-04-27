from bs4 import BeautifulSoup
from dbmanager import iccAPI
import MySQLdb
import os

#Location of .xml files
path = 'merged' #architectural models generated by covert
icc = iccAPI()

#Parse each app found in directory path
for name in os.listdir(path):
    file_path = os.path.join(path, name)
    if os.path.isfile(file_path):
       if os.path.splitext(file_path)[-1].lower() == ".xml":

          #parse file
          soup = BeautifulSoup(open(file_path), "xml")

          #get app general info
          app_name = soup.find('packageName').string
          print(app_name)
          appID= icc.addApplication(app_name)

          #get app permissions
          for p in soup.find('usesPermissions').find_all('permission'):
              icc.addAppPermission(appID,p.string)

          #get app components
          for c in soup.find_all('Component'):
              c_type = c.find('type').string
              name = c.find('name',recursive = False).string
              c_id = icc.addComponent(appID,name,c_type)

              #get components required permissions
              c_permissions = "";
              for p in c.find('RequiredPermissions').find_all('PRM'):
                  icc.addComponentPermission(c_id,p.string)

              #get components intent filters
              for f in c.find('IntentFilter').find_all('filter'):
              	  filter_id = icc.addIntentFilter(c_id)
                  #check filter actions (there may be more than one action per filter)
                  for action in f.find_all('actions'):
                      icc.addIFAction(filter_id,action.string)

                  for category in f.find_all('categories'):
                      icc.addIFCategory(filter_id,category.string)

                  for data in f.find_all('data'):
                  	  mimeType = data.find('mimeType').string
                  	  icc.addIFMimeTypes(filter_id, mimeType)

          #get app intents
          for i in soup.find('newIntents').find_all('Intent'):
              sender = i.find('sender').string
              component = i.find('component').string
              action = i.find('action').string
              dataType = i.find('dataType').string
              method = i.find('consumerMethod').string

              if component != None and sender != None:
              	 intent_id = icc.addIntent(appID,sender,0, method)
              	 icc.addIntentComponent(appID,intent_id,component)
              elif sender != None:
              	 intent_id = icc.addIntent(appID,sender,1, method)

              if action != None:
                 action = action[1:-1] #remove quotes
                 icc.addIntentAction(intent_id,action)

              if dataType != None:
              	 dataType = dataType[1:-1] #remove quotes
                 icc.addIntentMimeType(intent_id,dataType)
            
# disconnect from db
icc.close()
            