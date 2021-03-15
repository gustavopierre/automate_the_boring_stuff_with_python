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
# TODO: Salva conteúdo do clipboard
# TODO: Lista palavras-chave e carrega conteúdo.
mcbShelf.close()