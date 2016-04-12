'''
Contains all of the information for the current library.
'''


class LibraryDef:
    def __init__(self, field_types, field_list, table_columns):
        self.field_types = field_types
        self.field_list = field_list
        self.table_columns = table_columns
