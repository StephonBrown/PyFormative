import click
import os
import sys
from yattag import Doc, indent

#TODO 
    #-[X] Bootstrap integration
    #-[X] Html document export
    #-[ ] Plugin support
    #-[ ] Accesibility
class PyFormObject(object):
    def __init__(self, inputAmount=1, inputTypes=[], includeBootstrapClasses=False):
        super().__init__()
        self.inputAmount = inputAmount
        self.inputTypes = inputTypes
        self.includeBootstrapClasses = includeBootstrapClasses

    def GenerateForm(self):
        doc, tag, text, line = Doc().ttl()
        count = 1
        doc.asis('<!DOCTYPE html>')
        with tag('html'):
            if(self.includeBootstrapClasses):
                with tag('head'):
                    doc.stag('link', rel="stylesheet", href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css", integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm", crossorigin="anonymous")
            with tag('body'): 
                line('h1', 'PyFormative Form')
                with tag('form', action = ""):
                    for input in self.inputTypes:
                        if(input in ["text", "email","tel","number","password", "date","file"]):
                            with tag('div', klass="mb-3"):
                                if(self.includeBootstrapClasses):
                                    line('label', "input%d"% count, klass="form-label")
                                    doc.input(name="input%d"% count ,type=str(input), klass="form-control")
                                else:
                                    line('label', "input%d"% count)
                                    doc.input(name="input%d"% count ,type=str(input))
                            count = count + 1
                    doc.stag('input', type = 'submit', value = 'Send my message',klass="btn btn-primary")
            if(self.includeBootstrapClasses):
                tag('script',  src="https://code.jquery.com/jquery-3.2.1.slim.min.js", integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN", crossorigin="anonymous")
                tag('script',  src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js", integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q", crossorigin="anonymous")
                tag('script',  src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js", integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl", crossorigin="anonymous")
        return indent(
                    doc.getvalue(),
                    indentation = '     ',
                    newline = '\r\n',
                    indent_text = True
                )

    def ExportFile(self, filePath):
        if os.path.isdir(filePath):
            try:
                f = open("%s/home.html" % filePath, "w+")
                f.write(self.GenerateForm())
                f.close()
            except OSError:
                click.echo("Invalid path")
        elif os.path.isfile(filePath):
            try:
                filePath.replace(".html","")
                f = open("%s.html"% filePath, "w+")
                f.write(self.GenerateForm())
                f.close()
            except OSError:
                click.echo("Invalid file")
        else:
            try:
                filePath.replace(".html","")
                f = open("%s.html"% filePath, "w+")
                f.write(self.GenerateForm())
                f.close()
            except OSError:
                click.echo("Invalid file")

@click.command()
@click.option('--amount', prompt="Please enter the amount of inputs you would like", type=int, required=True, default=1)
@click.pass_context
def initial(context, amount):
    click.echo("WELCOME TO PYFORMATIVE")
    valid = False
    while not valid:
        bootstrapFile = click.prompt("Would you like to add Bootstrap 4 to into this project?", type=str)
        inputTypes = list(map(str.lower, [click.prompt("What is the input type you would like for input # %d (text, email, tel, number, password, date, file)" % x , type=str) for x in range(1, amount+1)]))

        if(inputTypes == None):
            click.echo("Inputs must not be empty")
            valid = False
            
        else:
            valid = all([x in ["text", "email","tel","number","password","date", "file"] for x in inputTypes ])

    bootstrapIncluded = True if bootstrapFile in ["yes", "y","Yes","YES"] else False
    repo = PyFormObject(amount, inputTypes, bootstrapIncluded)

    exportFile = click.prompt("Would you like to export the file?", type=str)

    if exportFile in ["yes", "y","Yes","YES"]:   
        filePath = click.prompt("Please enter the file name you would like to export", type=click.Path(dir_okay=True, file_okay=True))
        repo.ExportFile(filePath)
        click.echo(repo.GenerateForm())
        click.echo('Goodbye!')
    else:
        click.echo(repo.GenerateForm())
        click.echo('Goodbye!')

if getattr(sys, 'frozen', False):
    initial(sys.argv[1:])

