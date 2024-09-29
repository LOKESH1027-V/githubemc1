#nesteddictionary or nestedlistdictonary
d={
    "lokesh":{"id":18,"age":22,"course":"python"},
    "mohan":{"id":20,"age":44,"course":"python"},
    "morgan":{"id":22,"age":24,"course":"python"},
    
}
print(d["mohan"]["age"])
d["mohan"]["phone"]=9999
print(d["mohan"])
d["mohan"].pop(["phone"])
print(d.keys())
