# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

import requests

discordBot_GPA = "https://discord.com/api/webhooks/967055567061418024/Y1UNZnlf6gohtn73C6JJA6B13lB-QmzEbWamJ1REsyL9Wai4gGUgbHA4cK5sejysM4Ne"    #GPA webhook (hackable, but pointless)                                             
                
headers = {
    'Content-Type': 'application/json'
}

message = " UwU "
payload = {"content": message}
r = requests.post(discordBot_GPA,data=payload,headers=headers)









