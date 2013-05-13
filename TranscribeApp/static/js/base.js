
$(document).ready(function(){});
jQuery.toggleLogin = function()
{
	$("#auth").css("display", "none");
	$("#login-form").fadeIn(function(){$("side-username").focus()});
	return false;
}


	
