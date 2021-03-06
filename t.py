import requests
from blackbox import Record


r = Record()
r.metadata['test'] = True
r.metadata['life'] = 42
r.description = 'Snapshot of Douglas Adams article.'
r.content_type = 'text/html'
r.ref = 'http://en.wikipedia.org/wiki/Douglas_Adams'
r.upload_task.delay(r, data=requests.get(r.ref).content)
r.save()