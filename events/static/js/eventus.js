$(document).on("ready", main);

function main(){

	$.ajaxSetup({
		beforeSend: function(xhr, settings) {
			if(settings.type == "POST"){
				xhr.setRequestHeader("X-CSRFToken", 
					$('[name="csrfmiddlewaretoken"]').val());
			}
		}
	});

	$("#camentar").on("click", enviarComentario);
}

function enviarComentario(){
	var comentario = $("#comentario").val();

	if(comentario != ""){

		$.post("comentario/guardar/", { comentarioEnviar:comentario, 
			eventoId:$("#comentario").data('id')
		}, actualizarComentario);
	}
}

function actualizarComentario(data){
	var comentario = $("#comentario").val("");

	var ul = $("#comentario-ul");
	ul.html("");
	$.each(data, function (i, e){
		$('<li class="item card">').html('<img class="item-img" src='+e.avatar+'/>' 
			+ '<p class="item-p">' + e.email + ' - ' 
			+ e.comentario  +'</p>').appendTo(ul);
	});
}

