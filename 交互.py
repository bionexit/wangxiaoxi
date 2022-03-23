# %%
import click

@click.group()
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True)
@click.option('--name')
def cli(name,password):
    print ("name is %s, password is %s!" % (name, password))
    if name == '1':
        send_mes(message=name)

@cli.command()
@click.option('--message', '-m', multiple=True, help='you can input multi messages.')
def send_mes(message):
    print ("This is func send_mes. message is %s" % '\n'.join(message))


@cli.command()
@click.option('--func1','-f1', help='This is Function 1.')
def execute_func1(func1):
    print ("Function 1 is being executed. %s " % func1)

@cli.command()
@click.option('--func2','-f2', help='This is Function 2.')
def execute_func2(func2):
    print ("Function 2 is being executed. %s " % func2)

@cli.command()
@click.option('--type', '-t', type=click.Choice(['x', 'y']), help='Choic x or y')
def select_type(type):
    print ('Your choice is %s' % type)

cli()

# %%
