# Little-Ace

## Thesis 
Creating a Poker platform, don't know where I'm heading with this but I wanted to make a project to keep me inspired. I love card games and as it turns out Poker has the most "alpha" in relation to quant firms. So I thought this could be a fun side project to get better at Poker and coding. In a world of AI you get lost and don't get to implement many things ground up anymore, so I wanted to challenge myself. This is meant as a cute project I can build and use to get better at Poker, who knows one day maybe I will be a poker pro and all these big tech rejections will be past me. In this day and age I feel so untrue to myself trying to impress companies with these insane projects that still doesn't impress them. Although this project is a little contradictory since it appeals to the companies that pay the highest (ironic). I'm buidling it because I love playing cards and if poker has the most edge in a high paying space lets see how good I can get at it. I want this application to really reflect who I am and I hope that shine through it. I want it to be a cute, interactive place to play poker and deeply understand the game and your decisions throughout the game. We'll see how far I can go with this project 

Thank you, 
Fiona Magee

## Implmentation
Starting by developing simple deck and card classes to track those metrics 

### Deck
Created a deck class/object to create the deck of cards used throughout the game 
- Starts with constuctor creating an empty list deck then in the constuctor calling create_deck which creates a deck full of the card objects 
- You will notice I say clovers instead of clubs, thats an ongoing joke with my friends. I'm for some reason not good (reason why I never wanted to be a doctor) with words but the club looks like a clover to me, a 3-leaf clover. 

### Card
Created a class/object card that basically just stores the number/class and the suit 
- __str__ outputs the string text of cards 