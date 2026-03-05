from twilio.rest import Client

class Notifier:
    def __init__(self, account_sid, auth_token, from_number):
        self.client = Client(account_sid, auth_token)
        self.from_number = from_number

    def send(self, to_number, message):
        try:
            msg = self.client.messages.create(
                body=message,
                from_=self.from_number,
                to=to_number
            )
            print("SMS sent successfully. SID:", msg.sid)
        except Exception as e:
            print("SMS failed:", e)
