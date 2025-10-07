Prueba para practicar con diccionarios

Definimos un diccionario "dicc" mediante la instruccion "dict()", de momento vacio. Mostramos un menu donde se pueden agregar elementos, eliminarlos y listar el contenido.

Al agregar, empleamos "setdefault()" para prevenir si el elemento ya existe, en cuyo caso no hara nada.

Al eliminar, empleamos "pop" mostrando un texto por defecto en el caso de que no encuentre el elemento a eliminar, de forma que la comprobacion y la eliminacion la estamos realizand ocon una sola instruccion.

Al listar, primero mostramos el contenido completo del diccionario y luego repetimos el listado pero de una forma mas controlada; para distinguir cada clave de su valor trasnformamos el diccionaro en una lista de tuplas, mediante el metodo "items()", de forma que en cada tupla obtenemos
la posicion "[0]" que sera la clave y la posicion [1] que sera el valor.
