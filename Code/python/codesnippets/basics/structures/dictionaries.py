import string
# Some definitions
collections = {"val_1", "val_2", "val_3"}
collections2 = {"val_1" : 1, "val_2" :2 , "val_3" : 3}
keys_ = {"val_1", "val_2", "val_3"}
values_ = {1, 2, 3}

# --------------------------------------------------------------------------------------------------------------------------------------
# Initialize a dictionary
dict_a = {'red': 'rouge', 'blue': 'bleu'}                  # dictionary
dict_new= collections.defaultdict(lambda: 1)               # Creates a dict with default value 1.
dict_a['pink'] = "rouge"                                     # set data
# --------------------------------------------------------------------------------------------------------------------------------------

# Create Dictornaries
dict_new = collections.defaultdict(string)                 # Creates a dict with default value of type string.
dict_new= dict(collections2)                               # Creates a dict from coll. of key-value pairs.
dict_new = dict(zip(keys_, values_))                        # Creates a dict from two collections.
dict_new = dict.fromkeys(keys_ [1:2])                       # Creates a dict from collection of keys.

# Set Defaults
dict_a.setdefault('extra', []).append('cyan')              # init key with default
value  = dict_a.setdefault("Choose_a_key", default=None)            # Returns and writes default if key is missing.

# Add items
dict_a.update({'green': 'vert', 'brown': 'brun'})            # Adds items. Replaces ones with matching keys.

b = dict_a['red']                                           # translate item

# --------------------------------------------------------------------------------------------------------------------------------------
# Accesses Key, Values, Items, Pairs
dict_a.keys()                                                 # get list of keys
dict_a.values()                                               # get list of values
dict_a.items()                                                # get list of key-value pairs
# Get sepcific value or return a default
d = dict_a.get('yellow', default = 'no translation found')     # return default
# loop through contents
c = [value for key, value in dict_a.items()]         # loop through contents
# Check if Key is present in dict
'red' in dict_a                                      # true if dictionary a contains key 'red'
# --------------------------------------------------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------------------------------------------------------
# Delete Items ( whole, by key)
del dict_a['red']                                 # delete key and associated with it value
dict_a.pop('blue')                                # remove specified key and return the corresponding value

# --------------------------------------------------------------------------------------------------------------------------------------
# Dictionary Comprehension
{k: v for k ,v in dict_a.items()}                     # dict comprehension
{k for k, v in dict_a.items() if v == value}          # Returns set of keys that point to the value.
{k: v for k, v in dict_a.items() if k in "keys"}      # Returns a dictioary filtered by keys

