from bs4 import BeautifulSoup
from dbmanager import iccAPI
import os

#Location of .xml files
file_path = 'bundle.xml' 
icc = iccAPI()

if os.path.isfile(file_path):
    if os.path.splitext(file_path)[-1].lower() == ".xml":

         #parse file
         soup = BeautifulSoup(open(file_path), "xml")
         #get vulnerabilities
         for v in soup.find('vulnerabilities').find_all('vulnerability'): 
         	 #get type of attack
             v_type = v.find('type').string 
             v_elements = v.find("vulnerabilityElements")	 
             #get app vulnerabilities
             if v_elements.find('type').string == "APP":
             	v_app = v_elements.find('description').string
             	#get vulnerable components
             	for element in v_elements.find_all("element", recursive=False):
             	 	if element.find('type').string == "COMPONENT":
             	 		#get vulnerable component
             	 		v_component = element.find('description').string
             	 		if v_type == "Intent Spoofing":
             	 		   links = icc.markCovertSpoofingVulnerabilities(v_app, v_component)
        
            
# disconnect from db
icc.close()