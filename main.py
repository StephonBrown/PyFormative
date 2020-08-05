import click
class PyFormObject(object):
    def __init__(self, inputAmount=1, inputTypes=[]):
        super().__init__()
        self.inputAmount = inputAmount
        self.inputTypes = inputTypes

   
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


    repo = PyFormObject(amount,inputTypes)
    click.echo(repo.inputTypes)
    click.echo(repo.inputAmount)

