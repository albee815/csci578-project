import MySQLdb

class iccAPI:

  #connect to db
  def __init__(self):
    self.db = MySQLdb.connect("localhost","root","123","icc" )
    self.cursor = self.db.cursor()

  #close db connection
  def close(self):
    self.db.close()

  #Add an application 
  def addApplication(self, name):

    apps = [];
    sql = "INSERT INTO Applications(app) VALUES ('%s')" %(name)

    try:
      # Execute the SQL command
      self.cursor.execute(sql)
      self.db.commit()

      #Return application id
      return self.cursor.lastrowid

    except:
        self.db.rollback()
        print "Error: unable to add application"

  #Add an app permission
  def addComponent(self, app_id, component, ctype):

    sql = "INSERT INTO Components(app_id, component, type) VALUES ('%d','%s','%s')" %(app_id, component, ctype)

    try:
      # Execute the SQL command
      self.cursor.execute(sql)
      self.db.commit()

      #Return application id
      return self.cursor.lastrowid

    except:
        self.db.rollback()
        print "Error: unable to add app component"


  #Add an app intent
  def addIntent(self, app_id, sender, implicit, method):

    sender_id= self.getComponent(app_id, sender)

    if(sender_id < 0):
       sender_id = self.addComponent(app_id, sender, 'Unknown')

    sql = "INSERT INTO Intents(source, implicit, method) VALUES ('%d','%d','%s')" %(sender_id, implicit, method)

    try:
      # Execute the SQL command
      self.cursor.execute(sql)
      self.db.commit()

      #Return application id
      return self.cursor.lastrowid

    except:
        self.db.rollback()
        print "Error: unable to add intent"

  #Add an app component
  def addIntentComponent(self, app_id, intent_id, component):

    component_id= self.getComponent(app_id, component)

    if(component_id < 0):
       component_id = self.addComponent(app_id, component, 'Unknown')

    sql = "INSERT INTO IComponent(intent_id, component) VALUES ('%d','%d')" %(intent_id, component_id)

    try:
      # Execute the SQL command
      self.cursor.execute(sql)
      self.db.commit()

      #Return application id
      return self.cursor.lastrowid

    except:
        self.db.rollback()
        print "Error: unable to add intent component"

  #Add an intent action
  def addIntentAction(self, intent_id, action_st):

    action_id= self.getActionString(action_st)

    if(action_id < 0):
       action_id = self.addActionString(action_st)

    sql = "INSERT INTO IActions(intent_id, action) VALUES ('%d','%d')" %(intent_id, action_id)

    try:
      # Execute the SQL command
      self.cursor.execute(sql)
      self.db.commit()

      #Return application id
      return self.cursor.lastrowid

    except:
        self.db.rollback()
        print "Error: unable to add intent action"

  #Add an intent mimetype
  def addIntentMimeType(self, intent_id, mimetype):

    sql = "INSERT INTO IMimeTypes(intent_id, type) VALUES ('%d','%s')" %(intent_id, mimetype)

    try:
      # Execute the SQL command
      self.cursor.execute(sql)
      self.db.commit()

      #Return application id
      return self.cursor.lastrowid

    except:
        self.db.rollback()
        print "Error: unable to add intent mimetype"

  #Add an app permission
  def addAppPermission(self, app_id, permission_st):

    permission_id= self.getPermissionString(permission_st)

    if(permission_id < 0):
       permission_id = self.addPermissionString(permission_st)

    sql = "INSERT INTO AppPermissions(app_id, permission) VALUES ('%d','%d')" %(app_id, permission_id)

    try:
      # Execute the SQL command
      self.cursor.execute(sql)
      self.db.commit()

      #Return application id
      return self.cursor.lastrowid

    except:
        self.db.rollback()
        print "Error: unable to add app permission"

  #Add a component permission
  def addComponentPermission(self, component_id, permission_st):

    permission_id= self.getPermissionString(permission_st)

    if(permission_id < 0):
       permission_id = self.addPermissionString(permission_st)

    sql = "INSERT INTO ComponentPermissions(component_id, permission) VALUES ('%d','%d')" %(component_id, permission_id)

    try:
      # Execute the SQL command
      self.cursor.execute(sql)
      self.db.commit()

      #Return application id
      return self.cursor.lastrowid

    except:
        self.db.rollback()
        print "Error: unable to add component permission"

  #Add an intent filter action
  def addIFAction(self, app_id, action_st):

    action_id= self.getActionString(action_st)

    if(action_id < 0):
       action_id = self.addActionString(action_st)

    sql = "INSERT INTO IFActions(filter_id, action) VALUES ('%d','%d')" %(app_id, action_id)

    try:
      # Execute the SQL command
      self.cursor.execute(sql)
      self.db.commit()

      #Return application id
      return self.cursor.lastrowid

    except:
        self.db.rollback()
        print "Error: unable to add intent filter action"

  #Add an intent filter category
  def addIFCategory(self, app_id, category_st):

    category_id= self.getCategoryString(category_st)

    if(category_id < 0):
       category_id = self.addCategoryString(category_st)

    sql = "INSERT INTO IFCategories(filter_id, category) VALUES ('%d','%d')" %(app_id, category_id)

    try:
      # Execute the SQL command
      self.cursor.execute(sql)
      self.db.commit()

      #Return application id
      return self.cursor.lastrowid

    except:
        self.db.rollback()
        print "Error: unable to add intent filter category"

  #Add an intent filter mimetype
  def addIFMimeTypes(self, app_id, mimetype):

    sql = "INSERT INTO IFMimeTypes(filter_id, type) VALUES ('%d','%s')" %(app_id, mimetype)

    try:
      # Execute the SQL command
      self.cursor.execute(sql)
      self.db.commit()

      #Return application id
      return self.cursor.lastrowid

    except:
        self.db.rollback()
        print "Error: unable to add intent filter mimetype"

  #Add an intent filter
  def addIntentFilter(self, component_id):

    sql = "INSERT INTO IntentFilters(component_id) VALUES ('%d')" %(component_id)

    try:
      # Execute the SQL command
      self.cursor.execute(sql)
      self.db.commit()

      #Return application id
      return self.cursor.lastrowid

    except:
        self.db.rollback()
        print "Error: unable to add intent filter"


  #Add permission string
  def addPermissionString(self, permission_st):

    sql = "INSERT INTO PermissionStrings(st) VALUES ('%s')" %(permission_st)

    try:
      # Execute the SQL command
      self.cursor.execute(sql)
      self.db.commit()

      #Return application id
      return self.cursor.lastrowid

    except:
        self.db.rollback()
        print "Error: unable to add permission string"

  #Add action string
  def addActionString(self, action_st):

    sql = "INSERT INTO ActionStrings(st) VALUES ('%s')" %(action_st)

    try:
      # Execute the SQL command
      self.cursor.execute(sql)
      self.db.commit()

      #Return application id
      return self.cursor.lastrowid

    except:
        self.db.rollback()
        print "Error: unable to add action string"


  #Add category string
  def addCategoryString(self, category_st):

    sql = "INSERT INTO CategoryStrings(st) VALUES ('%s')" %(category_st)

    try:
      # Execute the SQL command
      self.cursor.execute(sql)
      self.db.commit()

      #Return application id
      return self.cursor.lastrowid

    except:
        self.db.rollback()
        print "Error: unable to add category string"

  def addLink(self, source, target, method, action):

    if self.linkExists(source,target, method, action):
       return "Link exists"

    sql = "INSERT INTO Links(source, target, method, action, covert, didfail) VALUES ('%d','%d','%s','%s',0,0)" %(source,target,method,action)

    try:
      # Execute the SQL command
      self.cursor.execute(sql)
      self.db.commit()

      #Return application id
      return self.cursor.lastrowid

    except:
        self.db.rollback()
        print "Error: unable to add link"

  #Get applications
  def getApplications(self):

    apps = [];
    sql = "SELECT * FROM Applications ORDER BY id"

    try:
      # Execute the SQL command
      self.cursor.execute(sql)
      results = self.cursor.fetchall()

      for app in results:
          apps.append({'id':app[0], 'name':app[1]})

      return apps;

    except:
        print "Error: unable to fetch applications"

  #Get action string
  def getActionString(self, action):

    sql = "SELECT id FROM ActionStrings WHERE st= '%s'" %(action)

    try:
      self.cursor.execute(sql)
      results = self.cursor.fetchall()

      if (len(results) > 0):
          return results[0][0];

      else:
        return -1;

    except:
        print "Error: unable to fetch action string"

  #Get category string
  def getCategoryString(self, category):

    sql = "SELECT id FROM CategoryStrings WHERE st= '%s'" %(category)

    try:
      self.cursor.execute(sql)
      results = self.cursor.fetchall()

      if (len(results) > 0):
          return results[0][0];

      else:
        return -1;

    except:
        print "Error: unable to fetch category string"

  #Get an app component
  def getComponent(self, app_id, component):

    sql = "SELECT id FROM Components WHERE app_id = '%s' AND component= '%s'" %(app_id, component)

    try:
      self.cursor.execute(sql)
      results = self.cursor.fetchall()

      if (len(results) > 0):
          return results[0][0];

      else:
        return -1;

    except:
        print "Error: unable to fetch app component"

  #Get permission id
  def getPermissionString(self, permission):

    sql = "SELECT id FROM PermissionStrings WHERE st= '%s'" %(permission)

    try:
      self.cursor.execute(sql)
      results = self.cursor.fetchall()

      if (len(results) > 0):
          return results[0][0];

      else:
        return -1;

    except:
        print "Error: unable to fetch permission id"

  #Get an app permissions
  def getApplicationPermissions(self, app_id):

    permissions = "";

    sql = "SELECT st FROM AppPermissions LEFT JOIN PermissionStrings ON AppPermissions.permission = PermissionStrings.id \
           WHERE app_id = '%d'" %(app_id)

    try:
      self.cursor.execute(sql)
      results = self.cursor.fetchall()

      for p in results:
          permissions += p[0].replace('android.permission.','') + ", "

      if (len(results) == 0):
          permissions = "None"

      else:
        permissions = permissions[:-2]

      return permissions;

    except:
        print "Error: unable to fetch app permissions"

  #Get an app components
  def getApplicationComponents(self, app_id):

    classes = [];

    sql = "SELECT Components.id, component FROM Components LEFT JOIN Applications ON Components.app_id = Applications.id \
           WHERE Applications.id ='%d' ORDER BY Components.id" %(app_id)

    try:
      self.cursor.execute(sql)
      results = self.cursor.fetchall()

      for c in results:
          classes.append({'id':c[0], 'name':c[1]})

      return classes;

    except:
        print "Error: unable to fetch app components"


  #Get components permissions
  def getComponentPermissions(self, component_id):

    permissions = "";

    sql = "SELECT st FROM ComponentPermissions LEFT JOIN PermissionStrings ON ComponentPermissions.permission = PermissionStrings.id \
           WHERE component_id = '%d'" %(component_id)

    try:
      self.cursor.execute(sql)
      results = self.cursor.fetchall()

      for p in results:
          permissions += p[0].replace('android.permission.','') + ", "

      if (len(results) == 0):
          permissions = "None"

      else:
        permissions = permissions[:-2]

      return permissions;

    except:
        print "Error: unable to fetch component permissions"

  #Get component intents
  def getComponentIntents(self, component_id):

    intents= [];

    sql = "SELECT Intents.id, Intents.implicit, Intents.method, ActionStrings.st FROM Intents LEFT JOIN IActions ON \
          Intents.id = IActions.intent_id LEFT JOIN ActionStrings ON IActions.action = ActionStrings.id WHERE Intents.source ='%d'" %(component_id)

    try:
      self.cursor.execute(sql)
      results = self.cursor.fetchall()
      for i in results:
          if i[3] != "android.intent.action.MAIN":
             intents.append({'id':i[0], 'implicit': i[1], 'method':i[2]})

      return intents;

    except:
        print "Error: unable to fetch component intents"


  #Get component links
  def getComponentLinks(self, component_id):

    links= [];

    sql = "SELECT target, method, action, covert, didfail FROM Links WHERE source = '%d'" %(component_id)

    try:
      self.cursor.execute(sql)
      results = self.cursor.fetchall()

      for i in results:
          links.append({'target': i[0], 'method':i[1], 'action':i[2], 'covert':i[3], 'didfail':i[4]})

      return links;

    except:
        print "Error: unable to fetch component links"


  #Get component vulnerable links
  def findVulnerableLinks(self, app1, app2):

    links= [];

    sql = "SELECT Links.id FROM Links LEFT JOIN Components as A ON Links.source = A.id \
    LEFT JOIN Components as B ON Links.target = B.id LEFT JOIN Applications as C ON A.app_id = C.id LEFT JOIN Applications\
    as D ON B.app_id = D.id WHERE C.app = '%s' AND D.app = '%s'" %(app1, app2)

    try:
      self.cursor.execute(sql)
      results = self.cursor.fetchall()

      for i in results:
          links.append(i[0])

      return links;

    except:
        print "Error: unable to find didfail vulnerable links"

  #Set difail link
  def setDidfailVulnerableLink(self, link_id):

    sql = "UPDATE Links SET didfail = 1 WHERE Links.id = '%d'" %(link_id)

    try:
      self.cursor.execute(sql)
      self.db.commit()

    except:
        self.db.rollback()
        print "Error: unable to set didfail link"

  #Get and set component vulnerable links
  def markCovertSpoofingVulnerabilities(self, app, component):

    sql = "UPDATE Links AS A, (SELECT Links.id FROM Links LEFT JOIN Components ON Links.target = Components.id \
    LEFT JOIN Applications ON Components.app_id = Applications.id WHERE Components.component = '%s' AND Applications.app= '%s') as B\
    SET covert = 1 WHERE A.id = B.id" %(component, app)

    try:
      self.cursor.execute(sql)
      self.db.commit()

    except:
        self.db.rollback()
        print "Error: unable to find covert vulnerable links"

  #Set covert link
  def setCovertVulnerableLink(self, link_id):

    sql = "UPDATE Links SET covert = 1 WHERE Links.id = '%d'" %(link_id)

    try:
      self.cursor.execute(sql)
      self.db.commit()

    except:
        self.db.rollback()
        print "Error: unable to set covert link"

  #Get component links
  def linkExists(self, source, target, method, action):

    sql = "SELECT * FROM Links WHERE source = '%d' AND target = '%d' AND method = '%s' AND action = '%s'" %(source, target, method, action)
    try:
      self.cursor.execute(sql)
      result = len(self.cursor.fetchall())
      if result > 0:
         return 1
      else:
         return 0
      
    except:
        print "Error: unable to check link existence"

  #Get explicit intent component
  def getIntentComponent(self, intent_id):

    sql = "SELECT component from IComponent WHERE intent_id ='%d'" %(intent_id)

    try:
      self.cursor.execute(sql)
      results = self.cursor.fetchall()

      if(len(results) > 0):
        return results[0][0]

      else:
        return None

    except:
        print "Error: unable to fetch intent component"

  #Get intent action
  def getIntentAction(self, intent_id):

    sql = "SELECT st FROM IActions LEFT JOIN ActionStrings ON IActions.action = ActionStrings.id WHERE intent_id ='%d'" %(intent_id)

    try:
      self.cursor.execute(sql)
      results = self.cursor.fetchall()

      if(len(results) > 0):
        return results[0][0]

      else:
        return None

    except:
        print "Error: unable to fetch intent action"

  #Get intent mimeTypes
  def getIntentMimeType(self, intent_id):

    sql = "SELECT type from IMimeTypes WHERE intent_id ='%d'" %(intent_id)

    try:
      self.cursor.execute(sql)
      results = self.cursor.fetchall()

      if(len(results) > 0):
        return results[0][0]

      return None

    except:
        print "Error: unable to fetch intent mimeType"

  #get intent category matches
  def getIntentMatches (self,action, mimetype):
    matches= []

    #If intent has an action specified, and no mimetype: only intent filters with no mimetype specified can be considered
    if action != None:

       if mimetype != None:
          #both action and mimetypes specified: matching intent filters must include the same action and mimetype as intent
          sql = "SELECT DISTINCT Components.id as id FROM Components LEFT JOIN IntentFilters ON \
          Components.id = IntentFilters.component_id LEFT JOIN IFMimeTypes ON IntentFilters.id = IFMimeTypes.filter_id \
          LEFT JOIN IFActions ON IFActions.filter_id = IntentFilters.id LEFT JOIN ActionStrings ON IFActions.action = ActionStrings.id\
          WHERE ActionStrings.st = '%s' and IFMimeTypes.type ='%s'" %(action, mimetype)

       else: 
            sql = "SELECT DISTINCT Components.id FROM Components LEFT JOIN IntentFilters ON \
            Components.id = IntentFilters.component_id LEFT JOIN IFMimeTypes ON IntentFilters.id = IFMimeTypes.filter_id \
            LEFT JOIN IFActions ON IFActions.filter_id = IntentFilters.id LEFT JOIN ActionStrings ON IFActions.action = ActionStrings.id \
            WHERE IFMimeTypes.type IS NULL AND ActionStrings.st = '%s'" %(action)

    #no actions specified
    else:
        if mimetype != None:
           sql = "SELECT DISTINCT Components.id FROM Components LEFT JOIN IntentFilters ON \
           Components.id = IntentFilters.component_id LEFT JOIN IFMimeTypes ON IntentFilters.id = IFMimeTypes.filter_id \
           LEFT JOIN IFActions ON IFActions.filter_id = IntentFilters.id LEFT JOIN ActionStrings ON IFActions.action = ActionStrings.id\
           WHERE IFMimeTypes.type ='%s'" %(mimetype)
        else:
            return matches

    try:
      self.cursor.execute(sql)
      results = self.cursor.fetchall()

      for i in results:
          matches.append(i[0])

      return matches;

    except:
        print "Error: unable to fetch intent matches"



