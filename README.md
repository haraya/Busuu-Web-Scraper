Busuu-Web-Scraper 📚👨🏻‍💻 <br>
This repository will help you to study any languages from Busuu platform 

PROBLEM:
Busuu has content from categories split into difference levels like A1, A2, B1, B2..
When I studied the clothes topic I saw that content in level A1 and A2, and I was difficult to me to study all chapters in order from level A1 to level B2.

For that reason I create this WebScraper bot, that it help me to get all lessons from different English levels and finally create a JSON format like this:<br>
A1: {<br>
    Chapter 1: Greeting{<br>
        Description 1,<br>
        Description 2,<br>
        ....<br>
    }<br>
     Chapter 2: Hobbies{<br>
        Description 1,<br>
        Description 2,<br>
        ....<br>
    }<br>
}<br>
A2: {<br>
    Chapter 1: Personality{<br>
        Description 1,<br>
        Description 2,<br>
        ....<br>
    }<br>
}<br>
...

The bot needs the url manual from different level that you need to get the data.

In this moment the bot only works with English languages, I am working if bot works with different languages from Busuu platform

RUN:
Create virtual environmment:
python -m venv venv

Install selenium and webdriver:
pip install selenium webdriver-manager