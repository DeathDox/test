#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from os import name, system

def banner():
    system("cls" if name == "nt" else "clear")
    print(BRIGHT + GREEN)
    print(r"  ")
    print(r"  ")
    print(r"  ")
    print(r"  ")
    print()
    print(r"          ")
    print(RESET_ALL)


def main():
    banner()
    print("[1] Поиск по телефону")
    print("[2] Поиск по голосу")
    print("[3] ВЫХОД.")
    print()
    face = input(f"{BRIGHT}{BLUE}Введите номер пункта: {RESET_ALL}")
    if face== "1":
        facefind()
    elif face == "2":
        single()
    elif face == "3":
        print()
        exit()
    else:
        print(f"\n{BRIGHT}{RED}[*] Номер пункта введён неверно!{RESET_ALL}")
        sleep(1)
        main()


        def face():
            check_internet()
    check_version()
    banner()
    print("ТЕХНИЧЕСКИЙ РАБОТЫ")
