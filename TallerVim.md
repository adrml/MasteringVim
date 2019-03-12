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
|``` ctrl-d ```| Desplaza hacia abajo la mitad de la pantalla, |  
|``` ctrl-u ```| Desplaza hacia arriba la mitad de la pantalla, |  
|``` ctrl-f ```| Desplaza hacia abajo una pantalla, |  
|``` ctrl-b ```| Desplaza hacia arriba una pantalla, |  
|``` ctrl-y ```| Desplaza hacia abajo una línea, |  
|``` ctrl-e ```| Desplaza hacia arriba una línea, |  
|```M``` | Mueve el cursor al centro de la página. |
|```H``` | Mueve el cursor al inicio de la página. |
|```L``` | Mueve el cursor al final de la página. |
|``` W ```| Mueve el cursor hasta la siguiente palabra. (Delimitado por espacios.) |
|``` w ```| Mueve el cursor hasta la siguiente palabra. (Delimitado por los carácteres no alfanuméricos.) |
|``` B ```| Mueve el cursor hasta la palabra anterior. (Delimitado por espacios.) |
|``` b ```| Mueve el cursor hasta la palabra anterior. (Delimitado por los carácteres no alfanuméricos.) |
|``` E ```| Mueve el cursor hasta el final de la palabra. (Delimitado por los espacios.) |
|``` e ```| Mueve el cursor hasta el final de la palabra. (Delimitado por los carácteres no alfanuméricos.) |
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
|``` m ```| Marca la línea donde esta ubicado el cursor. Es necesario, identificarlo con una letra. (Ejemplo: Con **ma**, marcaríamos la línea actual con la letra a.) |
|``` ' ```| Mueve el cursor a la línea marcada que le hemos indicado. (Ejemplo: Con **'a**, nos moveríamos a la línea que hemos marcado previamente con esa letra.) |
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
|``` Esc ```| Sale del modo inserción. (También se utiliza para finalizar otros modos, como el Visual.) |
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

# Comandos combinados

En algunos casos, como con los comandos ```c```, ```d``` o ```f``` una vez ejecutados, vim se queda esperando a una segunda acción, como podría ser, la afectación de la línea entera, o utilizando ciertos patrones que se mostrarán a continuación.

| Keystrokes | Acción |
| ---------- | -------| 
|``` *$  ```| Trabaja con lo marcado desde el cursor hasta el final de la línea actual. |
|``` *w ```| Trabaja con la palabra a partir del cursor. (Sigue las mismas reglas que "w" y "W".) |
|``` *- ```| Trabaja con la línea actual y la anterior, y entra en el modo inserción. |
|``` *fx ```| Trabaja  con lo seleccionado a partir de el cursor hasta la próxima aparición de la letra "x", y entra en el modo inserción. |
|``` *'x ```| Trabaja  con lo seleccionado a partir de el cursor hasta la línea marcada con el identificador "x", y entra en el modo inserción. |
|``` 'a*'b ```| Trabaja  con lo seleccionado a partir de la línea marcada con el identificador "a" hasta la línea marcada con el identificador "b", y entra en el modo inserción. |
|``` */x ```| Trabaja  con lo seleccionado a partir de el cursor hasta la próxima aparición de "x", sin afectar a este, y entra en el modo inserción. |

> Donde el  * se sustituiría por la acción a realizar.

# Macros 

En Vim una macro es un conjunto de comandos que pueden realizarse mediante un comando y/o una combinación de teclas.

Para grabar nuestra propia macro tendremos que hacer uso de la tecla **Q** , seguido del caracter al que queremos asignar la macro que vamos a grabar.

Por ejemplo:```Qa``` 

Empezará a grabar nuestras acciones en la tecla.A partir de aqui tenemos que ejecutar todos los comandos que queramos que registre la macro 
para ejecutarlos en bloque posteriormente
