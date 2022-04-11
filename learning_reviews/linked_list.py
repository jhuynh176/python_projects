class LinkedList:
    #
    def __init__(self, value = None):
        self.head_node = Node(value)    # initiate a head node once an instant is created

    def get_head_node(self):
        return self.head_node

    # insert a new node in front of head_node
    def insert_beginning(self, new_value):
        new_node = Node(new_value)  # create a new node
        new_node.set_next_node(self.head_node)  # set new_node link to current head_node
        self.head_node = new_node   # set current head_node to new_node

    # print all values in linked list starting from head_node
    def stringify_list(self):
        string_list = ""    # string to be returned

        current_node = self.get_head_node() # get current head_node

        # traverse the list until current_node is None
        while current_node:
            if current_node.get_value() != None:    # if current node has value
                # add value to string
                # try = normal
                # except = back-up once try failed
                try:
                    
                    string_list += "current_node value = " + current_node.get_value()\
                                + ",\t--> next_node value = " + current_node.get_next_node().get_value()\
                                + '\n' 
                except: 
                    string_list += "current_node value = " + current_node.get_value()\
                                + ",\t--> next_node value = \'ERROR: This is the end. Link to next_node is None\'" \
                                + '\n'
                current_node = current_node.get_next_node() # get next node in line

        return string_list

    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()   # get current head_node

        try:
            # checking if current node is the removing target
            if current_node.get_value() == value_to_remove:
                self.head_node = current_node.get_next_node()   # assign head_node to be the next in line
                                                                # current head_node will be orphaned/removed
            
            # traverse the list, checking for removing target
            else:
                while current_node:
                    next_node = current_node.get_next_node()    # checking next_node

                    # if found, skip current next_node, link current_node to the next node in line
                    if next_node.get_value() == value_to_remove:
                        current_node.set_next_node(next_node.get_next_node()) # link current_node to the next node in line

                        current_node = None     # break the loop by set current_node to None

                    else:   # continue by set current_node = next_node
                        current_node = next_node
        except:
            print("ERROR: \'", value_to_remove, "\' does not exists in linked list.\n")
