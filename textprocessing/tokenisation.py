__author__ = 'juliewe'
#aim - read in an XML file and tokenise, maintaining XML markup.

import ConfigParser,sys

try:
    from lxml import etree
    print "Running with lxml.etree"
except ImportError:
    try:
        import xml.etree.cElementTree as etree
        print "Running with cElementTree on Python 2.5+"
    except ImportError:

        print "Error importing lxml.etree"
        exit(-1)

class Tokeniser:

    def __init__(self,configfile):

        self.configfile=configfile
        self.config=ConfigParser.RawConfigParser()
        self.config.read(configfile)

    def getDataFile(self):
        try:
            datafile=self.config.get("default","datafile")
            return datafile
        except:
            print "Error: no datafile specified in config file ",self.configfile


    def runTokenisation(self):
        filename=self.getDataFile()
        print "Processing ",filename
        tree=etree.parse(filename)
        print etree.tostring(tree,pretty_print=True)

    def run(self):

        self.runTokenisation()


if __name__=="__main__":

    if len(sys.argv)>1:
        myTokeniser=Tokeniser(sys.argv[1])
        myTokeniser.run()

