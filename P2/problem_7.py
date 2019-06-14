from collections import defaultdict


class RouteTrieNode:

    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.handler = None
        self.children = defaultdict(RouteTrieNode)

    def set_handler(self, handler):
        self.handler = handler

    def get_handler(self):
        return self.handler


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:

    def __init__(self, handler):
        # Initialize the trie with an root node and a handler, this is the root
        # path or home page node
        self.root = RouteTrieNode()
        self.root.set_handler(handler)

    def insert(self, list_of_words, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of
        # this path
        itr = self.root
        for word in list_of_words:
            itr = itr.children[word]
        itr.set_handler(handler)

    def find(self, list_of_words):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        itr = self.root
        for word in list_of_words:
            if word not in itr.children:
                return None
            itr = itr.children[word]
        return itr.get_handler()

    def get_root_handler(self):
        return self.root.get_handler()

    def _iterate(self, node, lists, c_list=[]):
        for word in node.children:
            c = c_list + [word]
            self._iterate(node.children[word], lists, c)

        if node.get_handler() is not None:
            lists.append(c_list)

    def get_all_lists_of_words(self):
        itr = self.root
        lists = []
        self._iterate(itr, lists)
        return lists


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler, _404_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as
        # well!
        self.trie = RouteTrie(root_handler)
        self.error_handler = _404_handler

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        parts = self.split_path(path)
        self.trie.insert(parts, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        if path == "/":
            return self.trie.get_root_handler()

        parts = self.split_path(path)
        handler = self.trie.find(parts)
        if handler is None:
            return self.error_handler
        return handler

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and lookup functions,
        # so it should be placed in a function here
        _path = path if path[-1] != "/" else path[:-1]
        return _path.split("/")

    def get_sitemap(self):
        list_paths = self.trie.get_all_lists_of_words()
        paths = ["/".join(l) if l else "/" for l in list_paths]
        return paths


def test_cases():
    # Here are some test cases and expected outputs you can use to test your implementation
    # create the router and add a route
    # remove the 'not found handler' if you did not implement this
    router = Router("root handler", "not found handler")
    router.add_handler("/home/about", "about handler")  # add a route

    # some lookups with the expected output
    handler = router.lookup("/")
    # should print 'root handler'
    print(handler, ', is correct?', handler == 'root handler')
    handler = router.lookup("/home")
    # should print 'not found handler' or None if you did not implement one
    print(handler, ', is correct?', handler == 'not found handler')
    handler = router.lookup("/home/about")
    # should print 'about handler'
    print(handler, ', is correct?', handler == 'about handler')
    handler = router.lookup("/home/about/")
    # should print 'about handler' or None if you did not handle trailing
    # slashes
    print(handler, ', is correct?', handler == 'about handler')
    handler = router.lookup("/home/about/me")
    # should print 'not found handler' or None if you did not implemen
    print(handler, ', is correct?', handler == 'not found handler')

    router.add_handler(
        "/blog/2019-01-15/my-awesome-blog-post",
        "awesome blog post content")
    l = sorted(router.get_sitemap())
    print(
        l,
        ' is correct?',
        l == [
            '/',
            '/blog/2019-01-15/my-awesome-blog-post',
            '/home/about'])


test_cases()
# root handler , is correct? True
# not found handler , is correct? True
# about handler , is correct? True
# about handler , is correct? True
# not found handler , is correct? True
# ['/', '/blog/2019-01-15/my-awesome-blog-post', '/home/about']  is correct? True
