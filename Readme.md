# Hololand

## Introduction
A Line bot based on a finite state machine.

Guide you to the wonder land of Hololive!!!

[github repo](https://github.com/oscar9335/hololand)

![](https://i.imgur.com/iVWfoYe.png)


## Add Friend

![](https://i.imgur.com/zSvIV2C.png)


## Add by ID

@643yufyj

## FSM

![](https://i.imgur.com/mEpGsr3.png)


## Usage
The initial state is set to `user`.
* `user`
	* Input: **"any string except fsm and home"**
		* Reply:  Enter home or press the button for help
		
	* Input: **"fsm"**
		* Reply: fsm.png
		
	* Input: **"home"**
		* Reply: enter:[what is this] for information or [menu] for next step
		
![](https://i.imgur.com/yewctHQ.png)		
![](https://i.imgur.com/MeBIsed.jpg)

* `home`
	* Input: **"what is this"**
		* Reply:
		
		![](https://i.imgur.com/DEP8L2a.png)
		
	* Press button: **"home"**
		* Reply: enter:[what is this] for information or [menu] for next step
		
	* Press button: **"menu"**
		* Reply: 
		
		![](https://i.imgur.com/UCIEWRB.png)
		
	* Press button: **"Peko Peko"**
		* Reply:  a video
		
		![](https://i.imgur.com/nCQ5yGa.png)

* `menu`
	* Press button: **"Search with character"**
		* Reply: Enter a character
		* After enter if found : 
		
		![](https://i.imgur.com/snQRCKw.png)
		* After enter if not found : Reply : Not Found
		
	* Press button: **"Recommand"**
		* Reply: "recommand you a Hololive Vtuber"
		* Example : 
		
		![](https://i.imgur.com/jAsMl7S.png)
		
	* Press button: **"View all TALENT"**
		* Lead you to the Website of Hololive
		

* `others in the flex message`		
    
    * Press button: **"Introudce"**
		* Lead you to this Vtuber's introduction
		
	* Press button: **"Youtube"**
		* Lead you to this Vtuber's Youtube Channel
		
	![](https://i.imgur.com/dlFzA3k.png)
     

