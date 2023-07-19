# Proyecto Final Coderhouse
### Por: Daniel Alfredo Herbonniere Delacierte.


## Indice
* [Informacion General](#informacion-general)
    * [Video demostrativo](#video-demostrativo)
* [Funcionamiento](#funcionamiento)
    * [Usuario](#usuario)
    * [Publicación](#publicacion)
    * [Acount](#acount)

***

## Informacion General

Esta es un apliación web con la temática de blog para la creación de poemas. Funciona a través del manejo de usuarios, estará disponible el registro e inicio de sesión donde se solicitarán datos como nombre, correo y contraseña. Luego del logueo, se tiene acceso a la creación del contenido, que en este caso sería el poema a publicar. Dicho poema dispondrá de un formulario donde se podrán ingresar datos como el autor, título, contenido, portada y fecha de publicación. 

#### [Video demostrativo](https://drive.google.com/file/d/1myHitSmoRj-voLp1vlgSIA_5elmjlm8z/view?usp=sharing)
***

## Funcionamiento

### Vista General

El proyecto posee una pantalla de inicio o _Home_ dando un mensaje de bienvenida. Al no estar logueado solo se tendrá acceso a las vistas `login`, `registro`, y `poemas`, siendo esta útlima la visualización de la lista, pero limitada a las opciones de _ver más_ y a la búsqueda del contenido. Las demás opciones o vistas dentro de ella como _crear, modificar, eliminar_ y `acount` estarán disponibles solo con el inicio de sesión.

En este punto, el proyecto se puede divir en tres partes:

* [Usuario](#usuario)
* [Publicacion](#publicacion)
* [Acount](#acount)

## Usuario

La aplicación `usuario` tiene como finalidad gestionar todo el funcionamiento relacionado al usuario dentro del proyecto, el manejo de los datos en la base de datos, así como la limitación de los accesos. Consta de seis (6) templates que definen su funcionamiento:

* `registro`
* `login`
* `logout`
* `perfil`
* `edicion`
* `edicion_pass`



## Publicacion

Se le llama publicacion a la aplicacion `inicio`  ya que está enfocada principalmente en la gestión de la información relacionada con el contenido a visualizar o modificar en el proyecto. En este caso dicha información será dependiente de que el usuario este logueado o no. Esta aplicación consta de seis (6) templates que definen su funcionamiento:

* `inicio`
* `poemas`
* `crear_poema`
* `detale_poema`
* `modificar_poema`
* `eliminarpoema`

## Acount

Esta sección solo está representada por una vista, sin embargo para su visualización el usuario deberá esta logueado. En ella se encuentra la información relacionada con el creador del proyecto.