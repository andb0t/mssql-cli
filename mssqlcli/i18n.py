from importlib import import_module
import gettext
import os

CLI_NAME = 'mssql-cli'
MODULE = 'mssqlcli'

def translate():
    """
    Gets the localized translation of message, based on the current global
    domain, language, and locale directory of the module.
    :param mod: The module namespace containing the locale for translation.
    :return: The localized translation of message, based on the current global
             domain, language, and locale directory alias.
    """
    modulePath = os.path.dirname(import_module(MODULE).__file__)
    localedir = os.path.join(modulePath, 'locale')
    domain = CLI_NAME
    return gettext.translation(domain, localedir, fallback=True).gettext
