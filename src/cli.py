# -*- coding: utf-8 -*-

import click


@click.group()
@click.version_option()
@click.help_option()
def pygen():
    """ Pygen commands entry point."""
