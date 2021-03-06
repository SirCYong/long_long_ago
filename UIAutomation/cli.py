import logging

import click

from . import Utils


log = logging.getLogger(__name__)


@click.command()
@click.argument('feet')
def main(feet=None):
    logging.basicConfig(level=logging.INFO)

    meters = Utils.feet_to_meters(feet)

    if meters is not None:
        click.echo(meters)


if __name__ == '__main__':  # pragma: no cover
    main()
