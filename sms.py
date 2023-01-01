from twilio.rest import Client 
 
account_sid = '' 
auth_token = '' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='', 
                              body='Testing, 123!!!',      
                              to='' 
                          ) 
 
print(message.sid)