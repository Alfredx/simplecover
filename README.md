# simplecover
An application to create your unique cover letter in simple clicks! utilizing AI!

# Requirements

MacOS or Linux

Python >= 3.11

But in theory on lower version of Python and Windows are also supported, feel free to try :)

# Installation

```
pip install -r requirements.txt
```

# QuickStart

Write your own openai key in .env as followed

```
LLM_API_KEY=<your own key>
```

then run

```
./start.sh
```

Paste your CV and JD into the text area respectively and click `Generate` ! 

Don't forget to modify the cover letter AI gives you. After all, there is still a great chance to spot errors here and there.

# More about config

You can also put `LLM_API_BASE` in .env file. For me, I use [theb.ai](https://theb.ai). It allows me experimenting with multiple LLM models and find out what's the best!

If `LLM_API_BASE` is not set, it's openai by default.

# What's next

This is a small side project I created for myself to find a job, so I might continue to improve it as long as I find features that I can use.

But feel free to try it yourself! If you think there are anything useful, contact me via email. I will try to implement them when I have time:

alfredcameoutwithnonames@gmail.com