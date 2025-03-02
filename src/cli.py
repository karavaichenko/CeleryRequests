import click
from main import getByAddress, postByAddress, deleteByAddress
import json

@click.group()
def cli():
    pass

@click.command()
@click.option('--address')
def get(address):
    getByAddress(address)

@click.command()
@click.option('--address')
@click.option('--path')
def post(address, path):
    with open(path, "r") as file:
            data = json.load(file)
    postByAddress(address, data)

@click.command()
@click.option('--address')
@click.option('--authToken')
def delete(address, authToken):
    deleteByAddress(address, authToken)

cli.add_command(get)
cli.add_command(post)
cli.add_command(delete)

if __name__ == '__main__':
    cli()