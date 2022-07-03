# REDDIT QUESTION TO VIDEO SCRIPT

## __Requirements__
### You must have a reddit app setup on your account. Follow [this tutorial by sentdex](https://youtu.be/NRgfgtzIhBQ) for the same

### ***Run the following commands:-***
`$ sudo apt-get install ffmpeg`
<br></br>

## __Installation__
### ***Run the following commands:-***
`$ git clone https://github.com/Ishan-Choudhary/Reddit_question_to_video.git`

`$ cd Reddit_question_to_video/`

`$ pip3 install -r requirements.txt`

`$ touch config.ini`

### Then open config.ini in your preffered editor and use this format:-
```
[questionBot]
client_id = <Replace with your client id> 
client_secret = <Replace with your client secret> 
password = <Replace with your reddit password> 
user_agent = <Replace with the name of the reddit app you created>
username =  <Replace with your reddit username> 
```

<br></br>

## __Usage__
`$ python3 main.py`
