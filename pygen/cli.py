# -*- coding: utf-8 -*-

import click


@click.group()
@click.version_option()
def pygen():
    """ Pygen commands entry point."""
