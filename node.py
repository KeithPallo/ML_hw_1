class Node:
  def __init__(self, label = False, test_mode = None):
    self.label = label # Class type or attribute to split on
    self.children = {}
    self.parent_split = None
    self.type = "Leaf"
    self.test_mode = test_mode

    # you may want to add additional fields here...
    # self.examples = examples
    #self.type = "Leaf" # Leaf or Split

    # If examples are empty, then this is a leaf node and we use label
    # to test

  def add_subtree(self,subtree,attribute):
    self.children[attribute] = subtree
    self.type = "Split"

  def split_type(self):
    return self.label

  def evaluate(self,example):
    if self.is_leaf():
      return self.label

    else:

      try:
        split = example[self.label]
        sub = self.children[split]
        return sub.evaluate(example)
      except:
        return self.test_mode



  def add_parent_split(self,parent_split):
    self.parent_split = parent_split


  def is_leaf(self):
    if len(self.children) == 0 or self.type == "Leaf" or self.type == "Prune":
      return True
    else:
      return False

  def prune_evaluate(self,example):
    if self.all_children_leaf() == True:
      #print(self.test_mode)
      return self.test_mode

    else:
      try:
        split = example[self.label]
        sub = self.children[split]
        return sub.evaluate(example)
      except:
        return self.test_mode

      #split = example[self.label]
      #sub = self.children[split]
      #return sub.prune_evaluate(example)

  def all_children_leaf(self):
    if self.is_leaf():
      return False
    else:
      for i in self.children.values():
        if i.is_leaf():
          pass
        else:
          return False

      return True

  def self_prune(self,bool):
      if bool == True:
          self.children = {}
          self.type  = "Leaf"
          self.label = self.test_mode
      else:
          return
