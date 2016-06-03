import datetime

class File:
  def __init__(self, metadata= None, header = None):
    self.metadata = metadata
    self.header = header
    self.data = []

  def linkHeader(self, header):
    self.header = header

  def linkMetadata(self, metadata):
    self.metadata = metadata

  def linkData(self, element):
    self.data.append(element)

  def unlinkData(self, element):
    self.data.remove(element)

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

  def setCreationDate(self):
    self.creationDate = datetime.datetime.now()

  def setLastChange(self):
    self.lastChangeDate = datetime.datetime.now()

  def setFileID(self, newFileID):
    self.fileID = newFileID

  def updateLastChangeDate(self):
    self.setLastChange()

class header:
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

class Activity(Data):
  pass

class TrueOrFalse(Activity):
  def __init__(self, text = None):
    self.text    = text
    self.answers = []









