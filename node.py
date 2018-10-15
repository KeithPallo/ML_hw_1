class Node:
  def __init__(self, label = False):
    self.label = label # Class type or attribute
    self.children = {}
    self.parent_split = None
	# you may want to add additional fields here...
    # self.examples = examples
    #self.type = "Leaf" # Leaf or Split

    # If examples are empty, then this is a leaf node and we use label
    # to test
  def add_subtree(self,subtree,attribute):
    self.children[attribute] = subtree

  def split_type(self):
    return self.label

  def evaluate(self,example):
    if len(self.children) == 0:
      return self.label

    else:
      split = example[self.label]
      sub = self.children[split]
      return sub.evaluate(example)


  def add_parent_split(self,parent_split):
    self.parent_split = parent_split
