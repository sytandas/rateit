// calcution of the value of the movie
function movieResult() {
  var result = 1;
  var imdb = document.getElementById("imdbRating").value;
  var rotten = document.getElementById("rottenRating").value;
  result = (imdb * 0.5) + (rotten * 0.5);
  document.getElementById("op").innerHTML = result;
}
