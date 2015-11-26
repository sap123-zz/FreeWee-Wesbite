//this file is to hold functions that has calculations or manuplation of results

function secToTime(seconds){
  var min  = Math.floor(seconds/60);
  var sec  = Math.floor(seconds % 60);
  var time = ("0" + min).slice(-2) + ":" + ("0"+ sec).slice(-2);
  return time;
}
