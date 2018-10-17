class Node:
  def __init__(self, label = False, test_mode = None):
    self.label = label # Class type or attribute to split on
    self.children = {}
    self.parent_split = None
    self.type = "Leaf"
    self.test_mode = test_mode
    self.prune_test = False
    self.prune_hold = None

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

  def some_leaf(self):
    if self.is_leaf():
      return False
    else:
      for i in self.children.values():
        if i.is_leaf():
          True

      return False


  def self_prune(self,bool):
      if bool == True:
          self.children = {}
          self.type  = "Leaf"
          self.label = self.test_mode
          self.prune_test = False
      else:
          return


  def node_leaves(self):
      my_leaves = []

      for claim, i in self.children.items():
          if i.is_leaf() == True:
              my_leaves.append((claim))

      return my_leaves

  def prune_this_leaf(self,name):
      self.prune_hold = (name,self.children.pop(name))

  def finish_leaf_prune(self):
      self.prune_hold = None

  def unprune_leaf(self):
      name = self.prune_hold[0]
      sub = self.prune_hold[1]

      self.children[name] = sub
