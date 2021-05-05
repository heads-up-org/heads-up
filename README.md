# Heads-up!
___
## headsup.alerts.local

How to use the local alerts

from headsup.local import headsup
headsup()

or

from headsup.local import headsup
headsup(loop=True)

## headsup.alerts.remote 

How to use the remote alerts

from headsup.remote import watch, notify
watch_code = watch()
...
notify(watch_code, "Success!!")

alternatively, 

watch(QR=True, QRInline=True)
