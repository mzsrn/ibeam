import os
import json
from urllib import request, parse

_WEBHOOK_URI = os.environ.get('IBEAM_WEBHOOK_URI')
_CLIENT_IDENTIFIER = os.environ.get('IBEAM_CLIENT_IDENTIFIER')

class WebhookSender():
  
  def send_webhook(status, message):
    data = {
      "client": _CLIENT_IDENTIFIER,
      "status": status,
      "message": message
    }
    data = parse.urlencode(data).encode()
    req = request.Request(_WEBHOOK_URI, method="POST")
    r = request.urlopen(req, data=data)
    print(r.status)