import xmlrpc.client

# Connect to the Moses server
server = xmlrpc.client.ServerProxy("http://localhost:8080/RPC2")
response = server.translate({"text": "इन सब बातों म भी अय्यूब न नहीं त पाप करयो , अऊर नहीं परमेश्वर पर दोष लगायो ।"})
#print(response)
print("Translated Text:", response['text'])


# Send a translation request
# input_text = "इन सब बातों म भी अय्यूब न नहीं त पाप करयो , अऊर नहीं परमेश्वर पर दोष लगायो । "
# response = server.translate({"text": input_text, "align": "false"})

# Print the translated text
#print("Translated Text:", response['text'])
