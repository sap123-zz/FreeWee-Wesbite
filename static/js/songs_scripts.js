var client_id = 'eef823eb72081eccc8684bc619021062';
var SearchSong;   //function to search song
var ClearList;    // function to clear previous json_objects
var SteamSong;    // function to stream song
var DownloadSong; // function to download song 
var playpause = false ; // var to set play pause button
SC.initialize({
  client_id: client_id
});

$(document).ready(function() {
  $(".footer").hide();
  var json_object = {};
  var json_array  = [];
  var length = 0;
  ClearList = function(){
    json_object = {};
    json_array  = []
    length      = 0;
    $("#songTable tr").remove();
  }
  SearchSong = function(input){
    SC.get('/tracks',{
      q: input 
    }).then(function(tracks){
      length = tracks.length;
      for(var i in tracks){
        var items = tracks[i];
        json_array.push({
          "id"             : items.id,
          "title"          : items.title,
          "stream_url"     : items.stream_url,
        });
      }
      json_object.json_array = json_array;        // json object to store json array
      for(var i=0;i<length;i++){
        var string = json_object['json_array'][i].title.substring(0,25) + '...';
        var html = "<tr>" +
          "<td><button onclick='SongClick(this)' class='transparentButton'><span class='glyphicon glyphicon-play' id='track"+ i +"'></span>"+ '&nbsp;' +"</button></td>" 
          + "<td>" + string + "<span>&nbsp;</span></td>" +
          "<td><button class='transparentButton' onClick='Download(this)' data-toggle='modal' data-target='#myModal'><span class='glyphicon glyphicon-download' id='downloadSong'></span></button></td>" +
          "</tr>";
        $("#songTable > tbody:last-child").append(html);
      }
    }); 
  } // end of SearchSong()

  StreamSong = function(rowNo){
    var title = json_object['json_array'][rowNo].title ;
    var stream_url = json_object['json_array'][rowNo].stream_url + '?client_id=eef823eb72081eccc8684bc619021062';
    playpause = true;
    $(".footer").show();
    $(".back").text(title);
    playSong(stream_url); 
  }

  DownloadSong = function(rowNo){
    var title = json_object['json_array'][rowNo].title ;
    var stream_url = json_object['json_array'][rowNo].stream_url + '?client_id=eef823eb72081eccc8684bc619021062';
    SendSongStreamUrl(stream_url, title);
  }

}); // end of document.ready()


$("#songNameInput").keyup(function(){
  ClearList();
  var value = $("#songNameInput").val();
  if (value.length == 0){
    //nothing in search bar
  }
  else{
    SearchSong(value);
  }
});

function SongClick(element){
  var rowNo = element.parentNode.parentNode.rowIndex;
  StreamSong(rowNo);
}

function Download(element){
  var rowNo = element.parentNode.parentNode.rowIndex;
  DownloadSong(rowNo);
}

var streamurl = null; 
var sound = new Audio();
function playSong(stream_url){
  if(playpause){
    //play song
    $("#pbar").css('width','0%');
    sound.src = stream_url;
    sound.play();
    streamurl = stream_url;
    sound.addEventListener("timeupdate",function(){
      if(sound.currentTime > 0){
        value = (sound.currentTime/sound.duration)*100;
        $("#startTime").text(secToTime(sound.currentTime));
        $("#endTime").text(secToTime(sound.duration));
      }
      $("#pbar").css('width',value +'%');
    });
  }else{
    //pause song
    sound.pause();
  }
}

function play_pauseSong(){
  if($("#playpauseButton").hasClass('glyphicon-play')){
    // make it stop button
    $("#playpauseButton").removeClass('glyphicon-play').addClass('glyphicon-pause');
  }else{
    // make it play button
    $("#playpauseButton").removeClass('glyphicon-pause').addClass('glyphicon-play');
  }
  if (!playpause){
    // pause function is activated. start song
    playpause = true;
    sound.play();
  }else{
    playpause = false ;
    playSong(streamurl);
  }
}

function stopSong(){
  sound.pause();
  sound.currentTime = 0;
  $("#pbar").css('width','0%');
}

function SendSongStreamUrl(url, title){

  //javascript code to support .click() function in firefox 
  HTMLElement.prototype.click = function() {
    var evt = this.ownerDocument.createEvent('MouseEvents');
    evt.initMouseEvent('click', true, true, this.ownerDocument.defaultView, 1, 0, 0, 0, 0, false, false, false, false, 0, null);
    this.dispatchEvent(evt);
  }

  var jsonData = {'title':title,'url':url}
  var url     = "download/songs/v1?urlvalue=" + encodeURIComponent(JSON.stringify(jsonData));
  var link    = document.createElement("a");
  link.href   = url;
  link.id     = "downloadLink";
  link.click();
  $(".modal").modal('hide');
}

function CloseModal(){
  console.log('hidden')
  $(".modal").modal('hide');
}
