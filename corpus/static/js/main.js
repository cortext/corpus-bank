$(document).ready(function(){
	
//	$(document).bind("mouseup", get_selection)
	
	$("#search").submit(function(e){
		e.preventDefault();

		var current_corpus = document.location.pathname.split('/')[2];

		var path = "/corpus/" + current_corpus;

		if($("#search input").val() != ""){
			path += "/search/"+ $("#search input").val();
		}

		console.log("push:" + path);

		window.location.href = path;
	});
	
	$("#search input").keyup(function(e){
		e.preventDefault();

		var current_corpus = document.location.pathname.split('/')[2];
		var path = "/corpus/" + current_corpus + "/search/"+ $("#search input").val() + "/count";

		console.log("push:" + path);
		
		$("#num_results").html("...")
		$("#num_results").load(escape(path));
	});
	
	
});

function get_selection(){
	var t = '';
	if(window.getSelection){
		t = window.getSelection();
	} else if(document.getSelection){
		t = document.getSelection();
	}else if(document.selection){
		t = document.selection.createRange().text;
	}

	console.log(t);

	return t;
}