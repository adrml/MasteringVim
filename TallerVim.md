---
title: TallerVim
author: Adrian , Alberto
date: sáb mar  9 19:29:38 CET 2019 
---

# Moverse por el archivo

| Keystrokes | Acción |
| ---------- | -------| 
|``` h/j/k/l ```| Mueve el cursor izquierda/abajo/arriba/derecha. |  
|``` barra espaciadora ```| Mueve el cursor a la izquierda un espacio. |  
|``` -/+ ```| Mueve el cursor abajo/arriba en la primera columna. |  
|``` ctrl-d ```| Desplaza hacia abajo la mitad de la pantalla. |  
|``` ctrl-u ```| Desplaza hacia arriba la mitad de la pantalla. |  
|``` ctrl-f ```| Desplaza hacia abajo una pantalla. |  
|``` ctrl-b ```| Desplaza hacia arriba una pantalla. |  
|``` ctrl-y ```| Desplaza hacia abajo una línea. |  
|``` ctrl-e ```| Desplaza hacia arriba una línea. |  
|```M``` | Mueve el cursor al centro de la página. |
|```H``` | Mueve el cursor al inicio de la página. |
|```L``` | Mueve el cursor al final de la página. |
|``` W ```| Mueve el cursor hasta la siguiente palabra. *Delimitado por espacios.* |
|``` w ```| Mueve el cursor hasta la siguiente palabra. *Delimitado por los carácteres no alfanuméricos.* |
|``` B ```| Mueve el cursor hasta la palabra anterior. *Delimitado por espacios.* |
|``` b ```| Mueve el cursor hasta la palabra anterior. *Delimitado por los carácteres no alfanuméricos.* |
|``` E ```| Mueve el cursor hasta el final de la palabra. *Delimitado por los espacios.* |
|``` e ```| Mueve el cursor hasta el final de la palabra. *Delimitado por los carácteres no alfanuméricos.* |
|``` 0 ```| Mueve el cursor al inicio de la línea. |
|``` :[num] ```| Mueve el cursor a la línea indicada por [num]. |
|``` $ ```| Mueve el cursor al final de la línea. |
|``` * ```| Mueve el cursor al inicio de la siguiente frase. *Delimitado por ```.```,```?```,```!```.* |
|``` * ```| Mueve el cursor al inicio de la frase actual. |
|``` } ```| Mueve el cursor al inicio del siguiente párrafo. *Delimitado por líneas en blanco.* |
|``` { ```| Mueve el cursor al inicio del párrafo actual. |
|``` ]] ```| Mueve el cursor al inicio de la siguiente sección. |
|``` [[ ```| Mueve el cursor al inicio de la sección actual. |
|``` G ```| Mueve el cursor al final del fichero. |
|``` % ```| Mueve el cursor al cierre/inicio del paréntesis/corchete/etc, actual. |
|``` '. ```| Mueve el cursor a la última línea modificada. |
|``` m ```| Marca la línea donde esta ubicado el cursor. Es necesario, identificarlo con una letra. *Ejemplo: Con **ma**, marcaríamos la línea actual con la letra a.* |
|``` ' ```| Mueve el cursor a la línea marcada que le hemos indicado. *Ejemplo: Con **'a**, nos moveríamos a la línea que hemos marcado previamente con esa letra.* |
|``` ]' ```| Mueve el cursor a la siguiente línea marcada. |
|``` [' ```| Mueve el cursor a la anterior línea marcada. |
---

# Editar el contenido del archivo 

| Keystrokes | Acción |
| ---------- | -------| 
|``` : ```| Abre el modo inserción en la ubicación actual del cursor. |
|``` I ```| Abre el modo inserción al inicio de la línea en la que está ubicada el cursor. |
|``` a ```| Abre el modo inserción en la posición posterior al cursor. |
|``` A ```| Abre el modo inserción al final de la línea en la que está ubicada el cursor. |
|``` o ```| Inserta una línea a partir de la línea actual del cursor y entra en el modo inserción. |
|``` O ```| Inserta una línea en la línea anterior al cursor y entra en el modo inserción. |
|``` Esc ```| Sale del modo inserción. *También se utiliza para finalizar otros modos, como el Visual.* |
|``` u ```| Deshace el último cambio realizado. |
|``` U ```| Deshace todos los cambios de la línea actual. |
|``` x ```| Elimina el carácter sobre el que está el cursor. |
|``` X ```| Elimina el carácter anterior al cursor. |
|``` Y / yy ```| Copia el contenido de la línea actual en el buffer principal. |
|``` p ```| Pega lo almacenado en el buffer principal a partir de la posición del cursor. |
|``` P ```| Pega lo almacenado en el buffer principal antes de la posición del cursor. |
|``` r ```| Remplaza elcarácter ubicado en la posición actual del cursor. |
|``` R ```| Sobreescribe los carácteres escritos a partir de la posición del cursor. |
|``` s ```| Sustituye el carácter bajo el cursor y entra al modo inserción. |
|``` S ```| Sustituye la línea completa en la que está ubicada el cursor. |
|``` J ```| Une la línea actual y la siguiente y las une en una sola. | 
|``` ~ ```| Alterna entre mayúsculas y minúsculas en el carácter sobre el que este posicionado el cursor. |
|``` ctrl-a ```| Aumenta un número bajo el cursor. |
|``` ctrl-x ```| Disminuye un número bajo el cursor. |
|``` . ```| Repite el último comando ejecutado. |
---

# Comandos combinados

En algunos casos, como con los comandos ```c```, ```d``` o ```f``` una vez ejecutados, vim se queda esperando a una segunda acción, como podría ser, la afectación de la línea entera, o utilizando ciertos patrones que se mostrarán a continuación.

