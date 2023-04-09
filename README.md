#Slack Message Sender ChatGPT Plugin Tutorial
This plugin sends messages into a Slack channel when prompted in ChatGPT with a matching prompt. 

## Configuring this app 
- After cloning this repo run a `pip install -r requirements.txt` to install all required libraries
- After generating your Slack Webhook Url as indicated here https://api.slack.com/messaging/webhooks
- Once you run your application and a server url is available, update the following lines of code 
    - In the ai-plugin.json file on line 12 `"<YOUR SERVER URL>/.well-known/slack-openapi.yaml",` replace <YOUR SERVER URL> with your server url
    - In slack-openapi.yaml file on line 7 `- url: <YOUR Server URL>` replace <YOUR SERVER URL> with your server url 


