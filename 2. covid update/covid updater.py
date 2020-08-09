from twilio.rest import Client
import requests
import json

def formate_data(js):
    status = "*Covid Update*" + "\nCountry: India" + "\nTotal Cases: " + str(js['cases'])
    status+= "\nToday Case: " + str(js['todayCases'])
    status+= "\nRecovered till date: " + str(js['recovered'])
    status+= "\nActive Cases: " + str(js['active'])
    status+= "\n\nSTAY HOME,STAY SAFE🙏🏻\nHAVE A NICE DAY☺"
    status+="\n\nNote:- If Today Case is Zero that means data is not updated."
    return status

def get_status():
    url="https://coronavirus-19-api.herokuapp.com/countries/India"
    response=requests.request("GET",url)
    data=response.text.encode()
    #print(data)
    js=json.loads(data.decode())
    status=formate_data(js)
    #print(status)
    return status

def send_whatsapp_messege(status,no):
    account_sid = 'AC71a69974ac9ee287045d7750ad6cfcf2'
    auth_token = '6aa506daffbabdd7f92e90c8e2ec29e7'
    client = Client(account_sid, auth_token)
    whatsapp="whatsapp:"+str(no)
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=str(status),
        to=str(whatsapp)
    )
    print(message.sid)

def send_sms(status,no):
    account_sid = 'AC71a69974ac9ee287045d7750ad6cfcf2'
    auth_token = '6aa506daffbabdd7f92e90c8e2ec29e7'
    client = Client(account_sid, auth_token)
    mobile_no = str(no)
    message = client.messages.create(
        from_='+12543230007',
        body=str(status),
        to=mobile_no
    )
    print(message.sid)


def main():
    mobile_number=["+918469559091","+919712783442"]
    status=get_status()
    for no in mobile_number:
        send_whatsapp_messege(status,no)
        send_sms(status,no)



main()


# twiliopassJay...1@Ja...j1@_twilio
# pip installed -> twilio

