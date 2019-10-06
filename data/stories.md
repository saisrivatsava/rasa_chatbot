## happy path
* greet
  - utter_greet
* ask_state_of_bot
  - utter_ask_state_of_bot
* ask_what_are_you_doing
  - utter_ask_what_are_you_doing
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## who are you
* ask_isbot
  - utter_ask_isbot

## New Story
* greet
    - utter_greet
* ask_what_are_you_doing
    - utter_ask_what_are_you_doing

## time related
* ask_time
  - utter_ask_time

## good complements
* good_complement
  - utter_good_complement
* bad_complement
  - utter_bad_complement

## abuse
* abuse
  - utter_abuse

## New Story

* greet
    - utter_greet
* ask_time
    - utter_ask_time
* good_complement
    - utter_good_complement
* bad_complement
    - utter_bad_complement
* abuse
    - utter_abuse
* ask_isbot
    - utter_ask_isbot
* ask_isbot
    - utter_ask_isbot
* ask_what_are_you_doing
    - utter_ask_what_are_you_doing

## gold price
* ask_gold_price
    - action_ask_gold_price

## New Story 2

* greet
    - utter_greet
* mood_great
    - utter_happy
* ask_isbot
    - utter_ask_isbot
* ask_gold_price
    - action_ask_gold_price
* ask_gold_price
    - action_ask_gold_price

## Metal price
* ask_metal_price
    - action_ask_metal_price
* ask_metal_price
    - action_ask_metal_price

## New Story

* greet
    - utter_greet
* ask_state_of_bot
    - utter_ask_state_of_bot
* ask_metal_price{"metal_name":"silver","location":"hyderabad"}
    - slot{"location":"hyderabad"}
    - slot{"metal_name":"silver"}
    - action_ask_metal_price
* ask_metal_price{"metal_name":"silver","location":"chennai"}
    - action_ask_metal_price

## New Story

* greet
    - utter_greet
* ask_metal_price{"metal_name":"gold","location":"chennai"}
    - slot{"location":"chennai"}
    - slot{"metal_name":"gold"}
    - action_ask_metal_price
* ask_metal_price{"metal_name":"silver","location":"hyderabad"}
    - slot{"location":"hyderabad"}
    - slot{"metal_name":"silver"}
    - action_ask_metal_price
* ask_metal_price{"metal_name":"silver","location":"hyderabad"}
    - action_ask_metal_price
* ask_metal_price{"metal_name":"silver","location":"hyderabad"}
    - slot{"location":"hyderabad"}
    - action_ask_metal_price
