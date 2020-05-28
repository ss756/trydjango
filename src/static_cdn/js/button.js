$('.text-wrap .text').hover(function(){
	TweenMax.to($('.main-btn_wrapper'), 0.5, {opacity: 1, display: 'block', position: 'absolute', scale: 1, ease: Elastic.easeOut.config(1, 0.75)}),
	TweenMax.to($('.line'), 0.5, {css: { scaleY: 0.6, transformOrigin: "center center" }, ease: Expo.easeOut})},

	function(){
		TweenMax.to($('.main-btn_wrapper'), 0.5, {opacity: 0, display: 'none', scale: 0, ease: Elastic.easeOut.config(1, 0.75)}),
		TweenMax.to($('.line'), 0.5, {css: { scaleY: 1, transformOrigin: "center center" }, ease: Expo.easeOut})
});

