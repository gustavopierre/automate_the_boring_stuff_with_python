#!python3
'''
    mcb.pyw - salva e carrega porções de texto no clipboard.
    Usage: 
        py.exe mcb.pyw save <palavra chave> - salva clipboard na palavra-chave.
        py.exe mcb.pyw <palavra-chave> - carrega palavra-chave no clipboard.
        py.exe mcb.pyw list - carrega todas as palavras-chave no clipboard.
'''
import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Salva conteúdo do clipboard
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # TODO: Lista palavras-chave e carrega conteúdo.
    pass
mcbShelf.close()