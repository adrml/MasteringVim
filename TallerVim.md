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
|--------------|-----------------|
|``` ~ ``` |	Cambia el caso del caracter sobre el cursor en modo normal, o del texto seleccionado en modo visual. |
|``` u ``` | 	En modo visual, pasa todo el texto seleccionado a minúsculas. |
|``` U ``` | 	En modo visual, pasa todo el texto seleccionado a mayúsculas. |

--- 

# Buffers

Finalmente, tenemos los buffers. Nos permite abrir múltiples ficheros pero viendo sólo uno cada vez. Con comandos de vim de apenas 2 letras podemos saltar de uno a otro, ocultando en el cambio el que tuvieramos actualmente en pantalla. Si editamos múltiples ficheros desde línea de comandos con "vim *.c", cada fichero .c acaba en un buffer. 

| **Comando**  | **Significado** |
|--------------|-----------------|
|``` :buffers    ``` |	Ver el listado de buffers junto a sus números identificativos. |
|``` :buffer N   ``` | 	Abrir buffer número N. |
|``` :bn[ext]    ``` |	Ir al siguiente buffer. |
|``` :bp[revious]``` | 	Ir al anterior buffer. |
|``` :bf[irst]   ``` |	Ir al primer buffer. |
|``` :bl[ast]    ``` |	Ir al último buffer. |
|``` :bd[elete]  ``` |	Cerrar el buffer actual.  |
 
---

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

#VIMRC

 En vim podemos modificar muchos parámetros del editor mientras editamos los ficheros. Por ejemplo, tecleando en modo comando :set number (dos puntos, set number, intro), Vim activará la numeración de líneas (no dentro del fichero en sí, sino visualmente), algo que puede ser útil para programar.

Otro ejemplo, tecleando :syntax on, activaremos para el fichero actual el coloreado de sintaxis, es decir, que las palabras especiales que el editor entienda como que tienen un significado concreto aparecerán en diferentes colores. Si estamos programando en C, por ejemplo, las palabras claves aparecerán de un color, las cadenas de otro, etc (algo realmente útil a la hora de programar).

Pues bien, cualquier tipo de opción, macro, comando o función que vim entienda puede ser incluída en el fichero .vimrc en el directorio $HOME de nuestro usuario (o en un fichero _vimrc en el directorio de instalación de Vim o en el padre del Escritorio del usuario en Windows) de forma que se aplique como opción por defecto cuando lancemos Vim. Así, podemos crear un fichero .vimrc (por defecto normalmente no existirá), que contenga algo como lo siguiente:

	set nocompatible
	set number
	set ruler
	syntax on 

Esto hará que siempre que editemos un fichero, aparezca numeración de líneas (set number), un indicador de fila y columna en la barra de estado (set ruler) y resaltado de sintaxis (si está definida para el tipo de fichero que estamos editando) activado. Es algo así como el fichero de opciones de vim para nuestro usuario (y sólo para nuestro usuario). Existe un fichero de opciones general /etc/vimrc (normalmente) cuyos cambios afectan a todos los usuarios cuando arrancan vim, pero lo que incluyamos en nuestro .vimrc sólo afectará a vim cuando lo ejecutemos con nuestro usuario del sistema.

Así, podemos utilizar dicho fichero para indicar aquellas configuraciones con las que estemos más cómodos, de forma que podamos adaptar vim a nuestras necesidades. Es normal que en estos momentos iniciales no conozcamos vim lo suficiente como para hacernos un .vimrc decente, pero para empezar os recomiendo algo como lo que sigue:

	" Fichero .vimrc de mi usuario
	" Los comentarios se ponen con comillas dobles
	set nobackup 
	set ruler  

	" nocompatible permite funciones que VI no soporta
	set nocompatible 

	set tabstop=4
	set sw=4
	set expandtab
	    
	set vb 
	set noerrorbells 
	syntax on

Las posibilidades del fichero .vimrc son muy grandes, ya que no sólo soporta comandos simples de configuración sino que tiene un lenguaje propio que nos permite hacer casi cualquier tipo de cosa.
---
