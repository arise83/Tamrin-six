class RoseDictionary:
    def __init__(self):
        self.items = []
               
    
    def __getitem__(self, key):
        for (k, v) in self.items:
            if k == key:
                return v
        raise KeyError('error_msg')
    
    def __setitem__(self, key, value):
        for i, (k, v) in enumerate(self.items):
            if k == key:
                self.items[i] = (key, value)
                return
        self.items.append((key, value))
        
    def pop_item(self, raise_error=False, default=None, error_msg='error_msg'):
        if not self.items:
            if raise_error:
                raise KeyError(error_msg)
            elif default != None:
                return default
            elif error_msg != 'error_msg':
                print(error_msg)
            else:
                print('Dictionary was empty and no default value/message was specified.')
        else:
            popped_item = self.items.pop()
            return popped_item[1]

    def get_item(self, key, raise_error=False, default=None, error_msg='error_msg'):
        try:
            return self.__getitem__(key)
        except KeyError:   
            if not self.items: #Dictionary is empty
                if raise_error:
                    raise KeyError(error_msg)
                elif default != None:
                    return default
                elif error_msg != 'error_msg':
                    print(error_msg)
                else:
                    print('Value was not found and no default value/message was specified.')
            else: #Dictionary is not empty, but key is not found
               if raise_error:
                    raise KeyError(error_msg) 

