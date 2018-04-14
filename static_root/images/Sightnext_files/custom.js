$(window).ready(function(){
	var documentElem = $(window);
	var	lastScrollTop = 0;
	var height = $('.navbar').outerHeight()-0.031;
	$(window).on('scroll', function(){
		var currentScrollTop = $(this).scrollTop();
		if (lastScrollTop>=height){
			
			if( currentScrollTop > lastScrollTop){
			$('.navbar').addClass('nav-fix');
			$('.navbar').addClass('nav-down');
			
			

			} 
		//scroll up
			else {
				$('.navbar').removeClass('nav-down');
				
				
			}
			
		}
		else{
			$('.navbar').removeClass('nav-fix');
		}
		lastScrollTop = currentScrollTop;
		

		//scroll down
		// if( currentScrollTop > lastScrollTop){
		// 	$('.navbar').addClass('nav-down');

		// } 
		// //scroll up
		// else {
		// 	$('.navbar').removeClass('nav-down');
		// }
		// lastScrollTop = currentScrollTop;
		// alert('hey')
		// alert(lastScrollTop)
	});

});



/*$(document).ready(function() {
    $(document).on('click', '.profile_nav li a', function (e) {
        $(this).parent().addClass('active').siblings().removeClass('active');
    });
});*/

