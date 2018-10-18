class Node:
  def __init__(self, label = False, train_mode = None):
    self.label = label # Class type or attribute to split on
    self.children = {}
    self.type = "Leaf"
    self.train_mode = train_mode

    self.prune_test = False # Only used for additional prune method Prune A
    self.prune_hold = None  # Only used for additional prune method Prune A


# Core

  def add_subtree(self,subtree,attribute):
    """
    Adds children to current node.
    """
    self.children[attribute] = subtree
    self.type = "Split"

  def evaluate(self,example):
    """
    Performs evaluation. If node is a leaf, returns label as classification.
    If not, attempts to send down tree. If cannot send down because
    split attribute not present, classified as training mode.
    Itype: Dictionary
    Rtype: String (Classification)
    """
    if self.is_leaf():
      return self.label

    else:

      try:
        split = example[self.label]
        sub = self.children[split]
        return sub.evaluate(example)
      except:
        return self.train_mode

  def is_leaf(self):
    """
    Checks if current node is of type leaf. Redundantly checks
    type for safe pruning.
    """
    if len(self.children) == 0 or self.type == "Leaf" or self.type == "Prune":
      return True
    else:
      return False

  def all_children_leaf(self):
    """
    Checks is all children are leaves. Returns Boolean.
    """
    if self.is_leaf():
      return False
    else:
      for i in self.children.values():
        if i.is_leaf() != True:
          return False

      return True

  def some_leaf(self):
    """
    Checks is some children are leaves. Returns Boolean.
    """
    if self.is_leaf():
      return False
    else:
      for i in self.children.values():
        if i.is_leaf():
          True

      return False

  def self_prune(self,bool):
      """
      Permanantly prunes self. All childen are released from memory.
      To prune, input bool must be of type True.
      """
      if bool == True:
          self.children = {}
          self.type  = "Leaf"
          self.label = self.train_mode
          self.prune_test = False
      else:
          return

# Prune core with get_method_2

  def node_leaves(self):
      """
      Additional Prune method A helper. Returns all leafs.
      """
      my_leaves = []

      for claim, i in self.children.items():
          if i.is_leaf() == True:
              my_leaves.append(claim)

      return my_leaves

  def prune_this_leaf(self,name):
      """
      Additional Prune method A helper. Performs temporary prune.
      """
      self.prune_hold = (name,self.children.pop(name))

  def finish_leaf_prune(self):
      """
      Additional Prune method A helper. Performs permanent prune.
      """
      self.prune_hold = None

  def unprune_leaf(self):
      """
      Additional Prune method A helper. Mutates temporary prune back
      to original state.
      """
      name = self.prune_hold[0]
      sub = self.prune_hold[1]

      self.children[name] = sub


  def prune_evaluate(self,example):
    """
    Additional Prune method B helper.
    """
    if self.all_children_leaf() == True:
      return self.train_mode

    else:
      try:
        split = example[self.label]
        sub = self.children[split]
        return sub.evaluate(example)
      except:
        return self.train_mode

    #split = example[self.label]
    #sub = self.children[split]
    #return sub.prune_evaluate(example)



  #def add_parent_split(self,parent_split):
    #self.parent_split = parent_split

  #def split_type(self):
    #return self.label
