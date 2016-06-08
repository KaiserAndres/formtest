import datetime

#------------------------------------------------------------------------------
# Root class
#------------------------------------------------------------------------------

class File:
  '''
-
This is the 'root' class, which defines the main point of access for the entire
datastructure.

This class is responsible for holding the data of each document as well as
relative amount of metadata respective for said file and it's owner (in case it
happens to be lost from the database, although this should never happen [watch
it happen in like 5 minutes])

Atributes:

  metadata (Metadata):
    This object holds information used for processing the File, but is not
    rendered.

  header (Header):
    This object holds data used to determin the formatting for the render of
    the file.
  
  data [Data]:
    This list contains the data that is rendered.

Methods:

  linkHeader (header:Header):
    Adds the header pointer to the structure.

  linkMetaData (metadata:Metadata):
    Adds the metdata pointer to the structure.

  linkData (data:Data):
    Appends a data pointer to the structure.

  unlinkData (data:Data):
    Removes the data opinter from the structure.

  giveDict (void):
    Generates a dictionary object with the object structure. Used to generate
    the JSON file. This is quasi recursive, all objects contained within must
    also have a giveDict method. 

-
  '''

  def __init__(self, metadata = None, header = None):
    self.metadata = metadata
    self.header   = header
    self.data     = []

  def linkHeader(self, header):
    self.header   = header

  def linkMetaData(self, metadata):
    self.metadata = metadata

  def linkData(self, element):
    self.data.append(element)

  def unlinkData(self, element):
    self.data.remove(element)

  def giveDict(self):
    dictionary = {}
    dictionary["metadata"] = self.metadata.giveDict()
    dictionary[ "header" ] = self.header.giveDict()
    dictionary[  "data"  ] = []
    for element in self.data:
      dictionary["data"].append(element.giveDict())
    return dictionary

#------------------------------------------------------------------------------
# Central class group
#------------------------------------------------------------------------------

class MetaData:
  '''
-
This object holds data that is used for internal managment of the file, this
should not contin data used for the rendering aside from language, which is
also used for the editor's language and is set here to avoid repetition.

Atributes:

  userID (int):
    This represents the owning user's ID, used to ensure that the editing user
    can only be the respective owner of the file.

  creationDate (datetime):
    This tells the time when the file was first generated. Should never be
    changed with the exception of a file copy operation.
  
  lastChangeDate (datetime):
    This tells when a file was last saved to the database. Stored in server
    time.

  fileID (int):
    Unique file ID, should alwyas correspond with database ID number.

Methods:
  
  setUserID (newID:int):
    Sets the owning userID.

  setCrationDate (creationDate:datetime):
    Sets the creation date atribute. Should only be used during a File copy.

  setLastChange (void):
    Sets the last change date to the current server time.

  setFileID (newFileID:int):
    Sets the fileID atribute to a new value. Should only be used during a file
    copy operation.

  giveDict (void):
    returns a dictionary with the object data.
-
  '''

  def __init__(self, userID   = None, creationDate = None,
               lastChangeDate = None, fileID       = None):
    self.userID         = userID
    self.creationDate   = creationDate
    self.lastChangeDate = lastChangeDate
    self.fileID         = fileID

  def setUserID(self, newID):
    self.userID         = newID

  def setCreationDate(self, creationDate):
    self.creationDate   = creationDate

  def setLastChange(self):
    self.lastChangeDate = datetime.datetime.now()

  def setFileID(self, newFileID):
    self.fileID         = newFileID

  def giveDict(self):
    dictionary = {}
    dictionary[    "userID"    ] = self.userID
    dictionary[ "creationDate" ] = self.creationDate
    dictionary["lastChangeDate"] = self.lastChangeDate
    dictionary[    "fileID"    ] = self.fileID
    return dictionary

