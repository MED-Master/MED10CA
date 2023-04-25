# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import threading
import time

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pandas as pd

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
#DF[Rows:  questions, Columns: context[1-5], Reflective Questions[6], EXAMPLE[7]
#print(df.at[49, 7])
df = pd.read_csv("manuscript.csv", header=None)
df.drop(0, axis=1, inplace=True)
df.drop(0, axis=0, inplace=True)




answers = []

answer_svær = "Kunne slet ikke - Meget besvær -En del besvær - Lidt besvær - Intet besvær"

answer_enig = "Helt enig - Delvist enig - Hverken enig eller uenig - Delvist uenig - Helt uenig"

questions = ["Har De haft besvær med at tilberede et måltid?",
             "Har De haft besvær med at spise?",
             "Har De haft besvær med at tage tøj på?",
             "Har De haft besvær med at tage bad?",
             "Har De haft besvær med at gå på toilettet?",
             "Har De haft besvær med at se fjernsyn tydeligt nok?",
             "Har De haft besvær med at række ud efter ting på grund af dårligt syn?",
             "Har De haft besvær med at se ting til den ene side?",
             "Har De haft besvær med at tale?",
             "Har De haft besvær med at tale klart og tydeligt i telefon?",
             "Har andre mennesker haft besvær med at forstå, hvad De sagde?",
             "Har De haft besvær med at finde de ord, De gerne ville sige?",
             "Har De været nødt til at gentage Dem selv for at andre kunne forstå, hvad De sagde?",
             "Har De haft besvær med at gå?",
             "Har De haft besvær med at holde balancen, når De lænede Dem frem eller rakte ud efter noget?",
             "Har De haft besvær med at gå op ad trapper?",
             "Har De haft besvær, fordi De var nødt til at holde pause, mens De gik eller kørte i kørestol?",
             "Har De haft besvær med at stå oprejst?",
             "Har De haft besvær med at komme op fra en stol?",
             "Har De haft besvær med at klare de daglige gøremål i hjemmet?",
             "Har De haft besvær med at gøre det færdigt, som De var begyndt på?",
             "Har De haft besvær med at udføre De opgaver, De plejer?",
             "Har De haft besvær med at skrive i hånden eller på maskine?",
             "Har De haft besvær med at tage strømper på?",
             "Har De haft besvær med at knappe knapper?",
             "Har De haft besvær med at åbne en mælkekarton?",
             "Har De haft besvær med at åbne glas med skruelåg?",
             "Jeg har haft svært ved at koncentrere mig.",
             "Jeg har haft svært ved at huske ting.",
             "Jeg har været nødt til at skrive ting ned for at huske dem.",
             "Jeg har været irritabel.",
             "Jeg har været utålmodig over for andre.",
             "Min personlighed har ændret sig.",
             "Jeg har følt mig modløs med hensyn til fremtiden",
             "Jeg har været uinteresseret i andre mennesker eller aktiviteter.",
             "Jeg har deltaget mindre i fornøjelser med min familie",
             "Jeg har følt, at jeg var en byrde for min familie.",
             "Min fysiske tilstand har påvirket mit familieliv.",
             "Jeg er gået mindre i byen end jeg gerne ville.",
             "Jeg har beskæftiget mig med mine fritidsinteresser i kortere perioder, end jeg gerne ville.",
             "Jeg har været sammen med færre af mine venner end jeg gerne ville.",
             "Jeg har dyrket mindre sex end jeg gerne ville",
             "Min fysiske tilstand har påvirket mit sociale liv",
             "Jeg har følt mig isoleret fra andre mennesker.",
             "Min selvtillid har været lille",
             "Jeg har været uinteresseret i mad",
             "Jeg har følt mig træt det meste af tiden.",
             "Jeg har følt mig træt det meste af tiden.",
             "Jeg har været for træt til at gøre det, jeg gerne ville."]

context = ['a', 'b', 'c', 'd', 'e'] #TODO delete when df works

reflective_questions = ['aR', 'bR', 'cR', 'dR', 'eR'] #TODO delete when df works

examples = ['aE', 'bE', 'cE', 'dE', 'eE'] #TODO delete when df works

SSQOLAnswerOptionsSvær = [
    "Kunne slet ikke",
    "Meget besvær",
    "En del besvær",
    "Lidt besvær",
    "Intet besvær"
]

SSQOLAnswerOptionsEnig = [
    "Helt enig",
    "Delvist enig",
    "Hverken enig eller uenig",
    "Delvist uenig",
    "Helt uenig"
]


