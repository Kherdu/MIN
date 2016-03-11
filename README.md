# Práctica 1: Minería de datos y el paradigma Big Data
# Sistema de recomendación


* Alonso Fernández, Jorge
* Caturla Torrecilla, Rafael
* Slavi Marinov, Robert


## Distribución de datos

Hemos decidido realizar nuestro sistema de recomendación sobre un pool de datos de entrenamiento con 1000 usuarios y entre 100 y 120 items comprados por usuario.
Los productos están divididos en 10 categorías de 100 productos cada una.
Esta cantidad de datos debería ser suficiente para comprobar si un algoritmo de recomendación sencillo como el que vamos a implementar es más o menos adecuado.

Para que los productos sean coherentes con la situación queremos representar,  hemos decidido realizar un algoritmo de creación de datos y no simplemente rellenar con datos aleatorios, para que sea lo más similar posible a una situación real, en la que un usuario compra cosas de una o varias (pocas) categorías la mayoría de productos y alguno suelto en otras categorías de vez en cuando.

##Algoritmo de creación de datos

El algoritmo de creación de datos diseñado rellena las categorías eligiendo en primera instancia eligiendo la categoría dominante, es decir, en la que compra la mayoría de los productos, del usuario, en la cual situará entre un 70 y un 85 de las compras decidido de forma aleatoria, una vez hecho esto, y también de forma aleatoria situará el resto de los productos en otras categorías.

## Algoritmo de recomendación

Para el algoritmo de recomendación hemos usado la función de similitud de Jaccard modificada, comparando las categorías, pero solo aquellas en las que tengan al menos un artículo; para que dos usuarios sean elegibles para recomendaciones mutuas, su ratio en la función de jackard tiene que ser al menos de 0.6 en la categoría dominante.

Como según el algoritmo de creación de datos una categoría va a tener siempre un mínimo del 70% de los artículos adquiridos por el usuario, suponiendo que coincidan la categoría dominante de dos usuarios habría un mínimo posible de coincidencia del 40%, por lo que hemos considerado razonable aumentarlo al 60% para asegurarnos de que sus gustos sean más similares. Este valor es subjetivo y está sujeto a cambios dependiendo de la futura experimentación.

## Preguntas abiertas

### ¿Qué otras distancias se pueden utilizar?

User-to-user, cluster, item-to-item con similaridad de items.

### ¿Cómo evaluamos si el sistema funciona bien?

Hemos programado el script de forma que sea fácil hacer pruebas a pequeña escala y que  los resultados puedan ser interpretados a simple vista tanto para pequeños como para grandes casos de prueba. Para ello hemos tenido que adaptar un poco el método item-to-item añadiendo algunas cualidades del clustering como son las categorías de los productos.

 Al no contar con la abstracción del producto, las salidas serían difíciles de interpretar y más demostrar si son correctas o no, por tanto, hemos aplicado item-to-item a usuarios que tengan compras de la misma categoría  y en las que no tienen productos evitamos hacer cálculos, de esta forma se hacen menos cálculos además que el la salida es más intuitiva ya que podemos consultar el número de productos que tienen los usuarios en las categorías y hasta qué punto se asemejan los gustos de los usuarios entre ellos. Es decir Item-to-Item aplicado a categorías para hacer más fácil el interpretado de datos (menos datos).

### ¿Cómo se generan casos de prueba?

En el apartado de arriba explica cómo se generan los casos de prueba pero no se da la razón.

Nuestra intención era generar los datos lo más aleatorios posible, tanto la para elegir la categoría predominante del usuario, como para elegir las categorías de las cuales  ha adquirido productos, el nº de productos por categoría, al igual que el nº total de productos adquiridos.

Lo único que establecemos de forma fija son el nº de usuarios, nº de categorías y el tamaño de cada categoría, la relación entre usuarios y productos es 10 a 1.

### ¿Cómo se comparan diferentes opciones?

Modificando las distancias a medir, con estos mismos datos se podrían medir a parte de la similitud entre usuarios que es más o menos lo que queremos conseguir, la similaridad entre productos y categorías.

### ¿Cómo se modifica el sistema para incluir otros parámetros: “likes”, “comentarios”, … ?

Se podría modificar de varias formas, la más intuitiva sería añadir tablas al usuario para cada nuevo parámetro que se quiera tener en cuenta y hacer los mismos cálculos que con los productos, al final sobreponer todos los parámetros con diferentes pesos cada uno (No debería contar lo mismo un “like” que un comentario si ha comprado el producto) para obtener la relación entre productos.

### ¿Cómo se puede escalar el algoritmo para tratar millones de entradas?

Dejando de lado la plataforma sobre la que se llevarían los cálculos (sistemas/procesos paralelos, cloud ...), el algoritmos podría filtrar datos ya conocidos sobre usuarios o productos y evitar hacer cálculos innecesarios, parecido a lo que hacemos nosotros.

