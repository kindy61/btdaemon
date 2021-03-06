"""
Tutorial 05 - Object inheritance

You are free to derive your request handler classes from any base
class you wish. In most real-world applications, you will probably
want to create a central base class used for all your pages, which takes
care of things like printing a common page header and footer.
"""

from cherrypy import cpg

class Page:
    # Store the page title in a class attribute
    title = 'Untitled Page'

    def header(self):
        return '''
            <html>
            <head>
                <title>%s</title>
            <head>
            <body>
            <h2>%s</h2>
        ''' % (self.title, self.title)

    def footer(self):
        return '''
            </body>
            </html>
        '''

    # Note that header and footer don't get their exposed attributes
    # set to True. This isn't necessary since the user isn't supposed
    # to call header or footer directly; instead, we'll call them from
    # within the actually exposed handler methods defined in this
    # class' subclasses.


class HomePage(Page):
    # Different title for this page
    title = 'Tutorial 5'

    def __init__(self):
        # create a subpage
        self.another = AnotherPage()

    def index(self):
        # Note that we call the header and footer methods inherited
        # from the Page class!
        return self.header() + '''
            <p>
            Isn't this exciting? There's
            <a href="./another/">another page</a>, too!
            </p>
        ''' + self.footer()

    index.exposed = True


class AnotherPage(Page):
    title = 'Another Page'

    def index(self):
        return self.header() + '''
            <p>
            And this is the amazing second page!
            </p>
        ''' + self.footer()

    index.exposed = True


cpg.root = HomePage()

cpg.server.start(configFile = 'tutorial.conf')