class ValidationOfAnswer(Action):
    currentQuestionNumber = 0

    def name(self) -> Text:
        return "ValidationOfAnswer"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        q_answer = next(tracker.get_latest_entity_values('Q_answer'), None)
        q_number = next(tracker.get_latest_entity_values('question_num'), None)
        ValidationOfAnswer.currentQuestionNumber = int(q_number)  # what question the user is answering currently
        q_number = int(q_number) - 1
        answers.append(q_answer)
        print("q_answer: " + q_answer)

        if q_number < 26:  # svær
            dispatcher.utter_message(text="Du har svaret at du har: " + q_answer + ", hvilket betyder " + context[q_number] + '.')
            return []
        #enig
        dispatcher.utter_message(text="Du har svaret at du er: " + q_answer + ", hvilket betyder " + context[q_number] + '.')

        if q_number > 48:
            dispatcher.utter_message(text="Du har nu besvaret alle spørgsmål. Du kan nu se dine svar ved at skrive på 'Se alle svar'")


        print("ValidationOfAnswer: " + str(len(answers)))
        print(answers)

        return []

class AskForNewAnswer(Action):
    questionNumberToBeChanged = 0

    def name(self) -> Text:
        return "AskForNewAnswer"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if (len(answers) == 0):
            dispatcher.utter_message(text="Du har ikke svaret på nogle spørgsmål endnu.")
            return []

        question_number = next(tracker.get_latest_entity_values('get_number'), None)
        question_number_index = int(question_number) - 1
        dispatcher.utter_message(text="Do you mean the question: " + questions[question_number_index])
        dispatcher.utter_message(text="Your current answer is: " + answers[question_number_index])
        AskForNewAnswer.questionNumberToBeChanged = question_number_index
        # print("questionNumberToBeChanged " + str(AskForNewAnswer.questionNumberToBeChanged))

        if int(question_number) > 26:
            dispatcher.utter_message(
                text="Hvad vil du gerne ændre dit svar til? Skriv venligst et svar imellem: " + answer_enig)
        else:
            dispatcher.utter_message(
                text="Hvad vil du gerne ændre dit svar til? Skriv venligst et svar imellem: " + answer_svær)
        # print("AskForNewAnswer: " + question_number)
        return []


class ChangeAnswer(Action):

    def name(self) -> Text:
        return "ChangeAnswer"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if (len(answers) == 0):
            dispatcher.utter_message(text="Du har ikke svaret på nogle spørgsmål endnu.")
            return []

        new_answer = next(tracker.get_latest_entity_values('get_number'), None)
        index = int(new_answer) - 1
        saved_answer = ''

        print(answers)
        if AskForNewAnswer.questionNumberToBeChanged > 26:  # enig
            answers[AskForNewAnswer.questionNumberToBeChanged] = SSQOLAnswerOptionsEnig[index]
            saved_answer = SSQOLAnswerOptionsEnig[index]

        else:  # svær
            answers[AskForNewAnswer.questionNumberToBeChanged] = SSQOLAnswerOptionsSvær[index]
            saved_answer = SSQOLAnswerOptionsSvær[index]

        dispatcher.utter_message(text="Dit svar er ændret til: " + saved_answer)

        # print("new_answer: " + new_answer)
        # print("question_number: " + question_number)
        # print("questionNumberToBeChanged: " + int(questionNumberToBeChanged))
        print("Updated answers: " + str(answers))

        return []


class GiveHelp(Action):

    def name(self) -> Text:
        return "GiveHelp"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        help_type = 1  # reflective question
        current = ValidationOfAnswer.currentQuestionNumber
        print(current)

        if help_type is 1:  # reflective question
            dispatcher.utter_message(text="Her er noget hjælp " + reflective_questions[current])
        else:  # example
            dispatcher.utter_message(text="Her er noget hjælp " + examples[current])

        return []

class AnswerOverview(Action):

    def name(self) -> Text:
         return "AnswerOverview"

    def concat_lists(self, list1, list2):
        k = ""
        for index in range(len(list2)):
            s = "".join("\n" + str(index + 1) + " - " + list1[index] + "\n" + "Dit svar: " + list2[index] + "." + "\n")
            k += s
        return k

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if (len(answers) == 0):
            dispatcher.utter_message(text="Du har ikke svaret på nogle spørgsmål endnu.")
            return []

        overview = self.concat_lists(questions, answers)
        dispatcher.utter_message(text="Her er alle dine svar: " + overview)

        return []