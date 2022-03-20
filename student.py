
class Student(object):
  __slots__ = ('name','age')
  def __init__(self,name,score):
    self.name = name
    self.score = score
    pass
  Month = Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))
  pass