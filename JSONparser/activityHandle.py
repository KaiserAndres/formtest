import datetime

class File:
  def __init__(self, metadata= None, header = None):
    self.metadata = metadata
    self.header = header
    self.data = []

  def linkHeader(self, header):
    self.header = header

  def linkMetaData(self, metadata):
    self.metadata = metadata

  def linkData(self, element):
    self.data.append(element)

  def unlinkData(self, element):
    self.data.remove(element)

  def giveDict(self):
    dictionary = {}
    dictionary["metadata"] = self.metadata.giveDict()
    dictionary["header"] = self.header.giveDict()
    dictionary["data"] = []
    for element in self.data:
      dictionary["data"].append(element.giveDict())
    return dictionary

class MetaData:
  def __init__(self, userID = None, language = None, creationDate = None,
               lastChangeDate = None, fileID = None):
    self.userID         = userID
    self.language       = language
    self.creationDate   = creationDate
    self.lastChangeDate = lastChangeDate
    self.fileID         = fileID

  def setUserID(self, newID):
    self.userID = newID

  def setLanguage(self, newLanguage):
    self.language = newLanguage

  def setCreationDate(self, creationDate):
    self.creationDate = creationDate

  def setLastChange(self):
    self.lastChangeDate = datetime.datetime.now()

  def setFileID(self, newFileID):
    self.fileID = newFileID

  def updateLastChangeDate(self):
    self.setLastChange()

  def giveDict(self):
    dictionary = {}
    dictionary["userID"]         = self.userID
    dictionary["language"]       = self.language
    dictionary["creationDate"]   = self.creationDate
    dictionary["lastChangeDate"] = self.lastChangeDate
    dictionary["fileID"]         = self.fileID
    return dictionary

class Header:
  def __init__(self, organisation = None, hasHeader = None,
               hasStudentName = None, hasTeacherName = None,
               hasFillableDate = None):
    self.organisation     = organisation
    self.hasHeader        = hasHeader
    self.hasStudentName   = hasStudentName
    self.hasTeacherName   = hasTeacherName
    self.hasFillableDate  = hasFillableDate

  def setOrganisation(self, organisation):
    self.organisation = organisation

  def setHasHeader(self, hasHeader):
    self.hasHeader = hasHeader

  def setHasStudentName(self, hasStudentName):
    self.hasStudentName = hasStudentName

  def setHasTeacherName(self, hasTeacherName):
    self.hasTeacherName = hasTeacherName

  def setHasFillableDate(self, hasFillableDate):
    self.hasFillableDate = hasFillableDate

  def giveDict(self):
    dictionary = {}
    dictionary["organisation"]    = self.organisation
    dictionary["hasHeader"]       = self.hasHeader
    dictionary["hasStudentName"]  = self.hasStudentName
    dictionary["hasTeacherName"]  = self.hasTeacherName
    dictionary["hasFillableDate"] = self.hasFillableDate
    return dictionary

class Data:
  pass

class TextBlock(Data):
  def __init__(self, baseText):
    self.textBody      = baseText
    self.subActivities = []

  def setText(self, text):
    self.textBody = text

  def linkActivity(self, activity):
    self.subActivities.append(activity)

  def unlinkSubactivity(self, activity):
    self.subActivities.remove(activity)

  def giveDict(self):
    dictionary = {}
    dictionary["type"]          = "textBlock"
    dictionary["textBody"]      = self.textBody
    dictionary["subactivities"] = []
    for element in self.subActivities:
      dictionary["subactivities"].append(element.giveDict)
    return dictionary

class Activity(Data):
  pass

class TrueOrFalse(Activity):
  def __init__(self, text = None):
    self.text    = text
    self.answers = []

  def linkAnswer(self, answer):
    self.answers.append(answer)

  def unlinkAnswer(self, answer):
    self.answers.remove(answer)

  def giveDict(self):
    dictionary = {}
    dictionary["type"] = "t/f"
    dictionary["text"] = self.text
    dictionary["answer"] = []
    for element in self.answers:
      dictionary["answer"].append(element.giveDict())
    return dictionary

class TFanswer:
  def __init__(self, text = None, correct = False):
    self.text    = text
    self.correct = correct

  def setText(self, text):
    self.text = text

  def setCorrect(self, correct):
    self.correct = correct

  def giveDict(self):
    dictionary = {}
    dictionary["text"]    = self.text
    dictionary["correct"] = self.correct
    return dictionary

class AnswerQuestion(Activity):
  def __init__(self, questionText = None, answerLines = None):
    self.questionText = questionText
    self.answerLines  = answerLines

  def setQuestionText(self, text):
    self.questionText = text

  def setNumberOfLines(self, numberLines):
    self.answerLines = numberLines

  def giveDict(self):
    dictionary = {}
    dictionary["type"]         = "answerQuestion"
    dictionary["questionText"] = self.questionText
    dictionary["answerLines"]  = self.answerLines
    return dictionary

class OrderWords(Activity):
  def __init__(self, autoScramble = None):
    self.sentence     = []
    self.autoScramble = autoScramble

  def linkWord(self, word):
    self.sentence.append(word)

  def unlinkWord(self, word):
    self.sentence.remove(word)

  def setAutoScramble(self, scramble):
    self.autoScramble = scramble

  def giveDict(self):
    dictionary = {}
    dictionary["type"]     = "orderWords"
    dictionary["sentence"] = []
    for element in self.sentence:
      dictionary["sentence"].append(element.giveDict())
    dictionary["autoScramble"] = self.autoScramble

class OrderingWord:
  def __init__(self, text = None):
    self.text = text

  def setText(self, text):
    self.text = text

  def giveDict(self):
    dictionary = {}
    dictionary["text"] = self.text
    return dictionary






