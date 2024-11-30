# Gnome Theme Fix

Las versiones recientes de Gnome usa Libadwaita, esto hace que algunas aplicaciones como el navegador de archivos cajas no tome el borde
de ventana del tema que definamos.

Para solucionar esto básicamente hay que copiar o crear un enlace simbólico de los siguientes archivos

```
~/.themes/mi-tema/gtk-4.0/gtk.css
~/.themes/mi-tema/gtk-4.0/gtk-dark.css
~/.themes/mi-tema/gtk-4.0/assets
```

a la ruta `~/.config/gtk-4.0/` y ```~/.themes/mi-tema/assets/```
a la ruta `~/.config/`.

## Cómo usar?

1. Descargar el archivo o clonar el repositorio
2. Ejecutar el archivo con cualquiera de los 2 siguientes acciones

-   `python3 gtf.py`
-   `chmod +x gtf.py` y `./gtf.py`

Es posible que los cambios no surtan efecto de inmediato, si es así, reiniciar
el equipo.

## Dejar la configuración por defecto

Si queremos volver a usar Libawaita debemos eliminar los enlaces simbólicos creados manualmente o
agregando `--reset` al script

-   `python3 gtf.py --resset`
-   `./gtf.py --reset`

# Créditos

Este script es una modificación de [libadwaita-theme-changer](https://github.com/odziom91/libadwaita-theme-changer)
