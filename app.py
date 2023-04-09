import os
import httpx
import quart
import quart_cors
from quart import request, Response
from dotenv import load_dotenv
load_dotenv()


# Note: Setting CORS to allow chat.openapi.com is required for ChatGPT to access your plugin
app = quart_cors.cors(quart.Quart(__name__), allow_origin="https://chat.openai.com")
slack_webhook_url = os.environ.get("SLACK_WEBHOOK_URL")
@app.post("/send_slack_message/<string:message>")
async def send_slack_message(message: str):
    headers = {"Content-Type": "application/json"}
    data = {"text": message}

    async with httpx.AsyncClient() as client:
        response = await client.post(slack_webhook_url, json=data, headers=headers)

    if response.status_code == 200:
        return Response(response="OK", status=200)
    else:
        return Response(response="Failed to send message to Slack", status=response.status_code)

@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
    host = request.headers['Host']
    with open("ai-plugin.json") as f:
        text = f.read()
        # This is a trick we do to populate the PLUGIN_HOSTNAME constant in the manifest
        text = text.replace("PLUGIN_HOSTNAME", f"https://{host}")
        return quart.Response(text, mimetype="text/json")

@app.get("/.well-known/slack-openapi.yaml")
async def openapi_spec():
    host = request.headers['Host']
    with open("slack-openapi.yaml") as f:
        text = f.read()
        # This is a trick we do to populate the PLUGIN_HOSTNAME constant in the OpenAPI spec
        text = text.replace("PLUGIN_HOSTNAME", f"https://{host}")
        return quart.Response(text, mimetype="text/yaml")

def main():
    app.run(debug=True, host="0.0.0.0", port=5002)

if __name__ == "__main__":
    main()
