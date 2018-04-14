if (self.CavalryLogger) { CavalryLogger.start_js(["aBsrT"]); }

__d("VideoPlayerLoggerSource",[],(function a(b,c,d,e,f,g){f.exports=Object.freeze({ADS:"ads",ANIMATED_IMAGE_SHARE:"animated_image_share",ASSET:"asset",BROADCAST_REQUEST_ATTACHMENT:"broadcast_request_attachment",CAMERA_POST:"camera_post",CHAINED:"chained",CHAINED_SUGGESTION:"chained_suggestion",CHANNEL:"channel",CONTINUE_WATCHING_RECOMMENDATION:"continue_watching_recommendation",EMBEDDED:"embedded",EMBEDDED_PAGE_PLUGIN:"embedded_page_plugin",EMBEDDED_VIDEO:"embedded_video",EMBEDDED_VIDEO_FROM_UFI:"embedded_video_from_ufi",EMBEDDED_VIDEO_PREVIEW:"embedded_video_preview",GAMEROOM_LIVE_VIDEO_HERO_BANNER:"gameroom_live_video_hero_banner",GAMEROOM_LIVE_VIDEO_TAB:"gameroom_live_video_tab",GAMEROOM_LIVE_VIDEO_THUMBNAIL:"gameroom_live_video_thumbnail",GAMES_VIDEO_HOME:"games_video_home",GAMES_VIDEO_HOME_HERO:"games_video_home_hero",GAMES_VIDEO_SINGLE_GAME:"games_video_single_game",GROUP_LIVE_VIDEO_MODULE:"group_live_video_module",HTML5:"html5",INLINE:"inline",INSIGHTS:"insights",ISSUES_MODULE:"issues_module",LIVE_BEEPER:"live_beeper",LIVE_CONTROL_PANEL:"live_control_panel",LIVE_MAP:"live_map",LIVE_MAP_LISTVIEW:"live_map_listview",LIVE_MAP_SIDEBAR:"live_map_sidebar",LIVE_MAP_TOOLTIP:"live_map_tooltip",LIVE_MAP_TOOLTIP_FROM_LISTVIEW:"live_map_tooltip_from_listview",LIVE_MAP_TOOLTIP_FROM_MAP:"live_map_tooltip_from_map",LIVE_MAP_TOOLTIP_FROM_WEBGL:"live_map_tooltip_from_webgl",LIVE_VIDEO_BROADCAST:"live_video_broadcast",LIVE_VIDEO_PREVIEW:"live_video_preview",LIVING_ROOM:"living_room",LOOKBACK:"lookback",MEDIA_COLLAGE:"media_collage",MESSAGING:"messaging",MISC:"misc",MOBILE:"mobile",OFFERS_DETAIL:"offers_detail",PAGE_LIVE_VIDEO_MODULE:"page_live_video_module",PAGES_FINCH_MAIN_VIDEO:"pages_finch_main_video",PAGES_FINCH_THUMBNAIL_VIDEO:"pages_finch_thumbnail_video",PAGES_FINCH_TRAILER:"pages_finch_trailer",PAGES_VIDEO_SET:"pages_video_set",PERMALINK:"permalink",PROFILE_VIDEO:"profile_video",PROFILE_VIDEO_HOVERCARD:"profile_video_hovercard",PROFILE_VIDEO_THUMB:"profile_video_thumb",REPORT_FLOW:"report_flow",REVIEW:"review",SEARCH_LIVE_VIDEO_MODULE:"search_live_video_module",SLIDESHOW:"slideshow",SNOWLIFT:"snowlift",SRT_REVIEW:"srt_review",TAHOE:"tahoe",TRAILER_OG_ATTACHMENT:"trailer_og_attachment",TRAILER_TIMELINE_COLLECTIONS:"trailer_timeline_collections",TRAILER_TIMELINE_UNIT:"trailer_timeline_unit",TV:"tv",USER_VIDEO_TAB:"user_video_tab",VIDEO_COPYRIGHT_PREVIEW:"video_copyright_preview",VIDEO_HOME_INLINE:"video_home_inline",VIDEO_INLINE_CHAINING:"video_inline_chaining",VIDEOHUB_FEATURED:"videohub_featured",VIDEOHUB_LIVE:"videohub_live",VIDEOHUB_PLAYLIST:"videohub_playlist",WATCH_SCROLL:"watch_scroll",LIVE_AUTOPLAY_WATCH_AND_SCROLL:"live_autoplay_watch_and_scroll"})}),null);
__d("VideoAutoplayControllerAbortLoadingHelper",["invariant","VideoPlayerLoggerSource","VideoPlayerExperiments","VideoPlayerAbortLoadingExperiment","getViewportDimensions","Set","Map"],(function a(b,c,d,e,f,g,h){__p&&__p();function i(){"use strict";this.$VideoAutoplayControllerAbortLoadingHelper1=new(c("Set"))();this.$VideoAutoplayControllerAbortLoadingHelper2=new(c("Map"))()}i.prototype.maybeAbortLoading=function(){"use strict";__p&&__p();for(var j=this.$VideoAutoplayControllerAbortLoadingHelper1,k=Array.isArray(j),l=0,j=k?j:j[typeof Symbol==="function"?Symbol.iterator:"@@iterator"]();;){var m;if(k){if(l>=j.length)break;m=j[l++]}else{l=j.next();if(l.done)break;m=l.value}var n=m,o=c("VideoPlayerExperiments").deferWhichVideoToAbortLoadingDecisioningLogic,p=n.getVideoPlayerController(),q=p?p.isLiveVideo():null;if(q!==null&&(o==="vod"&&q||o==="live"&&!q))continue;if(!n.isState("playing")&&typeof n.abortLoading==="function"&&i.shouldAbortLoadingVideoUnit(n))if(c("VideoPlayerExperiments").abortLoadingHelperNegativeYAbortLoading)this.$VideoAutoplayControllerAbortLoadingHelper3(n);else this.$VideoAutoplayControllerAbortLoadingHelper4(n);else if(c("VideoPlayerExperiments").abortLoadingHelperNegativeYAbortLoading&&n.isState("playing")){var r=this.$VideoAutoplayControllerAbortLoadingHelper2.get(n);!!r||h(0);if(r&&r.abortedLoading)r.abortedLoading=false}}};i.prototype.$VideoAutoplayControllerAbortLoadingHelper3=function(j){"use strict";__p&&__p();if(c("VideoPlayerExperiments").abortLoadingHelperBoundedReloading){var k=c("getViewportDimensions")().height/-2;if(j.getDistanceToViewport()<c("VideoPlayerExperiments").abortedLoadingPixelBoundary+k&&!j.isVisible())this.$VideoAutoplayControllerAbortLoadingHelper5(j);else if(j.getDistanceToViewport()>c("VideoPlayerExperiments").reloadingPixelBoundary+k)this.$VideoAutoplayControllerAbortLoadingHelper6(j)}else if(j.getDistanceToViewport()<0&&!j.isVisible())this.$VideoAutoplayControllerAbortLoadingHelper5(j)};i.prototype.addVideoUnit=function(j){"use strict";if(!this.$VideoAutoplayControllerAbortLoadingHelper1.has(j)){this.$VideoAutoplayControllerAbortLoadingHelper1.add(j);this.$VideoAutoplayControllerAbortLoadingHelper2.set(j,{y:j.getDistanceToViewport(),timestamp:new Date().valueOf(),v:0,abortedLoading:false})}};i.prototype.removeVideoUnit=function(j){"use strict";this.$VideoAutoplayControllerAbortLoadingHelper1["delete"](j);this.$VideoAutoplayControllerAbortLoadingHelper2["delete"](j)};i.prototype.calculateFutureScrollPosition=function(j){"use strict";var k=j.y1-j.y0,l=j.t1-j.t0,m=k/l,n=m-j.v0,o=n/l,p=j.t,q=o*p*p/2+p*m+j.y1;return{v1:m,a:o,S:q}};i.prototype.preloadClosestVideoUnits=function(j){"use strict";this.$VideoAutoplayControllerAbortLoadingHelper7(j).forEach(function(k){return this.$VideoAutoplayControllerAbortLoadingHelper6(k)}.bind(this))};i.prototype.$VideoAutoplayControllerAbortLoadingHelper7=function(j){"use strict";return Array.from(this.$VideoAutoplayControllerAbortLoadingHelper1).filter(function(k){return k.getDistanceToViewport()>=0}).sort(function(k,l){return k.getDistanceToViewport()-l.getDistanceToViewport()}).slice(0,j)};i.prototype.$VideoAutoplayControllerAbortLoadingHelper6=function(j){"use strict";__p&&__p();var k=this.$VideoAutoplayControllerAbortLoadingHelper2.get(j);!!k||h(0);var l=void 0;if(k){l=k.abortedLoading;k.abortedLoading=false}if(l&&typeof j.preload==="function")j.preload()};i.prototype.$VideoAutoplayControllerAbortLoadingHelper5=function(j){"use strict";__p&&__p();var k=this.$VideoAutoplayControllerAbortLoadingHelper2.get(j);!!k||h(0);var l=void 0;if(k){l=k.abortedLoading;k.abortedLoading=true}if(!l&&typeof j.abortLoading==="function")j.abortLoading()};i.prototype.$VideoAutoplayControllerAbortLoadingHelper4=function(j){"use strict";__p&&__p();var k=c("getViewportDimensions")().height,l=1600,m=k/2,n=m+l,o=-m,p=o-l,q=this.$VideoAutoplayControllerAbortLoadingHelper2.get(j);!!q||h(0);if(!q)return;var r=j.getDistanceToViewport(),s=q.y;q.y=r;var t=new Date().valueOf(),u=q.timestamp;q.timestamp=t;var v=q.v;if(p<=r&&n>=r){if(q.abortedLoading)this.$VideoAutoplayControllerAbortLoadingHelper6(j);return}var w=500,x=this.calculateFutureScrollPosition({y0:s,y1:r,t0:u,t1:t,v0:v,t:w});q.v=x.v1;var y=x.S;if(q.abortedLoading){if(r<p&&y>p||r>n&&y<n)this.$VideoAutoplayControllerAbortLoadingHelper6(j)}else this.$VideoAutoplayControllerAbortLoadingHelper5(j)};i.prototype.$VideoAutoplayControllerAbortLoadingHelper8=function(j){"use strict";var k=j.getVideoPlayerController();return k?k.getVideoPlayerID():null};i.shouldAbortLoadingVideoUnit=function(j){"use strict";__p&&__p();var k=!c("VideoPlayerExperiments").abortLoadingDecisioningLogic,l=true;if(j){if(typeof j.getIsInChannel==="function")l=j.getIsInChannel();if(typeof j.getSource==="function"&&c("VideoPlayerExperiments").abortLoadingDecisioningLogic)k=j.getSource()===c("VideoPlayerLoggerSource").TAHOE;return c("VideoPlayerAbortLoadingExperiment").canAbort&&!l&&!k}return false};f.exports=i}),null);
__d("VideoPlayerReason",[],(function a(b,c,d,e,f,g){f.exports=Object.freeze({AUTOPLAY:"autoplay_initiated",COMMERCIAL_BREAK:"commercial_break",CONNECTION:"host-connection-error",EMBEDDED_VIDEO_API:"embedded_video_api_initiated",FALLBACK_MODE:"fallback_mode",HOVER:"hover",LOOP:"loop_initiated",PAGE_VISIBILITY:"page_visibility_initiated",SEEK:"seek_initiated",SPHERICAL_FALLBACK:"spherical_fallback",SPHERICAL_SWITCH_CANVAS:"spherical_switch_canvas",UNLOADED:"unloaded",USER:"user_initiated",VIDEO_DATA_REPLACED:"video_data_replaced",VIDEO_DATA_SWITCH:"video_data_switch",VIDEO_VISIBILITY:"video_visibility_initiated",VOD_NOT_READY:"vod_not_ready",WARNING_SCREEN_COVER:"warning_screen_cover"})}),null);
__d("VideoAutoplayControllerBase",["Arbiter","DesktopHscrollUnitEventConstants","Event","VideoPlayerExperiments","VideoPlayerAbortLoadingExperiment","VideoAutoplayControllerAbortLoadingHelper","VideoPlayerLoggerSource","VideoPlayerReason","Visibility","destroyOnUnload","SubscriptionsHandler","debounce","throttle","setTimeout","emptyFunction"],(function a(b,c,d,e,f,g){__p&&__p();var h=c("VideoPlayerExperiments").abortLoadingDelay;function i(l,m){var n=[];return function(){var o=Date.now();n.unshift(o);var p=0;while(n[++p]+m>o);n=n.slice(0,p);return n.length<=l}}function j(l,m,n){__p&&__p();var o=null;return function(){__p&&__p();var p;for(var q=arguments.length,r=Array(q),s=0;s<q;s++)r[s]=arguments[s];if(m()){l.apply(undefined,r);return c("emptyFunction").thatReturnsFalse}else if(!o)(function(){var t=c("setTimeout")(function(){o=null;l.apply(undefined,r)},n);o=function u(){if(!o)return false;clearTimeout(t);o=null;return true}})();return o}}function k(l){"use strict";__p&&__p();this.$VideoAutoplayControllerBase8=c("emptyFunction");this.$VideoAutoplayControllerBase9=c("emptyFunction");this.$VideoAutoplayControllerBase3=null;this.$VideoAutoplayControllerBase2=null;this.$VideoAutoplayControllerBase10=[];this.$VideoAutoplayControllerBase1=l;this.$VideoAutoplayControllerBase4=null;this.$VideoAutoplayControllerBase5=new(c("SubscriptionsHandler"))();c("destroyOnUnload")(function(){this.$VideoAutoplayControllerBase10=[];this.$VideoAutoplayControllerBase3=null;if(this.$VideoAutoplayControllerBase4){this.$VideoAutoplayControllerBase4.remove();this.$VideoAutoplayControllerBase4=null}this.$VideoAutoplayControllerBase5.release()}.bind(this));if(c("VideoPlayerExperiments").autoplayMaxCallsPerWindow)this.$VideoAutoplayControllerBase6=j(function(m){var n=this.$VideoAutoplayControllerBase3;if(n)n.playWithoutUnmute(m)}.bind(this),i(c("VideoPlayerExperiments").autoplayMaxCallsPerWindow,c("VideoPlayerExperiments").autoplayThrottleWindow),c("VideoPlayerExperiments").autoplayThrottleDelay);this.$VideoAutoplayControllerBase7=c("emptyFunction").thatReturnsFalse}k.prototype.getVideoUnits=function(){"use strict";return this.$VideoAutoplayControllerBase10};k.prototype.setVideoUnits=function(l){"use strict";this.$VideoAutoplayControllerBase10=l};k.prototype.addVideoUnit=function(l){"use strict";this.$VideoAutoplayControllerBase10.push(l)};k.prototype.removeVideoUnit=function(l){"use strict";var m=this.$VideoAutoplayControllerBase10.findIndex(function(n){return n===l});if(m>-1)this.$VideoAutoplayControllerBase10.splice(m,1)};k.prototype.getPlayingVideoUnit=function(){"use strict";return this.$VideoAutoplayControllerBase3};k.prototype.setPlayingVideoUnit=function(l){"use strict";this.$VideoAutoplayControllerBase3=l;if(this.$VideoAutoplayControllerBase3)this.setupPlayingVideoUnitSubscriptions()};k.prototype.playVideo=function(l,m){"use strict";__p&&__p();if(c("VideoPlayerExperiments").disableAutoplayForInactiveTab&&c("Visibility").isHidden()){this.$VideoAutoplayControllerBase2=l;return}this.setPlayingVideoUnit(l);if(this.$VideoAutoplayControllerBase3){var n=this.$VideoAutoplayControllerBase6;if(n)this.$VideoAutoplayControllerBase7=n.call(this,m);else this.$VideoAutoplayControllerBase3.playWithoutUnmute(m)}};k.prototype.setupPlayingVideoUnitSubscriptions=function(){"use strict";throw new Error("Should be overridden")};k.prototype.addSubscriberVideoUnit=function(){"use strict";if(!this.getVideoUnits().length){this.$VideoAutoplayControllerBase5.addSubscriptions(c("Event").listen(window,"resize",this.updateAutoplay.bind(this)),c("Event").listen(window,"blur",this.$VideoAutoplayControllerBase11.bind(this)),c("Event").listen(window,"focus",this.$VideoAutoplayControllerBase12.bind(this)),c("Visibility").addListener(c("Visibility").HIDDEN,this.$VideoAutoplayControllerBase11.bind(this)),c("Visibility").addListener(c("Visibility").VISIBLE,this.$VideoAutoplayControllerBase12.bind(this)),c("Arbiter").subscribe(c("DesktopHscrollUnitEventConstants").HSCROLL_ITEM_SHOWN_EVENT,this.updateAutoplay.bind(this)));if(!this.$VideoAutoplayControllerBase13())this.$VideoAutoplayControllerBase14()}};k.prototype.$VideoAutoplayControllerBase11=function(){"use strict";if(!this.$VideoAutoplayControllerBase2){this.$VideoAutoplayControllerBase2=this.getPlayingVideoUnit();this.$VideoAutoplayControllerBase15(c("VideoPlayerReason").PAGE_VISIBILITY)}};k.prototype.$VideoAutoplayControllerBase12=function(){"use strict";if(this.$VideoAutoplayControllerBase2){this.playVideo(this.$VideoAutoplayControllerBase2,c("VideoPlayerReason").PAGE_VISIBILITY);this.$VideoAutoplayControllerBase2=null}};k.prototype.$VideoAutoplayControllerBase14=function(){"use strict";__p&&__p();if(this.$VideoAutoplayControllerBase4)this.$VideoAutoplayControllerBase4.remove();this.$VideoAutoplayControllerBase8=c("throttle")(function(){return this.updateAutoplay()}.bind(this),this.$VideoAutoplayControllerBase1);this.$VideoAutoplayControllerBase9=c("debounce")(function(){return this.updateAutoplay()}.bind(this),this.$VideoAutoplayControllerBase1);this.$VideoAutoplayControllerBase4=c("Event").listen(window,"scroll",function(){this.$VideoAutoplayControllerBase8();if(c("VideoPlayerExperiments").useDebouncedScroll)this.$VideoAutoplayControllerBase9()}.bind(this))};k.prototype.$VideoAutoplayControllerBase13=function(){"use strict";return!!this.$VideoAutoplayControllerBase4};k.prototype.getClosestVideoUnits=function(l){"use strict";return this.$VideoAutoplayControllerBase10.filter(function(m){return m.getDistanceToViewport()>=0}).sort(function(m,n){return m.getDistanceToViewport()-n.getDistanceToViewport()}).slice(0,l)};k.prototype.getVisibleUnits=function(){"use strict";__p&&__p();var l=[];this.$VideoAutoplayControllerBase10.forEach(function(m){if(m.isVisible()){l.push(m);if(!m.wasVisible){m.wasVisible=true;m.logDisplayed()}}else m.wasVisible=false});return l};k.prototype.$VideoAutoplayControllerBase16=function(l){"use strict";var m=c("VideoPlayerExperiments").deferWhichVideoToAbortLoadingDecisioningLogic,n=l.getVideoPlayerController(),o=n?n.isLiveVideo():null;if(o!==null&&(m==="vod"&&o||m==="live"&&!o))return false;return c("VideoAutoplayControllerAbortLoadingHelper").shouldAbortLoadingVideoUnit(l)};k.prototype.pausePlayingVideo=function(l,m){__p&&__p();var n,o=this;"use strict";var p=this.$VideoAutoplayControllerBase3;if(p)(function(){__p&&__p();var q=function q(){if(!p.isState("playing")){if(c("VideoPlayerExperiments").abortLoadingReUpStillVisibleVideos&&p.isVisible())return c("setTimeout")(q,h);if(typeof p.abortLoading==="function")p.abortLoading()}};if(!o.$VideoAutoplayControllerBase7())p.pause(l);if(!c("VideoPlayerExperiments").decoupleAbortLoadingFromPause)if(o.$VideoAutoplayControllerBase16(p)&&!m)c("setTimeout")(q,h);o.$VideoAutoplayControllerBase3=null})()};k.prototype.$VideoAutoplayControllerBase15=function(l){"use strict";this.pausePlayingVideo(l,true)};k.prototype.updateAutoplay=function(){"use strict";throw new Error("Should be overridden")};f.exports=k}),null);
__d("Network",["mixInEventEmitter"],(function a(b,c,d,e,f,g){__p&&__p();var h=true,i=b.navigator.connection,j={0:"unknown",1:"ethernet",2:"wifi",3:"2g",4:"3g"};function k(){return h}function l(q){if(q==h)return;h=q;p.emit(q?"online":"offline")}function m(){return i?i.bandwidth:h?Infinity:0}function n(){return i?i.metered:false}function o(){var q=i?String(i.type):"0";return j[q]||q}var p={getBandwidth:m,getType:o,isMetered:n,isOnline:k,setOnline:l};c("mixInEventEmitter")(p,{online:true,offline:true});if(b.addEventListener){b.addEventListener("online",l.bind(null,true));b.addEventListener("offline",l.bind(null,false))}else if(b.attachEvent){b.attachEvent("online",l.bind(null,true));b.attachEvent("offline",l.bind(null,false))}f.exports=p}),null);
__d("XVideoAutoplayNuxAsyncController",["XController"],(function a(b,c,d,e,f,g){f.exports=c("XController").create("/video/autoplay/nux/",{})}),null);
__d("XVideoAutoplayNuxDismissAsyncController",["XController"],(function a(b,c,d,e,f,g){f.exports=c("XController").create("/video/autoplay/nux/dismiss/",{})}),null);
__d("XVideoAutoplayNuxLogViewAsyncController",["XController"],(function a(b,c,d,e,f,g){f.exports=c("XController").create("/video/autoplay/nux/log/view/",{})}),null);
__d("clearTimeout",["TimerStorage","TimeSliceReferenceCounting"],(function a(b,c,d,e,f,g){var h=b.clearTimeout.nativeBackup||b.clearTimeout,i=c("TimerStorage").TIMEOUT;f.exports=function(){for(var j=arguments.length,k=Array(j),l=0;l<j;l++)k[l]=arguments[l];c("TimerStorage").unset(i,k[0]);var m=i+k[0];if(k[0]!=null&&c("TimeSliceReferenceCounting").isValidCancellationToken(m))c("TimeSliceReferenceCounting").cancelTimeSlice(m);return Function.prototype.apply.call(h,b,k)}}),18);
__d("VideoAutoplayControllerX",["csx","AsyncRequest","DOM","Event","Network","Run","SubscriptionsHandler","VideoAutoplayControllerAbortLoadingHelper","VideoAutoplayControllerBase","VideoPlayerExperiments","VideoPlayerPreloadExperiment","VideoPlayerReason","XVideoAutoplayNuxAsyncController","XVideoAutoplayNuxDismissAsyncController","XVideoAutoplayNuxLogViewAsyncController","clearTimeout","destroyOnUnload","getViewportDimensions","ifRequired","setTimeout"],(function a(b,c,d,e,f,g,h){__p&&__p();var i,j,k=null,l=c("VideoPlayerExperiments").videoPollingFrequency,m=false;function n(){return!c("VideoPlayerExperiments").delayAutoplayUntilAfterLoad||m}i=babelHelpers.inherits(o,c("VideoAutoplayControllerBase"));j=i&&i.prototype;function o(){"use strict";__p&&__p();j.constructor.call(this,l);this.$VideoAutoplayControllerX1=new(c("VideoAutoplayControllerAbortLoadingHelper"))();this.$VideoAutoplayControllerX2=new(c("SubscriptionsHandler"))();this.$VideoAutoplayControllerX3=new(c("SubscriptionsHandler"))();this.$VideoAutoplayControllerX4=true;this.$VideoAutoplayControllerX5=true;this.$VideoAutoplayControllerX6=true;this.$VideoAutoplayControllerX7=null;this.$VideoAutoplayControllerX8=null;this.$VideoAutoplayControllerX9=false;this.$VideoAutoplayControllerX10=null;this.$VideoAutoplayControllerX11=false;this.$VideoAutoplayControllerX12=false;this.$VideoAutoplayControllerX13=false;var p=c("XVideoAutoplayNuxAsyncController").getURIBuilder().getURI();new(c("AsyncRequest"))(p).setAllowCrossPageTransition().send();c("destroyOnUnload")(function(){this.$VideoAutoplayControllerX14();if(c("VideoPlayerExperiments").disableAutoplayOnHomePgUpPgDownEnd){if(this.$VideoAutoplayControllerX15)c("clearTimeout")(this.$VideoAutoplayControllerX15);this.$VideoAutoplayControllerX16.remove()}if(this===k)k=null}.bind(this));c("Run").onAfterLoad(function(){m=true;if(c("VideoPlayerExperiments").delayAutoplayUntilAfterLoad)if(k)k.updateAutoplay();if(!document.hasFocus())c("Event").fire(window,"blur");if(c("VideoPlayerExperiments").disableAutoplayOnHomePgUpPgDownEnd)this.$VideoAutoplayControllerX17()}.bind(this))}o.prototype.$VideoAutoplayControllerX17=function(){"use strict";__p&&__p();var p=33,q=34,r=35,s=36;this.$VideoAutoplayControllerX15=null;var t=function(){this.$VideoAutoplayControllerX18(this.$VideoAutoplayControllerX5);c("clearTimeout")(this.$VideoAutoplayControllerX15);this.$VideoAutoplayControllerX15=null}.bind(this);this.$VideoAutoplayControllerX16=c("Event").listen(document.body,"keydown",function(u){__p&&__p();var v=-1;switch(u.keyCode){case p:case q:v=c("VideoPlayerExperiments").pressPgUpPgDownAutoplayShutoffInterval;break;case r:case s:v=c("VideoPlayerExperiments").pressHomeEndAutoplayShutoffInterval;break;default:break}if(v>-1)if(this.$VideoAutoplayControllerX15){c("clearTimeout")(this.$VideoAutoplayControllerX15);this.$VideoAutoplayControllerX15=c("setTimeout")(t,v)}else if(this.$VideoAutoplayControllerX4){this.$VideoAutoplayControllerX18(false);this.$VideoAutoplayControllerX15=c("setTimeout")(t,v)}}.bind(this))};o.prototype.$VideoAutoplayControllerX18=function(p){"use strict";this.$VideoAutoplayControllerX4=p;this.updateAutoplay()};o.registerVideoUnit=function(p){"use strict";__p&&__p();if(k==null)k=new o();k.addSubscriberVideoUnit();k.addVideoUnit(p);var q=new(c("SubscriptionsHandler"))();q.addSubscriptions.apply(q,k.$VideoAutoplayControllerX19(p));k.$VideoAutoplayControllerX20();if(p.isVisible()&&n())k.updateAutoplay();if(k.shouldRestoreAllSubsequentStreamBufferSizes())k.restoreStreamBufferSize();return function(){k&&k.removeVideoUnit(p);q.release();if(k&&p===k.getPlayingVideoUnit()){k.$VideoAutoplayControllerX3.release();k.setPlayingVideoUnit(null)}}};o.setShouldAutoplay=function(p){"use strict";if(k==null)k=new o();k.$VideoAutoplayControllerX4=p;k.$VideoAutoplayControllerX6=p;k.$VideoAutoplayControllerX5=p;k.updateAutoplay()};o.prototype.$VideoAutoplayControllerX14=function(){"use strict";this.$VideoAutoplayControllerX2.release();this.$VideoAutoplayControllerX3.release()};o.setAutoplayNux=function(p,q){"use strict";__p&&__p();if(k==null)return;k.$VideoAutoplayControllerX7=p;k.$VideoAutoplayControllerX8=q;k.$VideoAutoplayControllerX9=true;var r=c("DOM").find(q.getContentRoot(),"._5cqr");c("Event").listen(r,"click",function(){k.$VideoAutoplayControllerX21()});var s=c("DOM").scry(q.getContentRoot(),"._36gl")[0];if(s)c("Event").listen(s,"click",function(){k.$VideoAutoplayControllerX21()})};o.prototype.$VideoAutoplayControllerX21=function(){"use strict";this.$VideoAutoplayControllerX8.hide();this.$VideoAutoplayControllerX9=false;var p=c("XVideoAutoplayNuxDismissAsyncController").getURIBuilder().getURI();new(c("AsyncRequest"))(p).setAllowCrossPageTransition().send()};o.prototype.setupPlayingVideoUnitSubscriptions=function(){"use strict";__p&&__p();if(this.getPlayingVideoUnit().addListener){this.$VideoAutoplayControllerX2.release();this.$VideoAutoplayControllerX2.engage();if(!this.getPlayingVideoUnit().isLooping())this.$VideoAutoplayControllerX2.addSubscriptions(this.getPlayingVideoUnit().addListener("finishPlayback",function(){this.setPlayingVideoUnit(null)}.bind(this)));this.$VideoAutoplayControllerX2.addSubscriptions(this.getPlayingVideoUnit().addListener("turnOffAutoplay",function(){this.setPlayingVideoUnit(null)}.bind(this)),this.getPlayingVideoUnit().addListener("pausePlayback",function(){this.$VideoAutoplayControllerX20()}.bind(this)),this.getPlayingVideoUnit().addListener("finishPlayback",function(){this.$VideoAutoplayControllerX20()}.bind(this)),c("Network").addListener("online",function(){this.$VideoAutoplayControllerX20()}.bind(this)),c("Network").addListener("offline",function(){this.$VideoAutoplayControllerX20()}.bind(this)))}};o.prototype.$VideoAutoplayControllerX20=function(){"use strict";__p&&__p();if(c("VideoPlayerExperiments").webVideosBlockAutoplayWhenOffline)if(c("Network").isOnline())this.$VideoAutoplayControllerX4=this.$VideoAutoplayControllerX6;else{this.$VideoAutoplayControllerX6=this.$VideoAutoplayControllerX4;this.$VideoAutoplayControllerX4=false;return}var p=this.getVideoUnits();for(var q=0;q<p.length;q++){var r=p[q].getVideoPlayerController();if(r){if(r.getDataInsertionPosition()==="0"){this.$VideoAutoplayControllerX11=true;if(this.$VideoAutoplayControllerX12===false){r.restoreStreamBufferSize();r.once("beginPlayback",function(){this.$VideoAutoplayControllerX13=true;this.restoreStreamBufferSize()}.bind(this));this.$VideoAutoplayControllerX12=true}}if(!c("VideoPlayerExperiments").autoplayBlockBlacklist)r.updateAutoplayRestrained()}}if(!this.$VideoAutoplayControllerX11)this.restoreStreamBufferSize()};o.prototype.shouldRestoreAllSubsequentStreamBufferSizes=function(){"use strict";if(!this.$VideoAutoplayControllerX11)return true;return this.$VideoAutoplayControllerX13};o.prototype.restoreStreamBufferSize=function(){"use strict";var p=this.getVideoUnits();for(var q=0;q<p.length;q++){var r=p[q].getVideoPlayerController();if(r!==null)r.restoreStreamBufferSize()}};o.prototype.$VideoAutoplayControllerX19=function(p){__p&&__p();var q;"use strict";if(!p.addListener)return[];var r=function(){__p&&__p();var t=p.getVideoPlayerController();if(!t.isMuted()&&t.isState("playing")){if(this.$VideoAutoplayControllerX10&&this.$VideoAutoplayControllerX10!==p){var u=this.$VideoAutoplayControllerX10.getVideoPlayerController(),v=u.getOption("VideoWithLiveBroadcast","isLive");if(v)u.mute();else u.pause(c("VideoPlayerReason").USER)}this.$VideoAutoplayControllerX10=p}}.bind(this),s=[p.addListener("beginPlayback",r),p.addListener("changeVolume",r),p.addListener("unmuteVideo",r)];(q=this.$VideoAutoplayControllerX3).addSubscriptions.apply(q,s);return s};o.prototype.$VideoAutoplayControllerX22=function(){"use strict";__p&&__p();var p=this.getVisibleUnits(),q=p.length,r=null;if(q===1){r=p[0];r=r.isAutoplayable()?r:null}else if(q>1){var s=c("getViewportDimensions")().height/2;p.forEach(function(t){if(!t.isAutoplayable())return;var u=t.getDOMPosition(),v=u.y+u.height/2,w=Math.abs(v-s);t.playPriority=w;if(!r||t.playPriority<r.playPriority)r=t})}return r};o.prototype.showAutoplayNUX=function(p){"use strict";if(this.$VideoAutoplayControllerX8&&!this.$VideoAutoplayControllerX8.isShown()){var q=p.getVideoPlayerController().getRootNode();c("DOM").prependContent(q,this.$VideoAutoplayControllerX7);this.$VideoAutoplayControllerX8.show();var r=c("XVideoAutoplayNuxLogViewAsyncController").getURIBuilder().getURI();new(c("AsyncRequest"))(r).setAllowCrossPageTransition().send()}this.$VideoAutoplayControllerX9=false};o.getChannelVideos=function(){"use strict";if(k)return k.getVideoUnits().filter(function(p){return p.getIsInChannel()});return null};o.prototype.addVideoUnit=function(p){"use strict";j.addVideoUnit.call(this,p);if(c("VideoPlayerExperiments").decoupleAbortLoadingFromPause&&p)this.$VideoAutoplayControllerX1.addVideoUnit(p)};o.prototype.removeVideoUnit=function(p){"use strict";j.removeVideoUnit.call(this,p);if(c("VideoPlayerExperiments").decoupleAbortLoadingFromPause&&p)this.$VideoAutoplayControllerX1.removeVideoUnit(p)};o.prototype.updateAutoplay=function(){"use strict";__p&&__p();if(!this.$VideoAutoplayControllerX4){this.pausePlayingVideo(c("VideoPlayerReason").AUTOPLAY);return}if(!c("VideoPlayerExperiments").decoupleAbortLoadingFromPause)this.getClosestVideoUnits(c("VideoPlayerPreloadExperiment").preloadVideosCount).forEach(function(t){return t.preload()});else if(c("VideoPlayerExperiments").abortLoadingHelperDefaultPreloading)this.$VideoAutoplayControllerX1.preloadClosestVideoUnits(c("VideoPlayerPreloadExperiment").preloadVideosCount);var p=this.$VideoAutoplayControllerX22(),q=this.getPlayingVideoUnit();if(q){if(p!=q){var r=null;r=q.getVideoPlayerController();if(r)r.setSmartBufferAdjustmentEnabled(false);if(p){var s=null;s=p.getVideoPlayerController();if(s)s.setSmartBufferAdjustmentEnabled(true)}this.pausePlayingVideo(c("VideoPlayerReason").AUTOPLAY);this.playVideo(p,c("VideoPlayerReason").AUTOPLAY);if(this.$VideoAutoplayControllerX9)this.showAutoplayNUX(p)}}else if(p){this.playVideo(p,c("VideoPlayerReason").AUTOPLAY);if(this.$VideoAutoplayControllerX9)this.showAutoplayNUX(p)}if(c("VideoPlayerExperiments").decoupleAbortLoadingFromPause)this.$VideoAutoplayControllerX1.maybeAbortLoading()};f.exports=o}),null);
__d("VideoAutoplayPlayerBase",["EventEmitter","JSLog"],(function a(b,c,d,e,f,g){__p&&__p();var h,i;h=babelHelpers.inherits(j,c("EventEmitter"));i=h&&h.prototype;function j(){var k,l;"use strict";for(var m=arguments.length,n=Array(m),o=0;o<m;o++)n[o]=arguments[o];return l=(k=i.constructor).call.apply(k,[this].concat(n)),this.wasVisible=false,l}j.prototype.isVisible=function(){"use strict";throw new Error("Should be overridden")};j.prototype.getDistanceToViewport=function(){"use strict";throw new Error("Should be overridden")};j.prototype.getVideoPlayerController=function(){"use strict";c("JSLog").warn(["VideoAutoplayPlayerBase.getVideoPlayerController()","was called and returned null."].join(" "));return null};j.prototype.logDisplayed=function(){"use strict";throw new Error("Should be overridden")};j.prototype.playWithoutUnmute=function(k){"use strict";throw new Error("Should be overridden")};j.prototype.pause=function(k){"use strict";throw new Error("Should be overridden")};j.prototype.isAutoplayable=function(){"use strict";throw new Error("Should be overridden")};j.prototype.getDOMPosition=function(){"use strict";throw new Error("Should be overridden")};j.prototype.isLooping=function(){"use strict";throw new Error("Should be overridden")};j.prototype.isState=function(k){"use strict";throw new Error("Should be overridden")};f.exports=j}),null);
__d("DOMContainer.react",["invariant","React","ReactDOM","isNode"],(function a(b,c,d,e,f,g,h){__p&&__p();var i,j,k=c("React").PropTypes;i=babelHelpers.inherits(l,c("React").Component);j=i&&i.prototype;function l(){var m,n;"use strict";for(var o=arguments.length,p=Array(o),q=0;q<o;q++)p[q]=arguments[q];return n=(m=j.constructor).call.apply(m,[this].concat(p)),this.getDOMChild=function(){var r=this.props.children;c("isNode")(r)||h(0);return r}.bind(this),n}l.prototype.shouldComponentUpdate=function(m,n){"use strict";return m.children!==this.props.children};l.prototype.componentDidMount=function(){"use strict";c("ReactDOM").findDOMNode(this).appendChild(this.getDOMChild())};l.prototype.componentDidUpdate=function(){"use strict";var m=c("ReactDOM").findDOMNode(this);while(m.lastChild)m.removeChild(m.lastChild);m.appendChild(this.getDOMChild())};l.prototype.render=function(){"use strict";if(this.props.display==="block")return c("React").createElement("div",this.props,undefined);return c("React").createElement("span",this.props,undefined)};l.propTypes={display:k.oneOf(["inline","block"])};l.defaultProps={display:"inline"};f.exports=l}),18);
__d("VideoPlayerLoggerEvent",[],(function a(b,c,d,e,f,g){f.exports=Object.freeze({AUTOPLAY_PREFERENCE_CHANGED:"autoplay_preference_changed",END_STALL_TIME:"end_stall_time",AUTOPLAY_PREFERENCE_STATUS:"autoplay_preference_status",ERROR_ALERT_SHOWN:"video_error_alert_shown",COMMERCIAL_BREAK_OFFSCREEN:"commercial_break_offscreen",COMMERCIAL_BREAK_ONSCREEN:"commercial_break_onscreen",NOT_AUTOPLAYING:"not_autoplaying",VIDEO_CHANNEL_NO_RELATED_VIDEO:"video_channel_no_related_video",VIDEO_ORIENTATION_CHANGED:"video_orientation_changed",AD_BREAK_STARTING_INDICATOR:"ad_break_starting_indicator",ASSETS_LOADED:"assets_loaded",BUFFERED:"buffered",CANCELLED_REQUESTED_PLAYING:"cancelled_requested_playing",CAPTION_CHANGE:"caption_change",CAROUSEL_CHANGE:"carousel_change",CHROMECAST_AVAILABILITY_CHECKED:"chromecast_availabilty_checked",CHROMECAST_CAST_CLICKED:"chromecast_button_clicked",CHROMECAST_CAST_CONNECTED:"chromecast_connected",CHROMECAST_CAST_DISABLED:"chromecast_button_disabled",CHROMECAST_CAST_DISCONNECTED:"chromecast_disconnected",CHROMECAST_CAST_RECONNECTED:"chromecast_reconnected",CHROMECAST_CAST_VISIBLE:"chromecast_button_visible",CHROMECAST_NOT_SUPPORTED:"chromecast_not_supported",CLICK:"click",DISPLAYED:"displayed",ENTERED_FALLBACK:"entered_fallback",ENTERED_FS:"entered_fs",ENTERED_HD:"entered_hd",ERROR:"error",EXITED_FS:"exited_fs",EXITED_HD:"exited_hd",FINISHED_LOADING:"finished_loading",FINISHED_PLAYING:"finished_playing",HEADSET_CONNECTED:"headset_connected",HEADSET_DISCONNECTED:"headset_disconnected",HEART_BEAT:"heart_beat",HOST_ERROR:"host_error",HTTP_STATUS_UPDATE:"http_status_update",IMPRESSION:"impression",INLINE_CLICK_TO_PLAY:"inline_click_to_play",INVALID_URL:"invalid_url",MUTED:"muted",NO_SURFACE_UPDATE:"no_surface_update",PAUSED:"paused",PLAY_REQUESTED:"play_requested",PLAY_REQUESTED_OOB:"play_requested_oob",PLAYER_ALLOCATED:"player_allocated",PLAYER_FORMAT_CHANGED:"player_format_changed",PLAYER_LOADED:"player_loaded",PLAYING_LIVE_STARTED:"playing_live_started",PLAYING_LIVE_STOPPED:"playing_live_stopped",POP_FAILOVER:"pop_failover",PROGRESS:"progress",QUALITY_CHANGE:"quality_change",READY_TO_PLAY:"ready_to_play",REPLAYED:"replayed",REPRESENTATION_ENDED:"representation_ended",REPRESENTATION_FIRST_ENDED:"representation_first_ended",REQUESTED:"requested",REQUESTED_PLAYING:"requested_playing",SCRUBBED:"scrubbed",SPLASH_DISPLAYED:"splash_displayed",STALE:"stale",STARTED_PLAYING:"started_playing",STARTED_RECEIVING_BYTES:"started_receiving_bytes",STOPPED_PLAYING:"stopped_playing",STREAM_RESET:"stream_reset",SURFACE_UPDATED:"surface_updated",SWITCHED_IMPLEMENTATION:"switched_implementation",UNMUTED:"unmuted",UNPAUSED:"unpaused",VIDEO_CHAINING_IMPRESSION:"video_chaining_impression",VIDEO_CHAINING_TAP:"video_chaining_tap",VIDEO_CLICKED_WITHIN_PLAYER:"video_clicked_within_player",VIDEO_PLAYER_SERVICE_DISCONNECTED:"video_player_service_disconnected",VIDEO_PLAYER_SERVICE_RECONNECTED:"video_player_service_reconnected",VIDEO_PLAYER_SERVICE_UNAVAILABLE:"video_player_service_unavailable",VIDEO_PLAYING:"video_playing",VIDEO_SKIP_AD:"video_skip_ad",VOLUME_CHANGED:"volume_changed",VOLUME_DECREASE:"volume_decrease",VOLUME_INCREASE:"volume_increase",WATCH_AND_SCROLL_CHANNEL_ENTERED:"watch_and_scroll_channel_entered",WATCH_AND_SCROLL_EXITED:"watch_and_scroll_exited",WATCH_AND_SCROLL_ICON_HIGHLIGHTED:"watch_and_scroll_icon_highlighted",WATCH_AND_SCROLL_ICON_UNHIGHLIGHTED:"watch_and_scroll_icon_unhighlighted",WATCH_AND_SCROLL_PAUSED:"watch_and_scroll_paused",LIVE_SEGMENT_LOAD_ERROR:"live_segment_load_error",MANIFEST_DATA_TYPE_ERROR:"manifest_data_type_error",MANIFEST_LOAD_ERROR:"manifest_load_error",PLAYER_WARNING:"player_warning",PLAYHEAD_FELL_BEHIND_ERROR:"playhead_fell_behind_error",STREAM_SEGMENT_LOAD_ERROR:"stream_segment_load_error",UNEXPECTED_SEGMENT_ERROR:"unexpected_segment_error",NETWORK_TIMEOUT:"network_timeout",VIDEO_LOGGING_SESSION_TIMEOUT:"video_logging_session_timeout",COMPLETION:"completion",VIEW:"view",PLAYED_FOR_THREE_SECONDS:"played_for_three_seconds",GUIDE_ENTERED:"guide_entered",GUIDE_EXITED:"guide_exited",HEADING_RESET:"heading_reset",SPHERICAL_FALLBACK_ENTERED:"spherical_fallback_entered",SPHERICAL_VIDEO_FALLBACK_CTA_CLICKED:"spherical_video_fallback_cta_clicked",VIEWPORT_ROTATED:"viewport_rotated",VIEWPORT_ZOOMED:"viewport_zoomed",BANZAI_OAUTH_GK_ERROR:"banzai_oauth_gk_error",BANZAI_OAUTH_PARSE_ERROR:"banzai_oauth_parse_error",BANZAI_OAUTH_SESSION_ERROR:"banzai_oauth_session_error",VIEWABILITY_CHANGED:"viewability_changed"})}),null);
__d("fbjs/lib/CSSCore",["CSSCore"],(function a(b,c,d,e,f,g){"use strict";f.exports=c("CSSCore")}),null);
__d("cancelAnimationFramePolyfill",[],(function a(b,c,d,e,f,g){var h=b.cancelAnimationFrame&&b.cancelAnimationFrame.nativeBackup||b.cancelAnimationFrame||b.webkitCancelAnimationFrame||b.mozCancelAnimationFrame||b.oCancelAnimationFrame||b.msCancelAnimationFrame||b.clearTimeout;f.exports=h}),null);
__d("cancelAnimationFrame",["TimerStorage","TimeSliceReferenceCounting","cancelAnimationFramePolyfill"],(function a(b,c,d,e,f,g){var h=c("TimerStorage").ANIMATION_FRAME;f.exports=function(){for(var i=arguments.length,j=Array(i),k=0;k<i;k++)j[k]=arguments[k];c("TimerStorage").unset(h,j[0]);var l=h+j[0];if(j[0]!=null&&c("TimeSliceReferenceCounting").isValidCancellationToken(l))c("TimeSliceReferenceCounting").cancelTimeSlice(l);return Function.prototype.apply.call(c("cancelAnimationFramePolyfill"),b,j)}}),18);
__d("clearInterval",["TimerStorage","TimeSliceReferenceCounting"],(function a(b,c,d,e,f,g){var h=b.clearTimeout.nativeBackup||b.clearTimeout;f.exports=function(){for(var i=arguments.length,j=Array(i),k=0;k<i;k++)j[k]=arguments[k];var l=j[0];c("TimerStorage").unset(c("TimerStorage").INTERVAL,l);if(l!=null&&c("TimeSliceReferenceCounting").isValidCancellationToken(l))c("TimeSliceReferenceCounting").cancelTimeSlice(l);return Function.prototype.apply.call(h,b,j)}}),18);
__d("replaceNativeTimer",["cancelAnimationFrame","clearInterval","clearTimeout","requestAnimationFrame","setInterval","setTimeout"],(function a(b,c,d,e,f,g){__p&&__p();c("setTimeout").nativeBackup=b.setTimeout;c("clearTimeout").nativeBackup=b.clearTimeout;c("setInterval").nativeBackup=b.setInterval;c("clearInterval").nativeBackup=b.clearInterval;c("requestAnimationFrame").nativeBackup=b.requestAnimationFrame;c("cancelAnimationFrame").nativeBackup=b.cancelAnimationFrame;b.setTimeout=c("setTimeout");b.clearTimeout=c("clearTimeout");b.setInterval=c("setInterval");b.clearInterval=c("clearInterval");b.requestAnimationFrame=c("requestAnimationFrame");b.cancelAnimationFrame=c("cancelAnimationFrame")}),18);