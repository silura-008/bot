# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []





# from rasa_sdk import Action
# from rasa_sdk.events import SlotSet
# from typing import Text

# class ActionSeTone(Action):
#     def name(self) -> Text:
#         return "action_set_tone"

#     def run(self, dispatcher, tracker, domain):
#         intent = tracker.latest_message['intent']['name']
        
#         if intent == "greet_friendly":
#             return [SlotSet("tone", "friendly")]
#         elif intent == "greet_formal":
#             return [SlotSet("tone", "formal")]


from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

class ActionSeTone(Action):
   def name(self) -> Text:
      return "action_set_tone"

   def run(self,
           dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        intent = tracker.latest_message['intent']['name']
        
        if intent == "greet_friendly":
            return [SlotSet("tone", "friendly")]
        elif intent == "greet_formal":
            return [SlotSet("tone", "formal")]






# from typing import Text, Dict, Any, List
# from rasa_sdk import Action
# from rasa_sdk.events import SlotSet

# class ActionCheckRestaurants(Action):
#    def name(self) -> Text:
#       return "action_check_restaurants"

#    def run(self,
#            dispatcher: CollectingDispatcher,
#            tracker: Tracker,
#            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#       cuisine = tracker.get_slot('cuisine')
#       q = "select * from restaurants where cuisine='{0}' limit 1".format(cuisine)
#       result = db.query(q)

#       return [SlotSet("matches", result if result is not None else [])]
