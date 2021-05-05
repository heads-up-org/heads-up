# Heads-up!
If you are a developer, your life has a lot of suffering. Here is a package to bring some sunlight into the abyss that is your soul. 
Raise a hand if the following scenario is familiar to you. 

After a long session of coding, you finally run the script that trains your machine learning model (or data processing, or some other batch operation). 
You do not know when it will finish. You want to open a beer, sit on your couch and watch Netflix while your code is running. But something is eating you inside.
An uncontrollable urge compels you to check the computer. Maybe the code threw an exception. There is no way to know that, right? 
WRONG! From now on, you are in control! Use Heads up to be notified when your code completes execution (or practically at any stage of your code). 

You have two options: 
- headsup.local
- headsup.remote

headsup.local allows you to play a cool sound file when you call the headsup() method. Simple! Because it should be simple! 

headsup.remote on the other hand, allows you to communicate the status of your code with the Heads up server, which you can tap into using the browser your laptop or your mobile phone. You will simply be given a heads up when your code reaches a certain stage in execution. 

Check out the methods below.
___
### headsup.local
How to use the local alerts

```ruby
from headsup.local import headsup
headsup()
```
or
```ruby
from headsup.local import headsup
headsup(loop=True)
```
### headsup..remote 
How to use the remote alerts

```ruby
from headsup.remote import watch, notify
watch_code = watch()
# ... your code runs here
notify(watch_code, "Success!!")
```
alternatively, 
```ruby
watch(QR=True, QRInline=True)
```
