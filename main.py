import click
class PyFormObject(object):
    def __init__(self, inputAmount=1, inputTypes={"Text"}):
        super().__init__()
        self.inputAmount = inputAmount
        self.inputTypes = inputTypes

@click.command()
@click.option('--amount', prompt="Please enter the amount of inputs you would like")
def pyform(amount):
    click.echo("Hello welcome to PyFormative. Please enter the amount of input feilds you would like")
    click.echo(amount)