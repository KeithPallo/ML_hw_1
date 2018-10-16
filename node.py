class Node:
  def __init__(self, label = False):
    self.label = label # Class type or attribute
    self.children = {}
    self.parent_split = None
    self.type = "Leaf"
    self.is_pruned = False
    self.pruned_mode = None
	# you may want to add additional fields here...
    # self.examples = examples
    #self.type = "Leaf" # Leaf or Split

    # If examples are empty, then this is a leaf node and we use label
    # to test
  def add_subtree(self,subtree,attribute):
    self.children[attribute] = subtree
    self.type = "Value"

  def split_type(self):
    return self.label

  def evaluate(self,example):
    if self.is_leaf():
      return self.label

    else:
      split = example[self.label]
      sub = self.children[split]
      return sub.evaluate(example)


  def add_parent_split(self,parent_split):
    self.parent_split = parent_split

  def cross_validate(self,examples):
    if self.is_leaf():

    for i in examples:

  def is_leaf(self):
    if len(self.children) == 0 or self.type == "Leaf":
      return True
    else:
      return False
