function handleClicks() {

  window.onclick = function(event) {
    if (event.target.classList.contains("multi-button")) {
      refRequest = event.target.parentNode;

      var classes = refRequest.className.split(" ");
      var i = classes.indexOf("test");

      if (event.target.classList.contains("accept")) {
        var classes;
        var i;

        classes = event.target.className.split(" ");
        i = classes.indexOf("accept");
        classes.splice(i, 1);
        classes.push("complete");
        event.target.className = classes.join(" ");


        classes = event.target.parentNode.getElementsByClassName("deny")[0].className.split(" ");
        i = classes.indexOf("deny");
        classes.splice(i, 1);
        classes.push("print");
        event.target.parentNode.getElementsByClassName("deny")[0].className = classes.join(" ");
      }

      else if (event.target.classList.contains("deny")) {
        event.target.parentNode.parentNode.remove();
      }

      else if (event.target.classList.contains("complete")) {
        event.target.parentNode.parentNode.remove();
      }
    }
  }
}
