$(window).ready(function(){
	var documentElem = $(window);
	var	lastScrollTop = 0;
	$(window).on('scroll', function(){
		var currentScrollTop = $(this).scrollTop();

		//scroll down
		if( currentScrollTop > lastScrollTop){
			$('.navbar').addClass('nav-down');

		} 
		//scroll up
		else {
			$('.navbar').removeClass('nav-down');
		}
		lastScrollTop = currentScrollTop;
	});
});


$(".profile_nav li a").click(function(e) {

  // remove classes from all
  $(".profile_nav li a").removeClass("active");
  // add class to the one we clicked
  $(this).addClass("active");
});

$(".main_nav li a").click(function() {
  // remove classes from all
  $(".main_nav li a").removeClass("active");
  // add class to the one we clicked
  $(this).addClass("active");
});

/*$(document).ready(function() {
    $(document).on('click', '.profile_nav li a', function (e) {
        $(this).parent().addClass('active').siblings().removeClass('active');
    });
});*/
