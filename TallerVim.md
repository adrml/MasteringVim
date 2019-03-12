---
title: TallerVim
author: Adrian , Alberto
date: sáb mar  9 19:29:38 CET 2019 
---

# Moverse por el archivo

---
| Keystrokes | Acción |
| ---------- | -------| 
|``` h/j/k/l ```| Mueve el cursor izquierda/abajo/arriba/derecha. |  
|``` barra espaciadora ```| Mueve el cursor a la izquierda un espacio. |  
|``` -/+ ```| Mueve el cursor abajo/arriba en la primera columna. |  
|``` ctrl-d ```| Desplaza hacia abajo la mitad de la pantalla, en caso de poner un número precediendo el comando, solo descenderá el número de líneas indicado. |  
|``` ctrl-u ```| Desplaza hacia arriba la mitad de la pantalla, en caso de poner un número precediendo el comando, solo ascenderá el número de líneas indicado. |  
|``` ctrl-f ```| Desplaza hacia abajo una pantalla, en caso de poner un número precediendo el comando, se descenderá ese número de pantallas. |  
|``` ctrl-b ```| Desplaza hacia arriba una pantalla, en caso de poner un número precediendo el comando, se ascenderá ese número de pantallas. |  
|``` ctrl-y ```| Desplaza hacia abajo una línea, en caso de poner un número precediendo el comando se descenderá ese número de líneas. |  
|``` ctrl-e ```| Desplaza hacia arriba una línea, en caso de poner un número precediendo el comando se ascenderá ese número de líneas. |  
|``` ```M``` | Mueve el cursor al centro de la página. |
|``` ```H``` | Mueve el cursor al inicio de la página. |
|``` ```L``` | Mueve el cursor al final de la página. |
|``` W ```| Mueve el cursor hasta la siguiente palabra. En caso de ir precedido por un número, replicará esa acción ese número de veces. (Delimitado por espacios.) |
|``` w ```| Mueve el cursor hasta la siguiente palabra. En caso de ir precedido por un número, replicará esa acción ese número de veces. (Delimitado por los carácteres no alfanuméricos.) |
|``` B ```| Mueve el cursor hasta la palabra anterior. En caso de ir precedido por un número, replicará esa acción ese número de veces. (Delimitado por espacios.) |
|``` b ```| Mueve el cursor hasta la palabra anterior. En caso de ir precedido por un número, replicará esa acción ese número de veces. (Delimitado por los carácteres no alfanuméricos.) |
|``` E ```| Mueve el cursor hasta el final de la palabra. En caso de ir precedido por un número, replicará esa acción ese número de veces. (Delimitado por los espacios.) |
|``` e ```| Mueve el cursor hasta el final de la palabra. En caso de ir precedido por un número, replicará esa acción ese número de veces. (Delimitado por los carácteres no alfanuméricos.) |
|``` 0 ```| Mueve el cursor al inicio de la línea. |
|``` :[num] ```| Mueve el cursor a la línea indicada por [num]. |
|``` $ ```| Mueve el cursor al final de la línea. |
|``` ) ```| Mueve el cursor al inicio de la siguiente frase. (Delimitado por ```.```,'?','!'.) |
|``` ( ```| Mueve el cursor al inicio de la frase actual. |
|``` } ```| Mueve el cursor al inicio del siguiente párrafo. (Delimitado por líneas en blanco y las macros nroff **Mirar NROFF Macros**.) |
|``` { ```| Mueve el cursor al inicio del párrafo actual. |
|``` ]] ```| Mueve el cursor al inicio de la siguiente sección. |
|``` [[ ```| Mueve el cursor al inicio de la sección actual. |
|``` G ```| Mueve el cursor al final del fichero. |
|``` % ```| Mueve el cursor al cierre/inicio del paréntesis/corchete/etc, actual. |
|``` '. ```| Mueve el cursor a la última línea modificada. |
|``` m ```| Marca la línea donde esta ubicado el cursor. Es necesario, identificarlo con una letra. (Ejemplo: Con "ma", marcaríamos la línea actual con la letra a.) |
|``` ' ```| Mueve el cursor a la línea marcada que le hemos indicado. (Ejemplo: Con "'a", nos moveríamos a la línea que hemos marcado previamente con esa letra.) |
|``` ]' ```| Mueve el cursor a la siguiente línea marcada. |
|``` [' ```| Mueve el cursor a la anterior línea marcada. |
---

# Editar el contenido del archivo 

| Keystrokes | Acción |
| ---------- | -------| 
|``` : ```| abre el modo inserción en la ubicación actual del cursor. |
|``` I ```| abre el modo inserción al inicio de la línea en la que está ubicada el cursor. |
|``` a ```| abre el modo inserción en la posición posterior al cursor. |
|``` A ```| abre el modo inserción al final de la línea en la que está ubicada el cursor. |
|``` o ```| inserta una línea a partir de la línea actual del cursor y entra en el modo inserción. |
|``` O ```| inserta una línea en la línea anterior al cursor y entra en el modo inserción. |
|``` Esc ```| Sale del modo inserción. (También se utiliza para finalizar otros modos, como el Visual.) |
|``` u ```| deshace el último cambio realizado. |
|``` U ```| deshace todos los cambios de la línea actual. |
|``` dd ```| Elimina la línea actual. En caso de ir precedida por un número, eliminará el número de líneas indicado. (Y la/s almacena en un buffer.) |
|``` D / d$ ```| Elimina el contenido de la línea actual, a partir del cursor. |
|``` dw ```| Elimina la palabra a partir del cursor. En caso de ir precedido por un número eliminará el número de palabras indicado. (Sigue las mismas reglas que "w" y "W".) |
|``` d- ```| Elimina la línea actual y la anterior. |
|``` dfx ```| Elimina desde el cursor hasta la próxima aparición de la letra "x". |
|``` d'x ```| Elimina desde el cursor hasta la línea marcada con el identificador "x". |
|``` 'ad'b ```| Elimina desde la línea marcada con el identificador "a" hasta la línea marcada con el identificador "b". |
|``` d/x ```| Elimina desde el cursor hasta la próxima aparición de "x", sin eliminar este. |
|``` cc ```| Elimina la línea actual. En caso de ir precedida por un número, eliminará el número de líneas indicado, y entra en el modo inserción. |
|``` C / c$ ```| Elimina el contenido de la línea actual, a partir de cursor, y entra en el modo inserción. | 
|``` cw ```| Elimina la palabra a partir del cursor. En caso de ir precedido por un número eliminará el número de palabras indicado, y entra en el modo inserción.  (Sigue las mismas reglas que "w" y "W".) |
|``` c- ```| Elimina la línea actual y la anterior, y entra en el modo inserción. |
|``` cfx ```| Elimina desde el cursor hasta la próxima aparición de la letra "x", y entra en el modo inserción. |
|``` c'x ```| Elimina desde el cursor hasta la línea marcada con el identificador "x", y entra en el modo inserción. |
|``` 'ac'b ```| Elimina desde la línea marcada con el identificador "a" hasta la línea marcada con el identificador "b", y entra en el modo inserción. |
|``` c/x ```| Elimina desde el cursor hasta la próxima aparición de "x", sin eliminar este, y entra en el modo inserción. |
|``` x ```| elimina el carácter sobre el que está el cursor. |
|``` X ```| elimina el carácter anterior al cursor. |
|``` Y / yy ```| Copia el contenido de la línea actual en el buffer principal. En caso de ir precedido por un número, copiara tantas líneas como se indique. |
|``` p ```| pega lo almacenado en el buffer principal a partir de la posición del cursor. En caso de ir precedido por un número, lo pegará ese número de veces. |
|``` P ```| pega lo almacenado en el buffer principal antes de la posición del cursor. En caso de ir precedido por un número lo pegará tantas veces como se le indique. |
|``` r ```| remplaza elcarácter ubicado en la posición actual del cursor. |
|``` R ```| sobreescribe los carácteres escritos a partir de la posición del cursor. |
|``` s ```| sustituye el carácter bajo el cursor y entra al modo inserción. En caso de ir precedido por un número, eliminará tantos carácteres como se le indique. |
|``` S ```| sustituye la línea completa en la que está ubicada el cursor. En caso de ir precedido por un número, eliminará tantas líneas como se le indique. |
|``` J ```| une la línea actual y la siguiente(o siguientes en caso de ir precedido por un número) y las une en una sola. | 
|``` ~ ```| alterna entre mayúsculas y minúsculas en el carácter sobre el que este posicionado el cursor. |
|``` ctrl-a ```| Aumenta un número bajo el cursor. |
|``` ctrl-x ```| Disminuye un número bajo el cursor. |
|``` . ```| repite el último comando ejecutado. |

# Comandos combinados



# Macros 


