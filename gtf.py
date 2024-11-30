#!/bin/python3
"""
Script creado para automatizar la corrección al cambiar de tema en gnome 46+ ocasionado por Libadwaita
Desarrollado por blonder413
Basado en libadwaita-theme-changer (https://github.com/odziom91/libadwaita-theme-changer/tree/main)
"""

import sys
import os
import subprocess as sp

home_dir = os.getenv("HOME")
config_dir = "/.config"
themes_dir = "/.themes"

gtk = f"{home_dir}{config_dir}/gtk-4.0/gtk.css"
gtk_dark = f"{home_dir}{config_dir}/gtk-4.0/gtk-dark.css"
assets_gtk = f"{home_dir}{config_dir}/gtk-4.0/assets"
assets = f"{home_dir}{config_dir}/assets"


def reset():
    if os.path.isfile(gtk):
        sp.run(["rm", gtk])
    if os.path.isfile(gtk_dark):
        sp.run(["rm", gtk_dark])
    if os.path.isfile(assets_gtk):
        sp.run(["rm", assets_gtk])
    sp.run(["rm", "-rf", assets])

if __name__ == "__main__":
    try:
        if "--reset" in sys.argv:
            print("\n***\nReiniciando tema por defecto!\n***\n")
            reset()
        else:
            all_themes = str(
                sp.run(
                    ["ls", f"{home_dir}{themes_dir}/"], stdout=sp.PIPE
                ).stdout.decode("UTF-8")
            ).split()
            print("Seleccione un tema: ")
            for i, theme in enumerate(all_themes):
                print(f"{i+1}. {theme}")
            print("e. Salir")
            option = input("Elija su tema: ")
            match option:
                case "e":
                    print("Adiós!")
                case _:
                    option = int(option) - 1
                    chk_theme = all_themes[option]
                    print(f"\n***  Elegido: {chk_theme}  ***\n")
                    print("Eliminando tema anterior...")
                    reset()
                    print("Reparando nuevo tema...")
                    sp.run(
                        [
                            "ln",
                            "-s",
                            f"{home_dir}{themes_dir}/{chk_theme}/gtk-4.0/gtk.css",
                            gtk,
                        ]
                    )
                    sp.run(
                        [
                            "ln",
                            "-s",
                            f"{home_dir}{themes_dir}/{chk_theme}/gtk-4.0/gtk-dark.css",
                            gtk_dark,
                        ]
                    )
                    sp.run(
                        [
                            "ln",
                            "-s",
                            f"{home_dir}{themes_dir}/{chk_theme}/gtk-4.0/assets",
                            assets_gtk,
                        ]
                    )
                    sp.run(
                        [
                            "ln",
                            "-s",
                            f"{home_dir}{themes_dir}/{chk_theme}/assets",
                            assets,
                        ]
                    )
                    print("Hecho.")
    except ValueError as e:
        print("Opción incorrecta! Por favor intente de nuevo!")
