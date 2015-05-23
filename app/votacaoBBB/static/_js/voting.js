var participantSelected = 0;

/*
 * Alteracao da borda da imagem selecionada
 */
var mouseOverSelect = function(id){
	if (id === 'photo1'){
		document.getElementById('photo1').classList.add('photo_hover');
		document.getElementById('photo2').classList.remove('photo_hover');
		participantSelected = 1;
	} else if (id === 'photo2'){
		document.getElementById('photo2').classList.add('photo_hover');
		document.getElementById('photo1').classList.remove('photo_hover');
		participantSelected = 2;
	}

};

/*
 * Votacao
 */
var voting = function(){
	xmlhttp = new XMLHttpRequest();
	xmlhttp.onreadystatechange=function(){
		if (xmlhttp.readyState==4 && xmlhttp.status==200){
			response = JSON.parse(xmlhttp.responseText);
			if (typeof(response[0]['id']) == undefined){
				document.getElementById("buttom").innerHTML="Erro";
			}
			window.location = '/results';
		}
	}
	xmlhttp.open("GET", "/vote/"+participantSelected, true);
	//xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
	xmlhttp.send();
};

var onSubmitForm = function(){
	document.vote.action = "/vote/"+participantSelected;
	return true;
};

/*
 * Definicao dos listeners da pagina
 */
window.onload = function(){
	document.getElementById('photo1').addEventListener('mouseover', photo1Listener = function(){ mouseOverSelect('photo1'); }, true );
	document.getElementById('photo2').addEventListener('mouseover', photo2Listener = function(){ mouseOverSelect('photo2'); }, true );
}