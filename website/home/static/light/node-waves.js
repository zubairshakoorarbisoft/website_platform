/*! For license information please see node-waves.js.LICENSE.txt */
!function(e,t){if("object"==typeof exports&&"object"==typeof module)module.exports=t();else if("function"==typeof define&&define.amd)define([],t);else{var n=t();for(var o in n)("object"==typeof exports?exports:e)[o]=n[o]}}(self,(()=>(()=>{var e={8291:function(e,t,n){var o;!function(n,r){"use strict";void 0===(o=function(){return n.Waves=r.call(n),n.Waves}.apply(t,[]))||(e.exports=o)}("object"==typeof n.g?n.g:this,(function(){"use strict";var e=e||{},t=document.querySelectorAll.bind(document),n=Object.prototype.toString,o="ontouchstart"in window;function r(e){var t=typeof e;return"function"===t||"object"===t&&!!e}function a(e){var o,a=n.call(e);return"[object String]"===a?t(e):r(e)&&/^\[object (Array|HTMLCollection|NodeList|Object)\]$/.test(a)&&e.hasOwnProperty("length")?e:r(o=e)&&o.nodeType>0?[e]:[]}function i(e){var t,n,o={top:0,left:0},r=e&&e.ownerDocument;return t=r.documentElement,void 0!==e.getBoundingClientRect&&(o=e.getBoundingClientRect()),n=function(e){return null!==(t=e)&&t===t.window?e:9===e.nodeType&&e.defaultView;var t}(r),{top:o.top+n.pageYOffset-t.clientTop,left:o.left+n.pageXOffset-t.clientLeft}}function s(e){var t="";for(var n in e)e.hasOwnProperty(n)&&(t+=n+":"+e[n]+";");return t}var u={duration:750,delay:200,show:function(e,t,n){if(2===e.button)return!1;t=t||this;var o=document.createElement("div");o.className="waves-ripple waves-rippling",t.appendChild(o);var r=i(t),a=0,c=0;"touches"in e&&e.touches.length?(a=e.touches[0].pageY-r.top,c=e.touches[0].pageX-r.left):(a=e.pageY-r.top,c=e.pageX-r.left),c=c>=0?c:0,a=a>=0?a:0;var l="scale("+t.clientWidth/100*3+")",d="translate(0,0)";n&&(d="translate("+n.x+"px, "+n.y+"px)"),o.setAttribute("data-hold",Date.now()),o.setAttribute("data-x",c),o.setAttribute("data-y",a),o.setAttribute("data-scale",l),o.setAttribute("data-translate",d);var f={top:a+"px",left:c+"px"};o.classList.add("waves-notransition"),o.setAttribute("style",s(f)),o.classList.remove("waves-notransition"),f["-webkit-transform"]=l+" "+d,f["-moz-transform"]=l+" "+d,f["-ms-transform"]=l+" "+d,f["-o-transform"]=l+" "+d,f.transform=l+" "+d,f.opacity="1";var v="mousemove"===e.type?2500:u.duration;f["-webkit-transition-duration"]=v+"ms",f["-moz-transition-duration"]=v+"ms",f["-o-transition-duration"]=v+"ms",f["transition-duration"]=v+"ms",o.setAttribute("style",s(f))},hide:function(e,t){for(var n=(t=t||this).getElementsByClassName("waves-rippling"),r=0,a=n.length;r<a;r++)l(e,t,n[r]);o&&(t.removeEventListener("touchend",u.hide),t.removeEventListener("touchcancel",u.hide)),t.removeEventListener("mouseup",u.hide),t.removeEventListener("mouseleave",u.hide)}},c={input:function(e){var t=e.parentNode;if("i"!==t.tagName.toLowerCase()||!t.classList.contains("waves-effect")){var n=document.createElement("i");n.className=e.className+" waves-input-wrapper",e.className="waves-button-input",t.replaceChild(n,e),n.appendChild(e);var o=window.getComputedStyle(e,null),r=o.color,a=o.backgroundColor;n.setAttribute("style","color:"+r+";background:"+a),e.setAttribute("style","background-color:rgba(0,0,0,0);")}},img:function(e){var t=e.parentNode;if("i"!==t.tagName.toLowerCase()||!t.classList.contains("waves-effect")){var n=document.createElement("i");t.replaceChild(n,e),n.appendChild(e)}}};function l(e,t,n){if(n){n.classList.remove("waves-rippling");var o=n.getAttribute("data-x"),r=n.getAttribute("data-y"),a=n.getAttribute("data-scale"),i=n.getAttribute("data-translate"),c=350-(Date.now()-Number(n.getAttribute("data-hold")));c<0&&(c=0),"mousemove"===e.type&&(c=150);var l="mousemove"===e.type?2500:u.duration;setTimeout((function(){var e={top:r+"px",left:o+"px",opacity:"0","-webkit-transition-duration":l+"ms","-moz-transition-duration":l+"ms","-o-transition-duration":l+"ms","transition-duration":l+"ms","-webkit-transform":a+" "+i,"-moz-transform":a+" "+i,"-ms-transform":a+" "+i,"-o-transform":a+" "+i,transform:a+" "+i};n.setAttribute("style",s(e)),setTimeout((function(){try{t.removeChild(n)}catch(e){return!1}}),l)}),c)}}var d={touches:0,allowEvent:function(e){var t=!0;return/^(mousedown|mousemove)$/.test(e.type)&&d.touches&&(t=!1),t},registerEvent:function(e){var t=e.type;"touchstart"===t?d.touches+=1:/^(touchend|touchcancel)$/.test(t)&&setTimeout((function(){d.touches&&(d.touches-=1)}),500)}};function f(e){var t=function(e){if(!1===d.allowEvent(e))return null;for(var t=null,n=e.target||e.srcElement;n.parentElement;){if(!(n instanceof SVGElement)&&n.classList.contains("waves-effect")){t=n;break}n=n.parentElement}return t}(e);if(null!==t){if(t.disabled||t.getAttribute("disabled")||t.classList.contains("disabled"))return;if(d.registerEvent(e),"touchstart"===e.type&&u.delay){var n=!1,r=setTimeout((function(){r=null,u.show(e,t)}),u.delay),a=function(o){r&&(clearTimeout(r),r=null,u.show(e,t)),n||(n=!0,u.hide(o,t)),s()},i=function(e){r&&(clearTimeout(r),r=null),a(e),s()};t.addEventListener("touchmove",i,!1),t.addEventListener("touchend",a,!1),t.addEventListener("touchcancel",a,!1);var s=function(){t.removeEventListener("touchmove",i),t.removeEventListener("touchend",a),t.removeEventListener("touchcancel",a)}}else u.show(e,t),o&&(t.addEventListener("touchend",u.hide,!1),t.addEventListener("touchcancel",u.hide,!1)),t.addEventListener("mouseup",u.hide,!1),t.addEventListener("mouseleave",u.hide,!1)}}return e.init=function(e){var t=document.body;"duration"in(e=e||{})&&(u.duration=e.duration),"delay"in e&&(u.delay=e.delay),o&&(t.addEventListener("touchstart",f,!1),t.addEventListener("touchcancel",d.registerEvent,!1),t.addEventListener("touchend",d.registerEvent,!1)),t.addEventListener("mousedown",f,!1)},e.attach=function(e,t){var o,r;e=a(e),"[object Array]"===n.call(t)&&(t=t.join(" ")),t=t?" "+t:"";for(var i=0,s=e.length;i<s;i++)r=(o=e[i]).tagName.toLowerCase(),-1!==["input","img"].indexOf(r)&&(c[r](o),o=o.parentElement),-1===o.className.indexOf("waves-effect")&&(o.className+=" waves-effect"+t)},e.ripple=function(e,t){var n=(e=a(e)).length;if((t=t||{}).wait=t.wait||0,t.position=t.position||null,n)for(var o,r,s,c={},l=0,d={type:"mousedown",button:1},f=function(e,t){return function(){u.hide(e,t)}};l<n;l++)o=e[l],r=t.position||{x:o.clientWidth/2,y:o.clientHeight/2},s=i(o),c.x=s.left+r.x,c.y=s.top+r.y,d.pageX=c.x,d.pageY=c.y,u.show(d,o),t.wait>=0&&null!==t.wait&&setTimeout(f({type:"mouseup",button:1},o),t.wait)},e.calm=function(e){for(var t={type:"mouseup",button:1},n=0,o=(e=a(e)).length;n<o;n++)u.hide(t,e[n])},e.displayEffect=function(t){console.error("Waves.displayEffect() has been deprecated and will be removed in future version. Please use Waves.init() to initialize Waves effect"),e.init(t)},e}))}},t={};function n(o){var r=t[o];if(void 0!==r)return r.exports;var a=t[o]={exports:{}};return e[o].call(a.exports,a,a.exports,n),a.exports}n.n=e=>{var t=e&&e.__esModule?()=>e.default:()=>e;return n.d(t,{a:t}),t},n.d=(e,t)=>{for(var o in t)n.o(t,o)&&!n.o(e,o)&&Object.defineProperty(e,o,{enumerable:!0,get:t[o]})},n.g=function(){if("object"==typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"==typeof window)return window}}(),n.o=(e,t)=>Object.prototype.hasOwnProperty.call(e,t),n.r=e=>{"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})};var o={};return(()=>{"use strict";n.r(o),n.d(o,{nodeWaves:()=>t.a});var e=n(8291),t=n.n(e)})(),o})()));