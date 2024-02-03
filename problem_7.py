import typing as t

## A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root = '/', handler = None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler=handler)

    def insert(self, route_list: t.List[str], handler: str):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path

        node = self.root
        for r in route_list:
            if r in node.children.keys():
                node = node.children[r]
            else:
                new_node = RouteTrieNode()
                node.children[r] = new_node
                node = new_node

        node.handler = handler

    def find(self, route_list: t.List[str]):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match

        node = self.root
        for r in route_list:
            if r in node.children.keys():
                node = node.children[r]
            else:
                return None
            
        return node

## A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler = None):
        # Initialize the node with children as before, plus a handler
        self.handler = handler
        self.children = {}

    def __repr__(self):
        return f'{self.handler} -- {self.children}'

## The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler = None, non_found_handler = None):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.trie = RouteTrie(root = '/', handler = root_handler)
        self.not_found_handler = non_found_handler
        
    def add_handler(self, path: str, handler: str):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        if not path.startswith('/'):
            raise Exception('Path needs to start on root. Add / in the beginning of the path.')

        self.trie.insert(self.split_path(path), handler)

        
    def lookup(self, path: str):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        if len(path) == 0:
            return self.not_found_handler

        handler = self.trie.find(self.split_path(path))

        if handler and handler.handler:
            return handler.handler

        return self.not_found_handler 
        
    
    def split_path(self, path: str):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        splitted = path.split('/')
        splitted.pop(0) # pops empty string first first /
        if splitted[-1] == '':
            splitted.pop() # pops last empty string if exists
        return splitted

## Here are some test cases and expected outputs you can use to test your implementation

## create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route
router.add_handler("/home", "goes to homepage")
router.add_handler('/anotherpage', 'Goes to another page')
router.add_handler('/anotherpage/about/tmp', 'Goes to temporary')



## some lookups with the expected output
        
print('PASS' if router.lookup('/') == 'root handler' else 'FAIL')
print('PASS' if router.lookup('/home') == 'goes to homepage' else 'FAIL') 
print('PASS' if router.lookup('/home/about') == 'about handler' else 'FAIL') 
print('PASS' if router.lookup('/home/about/me') == 'not found handler' else 'FAIL')
print('PASS' if router.lookup('/anotherpage/about/tmp') == 'Goes to temporary' else 'FAIL')
print('PASS' if router.lookup('/anotherpage/about/') == 'not found handler' else 'FAIL')

# Edge Cases
print('PASS' if router.lookup('/home/about/') == 'about handler' else 'FAIL')  # trailing slash

# not adding the root slash throws an error
try:
    router.add_handler('home/about/me', 'about me')
except Exception as e:
    if str(e) == 'Path needs to start on root. Add / in the beginning of the path.':
        print('PASS')
    else:
        print('FAIL')

print('PASS' if router.lookup('about/me') == 'not found handler' else 'FAIL') # not found
print('PASS' if router.lookup('anotherpage/about/tmp') == 'not found handler' else 'FAIL') # Its a good path but the root slash is not provided
print('PASS' if router.lookup('') == 'not found handler' else 'FAIL') # provide empty string