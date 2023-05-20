import 'dart:math';
void main() {
  //a
  List <int> lista1 = [14,2,5,3,9];
  print('la lista 1 es: $lista1');
  //b
  //No pude hacer una lista ingresada por teclado asi que hice una aleatoria para poder seguir pipipi
  List <int> lista2 = List.generate(5, (_) => Random().nextInt(11));
  print('la lista 2 es: $lista2');

  /////INTENTO DE LISTA POR TECLADO///////
  /*int elementos = 5;
  List <int> lista2 = [];
  for (int numero in elementos) {
    print('ingrese un elemento de la lista:');
    int elemento = int.parse(stdin.readLineSync()!);
    lista2.add(elemento);
  }*/
  
  //c ,,,, no sé crear listas aleatorias de numeros negativos :(
  //cree una lista de aleatorios del 0 al 10 para poder seguir con resto
  List <int> listaAleatoria = List.generate(5, (_) => Random().nextInt(11));
  print('la lista aleatoriaa es: $listaAleatoria');
  //d
  List <int> listaResta = [];
  for (int i = 0; i < lista1.length; i++) {
    int elemento = lista1[i] - lista2[i];
    listaResta.add(elemento);
  }
  print('la lista resta es: $listaResta');

  List <int> listaSuma = [];
  for (int i = 0; i < lista1.length; i++) {
    int elemento = listaResta[i] + listaAleatoria[i];
    listaSuma.add(elemento);
  }
  print('la lista suma es: $listaSuma');

  //e
  listaSuma.insert(0, 17);
  listaSuma.insert(1, 24);
  print('la lista con elementos agregados es: $listaSuma');

  //f
  // me quedo ascendente pq no me acuerdo de la descendente jajas
  listaSuma.sort();
  print('la lista descendente es: $listaSuma');

}


