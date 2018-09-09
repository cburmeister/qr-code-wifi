"""
Generate a QR code containing WIFI credentials.

Share access to your WIFI network without exchanging any network name or
password.
"""
import click
import pyqrcode as pq


@click.command()
@click.argument('ssid')
@click.argument('security')
@click.argument('password')
@click.option(
    '--out',
    default=None,
    type=click.File('wb'),
    help='Save the QR code to the given path as a `png`.'
)
def create(ssid, security, password, out):
    qr = pq.create('WIFI:S:{ssid};T:{security};P:{password};;'.format(
        ssid=ssid,
        security=security,
        password=password,
    ))
    if out:
        qr.png(out)
    click.echo(qr.terminal())
