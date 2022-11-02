// search bar - fetch info from imdb + rottentomatoes -> show info
// show output
function movieResult(){ 
  var result = 1;
  var imdb = document.getElementById("imdbRate").value;
  var rotten = document.getElementById("rottenRate").value;
  result = (imdb * 0.5) + (rotten * 0.5);
  document.getElementById("op").innerHTML = result;
}
