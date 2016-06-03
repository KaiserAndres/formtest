import json
import sys
import activityHandle

'''
This script does a parsing of the JSON file containing the file to be rendered
taking the file name as a commandline argument, the JSON format is detailed in
the model.mdj file under the "JSON Activity" diagram.

This file generates an output of the same name as the original file name with
the "*.tex" extention marking that it was processed and is ready to be rendered
'''

'''
@param root: root object containing the data structure for the activity group

@returns: JSON string containing the data from the object
'''
def encode(root):
  dictObject = root.giveDict()
  return json.dumps(dictObject)

def makeTrueOrFalse(block):
  activity = activityHandle.TrueOrFalse(block["text"])
  for answer in block["answer"]:
    activity.linkAnswer(
      activityHandle.TFanswer(
        answer["text"], 
        answer["correct"]
      )
    )
  return activity

def makeAnswerQuestion(block):
  activity = activityHandle.AnswerQuestion(
    block["questionText"],
    block["answerLines"]
    )
  return activity

def makeOrderWords(block):

  activity = activityHandle.OrderWords(
      block["autoScramble"]
    )
  for word in block["words"]:
    activity.linkWord(
      OrderWord(word["text"])
    )
  return activity

def makeTextBlock(block):
  activity = activityHandle.TextBlock(block["textBody"])
  for subactivity in block["subactivities"]:
    loader[subactivity["type"]](subactivity)
  return activity

loader = {
  "t/f" : makeTrueOrFalse,
  "answerQuestion" : makeAnswerQuestion,
  "orderWords" : makeOrderWords,
  "textBlock" : makeTextBlock
}

'''
From a JSON string generates an object tree containing the data
'''

def decode(JSON):
  root = activityHandle.File()
  root.linkHeader(
    activityHandle.Header(
      JSON ["header"] ["organisation"],
      JSON ["header"] ["hasHeader"],
      JSON ["header"] ["hasStudentName"],
      JSON ["header"] ["hasTeacherName"],
      JSON ["header"] ["hasFillableDate"]
      )
    )
  root.linkMetaData(
    activityHandle.MetaData(
      JSON ["metadata"] ["userID"],
      JSON ["metadata"] ["language"],
      JSON ["metadata"] ["creationDate"],
      JSON ["metadata"] ["lastChangeDate"],
      JSON ["metadata"] ["fileID"]
      )
    )

  for element in JSON["data"]:
    root.linkData(loader[element["type"]](element))
  return root

def main():
  print("this shouldn't be ran")

if __name__ == "__main__":
  main()