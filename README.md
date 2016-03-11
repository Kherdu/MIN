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

Como según el algoritmo de creación de datos una categoría va a tener siempre un mínimo del 70% de los artículos adquiridos por el usuario, suponiendo que coincidan la categoría dominante de dos usuarios habrá un mínimo posible de coincidencia del 40%, por lo que hemos considerado razonable aumentarlo al 60% para asegurarnos de que sus gustos sean más similares. Este valor es subjetivo y esté sujeto a cambios dependiendo de la futura experimentación.
