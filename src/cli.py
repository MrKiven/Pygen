# -*- coding: utf-8 -*-

import click


@click.group()
@click.version_option()
@click.help_option()
def ppg():
    """ python project Generator(ppg) commands entry point."""
