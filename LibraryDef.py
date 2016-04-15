'''
Contains all of the information for the current library.
'''


class LibraryDef:
    def __init__(self, field_types, field_list, table_columns, true_columns):
        self.field_types = field_types
        self.field_list = field_list
        self.table_columns = table_columns
        self.true_columns = true_columns
