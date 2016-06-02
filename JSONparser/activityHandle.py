import datetime

class File:
  def __init__(self, metadata= None, header = None):
    self.metadata = metadata
    self.header = header
    self.data = []

  def linkData(self, element):
    self.data.append(element)

  def unlinkData(self, element):
    self.data.remove(element)

class MetaData:
  def __init__(self, userID, language, creationDate, lastChangeDate, fileID):
    self.userID = userID
    self.language = language
    self.creationDate = creationDate
    self.lastChangeDate = lastChangeDate
    self.fileID = fileID

  def setUserID(self, newID):
    self.userID = newID

  def setLanguage(self, newLanguage):
    self.language = newLanguage

  def setCreationDate(self):
    self.creationDate = datetime.datetime.now()

  def setLastChange(self):
    self.lastChangeDate = datetime.datetime.now()

  def setFileID(self, newFileID):
    self.fileID = newFileID

class Data:
  pass

class TextBlock(Data):
  def __init__(self, baseText):
    self.textBody = baseText
    self.subActivities = []

  def setText(self, text):
    self.textBody = text

  def linkActivity(self, activity):
    self.subActivities.append(activity)

class Activity(Data):
  pass