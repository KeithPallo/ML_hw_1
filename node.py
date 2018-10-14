class Node:
  def __init__(self, label = False, examples = []):
    self.label = None
    self.children = {}
	# you may want to add additional fields here...
    self.examples = examples
    self.type = "Leaf" # Leaf or Split

    # If examples are empty, then this is a leaf node and we use label
    # to test
  def add_subtree(self,subtree,attribute):
      self.children[attribute] = subtree
      self.type = "Split"

  def split_type(self):
      return self.label
