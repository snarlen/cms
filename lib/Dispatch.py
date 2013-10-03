import argparse
import os 

from File import File 


class Dispatch(object):
	def __init__(self):
		
		self.argParser = argparse.ArgumentParser(description='CMS is a command line content management system')
		
		
		self.argParser.add_argument('--create', action="append", dest="PROJECT_NAME", help='Creates a new site, example: "my_project"')
		self.argParser.add_argument('--add-root', action="append", dest="PAGE_NAME", help='Creates a new root page, example: "index"')
		
		self.argParser.add_argument('--parent', action="append", dest="PARENT_NAME", help='Use with --add-child, example: cms --parent foo --add-child bar')
		self.argParser.add_argument('--add-child', action="append", dest="SUB_PAGE_NAME", help='Creates a child page, use with --add-child, example: cms --parent foo --add-child bar')
		
		
		self.argParser.add_argument('--page', action="append", dest="PAGE_NAME", help='Use with --template or --edit-md')
		self.argParser.add_argument('--template', action="append", dest="TEMPLATE_FILENAME", help='Sets the page with the template, use with --page')
		
		
		self.argParser.add_argument('--edit-md', action="append", dest="CONTENT_BLOCK_MD", help='Use with --template')
		
		
	def route(self):
		args = vars(self.argParser.parse_args())
		
		if args['PARENT_NAME'] != None and args['SUB_PAGE_NAME'] != None:
			self.createSubPage(args['PARENT_NAME'], args['SUB_PAGE_NAME'])
		elif args['PAGE_NAME'] != None and args['TEMPLATE_FILENAME'] != '':
			self.setTemplate(args['PAGE_NAME'][0], args['TEMPLATE_FILENAME'][0])
		elif args['PAGE_NAME'] != None and args['PAGE_NAME'] != '':
			self.createRootPage(args['PAGE_NAME'][0])
		elif args['PROJECT_NAME'] != None and args['PROJECT_NAME'] != '':
			self.createProject(args['PROJECT_NAME'][0])
		else:
			self.argParser.print_help()
		
	def getProjectName(self):
		return "%s/_config/site.json" % os.getcwd()	
	
	def setTemplate(self, page_name, template_filename):
		print "Setting up template for %s" % page_name
		objFile = File()
		objFile.setTemplate(page_name, template_filename);
		
	def createSubPage(self, parent_page, child_page, name):
		project_name = self.getProjectName()
		print "Adding the child page %s to the parent page %s in %s" % (child_page, parent_page, project_name)
	
	def createRootPage(self, name):
		project_name = self.getProjectName()
		print "Adding a root page to %s" % project_name
		
		try:
			with open(project_name): 	
				objFile = File()
				objFile.createRootPage(name);
				
				
		except IOError:
			print 'Dang, make sure you\'re in the project folder'
		
		
		
			
	def createProject(self, name):
		print "Creating a new project in \"%s/%s\"" % (os.getcwd(), name)
		objFile = File()
		objFile.create("%s/%s" % (os.getcwd(), name))
		
