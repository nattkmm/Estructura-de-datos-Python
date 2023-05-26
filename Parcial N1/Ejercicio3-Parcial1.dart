import 'dart:io';
import 'dart:math';
void main() {
  List <int> lista1 = List.generate(10, (index) => Random().nextInt(20));
  print(lista1);

  List <int> lista2 = List.generate(10, (index) => Random().nextInt(20));
  print(lista2);

  int elementos = 5;
  List <int> lista3 = [];
  for (int i = 0; i < elementos; i++) {
    print('ingrese un elemento de la lista:');
    int elemento = int.parse(stdin.readLineSync()!);
    lista3.add(elemento);
  }

  List <int> listaSuma = lista1 + lista2 + lista3 ;
  print(listaSuma);

  listaSuma.sort();
  print(listaSuma);
  
}