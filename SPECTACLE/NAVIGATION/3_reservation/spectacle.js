// PAGE PROGRAMMATION ou ÉVÈNEMENTS

filtrerPar("toute")
function filtrerPar(c) {
  var x, i;
  x = document.getElementsByClassName("colonne");
  if (c == "toute") c = "";
  // Add the "show" class (display:block) to the filtered elements, and remove the "show" class from the elements that are not selected
  for (i = 0; i < x.length; i++) {
    w3RemoveClass(x[i], "montrer");
    if (x[i].className.indexOf(c) > -1) w3AddClass(x[i], "montrer");
  }
}

// On montre les éléments filtrés
function w3AddClass(element, name) {
  var i, arr1, arr2;
  arr1 = element.className.split(" ");
  arr2 = name.split(" ");
  for (i = 0; i < arr2.length; i++) {
    if (arr1.indexOf(arr2[i]) == -1) {
      element.className += " " + arr2[i];
    }
  }
}

// On cache les éléments qui ne sont pas sélectionnés
function w3RemoveClass(element, name) {
  var i, arr1, arr2;
  arr1 = element.className.split(" ");
  arr2 = name.split(" ");
  for (i = 0; i < arr2.length; i++) {
    while (arr1.indexOf(arr2[i]) > -1) {
      arr1.splice(arr1.indexOf(arr2[i]), 1);
    }
  }
  element.className = arr1.join(" ");
}

// On ajoute la classe "actif" sur le bouton de control
var btnContainer = document.getElementById("conteneur-bouton");
var btns = btnContainer.getElementsByClassName("btn");
for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function() {
    var current = document.getElementsByClassName("actif");
    current[0].className = current[0].className.replace(" actif", "");
    this.className += " actif";
  });
}