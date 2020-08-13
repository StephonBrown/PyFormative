import click
import os
import sys
from yattag import Doc, indent

#TODO 
    #-[ ] Bootstrap integration
    #-[X] Html document export
    #-[ ] plugin support
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
            with tag('body'): 
                line('h1', 'PyFormative Form')
                with tag('form', action = ""):
                    for input in self.inputTypes:
                        if(input in ["text", "email","tel","number","password", "date","file"]):
                            with tag('div', klass="form-control"):
                                line('label', "input%d"% count)
                                doc.input(name="input%d"% count ,type=str(input))
                            count = count + 1
                    doc.stag('input', type = 'submit', value = 'Send my message')
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
        inputTypes = list(map(str.lower, [click.prompt("What is the input type you would like for input # %d (text, email, tel, number, password, date, file)" % x , type=str) for x in range(1, amount+1)]))
        if(inputTypes == None):
            click.echo("Inputs must not be empty")
            valid = False
            
        else:
            valid = all([x in ["text", "email","tel","number","password","date", "file"] for x in inputTypes ])


    repo = PyFormObject(amount, inputTypes, False)
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