class Header:
  '''
-
This object contains all the data used for rendering that isn't directly rende-
red in the output file. This object needs to always be present in a File.

Atributes:

  language (str):
    Contains the ISO 639-1 language names (2 letters) used to render the docum-
    ent. For example "en" represents the English language, "es" represents spa-
    nish, etc. Look up the table for more detial seriously it's huge.
  
  organisation (str):
    Contains the organisation name.

  hasHeader (bool):
    This atribute determines wether the render of the document should have a 
    "header" with the company name, date, etc.

  hasStudentName (bool):
    This atribute determines whether the render should have a "slot" for the
    student to fill in their name.

  hasTeacherName (bool):
    This atribute determines whether a "signature" is applied.

  hasFillableDate (bool):
    This atribute determines whether the render should have a "slot" for the
    date to be filled in. (using xx/xx/xxxx to avoid trouble, becuase america)

Mthods:

  setLanguage (newLanguage : str):
    Sets the language atribute to the corresponding ISO 639-1 (2 leters) of the
    language to use for the rendering.

  setOrganisation (organisation : str):
    Sets the organisation atribute to the desired string.

  setHasHeader (hasHeader : bool):
    Sets the hasHeader atribute to true or flase.

  setHasStudentName (hasStudentName : bool):
    Sets the hasStudentName atribute to true or flase.

  setHasTeacherName (hasTeacherName : bool):
    Sets the hasTeacherName atribute to true or flase.

  setHasFillableDate (hasFillableDate : bool):
    Sets the hasFillableDate atribute to true or flase.

  giveDict (void):
    Generates a dictionary object with the corresponding object data.
-
  '''
  def __init__(self, language  = None, organisation   = None, hasHeader = None,
               hasStudentName  = None, hasTeacherName = None,
               hasFillableDate = None):
    self.language         = language
    self.organisation     = organisation
    self.hasHeader        = hasHeader
    self.hasStudentName   = hasStudentName
    self.hasTeacherName   = hasTeacherName
    self.hasFillableDate  = hasFillableDate

  def setLanguage(self, newLanguage):
    self.language         = newLanguage

  def setOrganisation(self, organisation):
    self.organisation     = organisation

  def setHasHeader(self, hasHeader):
    self.hasHeader        = hasHeader

  def setHasStudentName(self, hasStudentName):
    self.hasStudentName   = hasStudentName

  def setHasTeacherName(self, hasTeacherName):
    self.hasTeacherName   = hasTeacherName

  def setHasFillableDate(self, hasFillableDate):
    self.hasFillableDate  = hasFillableDate

  def giveDict(self):
    dictionary = {}
    dictionary[    "language"   ] = self.language
    dictionary[  "organisation" ] = self.organisation
    dictionary[   "hasHeader"   ] = self.hasHeader
    dictionary[ "hasStudentName"] = self.hasStudentName
    dictionary[ "hasTeacherName"] = self.hasTeacherName
    dictionary["hasFillableDate"] = self.hasFillableDate
    return dictionary

class Data:
  pass

#------------------------------------------------------------------------------
# Special block classes
#------------------------------------------------------------------------------


class TextBlock(Data):
  '''
-
This is a special data block in that it can hold multiple data blocks within 
itself.

Atributes:

  textBody (str):
    This is the main heart of the text block containing what data is rendered
    directly within the activity.

  subActivities (Data):
    This delimits the sub activities that are set under the text block, it bei-
    ng an overarching element throught them.

Methods:

  setText (text:str):
    This resets the text element to the new given string.

  linkActivity (activity:Data):
    This adds an activity to the subActivity array.

  unlinkSubactivity (activity:Data):
    This removes an activity from the subActivity array.

  giveDict (void):
    This generates a dictionary with the data stored in the object.
- 
  '''
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
    dictionary[     "type"    ] = "textBlock"
    dictionary[   "textBody"  ] = self.textBody
    dictionary["subactivities"] = []

    for element in self.subActivities:
      dictionary["subactivities"].append(element.giveDict)
    return dictionary

#------------------------------------------------------------------------------
# Activity class group
#------------------------------------------------------------------------------


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
    dictionary[ "type" ] = "t/f"
    dictionary[ "text" ] = self.text
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
    dictionary[  "text" ] = self.text
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
    dictionary[     "type"    ] = "answerQuestion"
    dictionary["questionText" ] = self.questionText
    dictionary[ "answerLines" ] = self.answerLines
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
    dictionary[  "type"  ] = "orderWords"
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
