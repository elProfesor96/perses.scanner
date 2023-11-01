import config
from slack_sdk.webhook import WebhookClient

### slack implementation is based on the slack webhook
### (optional) slack bot with /scan command into the chat/channel
#  to scan a file directly from slack
class Integrations:
    def __init__(self):
        self.config = config.Config()
        self.slack_webhook_token = self.config.readSlack()
        self.message = ''

    def slack(self, message):
        self.message = message
        webhook = WebhookClient(self.slack_webhook_token)
        response = webhook.send(text=self.message)
        assert response.status_code == 200
        assert response.body == "ok"
        return response

    def rocketchat(self):
        pass

### rocket.chat