| Keystrokes | Acción |
| ---------- | -------| 
|``` *$  ```| Trabaja con lo marcado desde el cursor hasta el final de la línea actual. |
|``` *w ```| Trabaja con la palabra a partir del cursor. *Sigue las mismas reglas que ```w``` y ```W```.* |
|``` *- ```| Trabaja con la línea actual y la anterior, y entra en el modo inserción. |
|``` *fx ```| Trabaja  con lo seleccionado a partir de el cursor hasta la próxima aparición de la letra ```x```, y entra en el modo inserción. |
|``` *'x ```| Trabaja  con lo seleccionado a partir de el cursor hasta la línea marcada con el identificador ```x```, y entra en el modo inserción. |
|``` 'a*'b ```| Trabaja  con lo seleccionado a partir de la línea marcada con el identificador ```a``` hasta la línea marcada con el identificador ```b```, y entra en el modo inserción. |
|``` */x ```| Trabaja  con lo seleccionado a partir de el cursor hasta la próxima aparición de ```x```, sin afectar a este, y entra en el modo inserción. |

> Donde el  * se sustituiría por la acción a realizar.

---

# Deshacer cambios

 En vim, podemos deshacer múltiples pasos con la tecla ```u```, y rehacer pasos de nuevo con ```Ctrl-R```

Esto es diferente del ví clásico, donde sólo podías deshacer un paso, y volviendo a dar a "u" deshacías lo deshecho, es decir, hacías un undo del undo.

Para rizar más el rizo, vim dispone incluso de funcionalidad de undo especificando el tiempo. Podemos volver el documento atrás en el tiempo con el comando **:earlier**, y volver de nuevo adelante el tiempo necesario con **:later:**

```
:earlier 1h   <-- Volvemos el documento a como estaba hace 1 hora
:later 10m    <-- Ahora avanzamos 30 minutos (a como estaba hace 60-10=50m)
```
---

# Conversion Mayusculas/Minusculas

Para los programadores puede ser necesario, en ocasiones, cambiar el "case" de un texto a minúsculas, mayúsculas, o alternarlo. Esto lo podemos hacer (una vez seleccionado el texto en modo visual) con:


| **Comando**  | **Significado** |
|``` ~ ``` |	Cambia el caso del caracter sobre el cursor en modo normal, o del texto seleccionado en modo visual. |
|``` u ``` | 	En modo visual, pasa todo el texto seleccionado a minúsculas. |
|``` U ``` | 	En modo visual, pasa todo el texto seleccionado a mayúsculas. |


# Macros 

En Vim una macro es un conjunto de comandos que pueden realizarse mediante un comando y/o una combinación de teclas.

Para grabar nuestra propia macro tendremos que hacer uso de la tecla **Q** , seguido del caracter al que queremos asignar la macro que vamos a grabar.

Por ejemplo&rarr;```Qa``` 

Empezará a grabar nuestras acciones en la tecla **a**.A partir de aqui tenemos que ejecutar todos los comandos que queramos que registre la macro 
para ejecutarlos en bloque posteriormente

## Ejecutar Macros 

Ejecutar macros en vim es casi tan sencillo como presionar la tecla a la que se la hemos asignado precedido por la tecla ```@``` , siguiendo el ejemplo anterior , para llamar a la macro grabada en **a**

Por ejemplo&rarr;```@a```

Ejecutará los bloques de comandos asignados a la macro almacenada en **a**.

---
# Archivo vimrc

```vimrc
		set nocompatible              " be improved, required
		filetype off                  " required
		filetype plugin on
		" set the runtime path to include vundle and initialize
		set rtp+=~/.vim/bundle/vundle.vim
		call vundle#begin()

		" let vundle manage vundle, required
		plugin 'vundlevim/vundle.vim'
		plugin 'scrooloose/nerdtree'
		plugin 'raimondi/delimitmate'
		plugin 'yggdroot/indentline'
		plugin 'itchyny/lightline.vim'
		plugin 'othree/xml.vim.git'
		plugin 'moiatgit/vim-rst-sections.git'
		plugin 'mattn/emmet-vim'
		plugin 'scrooloose/nerdcommenter'
		plugin 'sql.vim--stinson'

		" all of your plugins must be added before the following line
		call vundle#end()            " required
		filetype plugin indent on    " required
		nnoremap <s-n> :nerdtreetoggle <cr>
		nnoremap <s-left> :tabprevious<cr>
		nnoremap <s-right> :tabnext<cr>
		nnoremap <s-up> :tabnew<cr>
		nnoremap <s-down> :tabclose<cr>
		map <s-q> :w <bar> :autocmd bufwritepost * call autocommit()<cr>
		"colorscheme sahara 
		syntax on
		"habilitar paleta de colores 256bits 
		if $colorterm =='gnome-terminal'
			set t_co=256
		endif

		"try 
			"colorscheme sahara
		"catch
		"endtry
		"
		"mapear en modo normal el espacio a / y el ctrl+espacio a ? para buscar
		map <space> /
		map <c-space> ?
		"set background=dark 
		"" encoding
		set encoding=utf-8
		"colores indentación
		let g:indentline_color_term=196
		let g:indentline_char='└'
		let g:user_emmet_mode='a'
		"color barra
		set laststatus =2
		let g:lightline = {
		\'colorscheme': 'solarized',
		\}
		set visualbell
		"highlight en las busquedas
		set hlsearch  
		"mejora la busqueda
		set incsearch
		"quita ruido de errores
		set noerrorbells

		set omnifunc=syntaxcomplete#complete
		function! autocommit()
			call system('git rev-parse --git-dir > /dev/null 2>&1')
			let message = 'adrupdated ' . expand('%:.')
			call system('git add ' . expand('%:p'))
			call system('git commit -m ' . shellescape(message, 1))
			call system('git push')
		endfun
```
---
