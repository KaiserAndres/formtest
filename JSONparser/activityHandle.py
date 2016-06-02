import datetime

class file:
  def __init__(self, metadata, header):
    self.metadata = metadata
    self.header = header
    self.data = []

  def setData(self, element):
    self.data.append(element)

class metaData:
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

class data:
  pass

class textBlock(data):
  def __init__(self, baseText):
    self.textBody = baseText
    self.subActivities = []

  def setText(self, text):
    self.textBody = text

  def linkActivity(self, activity):
    self.subActivities.append(activity)

class activity(data):
  pass