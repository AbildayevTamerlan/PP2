import json

with open("sample-data.json", "r") as file:
    data = json.load(file)

header = """Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------"""

print(header)

interfaces = data["imdata"]

for item in interfaces:
   attributes = item["l1PhysIf"]["attributes"]
   dn = attributes["dn"]
   description = attributes.get("descr", "")
   speed = attributes.get("speed", "inherit")
   mtu = attributes["mtu"]

   print(f"{dn:<50} {description:<20} {speed:<7} {mtu}")