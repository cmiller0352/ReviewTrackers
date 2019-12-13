content = """

<!doctype html>
<html>
<head>
<meta charset="utf-8">
<meta http-equiv="x-ua-compatible" content="ie=edge"><script type="5870d3775a1169cbe2c6706a-text/javascript">(window.NREUM||(NREUM={})).loader_config={xpid:"VQEFUlBXDxAHXFRVBwUFVQ==",licenseKey:"b6d3a1e0ad",applicationID:"78570423"};window.NREUM||(NREUM={}),__nr_require=function(t,n,e){function r(e){if(!n[e]){var o=n[e]={exports:{}};t[e][0].call(o.exports,function(n){var o=t[e][1][n];return r(o||n)},o,o.exports)}return n[e].exports}if("function"==typeof __nr_require)return __nr_require;for(var o=0;o<e.length;o++)r(e[o]);return r}({1:[function(t,n,e){function r(t){try{s.console&&console.log(t)}catch(n){}}var o,i=t("ee"),a=t(20),s={};try{o=localStorage.getItem("__nr_flags").split(","),console&&"function"==typeof console.log&&(s.console=!0,o.indexOf("dev")!==-1&&(s.dev=!0),o.indexOf("nr_dev")!==-1&&(s.nrDev=!0))}catch(c){}s.nrDev&&i.on("internal-error",function(t){r(t.stack)}),s.dev&&i.on("fn-err",function(t,n,e){r(e.stack)}),s.dev&&(r("NR AGENT IN DEVELOPMENT MODE"),r("flags: "+a(s,function(t,n){return t}).join(", ")))},{}],2:[function(t,n,e){function r(t,n,e,r,s){try{p?p-=1:o(s||new UncaughtException(t,n,e),!0)}catch(f){try{i("ierr",[f,c.now(),!0])}catch(d){}}return"function"==typeof u&&u.apply(this,a(arguments))}function UncaughtException(t,n,e){this.message=t||"Uncaught error with no additional information",this.sourceURL=n,this.line=e}function o(t,n){var e=n?null:c.now();i("err",[t,e])}var i=t("handle"),a=t(21),s=t("ee"),c=t("loader"),f=t("gos"),u=window.onerror,d=!1,l="nr@seenError",p=0;c.features.err=!0,t(1),window.onerror=r;try{throw new Error}catch(h){"stack"in h&&(t(9),t(8),"addEventListener"in window&&t(5),c.xhrWrappable&&t(10),d=!0)}s.on("fn-start",function(t,n,e){d&&(p+=1)}),s.on("fn-err",function(t,n,e){d&&!e[l]&&(f(e,l,function(){return!0}),this.thrown=!0,o(e))}),s.on("fn-end",function(){d&&!this.thrown&&p>0&&(p-=1)}),s.on("internal-error",function(t){i("ierr",[t,c.now(),!0])})},{}],3:[function(t,n,e){t("loader").features.ins=!0},{}],4:[function(t,n,e){function r(t){}if(window.performance&&window.performance.timing&&window.performance.getEntriesByType){var o=t("ee"),i=t("handle"),a=t(9),s=t(8),c="learResourceTimings",f="addEventListener",u="resourcetimingbufferfull",d="bstResource",l="resource",p="-start",h="-end",m="fn"+p,w="fn"+h,v="bstTimer",g="pushState",y=t("loader");y.features.stn=!0,t(7),"addEventListener"in window&&t(5);var x=NREUM.o.EV;o.on(m,function(t,n){var e=t[0];e instanceof x&&(this.bstStart=y.now())}),o.on(w,function(t,n){var e=t[0];e instanceof x&&i("bst",[e,n,this.bstStart,y.now()])}),a.on(m,function(t,n,e){this.bstStart=y.now(),this.bstType=e}),a.on(w,function(t,n){i(v,[n,this.bstStart,y.now(),this.bstType])}),s.on(m,function(){this.bstStart=y.now()}),s.on(w,function(t,n){i(v,[n,this.bstStart,y.now(),"requestAnimationFrame"])}),o.on(g+p,function(t){this.time=y.now(),this.startPath=location.pathname+location.hash}),o.on(g+h,function(t){i("bstHist",[location.pathname+location.hash,this.startPath,this.time])}),f in window.performance&&(window.performance["c"+c]?window.performance[f](u,function(t){i(d,[window.performance.getEntriesByType(l)]),window.performance["c"+c]()},!1):window.performance[f]("webkit"+u,function(t){i(d,[window.performance.getEntriesByType(l)]),window.performance["webkitC"+c]()},!1)),document[f]("scroll",r,{passive:!0}),document[f]("keypress",r,!1),document[f]("click",r,!1)}},{}],5:[function(t,n,e){function r(t){for(var n=t;n&&!n.hasOwnProperty(u);)n=Object.getPrototypeOf(n);n&&o(n)}function o(t){s.inPlace(t,[u,d],"-",i)}function i(t,n){return t[1]}var a=t("ee").get("events"),s=t("wrap-function")(a,!0),c=t("gos"),f=XMLHttpRequest,u="addEventListener",d="removeEventListener";n.exports=a,"getPrototypeOf"in Object?(r(document),r(window),r(f.prototype)):f.prototype.hasOwnProperty(u)&&(o(window),o(f.prototype)),a.on(u+"-start",function(t,n){var e=t[1],r=c(e,"nr@wrapped",function(){function t(){if("function"==typeof e.handleEvent)return e.handleEvent.apply(e,arguments)}var n={object:t,"function":e}[typeof e];return n?s(n,"fn-",null,n.name||"anonymous"):e});this.wrapped=t[1]=r}),a.on(d+"-start",function(t){t[1]=this.wrapped||t[1]})},{}],6:[function(t,n,e){function r(t,n,e){var r=t[n];"function"==typeof r&&(t[n]=function(){var t=i(arguments),n={};o.emit(e+"before-start",[t],n);var a;n[m]&&n[m].dt&&(a=n[m].dt);var s=r.apply(this,t);return o.emit(e+"start",[t,a],s),s.then(function(t){return o.emit(e+"end",[null,t],s),t},function(t){throw o.emit(e+"end",[t],s),t})})}var o=t("ee").get("fetch"),i=t(21),a=t(20);n.exports=o;var s=window,c="fetch-",f=c+"body-",u=["arrayBuffer","blob","json","text","formData"],d=s.Request,l=s.Response,p=s.fetch,h="prototype",m="nr@context";d&&l&&p&&(a(u,function(t,n){r(d[h],n,f),r(l[h],n,f)}),r(s,"fetch",c),o.on(c+"end",function(t,n){var e=this;if(n){var r=n.headers.get("content-length");null!==r&&(e.rxSize=r),o.emit(c+"done",[null,n],e)}else o.emit(c+"done",[t],e)}))},{}],7:[function(t,n,e){var r=t("ee").get("history"),o=t("wrap-function")(r);n.exports=r;var i=window.history&&window.history.constructor&&window.history.constructor.prototype,a=window.history;i&&i.pushState&&i.replaceState&&(a=i),o.inPlace(a,["pushState","replaceState"],"-")},{}],8:[function(t,n,e){var r=t("ee").get("raf"),o=t("wrap-function")(r),i="equestAnimationFrame";n.exports=r,o.inPlace(window,["r"+i,"mozR"+i,"webkitR"+i,"msR"+i],"raf-"),r.on("raf-start",function(t){t[0]=o(t[0],"fn-")})},{}],9:[function(t,n,e){function r(t,n,e){t[0]=a(t[0],"fn-",null,e)}function o(t,n,e){this.method=e,this.timerDuration=isNaN(t[1])?0:+t[1],t[0]=a(t[0],"fn-",this,e)}var i=t("ee").get("timer"),a=t("wrap-function")(i),s="setTimeout",c="setInterval",f="clearTimeout",u="-start",d="-";n.exports=i,a.inPlace(window,[s,"setImmediate"],s+d),a.inPlace(window,[c],c+d),a.inPlace(window,[f,"clearImmediate"],f+d),i.on(c+u,r),i.on(s+u,o)},{}],10:[function(t,n,e){function r(t,n){d.inPlace(n,["onreadystatechange"],"fn-",s)}function o(){var t=this,n=u.context(t);t.readyState>3&&!n.resolved&&(n.resolved=!0,u.emit("xhr-resolved",[],t)),d.inPlace(t,g,"fn-",s)}function i(t){y.push(t),h&&(b?b.then(a):w?w(a):(E=-E,R.data=E))}function a(){for(var t=0;t<y.length;t++)r([],y[t]);y.length&&(y=[])}function s(t,n){return n}function c(t,n){for(var e in t)n[e]=t[e];return n}t(5);var f=t("ee"),u=f.get("xhr"),d=t("wrap-function")(u),l=NREUM.o,p=l.XHR,h=l.MO,m=l.PR,w=l.SI,v="readystatechange",g=["onload","onerror","onabort","onloadstart","onloadend","onprogress","ontimeout"],y=[];n.exports=u;var x=window.XMLHttpRequest=function(t){var n=new p(t);try{u.emit("new-xhr",[n],n),n.addEventListener(v,o,!1)}catch(e){try{u.emit("internal-error",[e])}catch(r){}}return n};if(c(p,x),x.prototype=p.prototype,d.inPlace(x.prototype,["open","send"],"-xhr-",s),u.on("send-xhr-start",function(t,n){r(t,n),i(n)}),u.on("open-xhr-start",r),h){var b=m&&m.resolve();if(!w&&!m){var E=1,R=document.createTextNode(E);new h(a).observe(R,{characterData:!0})}}else f.on("fn-end",function(t){t[0]&&t[0].type===v||a()})},{}],11:[function(t,n,e){function r(){var t=window.NREUM;if(!t.loader_config)return null;var n=(t.loader_config.accountID||"").toString()||null,e=(t.loader_config.agentID||"").toString()||null,r=(t.loader_config.trustKey||"").toString()||null;if(!n||!e)return null;var a=i.generateCatId(),s=i.generateCatId(),c=Date.now(),f=o(a,s,c,n,e,r);return{header:f,guid:a,traceId:s,timestamp:c}}function o(t,n,e,r,o,i){var a="btoa"in window&&"function"==typeof window.btoa;if(!a)return null;var s={v:[0,1],d:{ty:"Browser",ac:r,ap:o,id:t,tr:n,ti:e}};return i&&r!==i&&(s.d.tk=i),btoa(JSON.stringify(s))}var i=t(18);n.exports={generateTracePayload:r,generateTraceHeader:o}},{}],12:[function(t,n,e){function r(t){var n=this.params,e=this.metrics;if(!this.ended){this.ended=!0;for(var r=0;r<p;r++)t.removeEventListener(l[r],this.listener,!1);n.aborted||(e.duration=s.now()-this.startTime,this.loadCaptureCalled||4!==t.readyState?null==n.status&&(n.status=0):a(this,t),e.cbTime=this.cbTime,d.emit("xhr-done",[t],t),c("xhr",[n,e,this.startTime]))}}function o(t,n){var e=t.responseType;if("json"===e&&null!==n)return n;var r="arraybuffer"===e||"blob"===e||"json"===e?t.response:t.responseText;return w(r)}function i(t,n){var e=f(n),r=t.params;r.host=e.hostname+":"+e.port,r.pathname=e.pathname,t.sameOrigin=e.sameOrigin}function a(t,n){t.params.status=n.status;var e=o(n,t.lastSize);if(e&&(t.metrics.rxSize=e),t.sameOrigin){var r=n.getResponseHeader("X-NewRelic-App-Data");r&&(t.params.cat=r.split(", ").pop())}t.loadCaptureCalled=!0}var s=t("loader");if(s.xhrWrappable){var c=t("handle"),f=t(13),u=t(11).generateTracePayload,d=t("ee"),l=["load","error","abort","timeout"],p=l.length,h=t("id"),m=t(16),w=t(15),v=window.XMLHttpRequest;s.features.xhr=!0,t(10),t(6),d.on("new-xhr",function(t){var n=this;n.totalCbs=0,n.called=0,n.cbTime=0,n.end=r,n.ended=!1,n.xhrGuids={},n.lastSize=null,n.loadCaptureCalled=!1,t.addEventListener("load",function(e){a(n,t)},!1),m&&(m>34||m<10)||window.opera||t.addEventListener("progress",function(t){n.lastSize=t.loaded},!1)}),d.on("open-xhr-start",function(t){this.params={method:t[0]},i(this,t[1]),this.metrics={}}),d.on("open-xhr-end",function(t,n){"loader_config"in NREUM&&"xpid"in NREUM.loader_config&&this.sameOrigin&&n.setRequestHeader("X-NewRelic-ID",NREUM.loader_config.xpid);var e=!1;if("init"in NREUM&&"distributed_tracing"in NREUM.init&&(e=!!NREUM.init.distributed_tracing.enabled),e&&this.sameOrigin){var r=u();r&&r.header&&(n.setRequestHeader("newrelic",r.header),this.dt=r)}}),d.on("send-xhr-start",function(t,n){var e=this.metrics,r=t[0],o=this;if(e&&r){var i=w(r);i&&(e.txSize=i)}this.startTime=s.now(),this.listener=function(t){try{"abort"!==t.type||o.loadCaptureCalled||(o.params.aborted=!0),("load"!==t.type||o.called===o.totalCbs&&(o.onloadCalled||"function"!=typeof n.onload))&&o.end(n)}catch(e){try{d.emit("internal-error",[e])}catch(r){}}};for(var a=0;a<p;a++)n.addEventListener(l[a],this.listener,!1)}),d.on("xhr-cb-time",function(t,n,e){this.cbTime+=t,n?this.onloadCalled=!0:this.called+=1,this.called!==this.totalCbs||!this.onloadCalled&&"function"==typeof e.onload||this.end(e)}),d.on("xhr-load-added",function(t,n){var e=""+h(t)+!!n;this.xhrGuids&&!this.xhrGuids[e]&&(this.xhrGuids[e]=!0,this.totalCbs+=1)}),d.on("xhr-load-removed",function(t,n){var e=""+h(t)+!!n;this.xhrGuids&&this.xhrGuids[e]&&(delete this.xhrGuids[e],this.totalCbs-=1)}),d.on("addEventListener-end",function(t,n){n instanceof v&&"load"===t[0]&&d.emit("xhr-load-added",[t[1],t[2]],n)}),d.on("removeEventListener-end",function(t,n){n instanceof v&&"load"===t[0]&&d.emit("xhr-load-removed",[t[1],t[2]],n)}),d.on("fn-start",function(t,n,e){n instanceof v&&("onload"===e&&(this.onload=!0),("load"===(t[0]&&t[0].type)||this.onload)&&(this.xhrCbStart=s.now()))}),d.on("fn-end",function(t,n){this.xhrCbStart&&d.emit("xhr-cb-time",[s.now()-this.xhrCbStart,this.onload,n],n)}),d.on("fetch-before-start",function(t){var n,e=t[1]||{};"string"==typeof t[0]?n=t[0]:t[0]&&t[0].url&&(n=t[0].url),n&&(this.sameOrigin=f(n).sameOrigin);var r=!1;if("init"in NREUM&&"distributed_tracing"in NREUM.init&&(r=!!NREUM.init.distributed_tracing.enabled),r&&this.sameOrigin){var o=u();if(!o||!o.header)return;var i=o.header;if("string"==typeof t[0]){var a={};for(var s in e)a[s]=e[s];a.headers=new Headers(e.headers||{}),a.headers.set("newrelic",i),this.dt=o,t.length>1?t[1]=a:t.push(a)}else t[0]&&t[0].headers&&(t[0].headers.append("newrelic",i),this.dt=o)}})}},{}],13:[function(t,n,e){n.exports=function(t){var n=document.createElement("a"),e=window.location,r={};n.href=t,r.port=n.port;var o=n.href.split("://");!r.port&&o[1]&&(r.port=o[1].split("/")[0].split("@").pop().split(":")[1]),r.port&&"0"!==r.port||(r.port="https"===o[0]?"443":"80"),r.hostname=n.hostname||e.hostname,r.pathname=n.pathname,r.protocol=o[0],"/"!==r.pathname.charAt(0)&&(r.pathname="/"+r.pathname);var i=!n.protocol||":"===n.protocol||n.protocol===e.protocol,a=n.hostname===document.domain&&n.port===e.port;return r.sameOrigin=i&&(!n.hostname||a),r}},{}],14:[function(t,n,e){function r(){}function o(t,n,e){return function(){return i(t,[f.now()].concat(s(arguments)),n?null:this,e),n?void 0:this}}var i=t("handle"),a=t(20),s=t(21),c=t("ee").get("tracer"),f=t("loader"),u=NREUM;"undefined"==typeof window.newrelic&&(newrelic=u);var d=["setPageViewName","setCustomAttribute","setErrorHandler","finished","addToTrace","inlineHit","addRelease"],l="api-",p=l+"ixn-";a(d,function(t,n){u[n]=o(l+n,!0,"api")}),u.addPageAction=o(l+"addPageAction",!0),u.setCurrentRouteName=o(l+"routeName",!0),n.exports=newrelic,u.interaction=function(){return(new r).get()};var h=r.prototype={createTracer:function(t,n){var e={},r=this,o="function"==typeof n;return i(p+"tracer",[f.now(),t,e],r),function(){if(c.emit((o?"":"no-")+"fn-start",[f.now(),r,o],e),o)try{return n.apply(this,arguments)}catch(t){throw c.emit("fn-err",[arguments,this,t],e),t}finally{c.emit("fn-end",[f.now()],e)}}}};a("actionText,setName,setAttribute,save,ignore,onEnd,getContext,end,get".split(","),function(t,n){h[n]=o(p+n)}),newrelic.noticeError=function(t,n){"string"==typeof t&&(t=new Error(t)),i("err",[t,f.now(),!1,n])}},{}],15:[function(t,n,e){n.exports=function(t){if("string"==typeof t&&t.length)return t.length;if("object"==typeof t){if("undefined"!=typeof ArrayBuffer&&t instanceof ArrayBuffer&&t.byteLength)return t.byteLength;if("undefined"!=typeof Blob&&t instanceof Blob&&t.size)return t.size;if(!("undefined"!=typeof FormData&&t instanceof FormData))try{return JSON.stringify(t).length}catch(n){return}}}},{}],16:[function(t,n,e){var r=0,o=navigator.userAgent.match(/Firefox[\/\s](\d+\.\d+)/);o&&(r=+o[1]),n.exports=r},{}],17:[function(t,n,e){function r(t,n){var e=t.getEntries();e.forEach(function(t){"first-paint"===t.name?a("timing",["fp",Math.floor(t.startTime)]):"first-contentful-paint"===t.name&&a("timing",["fcp",Math.floor(t.startTime)])})}function o(t){if(t instanceof c&&!u){var n,e=Math.round(t.timeStamp);n=e>1e12?Date.now()-e:s.now()-e,u=!0,a("timing",["fi",e,{type:t.type,fid:n}])}}if(!("init"in NREUM&&"page_view_timing"in NREUM.init&&"enabled"in NREUM.init.page_view_timing&&NREUM.init.page_view_timing.enabled===!1)){var i,a=t("handle"),s=t("loader"),c=NREUM.o.EV;if("PerformanceObserver"in window&&"function"==typeof window.PerformanceObserver){i=new PerformanceObserver(r);try{i.observe({entryTypes:["paint"]})}catch(f){}}if("addEventListener"in document){var u=!1,d=["click","keydown","mousedown","pointerdown","touchstart"];d.forEach(function(t){document.addEventListener(t,o,!1)})}}},{}],18:[function(t,n,e){function r(){function t(){return n?15&n[e++]:16*Math.random()|0}var n=null,e=0,r=window.crypto||window.msCrypto;r&&r.getRandomValues&&(n=r.getRandomValues(new Uint8Array(31)));for(var o,i="xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx",a="",s=0;s<i.length;s++)o=i[s],"x"===o?a+=t().toString(16):"y"===o?(o=3&t()|8,a+=o.toString(16)):a+=o;return a}function o(){function t(){return n?15&n[e++]:16*Math.random()|0}var n=null,e=0,r=window.crypto||window.msCrypto;r&&r.getRandomValues&&Uint8Array&&(n=r.getRandomValues(new Uint8Array(31)));for(var o=[],i=0;i<16;i++)o.push(t().toString(16));return o.join("")}n.exports={generateUuid:r,generateCatId:o}},{}],19:[function(t,n,e){function r(t,n){if(!o)return!1;if(t!==o)return!1;if(!n)return!0;if(!i)return!1;for(var e=i.split("."),r=n.split("."),a=0;a<r.length;a++)if(r[a]!==e[a])return!1;return!0}var o=null,i=null,a=/Version\/(\S+)\s+Safari/;if(navigator.userAgent){var s=navigator.userAgent,c=s.match(a);c&&s.indexOf("Chrome")===-1&&s.indexOf("Chromium")===-1&&(o="Safari",i=c[1])}n.exports={agent:o,version:i,match:r}},{}],20:[function(t,n,e){function r(t,n){var e=[],r="",i=0;for(r in t)o.call(t,r)&&(e[i]=n(r,t[r]),i+=1);return e}var o=Object.prototype.hasOwnProperty;n.exports=r},{}],21:[function(t,n,e){function r(t,n,e){n||(n=0),"undefined"==typeof e&&(e=t?t.length:0);for(var r=-1,o=e-n||0,i=Array(o<0?0:o);++r<o;)i[r]=t[n+r];return i}n.exports=r},{}],22:[function(t,n,e){n.exports={exists:"undefined"!=typeof window.performance&&window.performance.timing&&"undefined"!=typeof window.performance.timing.navigationStart}},{}],ee:[function(t,n,e){function r(){}function o(t){function n(t){return t&&t instanceof r?t:t?c(t,s,i):i()}function e(e,r,o,i){if(!l.aborted||i){t&&t(e,r,o);for(var a=n(o),s=m(e),c=s.length,f=0;f<c;f++)s[f].apply(a,r);var d=u[y[e]];return d&&d.push([x,e,r,a]),a}}function p(t,n){g[t]=m(t).concat(n)}function h(t,n){var e=g[t];if(e)for(var r=0;r<e.length;r++)e[r]===n&&e.splice(r,1)}function m(t){return g[t]||[]}function w(t){return d[t]=d[t]||o(e)}function v(t,n){f(t,function(t,e){n=n||"feature",y[e]=n,n in u||(u[n]=[])})}var g={},y={},x={on:p,addEventListener:p,removeEventListener:h,emit:e,get:w,listeners:m,context:n,buffer:v,abort:a,aborted:!1};return x}function i(){return new r}function a(){(u.api||u.feature)&&(l.aborted=!0,u=l.backlog={})}var s="nr@context",c=t("gos"),f=t(20),u={},d={},l=n.exports=o();l.backlog=u},{}],gos:[function(t,n,e){function r(t,n,e){if(o.call(t,n))return t[n];var r=e();if(Object.defineProperty&&Object.keys)try{return Object.defineProperty(t,n,{value:r,writable:!0,enumerable:!1}),r}catch(i){}return t[n]=r,r}var o=Object.prototype.hasOwnProperty;n.exports=r},{}],handle:[function(t,n,e){function r(t,n,e,r){o.buffer([t],r),o.emit(t,n,e)}var o=t("ee").get("handle");n.exports=r,r.ee=o},{}],id:[function(t,n,e){function r(t){var n=typeof t;return!t||"object"!==n&&"function"!==n?-1:t===window?0:a(t,i,function(){return o++})}var o=1,i="nr@id",a=t("gos");n.exports=r},{}],loader:[function(t,n,e){function r(){if(!E++){var t=b.info=NREUM.info,n=p.getElementsByTagName("script")[0];if(setTimeout(u.abort,3e4),!(t&&t.licenseKey&&t.applicationID&&n))return u.abort();f(y,function(n,e){t[n]||(t[n]=e)}),c("mark",["onload",a()+b.offset],null,"api");var e=p.createElement("script");e.src="https://"+t.agent,n.parentNode.insertBefore(e,n)}}function o(){"complete"===p.readyState&&i()}function i(){c("mark",["domContent",a()+b.offset],null,"api")}function a(){return R.exists&&performance.now?Math.round(performance.now()):(s=Math.max((new Date).getTime(),s))-b.offset}var s=(new Date).getTime(),c=t("handle"),f=t(20),u=t("ee"),d=t(19),l=window,p=l.document,h="addEventListener",m="attachEvent",w=l.XMLHttpRequest,v=w&&w.prototype;NREUM.o={ST:setTimeout,SI:l.setImmediate,CT:clearTimeout,XHR:w,REQ:l.Request,EV:l.Event,PR:l.Promise,MO:l.MutationObserver};var g=""+location,y={beacon:"bam.nr-data.net",errorBeacon:"bam.nr-data.net",agent:"js-agent.newrelic.com/nr-1153.min.js"},x=w&&v&&v[h]&&!/CriOS/.test(navigator.userAgent),b=n.exports={offset:s,now:a,origin:g,features:{},xhrWrappable:x,userAgent:d};t(14),t(17),p[h]?(p[h]("DOMContentLoaded",i,!1),l[h]("load",r,!1)):(p[m]("onreadystatechange",o),l[m]("onload",r)),c("mark",["firstbyte",s],null,"api");var E=0,R=t(22)},{}],"wrap-function":[function(t,n,e){function r(t){return!(t&&t instanceof Function&&t.apply&&!t[a])}var o=t("ee"),i=t(21),a="nr@original",s=Object.prototype.hasOwnProperty,c=!1;n.exports=function(t,n){function e(t,n,e,o){function nrWrapper(){var r,a,s,c;try{a=this,r=i(arguments),s="function"==typeof e?e(r,a):e||{}}catch(f){l([f,"",[r,a,o],s])}u(n+"start",[r,a,o],s);try{return c=t.apply(a,r)}catch(d){throw u(n+"err",[r,a,d],s),d}finally{u(n+"end",[r,a,c],s)}}return r(t)?t:(n||(n=""),nrWrapper[a]=t,d(t,nrWrapper),nrWrapper)}function f(t,n,o,i){o||(o="");var a,s,c,f="-"===o.charAt(0);for(c=0;c<n.length;c++)s=n[c],a=t[s],r(a)||(t[s]=e(a,f?s+o:o,i,s))}function u(e,r,o){if(!c||n){var i=c;c=!0;try{t.emit(e,r,o,n)}catch(a){l([a,e,r,o])}c=i}}function d(t,n){if(Object.defineProperty&&Object.keys)try{var e=Object.keys(t);return e.forEach(function(e){Object.defineProperty(n,e,{get:function(){return t[e]},set:function(n){return t[e]=n,n}})}),n}catch(r){l([r])}for(var o in t)s.call(t,o)&&(n[o]=t[o]);return n}function l(n){try{t.emit("internal-error",n)}catch(e){}}return t||(t=o),e.inPlace=f,e.flag=a,e}},{}]},{},["loader",2,12,4,3]);</script>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>First Midwest Bank - Personal Loan Company Reviews | LendingTree</title>
<script data-cfasync='false'>
			window.disabletargetbodyhiding = true;
		</script>

<meta name="description" content="Use LendingTree&amp;apos;s lender ratings &amp; reviews as a resource to help you find out how our consumers have rated First Midwest Bank." />
<link rel="canonical" href="https://www.lendingtree.com/personal/reviews/first-midwest-bank/" />
<script type='application/ld+json' class='yoast-schema-graph yoast-schema-graph--main'>{"@context":"https://schema.org","@graph":[{"@type":"WebSite","@id":"https://www.lendingtree.com/#website","url":"https://www.lendingtree.com/","name":"LendingTree","potentialAction":{"@type":"SearchAction","target":"https://www.lendingtree.com/?s={search_term_string}","query-input":"required name=search_term_string"}},{"@type":"WebPage","@id":"#webpage","url":false,"inLanguage":"en-US","name":"First Midwest Bank - Personal Loan Company Reviews | LendingTree","isPartOf":{"@id":"https://www.lendingtree.com/#website"},"description":"Use LendingTree&apos;s lender ratings &amp; reviews as a resource to help you find out how our consumers have rated First Midwest Bank."}]}</script>

<link rel="preconnect" href="https://dpm.demdex.net/" crossorigin><link rel="preconnect" href="https://lendingtreellc.tt.omtrdc.net/" crossorigin><link rel='stylesheet' id='sage/css-css' href='https://www.lendingtree.com/content/themes/lt-wp-www-theme/dist/styles/main-v2-0b7afe55ab.css?ver=v2.1' type='text/css' media='all' />
<link rel='stylesheet' id='review-css' href='https://www.lendingtree.com/content/themes/lt-wp-www-theme/dist/styles/review-0eef24d1ad.css?ver=5.2.4' type='text/css' media='all' />
<style id='rocket-lazyload-inline-css' type='text/css'>
.rll-youtube-player{position:relative;padding-bottom:56.23%;height:0;overflow:hidden;max-width:100%;}.rll-youtube-player iframe{position:absolute;top:0;left:0;width:100%;height:100%;z-index:100;background:0 0}.rll-youtube-player img{bottom:0;display:block;left:0;margin:auto;max-width:100%;width:100%;position:absolute;right:0;top:0;border:none;height:auto;cursor:pointer;-webkit-transition:.4s all;-moz-transition:.4s all;transition:.4s all}.rll-youtube-player img:hover{-webkit-filter:brightness(75%)}.rll-youtube-player .play{height:72px;width:72px;left:50%;top:50%;margin-left:-36px;margin-top:-36px;position:absolute;background:url(https://www.lendingtree.com/content/plugins/rocket-lazy-load/assets/img/youtube.png) no-repeat;cursor:pointer}
</style>
<script data-cfasync='false' type='text/javascript'>
    window.launch_key = 'EN21cb38a11dec4a578659a774081ffe40';
    function targetPageParams() {
        return {
                entity: {
                    id: '',
                    name: '',
                    categoryId: '',
                    pageURL: '',
                    thumbnailURL: '',
                    pageType: 'index'
            },
                user: {
                    categoryId: '',
                    pageType: 'index'
            }
        }
    }
    
</script>
<script data-cfasync='false' type='text/javascript' src='https://www.lendingtree.com/analytics/lta-launchstrap.min.js'></script>
<script type="5870d3775a1169cbe2c6706a-text/javascript" src='https://www.lendingtree.com/content/themes/lt-wp-www-theme/dist/scripts/jquery.js?ver=3.3.1'></script>
<noscript><style id="rocket-lazyload-nojs-css">.rll-youtube-player, [data-lazy-src]{display:none !important;}</style></noscript> <link rel="search" href="
     https://www.lendingtree.com/content/plugins/lt-search/xml/search-prod.xml" type="application/opensearchdescription+xml" title="Lending Tree" />
</head> <body>
<a class="visually-hidden skip-link" href="#main">Skip to main content</a>
<header class="mainHeader hidden-xs">
<div class="container">
<div class="row">
<div class="col-md-1 col-sm-2 menuNav">
<a class="button-nav-toggle"><span></span>Menu</a>
</div>
<div class="col-md-1 col-sm-2 mainProducts">
<a>Products<span class="lt4-ChevronDown"></span></a>
</div>
<div class="col-md-2 col-sm-2 logoMain glob-marg">
<a class="logo" href="https://www.lendingtree.com" title="LendingTree">LendingTree</a>
</div>
<div class="col-md-5 col-sm-5 pull-right ltNav">
<div class="ltSignIn">
<p class="ltFCS"><a href="https://my.lendingtree.com/Signup">Sign up for Free</a></p>
<p class="ltSign"><a class="signin" href="https://www.lendingtree.com/account/logon?icid=header+signin" rel="nofollow">Log in</a></p>
<p class="ltNum"><a href="tel:+18008134620" rel="nofollow">1-800-813-4620</a></p>
</div>
<div class="col-md-1 col-sm-1 pull-right ltSearch">
<button class="lt4-Search"></button>
</div>
<div class="ltMember"></div>
</div>
</div>
</div>
<div class="col-xs-12 mainSearchBar">
<div class="container glob-marg">
<div class="row desktop-search">
<div class="search-section">
<div>
<form role="search" method="get" class="search-form form-inline" action="https://www.lendingtree.com/index.php">
<label class="form-group">
<span class="lt4-Search"></span>
<input type="search" class="search-field form-control" placeholder="Search LendingTree" value="" name="s" autocomplete="off" aria-label="Search LendingTree" />
<span class="lt4-Ex clear-search"></span>
</label>
<button type="submit" class="search-submit btn btn-orange">Search</button>
</form>
</div>
</div> </div>
</div>
</div>
<div class="col-xs-12 glob-marg productNav">
<div class="container glob-marg">
<div class="row">
<div class="col-sm-12 col-md-10 col-lg-10 glob-marg">
<div class="carousel-conrol-white owl-carousel owl-centered" id="prodNav-carousel">
<a class="col-md-2 col-sm-2 productSelection" href="https://www.lendingtree.com/redirect/offers?id=wp-refinance&icid=header+refi" rel="nofollow">
<div class="item"><span class="lt4-Refinance icon"></span><p class="title">Home Refinance</p></div>
</a>
<a class="col-md-2 col-sm-2 productSelection" href="https://www.lendingtree.com/redirect/offers?id=wp-mortgage&icid=header+pur" rel="nofollow">
<div class="item"><span class="lt4-Mortgage icon"></span><p class="title">Home Purchase</p></div>
</a>
<a class="col-md-2 col-sm-2 productSelection" href="https://www.lendingtree.com/redirect/offers?id=wp-personal&icid=header+pl" rel="nofollow">
<div class="item"><span class="lt4-DollarSign icon"></span><p class="title">Personal Loans</p></div>
</a>
<a class="col-md-2 col-sm-2 productSelection" href="https://www.lendingtree.com/redirect/offers?id=cc-cw-main&icid=header+cc" rel="nofollow">
<div class="item"><span class="lt4-CreditCards icon"></span><p class="title">Credit Cards</p></div>
</a>
<a class="col-md-2 col-sm-2 productSelection" href="https://www.lendingtree.com/redirect/offers?id=wp-home-equity&icid=header+homeeq" rel="nofollow">
<div class="item"><span class="lt4-HomeEquity icon"></span><p class="title">Home Equity</p></div>
</a>
<a class="col-md-2 col-sm-2 productSelection" href="https://www.lendingtree.com/redirect/offers?id=wp-auto&icid=header+auto" rel="nofollow">
<div class="item"><span class="lt4-Autos icon"></span><p class="title">Auto Loans</p></div>
</a>
<a class="col-md-2 col-sm-2 productSelection" href="https://www.lendingtree.com/redirect/offers?id=wp-business&icid=header+bus" rel="nofollow">
<div class="item"><span class="lt4-BusinessLoans icon"></span><p class="title">Business Loans</p></div>
</a>
<a class="col-md-2 col-sm-2 productSelection" href="https://www.lendingtree.com/redirect/offers?id=wp-student&icid=header+sl" rel="nofollow">
<div class="item"><span class="lt4-Student icon"></span><p class="title">Student Loans</p></div>
</a>
<a class="col-md-2 col-sm-2 productSelection" href="https://www.lendingtree.com/debt-relief/?icid=header+debt">
<div class="item"><span class="lt4-DebtRelief icon"></span><p class="title">Debt Relief</p></div>
</a>
 <a class="col-md-2 col-sm-2 productSelection" href="https://www.lendingtree.com/insurance/?icid=header+ins">
<div class="item"><span class="lt4-Umbrella icon"></span><p class="title">Insurance</p></div>
</a>
<a class="col-md-2 col-sm-2 productSelection" href="https://www.lendingtree.com/credit-repair/?icid=header+cr">
<div class="item"><span class="lt4-CreditRepair icon"></span><p class="title">Credit Repair</p></div>
</a>
<a class="col-md-2 col-sm-2 productSelection" href="https://www.lendingtree.com/banking/?icid=header+bank">
<div class="item"><span class="lt4-PiggyBank icon"></span><p class="title">Banking Products</p></div>
</a>
<a class="col-md-2 col-sm-2 productSelection" href="https://www.lendingtree.com/lp/credit-analyzer.html?icid=header+cda">
<div class="item"><span class="lt4-Target icon"></span><p class="title">Credit/Debt Analyzer</p></div>
</a>
</div>
</div>
</div>
</div>
</div>
<div class="col-xs-12 glob-marg myLTprofile" id="myLTprofile">
</div>
</header>
<div id="mobileHead" class="mobileHeader visible-xs">
<ul class="mobile-nav">
<li class="mobile-login">
<a id="login-link" href="https://www.lendingtree.com/account/logon">
<img src="https://www.lendingtree.com/content/themes/lt-wp-www-theme/dist/images/people-white2.png" width="50" height="50" alt="Login" class="people-img" />
<img src="https://www.lendingtree.com/content/themes/lt-wp-www-theme/dist/images/people-active.png" width="50" height="50" alt="Login" class="people-active-img" />
</a>
</li>
<li class="mobile-logo">
<a href="https://www.lendingtree.com" data-transition="fade">
<span>
<img src="https://www.lendingtree.com/content/themes/lt-wp-www-theme/dist/images/lt-logo.svg" width="161" height="48" alt="Lending Tree" />
</span>
</a>
</li>
<li class="slide-panel">
<a class="button-nav-toggle"><span></span></a>
</li>
</ul>
</div>
<nav class="nav-main" itemscope itemtype="https://schema.org/SiteNavigationElement">
<div class="nav-container">
<ul class="mainMenu">
<li class="searchline">
<div class="slide-pad mobile-search">
<div class="search-section">
<div>
<form role="search" method="get" class="search-form form-inline" action="https://www.lendingtree.com/index.php">
<label class="form-group">
<span class="lt4-Search"></span>
<input id="search-term-header" type="search" class="search-field form-control" placeholder="Search LendingTree" value="" name="s" autocomplete="off" aria-label="Search LendingTree" />
<span class="clear-search">Clear</span>
</label>
<button type="submit" class="search-submit btn btn-orange">Search</button>
</form>
</div>
</div> </div>
<div class="clear-fix"></div>
</li>
<li><a class="subMenuTrigger"><span class="navIcon lt4-Mortgage"></span>Home Loans<span class="arrow lt4-ChevronRight"></span></a>
<ul class="subMenu">
<li><a class="subMenuBack"><span class="backarrow lt4-ChevronLeft"></span>Main Menu</a></li>
<li><a href="https://www.lendingtree.com/home/" itemprop="url">Home Loans</a></li>
<li><a href="https://www.lendingtree.com/home/refinance/" itemprop="url">Refinance</a></li>
<li><a href="https://www.lendingtree.com/home/mortgage/" itemprop="url">Mortgage</a></li>
<li><a href="https://www.lendingtree.com/home/home-equity/" itemprop="url">Home Equity Loans</a></li>
<li><a href="https://www.lendingtree.com/home/home-equity/heloc/" itemprop="url">Home Equity Line of Credit</a></li>
<li><a href="https://www.lendingtree.com/home/reverse/" itemprop="url">Reverse Mortgage</a></li>
<li><a href="https://www.lendingtree.com/insurance/home/" itemprop="url">Home Insurance</a></li>
<li><a href="https://www.lendingtree.com/home/fha/" itemprop="url">FHA Loans</a></li>
<li><a href="https://www.lendingtree.com/home/va/" itemprop="url">VA Loans</a></li>
<li>
<a class="subLevelTrigger"><span class="navIcon lt4-Calculator"></span>Calculators<span class="arrow lt4-ChevronRight"></span></a>
<ul class="subLevel">
<li><a class="subLevelBack"><span class="backarrow lt4-ChevronLeft"></span>Home Loans</a></li>
<li><a href="https://www.lendingtree.com/home/mortgage/calculators/mortgage-payment/">Mortgage Calculator</a></li>
<li><a href="https://www.lendingtree.com/home/mortgage/calculators/home-affordability/">Home Affordability Calculator</a></li>
<li><a href="https://www.lendingtree.com/home/mortgage/calculators/refinance/">Refinance Calculator</a></li>
<li><a href="https://www.lendingtree.com/home/mortgage/calculators/fha/">FHA Loan Calculator</a></li>
<li><a href="https://www.lendingtree.com/home/mortgage/calculators/va/">VA Loan Calculator</a></li>
<li><a href="https://www.lendingtree.com/home/mortgage/calculators/cash-out-refinance/">Cash-out Refinance Calculator</a></li>
<li><a href="https://www.lendingtree.com/home/mortgage/calculators/home-equity/">Home Equity Loan Calculator</a></li>
<li><a href="https://www.lendingtree.com/home/mortgage/calculators/reverse/">Reverse Mortgage Calculator</a></li>
<li><a href="https://www.lendingtree.com/home/mortgage/calculators/rent-vs-buy/">Rent Vs. Buy Calculator</a></li>
</ul>
</li>
<li>
<a class="subLevelTrigger"><span class="navIcon lt4-Document"></span>Resources<span class="arrow lt4-ChevronRight"></span></a>
<ul class="subLevel">
<li><a class="subLevelBack"><span class="backarrow lt4-ChevronLeft"></span>Home Loans</a></li>
<li><a href="https://www.lendingtree.com/home/mortgage/rates/" itemprop="url">Mortgage Rates</a></li>
<li><a href="https://www.lendingtree.com/home/refinance/rates/" itemprop="url">Refinance Rates</a></li>
<li><a href="https://www.lendingtree.com/home/fha/rates/" itemprop="url">FHA Rates</a></li>
<li><a href="https://www.lendingtree.com/home/va/rates/" itemprop="url">VA Rates</a></li>
<li><a href="https://www.lendingtree.com/homevalue/" itemprop="url">Check Home Value</a></li>
<li><a href="https://www.lendingtree.com/reviews/mortgage/" itemprop="url">Mortgage Lender Reviews</a></li>
<li><a href="https://loanofficers.lendingtree.com/" itemprop="url" rel="nofollow">Loan Officer Directory</a></li>
<li><a href="https://www.lendingtree.com/glossary/" itemprop="url" rel="nofollow">Glossary</a></li>
</ul>
</li>
</ul>
</li>
<li><a class="subMenuTrigger"><span class="navIcon lt4-Autos"></span>Auto Loans<span class="arrow lt4-ChevronRight"></span></a>
<ul class="subMenu">
<li><a class="subMenuBack"><span class="backarrow lt4-ChevronLeft"></span>Main Menu</a></li>
<li><a href="https://www.lendingtree.com/auto/" itemprop="url">Auto Loans</a></li>
<li><a href="https://www.lendingtree.com/auto/refinance/" itemprop="url">Auto Refinance</a></li>
<li><a href="https://www.lendingtree.com/insurance/auto/" itemprop="url">Auto Insurance</a></li>
<li><a href="https://www.lendingtree.com/boat/" itemprop="url">Boat Loans</a></li>
<li><a href="https://www.lendingtree.com/auto/rv/" itemprop="url">RV Loans</a></li>
<li><a href="https://www.lendingtree.com/auto/motorcycle/" itemprop="url">Motorcycle Loans</a></li>
<li><a href="https://www.lendingtree.com/auto/powersport/" itemprop="url">Powersport Loans</a></li>
<li><a href="https://www.lendingtree.com/auto/financing/" itemprop="url">New Car Financing</a></li>
<li>
<a class="subLevelTrigger"><span class="navIcon lt4-Calculator"></span>Calculators<span class="arrow lt4-ChevronRight"></span></a>
<ul class="subLevel">
<li><a class="subLevelBack"><span class="backarrow lt4-ChevronLeft"></span>Auto Loans</a></li>
<li><a href="https://www.lendingtree.com/auto/calculators/" itemprop="url">Auto Calculators</a></li>
<li><a href="https://www.lendingtree.com/auto/calculators/payment/" itemprop="url">Auto Loan Calculator</a></li>
<li><a href="https://www.lendingtree.com/auto/calculators/refinance/" itemprop="url">Auto Refinance Calculator</a></li>
<li><a href="https://www.lendingtree.com/auto/calculators/affordability/" itemprop="url">Auto Affordability Calculator</a></li>
</ul>
</li>
<li>
<a class="subLevelTrigger"><span class="navIcon lt4-Document"></span>Resources<span class="arrow lt4-ChevronRight"></span></a>
<ul class="subLevel">
<li><a class="subLevelBack"><span class="backarrow lt4-ChevronLeft"></span>Auto Loans</a></li>
<li><a href="https://www.lendingtree.com/reviews/auto/" itemprop="url">Auto Lender Reviews</a></li>
<li><a href="https://www.lendingtree.com/glossary/" itemprop="url" rel="nofollow">Glossary</a></li>
</ul>
</li>
</ul>
</li>
<li><a class="subMenuTrigger"><span class="navIcon lt4-DollarSign"></span>Personal Loans<span class="arrow lt4-ChevronRight"></span></a>
<ul class="subMenu">
<li><a class="subMenuBack"><span class="backarrow lt4-ChevronLeft"></span>Main Menu</a></li>
<li><a href="https://www.lendingtree.com/personal/" itemprop="url">Personal Loans</a></li>
<li><a href="https://www.lendingtree.com/debt-consolidation/" itemprop="url">Debt Consolidation</a></li>
<li><a href="https://www.lendingtree.com/personal/unsecured/" itemprop="url">Unsecured Loans</a></li>
<li><a href="https://www.lendingtree.com/personal/holiday/" itemprop="url">Holiday Loans</a></li>
<li><a href="https://www.lendingtree.com/personal/pool-loans/" itemprop="url">Pool Loans</a></li>
<li><a href="https://www.lendingtree.com/personal/medical/dental-loans/" itemprop="url">Dental Loans</a></li>
<li><a href="https://www.lendingtree.com/personal/emergency/" itemprop="url">Emergency Loans</a></li>
<li>
<a class="subLevelTrigger"><span class="navIcon lt4-Calculator"></span>Calculators<span class="arrow lt4-ChevronRight"></span></a>
<ul class="subLevel">
<li><a class="subLevelBack"><span class="backarrow lt4-ChevronLeft"></span>Personal Loans</a></li>
<li><a href="https://www.lendingtree.com/personal/loan-payment-calculator/">Loan Payment Calculator</a></li>
<li><a href="https://www.lendingtree.com/debt-consolidation/debt-management-advisor-v2/">Debt Consolidation Calculator</a></li>
</ul>
</li>
<li>
<a class="subLevelTrigger"><span class="navIcon lt4-Document"></span>Resources<span class="arrow lt4-ChevronRight"></span></a>
<ul class="subLevel">
<li><a class="subLevelBack"><span class="backarrow lt4-ChevronLeft"></span>Personal Loans</a></li>
<li><a href="https://www.lendingtree.com/personal-loan-lender-reviews/" itemprop="url">Personal Loan Lender Consumer Reviews</a></li>
<li><a href="https://www.lendingtree.com/personal/reviews/" itemprop="url">Personal Loan In-Depth Lender Reviews</a></li>
<li><a href="https://www.lendingtree.com/glossary/" itemprop="url" rel="nofollow">Glossary</a></li>
</ul>
</li>
</ul>
</li>
<li>
<a class="subMenuTrigger"><span class="navIcon lt4-BusinessLoans"></span>Business Loans<span class="arrow lt4-ChevronRight"></span></a>
<ul class="subMenu">
<li><a class="subMenuBack"><span class="backarrow lt4-ChevronLeft"></span>Main Menu</a></li>
<li><a href="https://www.lendingtree.com/business/" itemprop="url">Business Loans</a></li>
<li><a href="https://www.lendingtree.com/business/small/" itemprop="url">Small Business Loans</a></li>
<li><a href="https://www.lendingtree.com/business/sba/" itemprop="url">SBA Loans</a></li>
<li><a href="https://www.lendingtree.com/business/short-term/" itemprop="url">Short Term Business Loans</a></li>
<li><a href="https://www.lendingtree.com/business/long-term/" itemprop="url">Long Term Business Loans</a></li>
<li><a href="https://www.lendingtree.com/business/line-of-credit/" itemprop="url">Business Line of Credit</a></li>
<li><a href="https://www.lendingtree.com/business/working-capital/" itemprop="url">Working Capital Loans</a></li>
<li><a href="https://www.lendingtree.com/business/equipment/" itemprop="url">Equipment Financing</a></li>
<li><a href="https://www.lendingtree.com/business/accounts-receivable/" itemprop="url">Accounts Receivable Financing</a></li>
<li><a href="https://www.lendingtree.com/business/merchant-cash-advance/" itemprop="url">Merchant Cash Advance</a></li>
<li><a href="https://creditcards.lendingtree.com/business/">Business Credit Cards</a></li>
<li>
<a class="subLevelTrigger"><span class="navIcon lt4-Calculator"></span>Calculators<span class="arrow lt4-ChevronRight"></span></a>
<ul class="subLevel">
<li><a class="subLevelBack"><span class="backarrow lt4-ChevronLeft"></span>Business Loans</a></li>
<li><a href="https://www.lendingtree.com/business/business-loan-calculator/" itemprop="url">Business Loan Calculator</a></li>
<li><a href="https://www.lendingtree.com/business/refinance-calculator/" itemprop="url">Business Loan Refinance Calculator</a></li>
</ul>
</li>
<li>
<a class="subLevelTrigger"><span class="navIcon lt4-Document"></span>Resources<span class="arrow lt4-ChevronRight"></span></a>
<ul class="subLevel">
<li><a class="subLevelBack"><span class="backarrow lt4-ChevronLeft"></span>Business Loans</a></li>
<li><a href="https://www.lendingtree.com/business-loan-lender-reviews/" itemprop="url">Business Loan Lender Consumer Reviews</a></li>
<li><a href="https://www.lendingtree.com/glossary/" itemprop="url" rel="nofollow">Glossary</a></li>
<li><a href="https://www.lendingtree.com/business/reviews/" itemprop="url">Business Loan In-Depth Lender Reviews</a></li>
<li><a href="https://www.lendingtree.com/business/growing/" itemprop="url">Growing a Business</a></li>
<li><a href="https://www.lendingtree.com/business/managing/" itemprop="url">Managing a Business</a></li>
<li><a href="https://www.lendingtree.com/business/starting/" itemprop="url">Starting a Business</a></li>
<li><a href="https://www.lendingtree.com/business/accounting/" itemprop="url">Small Business Accounting</a></li>
<li><a href="https://www.lendingtree.com/business/grant/" itemprop="url">Small Business Grants</a></li>
<li><a href="https://www.lendingtree.com/business/banking/" itemprop="url">Business Banking</a></li>
</ul>
</li>
</ul>
</li>
<li>
<a class="subMenuTrigger"><span class="navIcon lt4-Student"></span>Student Loans<span class="arrow lt4-ChevronRight"></span></a>
<ul class="subMenu">
<li><a class="subMenuBack"><span class="backarrow lt4-ChevronLeft"></span>Main Menu</a></li>
<li><a href="https://www.lendingtree.com/student/" itemprop="url">Student Loans</a></li>
<li><a href="https://www.lendingtree.com/student/refinance/" itemprop="url">Student Loan Refinance</a></li>
<li>
<a class="subLevelTrigger"><span class="navIcon lt4-Document"></span>Resources<span class="arrow lt4-ChevronRight"></span></a>
<ul class="subLevel">
<li><a class="subLevelBack"><span class="backarrow lt4-ChevronLeft"></span>Student Loans</a></li>
<li><a href="https://www.lendingtree.com/student/interest-rates/" itemprop="url">Student Loan Interest Rates</a></li>
<li><a href="https://www.lendingtree.com/reviews/student/" itemprop="url">Student Loan Lender Reviews</a></li>
<li><a href="https://www.lendingtree.com/glossary/" itemprop="url" rel="nofollow">Glossary</a></li>
</ul>
</li>
</ul>
</li>
<li>
<a class="subMenuTrigger"><span class="navIcon lt4-RatingReviews"></span>Ratings & Reviews<span class="arrow lt4-ChevronRight"></span></a>
<ul class="subMenu">
<li><a class="subMenuBack"><span class="backarrow lt4-ChevronLeft"></span>Main Menu</a></li>
<li><a href="https://www.lendingtree.com/reviews/" itemprop="url" rel="nofollow">Lender Reviews</a></li>
<li><a href="https://www.lendingtree.com/reviews/mortgage/" itemprop="url" rel="nofollow">Mortgage Lender Reviews</a></li>
<li><a href="https://loanofficers.lendingtree.com" itemprop="url" rel="nofollow">Loan Officer Directory</a></li>
<li><a href="https://www.lendingtree.com/reviews/personal/" itemprop="url" rel="nofollow">Personal Loan Lender Reviews</a></li>
<li><a href="https://www.lendingtree.com/reviews/business/" itemprop="url" rel="nofollow">Business Loan Lender Reviews</a></li>
<li><a href="https://www.lendingtree.com/reviews/auto/" itemprop="url" rel="nofollow">Auto Loan Lender Reviews</a></li>
<li><a href="https://www.lendingtree.com/reviews/student/" itemprop="url" rel="nofollow">Student Loan Lender Reviews</a></li>
<li><a href="https://www.lendingtree.com/reviews/credit-repair/" itemprop="url" rel="nofollow">Credit Repair Lender Reviews</a></li>
<li><a href="https://www.lendingtree.com/reviews/debt-relief/" itemprop="url" rel="nofollow">Debt Relief Lender Reviews</a></li>
</ul>
</li>
<li>
<a class="subMenuTrigger"><span class="navIcon lt4-CreditCards"></span>Credit Cards<span class="arrow lt4-ChevronRight"></span></a>
<ul class="subMenu">
<li><a class="subMenuBack"><span class="backarrow lt4-ChevronLeft"></span>Main Menu</a></li>
<li><a href="https://www.lendingtree.com/redirect/offers?id=cc-cw-main&Placement=Hp-Top-Menu-CreditCards" itemprop="url">Credit Cards</a></li>
<li><a href="https://creditcards.lendingtree.com/best-credit-card-offers" rel="nofollow">Featured Credit Cards</a></li>
<li><a href="https://creditcards.lendingtree.com/balance-transfer" rel="nofollow">Balance Transfer Credit Cards</a></li>
<li><a href="https://creditcards.lendingtree.com/cash-back" rel="nofollow">Cash Back Credit Cards</a></li>
<li><a href="https://creditcards.lendingtree.com/airline" rel="nofollow">Travel Credit Cards</a></li>
<li><a href="https://creditcards.lendingtree.com/reward" rel="nofollow">Rewards Credit Cards</a></li>
<li><a href="https://creditcards.lendingtree.com/low-interest" rel="nofollow">Low Interest</a></li>
<li><a href="https://creditcards.lendingtree.com/0-annual-fee-credit-cards" rel="nofollow">No Annual Fee Credit Cards</a></li>
 <li><a href="https://creditcards.lendingtree.com/business">Business Credit Cards</a></li>
<li><a href="https://creditcards.lendingtree.com/student" rel="nofollow">Student Credit Cards</a></li>
<li>
<a class="subLevelTrigger"><span class="navIcon lt4-CreditCards" rel="nofollow"></span>Cards by Credit Band<span class="arrow lt4-ChevronRight"></span></a>
<ul class="subLevel">
<li><a class="subLevelBack"><span class="backarrow lt4-ChevronLeft"></span>Credit Cards</a></li>
<li><a href="https://creditcards.lendingtree.com/credit-quality/excellent" rel="nofollow">Excellent Credit</a></li>
<li><a href="https://creditcards.lendingtree.com/credit-quality/good" rel="nofollow">Good Credit</a></li>
<li><a href="https://creditcards.lendingtree.com/credit-quality/fair" rel="nofollow">Fair Credit</a></li>
<li><a href="https://creditcards.lendingtree.com/credit-quality/bad" rel="nofollow">Poor Credit</a></li>
<li><a href="https://creditcards.lendingtree.com/credit-quality/no-credit" rel="nofollow">New Credit Users</a></li>
</ul>
</li>
<li>
<a class="subLevelTrigger"><span class="navIcon lt4-Document"></span>Resources<span class="arrow lt4-ChevronRight"></span></a>
<ul class="subLevel">
<li><a class="subLevelBack"><span class="backarrow lt4-ChevronLeft"></span>Credit Cards</a></li>
<li><a href="https://www.lendingtree.com/credit-cards/tips/" itemprop="url" rel="nofollow">Finding the Right Card</a></li>
<li><a href="https://www.lendingtree.com/debt-consolidation/debt-relief-calculator/" rel="nofollow">Debt Consolidation Calculator</a></li>
<li><a href="https://www.lendingtree.com/glossary/" itemprop="url" rel="nofollow">Glossary</a></li>
</ul>
</li>
</ul>
</li>
<li>
<a class="subMenuTrigger"><span class="navIcon lt4-CreditScore"></span>Free Credit Score<span class="arrow lt4-ChevronRight"></span></a>
<ul class="subMenu">
<li><a class="subMenuBack"><span class="backarrow lt4-ChevronLeft"></span>Main Menu</a></li>
<li><a href="https://my.lendingtree.com/Signup" itemprop="url">Sign up for Free</a></li>
<li><a href="https://www.lendingtree.com/credit-repair/" itemprop="url">Credit Repair</a></li>
<li><a href="https://www.lendingtree.com/lp/credit-analyzer.html?icid=header+cda" itemprop="url" rel="nofollow">Credit/Debt Analyzer</a></li>
<li><a href="https://my.lendingtree.com">My LendingTree</a> </li>
<li>
<a class="subLevelTrigger"><span class="navIcon lt4-Document"></span>Resources<span class="arrow lt4-ChevronRight"></span></a>
<ul class="subLevel">
<li><a class="subLevelBack"><span class="backarrow lt4-ChevronLeft"></span>Free Credit Score</a></li>
<li><a href="https://www.lendingtree.com/glossary/" itemprop="url" rel="nofollow">Glossary</a></li>
</ul>
</li>
</ul>
</li>
<li>
<a class="subMenuTrigger"><span class="navIcon lt4-PiggyBank"></span>Banking Products<span class="arrow lt4-ChevronRight"></span></a>
<ul class="subMenu">
<li><a class="subMenuBack"><span class="backarrow lt4-ChevronLeft"></span>Main Menu</a></li>
<li><a href="https://www.lendingtree.com/banking/" itemprop="url">Banking Products</a></li>
<li><a href="https://www.lendingtree.com/banking/savings/" itemprop="url">Savings Accounts</a></li>
<li><a href="https://www.lendingtree.com/banking/cd/" itemprop="url">Certificates of Deposit (CDS)</a></li>
<li><a href="https://www.lendingtree.com/banking/checking/" itemprop="url">Checking Accounts</a></li>
<li><a href="https://www.lendingtree.com/banking/money-market/" itemprop="url">Money Market Accounts</a></li>
<li><a href="https://www.lendingtree.com/banking/ira/" itemprop="url">IRA Accounts</a></li>
</ul>
</li>
<li>
<a class="subMenuTrigger"><span class="navIcon lt4-Checklist"></span>Financial Help<span class="arrow lt4-ChevronRight"></span></a>
<ul class="subMenu">
<li><a class="subMenuBack"><span class="backarrow lt4-ChevronLeft"></span>Main Menu</a></li>
<li><a href="https://www.lendingtree.com/debt-relief/" itemprop="url">Debt Relief</a></li>
<li><a href="https://www.lendingtree.com/credit-repair/" itemprop="url">Credit Repair</a></li>
<li><a href="https://www.lendingtree.com/lp/credit-analyzer.html?icid=header+cda" itemprop="url">Credit/Debt Analyzer</a></li>
<li><a href="https://www.lendingtree.com/bankruptcy/" itemprop="url">Understanding Bankruptcy</a></li>
</ul>
</li>
</ul>
<ul class="more-nav">
<li><h4>More From LendingTree</h4></li>
<li><a href="tel:+18882816836" rel="nofollow">Call Us</a></li>
<li><a href="https://www.lendingtree.com/press/" rel="nofollow">About LendingTree</a></li>
<li><a href="https://www.lendingtree.com/press/press-releases/" rel="nofollow">Press Room</a></li>
<li><a href="https://www.lendingtree.com/blog/">Blog</a></li>
<li><a href="https://www.lendingtree.com/about/partner-with-us/">Partner with Us</a></li>
</ul>
<ul class="sign-in-btn-block">
<li class="sign-in-link"><a href="https://www.lendingtree.com/account/logon" rel="nofollow">Sign In</a></li>
<li class="sign-out-link"><a href="https://www.lendingtree.com/account/LogOff" rel="nofollow">Sign Out</a></li>
</ul>
</div>
</nav>
<div class="clear-fix"></div>
<main id='main'>
<section class="mainLenderDetail">
<div class="container">
<div class="row">
<div class="col-xs-12 col-sm-12 col-md-12 lenderHeader">
<div class="col-xs-12 col-sm-5 col-md-4 lenderSignage">
<div class="lenderLogo">
<div class="img-container">
<img class="img-responsive" src="https://lt-scorecard-logo.s3.amazonaws.com/52903183SEO.gif" alt="First Midwest Bank">
</div>
</div>
<p class="lendNum"> NMLS# <a href="http://www.nmlsconsumeraccess.org/EntityDetails.aspx/COMPANY/423112" target="_blank">423112 </a> </p>
<div class="mainRating">
<div class="rating-stars-wrapper" itemprop="aggregateRating">
<div class="rating-stars-bottom">
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
</div>
<div class="rating-stars-top">
<div class="rating-stars-bar" style="width:98.6%;">
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
</div>
</div>
</div>
<p>4.9 of 5<span class="visually-hidden">stars</span><span><a href="#reviewBlockStart" class="scrolltoreview" aria-label="2255 reviews for First Midwest Bank">2255 Reviews</a></span></p>
</div>
</div>
<div class="col-md-7 col-sm-7 col-xs-12 lenderInfo">
<h1>First Midwest Bank</h1>
<ul class="lenderAwards">
<li>
<div class="recommend">
<img src="https://www.lendingtree.com/content/themes/lt-wp-www-theme/dist/images/lender-review/recc-100.png" class="img-responsive" alt="Recommended Lender">
<div class="recommend-text">
<small>Recommended</small>
<span>99%</span>
</div>
</div>
</li>
</ul>
<ul class="lenderAwardsMobile">
<li class="lenderAwardsMobileRatingBlock col-xs-6">
<div class="rating-stars-wrapper" itemprop="aggregateRating">
<div class="rating-stars-bottom">
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
</div>
<div class="rating-stars-top">
<div class="rating-stars-bar" style="width:98.6%;">
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
</div>
</div>
</div>
<p>4.9 of 5<span class="visually-hidden">stars</span><span><a href="#reviewBlockStart" class="scrolltoreview" aria-label="2255 reviews for First Midwest Bank">2255 Reviews</a></span></p>
</li>
<li class="col-xs-6">
<div class="recommend">
<div class="recommend-text">
<small>Recommended</small>
<span>99%</span>
</div>
</div>
</li>
</ul>
<a data-toggle="modal" data-target="#disclaimerModal" class="ratesBtn">View Rates</a>
<a data-toggle="modal" data-target="#review" data-backdrop="false" class="reviewBtn write-review" data-lendername="First Midwest Bank" data-lenderid="52903183" data-lenderreviewid="27085" data-vertical="personal">Write a Review</a>
</div>
</div>
<div class="col-md-12 col-sm-12 col-xs-12 lenderSummary">
<div class="col-md-4 col-sm-5 col-xs-12 rating">
<ul class="customer-satisfaction topCustSat">
<li><a data-target="#custSatisfactionModal" data-toggle="modal"><img class="img-responsive" src="https://www.lendingtree.com/content/themes/lt-wp-www-theme/dist/images/lender-review/TopRated-personal-winner.png" alt="Customer Satisfaction Award"> <span class="bg-yellow quarter-winner">Q3 2019</span></a></li>
<li><a data-target="#custSatisfactionModal" data-toggle="modal"><img class="img-responsive" src="https://www.lendingtree.com/content/themes/lt-wp-www-theme/dist/images/lender-review/TopRated-personal-winner.png" alt="Customer Satisfaction Award"> <span class="bg-yellow quarter-winner">Q2 2019</span></a></li>
<li><a data-target="#custSatisfactionModal" data-toggle="modal"><img class="img-responsive" src="https://www.lendingtree.com/content/themes/lt-wp-www-theme/dist/images/lender-review/TopRated-personal-winner.png" alt="Customer Satisfaction Award"> <span class="bg-yellow quarter-winner">Q1 2019</span></a></li>
<li><a data-target="#custSatisfactionModal" data-toggle="modal"><img class="img-responsive" src="https://www.lendingtree.com/content/themes/lt-wp-www-theme/dist/images/lender-review/TopRated-personal-winner.png" alt="Customer Satisfaction Award"> <span class="bg-yellow quarter-winner">Q4 2018</span></a></li>
</ul>
<ul class="customer-satisfaction topCustSatIcons">
<li><a data-target="#custSatisfactionModal" data-toggle="modal"><img class="img-responsive" src=" https://www.lendingtree.com/content/themes/lt-wp-www-theme/dist/images/lender-review/TopRated-personal-winner.png" alt="Customer Satisfaction Award"> <span class="bg-yellow quarter-winner">Q3 2019</span></a></li>
<li><a data-target="#custSatisfactionModal" data-toggle="modal"><img class="img-responsive" src=" https://www.lendingtree.com/content/themes/lt-wp-www-theme/dist/images/lender-review/TopRated-personal-winner.png" alt="Customer Satisfaction Award"> <span class="bg-yellow quarter-winner">Q2 2019</span></a></li>
<li><a data-target="#custSatisfactionModal" data-toggle="modal"><img class="img-responsive" src=" https://www.lendingtree.com/content/themes/lt-wp-www-theme/dist/images/lender-review/TopRated-personal-winner.png" alt="Customer Satisfaction Award"> <span class="bg-yellow quarter-winner">Q1 2019</span></a></li>
<li><a data-target="#custSatisfactionModal" data-toggle="modal"><img class="img-responsive" src=" https://www.lendingtree.com/content/themes/lt-wp-www-theme/dist/images/lender-review/TopRated-personal-winner.png" alt="Customer Satisfaction Award"> <span class="bg-yellow quarter-winner">Q4 2018</span></a></li>
</ul>
</div>
<div class="col-md-7 col-sm-7 col-xs-12 Summary">
<h2 class="Title">Lender Summary</h2>
<pre class="lender-desc">At First Midwest, you'll get the financing you want and the momentum you need to tackle whatever is on your to do list. Our Gold Leaf certified bankers will be with you every step of the way with low rates, an easy application process, and quick and convenient closings. Get connected to a First Midwest Banker today. You'll be glad you did.</pre>
</div>
</div>
</div>
</div>
</section>
<section class="reviewBreakdown">
<div class="container">
<h2 class="text-center">What they're saying</h2>
<div class="row">
<div class="col-xs-12 col-md-5">
<div class="start-rating-reviews">
<b class="hidden-xs" aria-label="2255 reviews for First Midwest Bank">2255 Reviews</b>
<b class="visible-xs mob-heading">Ratings & Reviews</b>
<div class="rating-stars-wrapper" itemprop="aggregateRating">
<div class="rating-stars-bottom">
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
</div>
<div class="rating-stars-top">
<div class="rating-stars-bar" style="width: 98.6%;">
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
</div>
</div>
</div>
<span class="hidden-xs">(4.9 of 5)<span class="visually-hidden">stars</span></span>
<a href="#reviewBlockStart" class="reviews-count" aria-label="2255 reviews for First Midwest Bank">2255 Reviews</a>
</div>
<ul class="rating-bar-section">
<li>
<span class="rating-bar-title">Interest Rates</span>
<div class="rating-bar">
<div class="rating-bar-top" style="width:94.8%;">
<span></span><span></span><span></span><span></span><span></span>
</div>
<div class="rating-bar-bottom">
<span></span><span></span><span></span><span></span><span></span>
</div>
</div>
<span class="rating-val">Excellent</span>
</li>
<li>
<span class="rating-bar-title">Fees & Closing Costs</span>
<div class="rating-bar">
<div class="rating-bar-top" style="width:93%;">
<span></span><span></span><span></span><span></span><span></span>
</div>
<div class="rating-bar-bottom">
 <span></span><span></span><span></span><span></span><span></span>
</div>
</div>
<span class="rating-val">Excellent</span>
</li>
<li>
<span class="rating-bar-title">Responsiveness</span>
<div class="rating-bar">
<div class="rating-bar-top" style="width:98.6%;">
<span></span><span></span><span></span><span></span><span></span>
</div>
<div class="rating-bar-bottom">
<span></span><span></span><span></span><span></span><span></span>
</div>
</div>
<span class="rating-val">Excellent</span>
</li>
<li>
<span class="rating-bar-title">Customer Service</span>
<div class="rating-bar">
<div class="rating-bar-top" style="width:98.8%;">
<span></span><span></span><span></span><span></span><span></span>
</div>
<div class="rating-bar-bottom">
<span></span><span></span><span></span><span></span><span></span>
</div>
</div>
<span class="rating-val">Excellent</span>
</li>
</ul>
</div>
<div class="col-xs-12 col-md-7">
<div class="reviews-breakdown">
<h3>Review Breakdown</h3>
<ul>
<li>
<span class="star-value">5 Star</span>
<div class="breakdown-bar">
<div style="width:96.141906873614%" ;></div>
</div>
<a href="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&pid=1&OverallRating=5" class="review-count-text" aria-label="2168 5 star reviews">(2168)</a>
</li>
<li>
<span class="star-value">4 Star</span>
<div class="breakdown-bar">
<div style="width:2.7050997782705%;"></div>
</div>
<a href="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&pid=1&OverallRating=4" class="review-count-text" aria-label="61 4 star reviews">(61)</a>
</li>
<li>
<span class="star-value">3 Star</span>
<div class="breakdown-bar">
<div style="width:0.26607538802661%;"></div>
</div>
<a href="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&pid=1&OverallRating=3" class="review-count-text" aria-label="6 3 star reviews">(6)</a>
</li>
<li>
<span class="star-value">2 Star</span>
<div class="breakdown-bar">
<div style="width:0.088691796008869%;"></div>
</div>
<a href="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&pid=1&OverallRating=2" class="review-count-text" aria-label="2 2 star reviews">(2)</a>
</li>
<li>
<span class="star-value">1 Star</span>
<div class="breakdown-bar">
<div style="width:0.79822616407982%;"></div>
</div>
<a href="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&pid=1&OverallRating=1" class="review-count-text" aria-label="18 1 star reviews">(18)</a>
</li>
</ul>
<div class="clear-fix"></div>
</div>
</div>
</div>
</div>
</section>
<section class="lenderReviews">
<div class="container">
<div class="row">
<div class="col-xs-12 lenderFilters">
<div class="row">
<input type="hidden" id="cacheKey" value="Br:27085-Is:False-Is:False-Le:0-Mo:Approved-Of:0-Ov:0-Pa:0-Pa:10-Re:reviewsstatsratingconfigpropertyconfig-So:ReviewSubmitted-So:desc">
<div class="col-md-3 col-xs-12 writeReview pull-right">
<a data-toggle="modal" data-target="#review" data-backdrop="false" class="btn btn-blue reviewBtn write-review" data-lendername="First Midwest Bank" data-lenderid="52903183" data-lenderreviewid="27085" data-vertical="personal">Write a Review</a>
</div>
<div class="col-md-9 col-xs-12 searchFilters">
<form>
<ul id="filter_select">
<li class="filterin lender_detail_filter">
<label class="left">Show:</label>
<select class="filter_select state-filter">
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&state=All&pid=1" data-state="All">Nationwide</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&state=AL&pid=1" data-state="AL">Alabama</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&state=AK&pid=1" data-state="AK">Alaska</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&state=AZ&pid=1" data-state="AZ">Arizona</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&state=AR&pid=1" data-state="AR">Arkansas</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&state=CA&pid=1" data-state="CA">California</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&state=CO&pid=1" data-state="CO">Colorado</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&state=CT&pid=1" data-state="CT">Connecticut</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&state=DE&pid=1" data-state="DE">Delaware</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&state=DC&pid=1" data-state="DC">District of Columbia</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&state=FL&pid=1" data-state="FL">Florida</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&state=GA&pid=1" data-state="GA">Georgia</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&state=HI&pid=1" data-state="HI">Hawaii</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&state=ID&pid=1" data-state="ID">Idaho</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&state=IL&pid=1" data-state="IL">Illinois</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&state=IN&pid=1" data-state="IN">Indiana</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&state=IA&pid=1" data-state="IA">Iowa</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&state=KS&pid=1" data-state="KS">Kansas</option>
 <option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&state=KY&pid=1" data-state="KY">Kentucky</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&state=LA&pid=1" data-state="LA">Louisiana</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&state=ME&pid=1" data-state="ME">Maine</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&state=MD&pid=1" data-state="MD">Maryland</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&state=MA&pid=1" data-state="MA">Massachusetts</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&state=MI&pid=1" data-state="MI">Michigan</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&state=MN&pid=1" data-state="MN">Minnesota</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&state=MS&pid=1" data-state="MS">Mississippi</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&state=MO&pid=1" data-state="MO">Missouri</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&state=MT&pid=1" data-state="MT">Montana</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&state=NE&pid=1" data-state="NE">Nebraska</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&state=NV&pid=1" data-state="NV">Nevada</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&state=NH&pid=1" data-state="NH">New Hampshire</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&state=NJ&pid=1" data-state="NJ">New Jersey</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&state=NM&pid=1" data-state="NM">New Mexico</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&state=NY&pid=1" data-state="NY">New York</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&state=NC&pid=1" data-state="NC">North Carolina</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&state=ND&pid=1" data-state="ND">North Dakota</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&state=OH&pid=1" data-state="OH">Ohio</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&state=OK&pid=1" data-state="OK">Oklahoma</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&state=OR&pid=1" data-state="OR">Oregon</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&state=PA&pid=1" data-state="PA">Pennsylvania</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&state=RI&pid=1" data-state="RI">Rhode Island</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&state=SC&pid=1" data-state="SC">South Carolina</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&state=SD&pid=1" data-state="SD">South Dakota</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&state=TN&pid=1" data-state="TN">Tennessee</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&state=TX&pid=1" data-state="TX">Texas</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&state=UT&pid=1" data-state="UT">Utah</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&state=VT&pid=1" data-state="VT">Vermont</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&state=VA&pid=1" data-state="VA">Virginia</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&state=WA&pid=1" data-state="WA">Washington</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&state=WV&pid=1" data-state="WV">West Virginia</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&state=WI&pid=1" data-state="WI">Wisconsin</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&state=WY&pid=1" data-state="WY">Wyoming</option>
</select>
</li>
<li class="filterin lender_detail_filter">
<label class="left">By:</label>
<select class="filter_select sort-filter">
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&pid=1" data-sort="reviewsubmitted_desc">Most Recent</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=b3ZlcmFsbHJhdGluZ19kZXNj&pid=1" data-sort="overallrating_desc">High to Low Rating</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=b3ZlcmFsbHJhdGluZ19hc2M=&pid=1" data-sort="overallrating_asc">Low to High Rating</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2FzYw==&pid=1" data-sort="reviewsubmitted_asc">Oldest Review</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=aXNyZWNvbW1lbmRlZF9kZXNj&pid=1" data-sort="isrecommended_desc">Is Recommended</option>
<option value="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=aXNsb2FuY2xvc2VkX2Rlc2M=&pid=1" data-sort="isloanclosed_desc">Closed with Lender</option>
</select>
</li>
</ul>
</form>
</div>
</div>
</div>
 <div id="reviewBlockStart"></div>
<div class="col-xs-12 mainReviews ">
<div class="col-xs-12 starReviews">
<div class="rating-stars-wrapper" itemprop="aggregateRating">
<div class="rating-stars-bottom">
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
</div>
<div class="rating-stars-top">
<div class="rating-stars-bar" style="width:20%;">
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
</div>
</div>
</div>
<div class="recommended">
<div class="numRec">(1 of 5)<span class="visually-hidden">stars</span></div>
</div>
</div>
<div class="col-lg-9 col-sm-8 col-xs-12 reviewDetail">
<p class="reviewTitle">Not as good as it sounds</p>
<p class="reviewText">It is false advertising. Even though all my information is available to them to make me an offer. They offered me a loan then declined me due to my credit score. </p>
<div class="hideText">
<p class="consumerName">Christopher <span>from Cloverdale, IN</span></p>
<p class="consumerReviewDate">Reviewed in December 2019</p>
</div>
<div class="helpfull-count desktop-view">
<div class="review-type">WAS THIS REVIEW HELPFUL?</div>
<div class="helpfull-section">
<input type="hidden" class="reviewId" name="reviewId" value="5df2654edb03740001f79b8b">
<div class="vote-action">
<button class="voteUp hover" id="voteupclick" data-voteupclick=0 aria-label="Mark this review as helpful">
<i class="lt4-ThumbsUp like-icon"></i>
<span class="likes helpfulAction" aria-hidden="true">0</span>
</button>
<span class="visually-hidden hiddenLike">0 People found this helpful</span>
</div>
<div class="vote-action">
<button class="voteDown hover" id="votedownclick" data-votedownclick=0 aria-label="Mark this review as not helpful">
<i class="lt4-ThumbsDown dislike-icon"></i>
<span class="dislikes helpfulAction" aria-hidden="true">0</span>
</button>
<span class="visually-hidden hiddenDislike">0 People found this not helpful</span>
</div>
<div class="flagged-review">
<button class="flag" id="flag-5df2654edb03740001f79b8b" aria-label="Mark this review as flagged">
<div class='flag-content'>
<img src="https://www.lendingtree.com/content/themes/lt-wp-www-theme/dist/images/lender-review/review-flag-desktop.png" alt="">
<span class="flag-text">Flag review</span>
</div>
</button>
</div>
</div>
</div>
</div>
<div class="col-lg-3 col-sm-4 col-xs-12 reviewPoints">
<div class="hideText">
<ul>
<li><p>LendingTree Customer:</p> <div class="yes">Yes</div></li>
<li><p>Loan Type:</p> <div class="loanType">Personal Loan</div></li>
<li><p>Review Type:</p> <div class="loanType">Lender Review</div></li>
</ul>

<div class="helpfull-count mobile-view">
<div class="review-type">WAS THIS REVIEW HELPFUL?</div>
<div class="helpfull-section">
<input type="hidden" class="reviewId" name="reviewId" value="5df2654edb03740001f79b8b">
<div class="vote-action">
<button class="voteUp hover" id="voteupclick" data-voteupclick=0 aria-label="Mark this review as helpful">
<i class="lt4-ThumbsUp like-icon"></i>
<span class="likes helpfulAction">0</span>
</button>
<span class="visually-hidden hiddenLike">0 People found this helpful</span>
</div>
<div class="vote-action">
<button class="voteDown hover" id="votedownclick" data-votedownclick=0>
<i class="lt4-ThumbsDown dislike-icon"></i>
<span class="dislikes helpfulAction">0</span>
</button>
<span class="visually-hidden hiddenDislike">0 People found this not helpful</span>
</div>
<div class="flagged-review">
<button class="flag" id="m-flag-5df2654edb03740001f79b8b" aria-label="Mark this review as flagged">
<img src="https://www.lendingtree.com/content/themes/lt-wp-www-theme/dist/images/lender-review/review-flag-mobile.png" alt="">
</button>
</div>
<div class="review-flag" id="m-review-flag-5df2654edb03740001f79b8b">
<div class="review-flag-type">Do you want to flag this review?</div>
<button class="btn btn-secondary-bluelg save">Yes</button>
<button class="btn btn-secondary-bluelg cancel">No</button>
</div>
</div>
</div>

</div>
</div>
<div class="col-xs-12 reviewBtn">
<a class="clsReview" href="#">Full Review</a>
</div>
</div>
<div class="col-xs-12 mainReviews ">
<div class="col-xs-12 starReviews">
<div class="rating-stars-wrapper" itemprop="aggregateRating">
<div class="rating-stars-bottom">
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
</div>
<div class="rating-stars-top">
<div class="rating-stars-bar" style="width:100%;">
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
</div>
</div>
</div>
<div class="recommended">
<div class="numRec">(5 of 5)<span class="visually-hidden">stars</span></div>
<div class="lenderRec">Recommended</div>
</div>
</div>
<div class="col-lg-9 col-sm-8 col-xs-12 reviewDetail">
<p class="reviewTitle"> Easy and Painless process start to finish!</p>
<p class="reviewText">I saw the great rates being offered so I applied for a loan. The application was straight forward, and the response time was literally same day. Patrick was awesome, and I appreciated the whole process being headache free and so fast!</p>
<div class="hideText">
<p class="consumerName">Jeff <span>from COVENTRY, RI </span></p>
<p class="consumerReviewDate">Reviewed in December 2019</p>
 </div>
<div class="helpfull-count desktop-view">
<div class="review-type">WAS THIS REVIEW HELPFUL?</div>
<div class="helpfull-section">
<input type="hidden" class="reviewId" name="reviewId" value="5df23499b527b4000157ea4e">
<div class="vote-action">
<button class="voteUp hover" id="voteupclick" data-voteupclick=0 aria-label="Mark this review as helpful">
<i class="lt4-ThumbsUp like-icon"></i>
<span class="likes helpfulAction" aria-hidden="true">0</span>
</button>
<span class="visually-hidden hiddenLike">0 People found this helpful</span>
</div>
<div class="vote-action">
<button class="voteDown hover" id="votedownclick" data-votedownclick=0 aria-label="Mark this review as not helpful">
<i class="lt4-ThumbsDown dislike-icon"></i>
<span class="dislikes helpfulAction" aria-hidden="true">0</span>
</button>
<span class="visually-hidden hiddenDislike">0 People found this not helpful</span>
</div>
<div class="flagged-review">
<button class="flag" id="flag-5df23499b527b4000157ea4e" aria-label="Mark this review as flagged">
<div class='flag-content'>
<img src="https://www.lendingtree.com/content/themes/lt-wp-www-theme/dist/images/lender-review/review-flag-desktop.png" alt="">
<span class="flag-text">Flag review</span>
</div>
</button>
</div>
</div>
</div>
</div>
<div class="col-lg-3 col-sm-4 col-xs-12 reviewPoints">
<div class="hideText">
<ul>
<li><p>Closed with Lender:</p> <div class="yes">Yes</div></li>
<li><p>Loan Type:</p> <div class="loanType">Personal Loan</div></li>
<li><p>Review Type:</p> <div class="loanType">Lender Review</div></li>
</ul>

<div class="helpfull-count mobile-view">
<div class="review-type">WAS THIS REVIEW HELPFUL?</div>
<div class="helpfull-section">
<input type="hidden" class="reviewId" name="reviewId" value="5df23499b527b4000157ea4e">
<div class="vote-action">
<button class="voteUp hover" id="voteupclick" data-voteupclick=0 aria-label="Mark this review as helpful">
<i class="lt4-ThumbsUp like-icon"></i>
<span class="likes helpfulAction">0</span>
</button>
<span class="visually-hidden hiddenLike">0 People found this helpful</span>
</div>
<div class="vote-action">
<button class="voteDown hover" id="votedownclick" data-votedownclick=0>
<i class="lt4-ThumbsDown dislike-icon"></i>
<span class="dislikes helpfulAction">0</span>
</button>
<span class="visually-hidden hiddenDislike">0 People found this not helpful</span>
</div>
<div class="flagged-review">
<button class="flag" id="m-flag-5df23499b527b4000157ea4e" aria-label="Mark this review as flagged">
<img src="https://www.lendingtree.com/content/themes/lt-wp-www-theme/dist/images/lender-review/review-flag-mobile.png" alt="">
</button>
</div>
<div class="review-flag" id="m-review-flag-5df23499b527b4000157ea4e">
<div class="review-flag-type">Do you want to flag this review?</div>
<button class="btn btn-secondary-bluelg save">Yes</button>
<button class="btn btn-secondary-bluelg cancel">No</button>
</div>
</div>
</div>

</div>
</div>
<div class="col-xs-12 reviewBtn">
<a class="clsReview" href="#">Full Review</a>
</div>
</div>
<div class="col-xs-12 mainReviews ">
<div class="col-xs-12 starReviews">
<div class="rating-stars-wrapper" itemprop="aggregateRating">
<div class="rating-stars-bottom">
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
</div>
<div class="rating-stars-top">
<div class="rating-stars-bar" style="width:100%;">
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
 <span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
</div>
</div>
</div>
<div class="recommended">
<div class="numRec">(5 of 5)<span class="visually-hidden">stars</span></div>
<div class="lenderRec">Recommended</div>
</div>
</div>
<div class="col-lg-9 col-sm-8 col-xs-12 reviewDetail">
<p class="reviewTitle">Very good experiance, timely and friedly staff</p>
<p class="reviewText">The process was easy, timely and the person we dealt with was knowledgeable, friendly and provided easy to understand instructions. It was a very good experience.</p>
<div class="hideText">
<p class="consumerName">Jeffrey <span>from STURGEON BAY, WI </span></p>
<p class="consumerReviewDate">Reviewed in December 2019</p>
</div>
<div class="helpfull-count desktop-view">
<div class="review-type">WAS THIS REVIEW HELPFUL?</div>
<div class="helpfull-section">
<input type="hidden" class="reviewId" name="reviewId" value="5df1b258cb4ee300015ca599">
<div class="vote-action">
<button class="voteUp hover" id="voteupclick" data-voteupclick=0 aria-label="Mark this review as helpful">
<i class="lt4-ThumbsUp like-icon"></i>
<span class="likes helpfulAction" aria-hidden="true">0</span>
</button>
<span class="visually-hidden hiddenLike">0 People found this helpful</span>
</div>
<div class="vote-action">
<button class="voteDown hover" id="votedownclick" data-votedownclick=0 aria-label="Mark this review as not helpful">
<i class="lt4-ThumbsDown dislike-icon"></i>
<span class="dislikes helpfulAction" aria-hidden="true">0</span>
</button>
<span class="visually-hidden hiddenDislike">0 People found this not helpful</span>
</div>
<div class="flagged-review">
<button class="flag" id="flag-5df1b258cb4ee300015ca599" aria-label="Mark this review as flagged">
<div class='flag-content'>
<img src="https://www.lendingtree.com/content/themes/lt-wp-www-theme/dist/images/lender-review/review-flag-desktop.png" alt="">
<span class="flag-text">Flag review</span>
</div>
</button>
</div>
</div>
</div>
</div>
<div class="col-lg-3 col-sm-4 col-xs-12 reviewPoints">
<div class="hideText">
<ul>
<li><p>Closed with Lender:</p> <div class="yes">Yes</div></li>
<li><p>Loan Type:</p> <div class="loanType">Personal Loan</div></li>
<li><p>Review Type:</p> <div class="loanType">Lender Review</div></li>
</ul>

<div class="helpfull-count mobile-view">
<div class="review-type">WAS THIS REVIEW HELPFUL?</div>
<div class="helpfull-section">
<input type="hidden" class="reviewId" name="reviewId" value="5df1b258cb4ee300015ca599">
<div class="vote-action">
<button class="voteUp hover" id="voteupclick" data-voteupclick=0 aria-label="Mark this review as helpful">
<i class="lt4-ThumbsUp like-icon"></i>
<span class="likes helpfulAction">0</span>
</button>
<span class="visually-hidden hiddenLike">0 People found this helpful</span>
</div>
<div class="vote-action">
<button class="voteDown hover" id="votedownclick" data-votedownclick=0>
<i class="lt4-ThumbsDown dislike-icon"></i>
<span class="dislikes helpfulAction">0</span>
</button>
<span class="visually-hidden hiddenDislike">0 People found this not helpful</span>
</div>
<div class="flagged-review">
<button class="flag" id="m-flag-5df1b258cb4ee300015ca599" aria-label="Mark this review as flagged">
<img src="https://www.lendingtree.com/content/themes/lt-wp-www-theme/dist/images/lender-review/review-flag-mobile.png" alt="">
</button>
</div>
<div class="review-flag" id="m-review-flag-5df1b258cb4ee300015ca599">
<div class="review-flag-type">Do you want to flag this review?</div>
<button class="btn btn-secondary-bluelg save">Yes</button>
<button class="btn btn-secondary-bluelg cancel">No</button>
</div>
</div>
</div>

</div>
</div>
<div class="col-xs-12 reviewBtn">
 <a class="clsReview" href="#">Full Review</a>
</div>
</div>
<div class="col-xs-12 mainReviews hiddenReviews">
<div class="col-xs-12 starReviews">
<div class="rating-stars-wrapper" itemprop="aggregateRating">
<div class="rating-stars-bottom">
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
</div>
<div class="rating-stars-top">
<div class="rating-stars-bar" style="width:100%;">
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
</div>
</div>
</div>
<div class="recommended">
<div class="numRec">(5 of 5)<span class="visually-hidden">stars</span></div>
<div class="lenderRec">Recommended</div>
</div>
</div>
<div class="col-lg-9 col-sm-8 col-xs-12 reviewDetail">
<p class="reviewTitle">A good experience</p>
<p class="reviewText">Everything want smooth no issue's at all. Everyone I talked to was very nice. Marcella the main one that started the loan, was very pleasant and very helpful Thank's Everyone</p>
<div class="hideText">
<p class="consumerName">Jane <span>from VALPARAISO, IN </span></p>
<p class="consumerReviewDate">Reviewed in December 2019</p>
</div>
<div class="helpfull-count desktop-view">
<div class="review-type">WAS THIS REVIEW HELPFUL?</div>
<div class="helpfull-section">
<input type="hidden" class="reviewId" name="reviewId" value="5df18909db03740001f79b7e">
<div class="vote-action">
<button class="voteUp hover" id="voteupclick" data-voteupclick=0 aria-label="Mark this review as helpful">
<i class="lt4-ThumbsUp like-icon"></i>
<span class="likes helpfulAction" aria-hidden="true">0</span>
</button>
<span class="visually-hidden hiddenLike">0 People found this helpful</span>
</div>
<div class="vote-action">
<button class="voteDown hover" id="votedownclick" data-votedownclick=0 aria-label="Mark this review as not helpful">
<i class="lt4-ThumbsDown dislike-icon"></i>
<span class="dislikes helpfulAction" aria-hidden="true">0</span>
</button>
<span class="visually-hidden hiddenDislike">0 People found this not helpful</span>
</div>
<div class="flagged-review">
<button class="flag" id="flag-5df18909db03740001f79b7e" aria-label="Mark this review as flagged">
<div class='flag-content'>
<img src="https://www.lendingtree.com/content/themes/lt-wp-www-theme/dist/images/lender-review/review-flag-desktop.png" alt="">
<span class="flag-text">Flag review</span>
</div>
</button>
</div>
</div>
</div>
</div>
<div class="col-lg-3 col-sm-4 col-xs-12 reviewPoints">
<div class="hideText">
<ul>
<li><p>Closed with Lender:</p> <div class="yes">Yes</div></li>
<li><p>Loan Type:</p> <div class="loanType">Personal Loan</div></li>
<li><p>Review Type:</p> <div class="loanType">Lender Review</div></li>
</ul>

<div class="helpfull-count mobile-view">
<div class="review-type">WAS THIS REVIEW HELPFUL?</div>
<div class="helpfull-section">
<input type="hidden" class="reviewId" name="reviewId" value="5df18909db03740001f79b7e">
<div class="vote-action">
<button class="voteUp hover" id="voteupclick" data-voteupclick=0 aria-label="Mark this review as helpful">
<i class="lt4-ThumbsUp like-icon"></i>
<span class="likes helpfulAction">0</span>
</button>
<span class="visually-hidden hiddenLike">0 People found this helpful</span>
</div>
<div class="vote-action">
<button class="voteDown hover" id="votedownclick" data-votedownclick=0>
<i class="lt4-ThumbsDown dislike-icon"></i>
<span class="dislikes helpfulAction">0</span>
</button>
<span class="visually-hidden hiddenDislike">0 People found this not helpful</span>
</div>
 <div class="flagged-review">
<button class="flag" id="m-flag-5df18909db03740001f79b7e" aria-label="Mark this review as flagged">
<img src="https://www.lendingtree.com/content/themes/lt-wp-www-theme/dist/images/lender-review/review-flag-mobile.png" alt="">
</button>
</div>
<div class="review-flag" id="m-review-flag-5df18909db03740001f79b7e">
<div class="review-flag-type">Do you want to flag this review?</div>
<button class="btn btn-secondary-bluelg save">Yes</button>
<button class="btn btn-secondary-bluelg cancel">No</button>
</div>
</div>
</div>

</div>
</div>
<div class="col-xs-12 reviewBtn">
<a class="clsReview" href="#">Full Review</a>
</div>
</div>
<div class="col-xs-12 mainReviews hiddenReviews">
<div class="col-xs-12 starReviews">
<div class="rating-stars-wrapper" itemprop="aggregateRating">
<div class="rating-stars-bottom">
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
</div>
<div class="rating-stars-top">
<div class="rating-stars-bar" style="width:100%;">
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
</div>
</div>
</div>
<div class="recommended">
<div class="numRec">(5 of 5)<span class="visually-hidden">stars</span></div>
<div class="lenderRec">Recommended</div>
</div>
</div>
<div class="col-lg-9 col-sm-8 col-xs-12 reviewDetail">
<p class="reviewTitle">Everything was so easy.</p>
<p class="reviewText">I would like to thank Christine Ruiz. She contacted me after I checked First Midwest Bank rates she made me feel at ease and was very helpful thanks once again and process was so easy.</p>
<div class="hideText">
<p class="consumerName">Ricky <span>from BLACKSHEAR, GA </span></p>
<p class="consumerReviewDate">Reviewed in December 2019</p>
</div>
<div class="helpfull-count desktop-view">
<div class="review-type">WAS THIS REVIEW HELPFUL?</div>
<div class="helpfull-section">
<input type="hidden" class="reviewId" name="reviewId" value="5df165acdb03740001f79b73">
<div class="vote-action">
<button class="voteUp hover" id="voteupclick" data-voteupclick=0 aria-label="Mark this review as helpful">
<i class="lt4-ThumbsUp like-icon"></i>
<span class="likes helpfulAction" aria-hidden="true">0</span>
</button>
<span class="visually-hidden hiddenLike">0 People found this helpful</span>
</div>
<div class="vote-action">
<button class="voteDown hover" id="votedownclick" data-votedownclick=0 aria-label="Mark this review as not helpful">
<i class="lt4-ThumbsDown dislike-icon"></i>
<span class="dislikes helpfulAction" aria-hidden="true">0</span>
</button>
<span class="visually-hidden hiddenDislike">0 People found this not helpful</span>
</div>
<div class="flagged-review">
<button class="flag" id="flag-5df165acdb03740001f79b73" aria-label="Mark this review as flagged">
<div class='flag-content'>
<img src="https://www.lendingtree.com/content/themes/lt-wp-www-theme/dist/images/lender-review/review-flag-desktop.png" alt="">
<span class="flag-text">Flag review</span>
</div>
</button>
</div>
</div>
</div>
</div>
<div class="col-lg-3 col-sm-4 col-xs-12 reviewPoints">
<div class="hideText">
<ul>
<li><p>Closed with Lender:</p> <div class="yes">Yes</div></li>
<li><p>Loan Type:</p> <div class="loanType">Personal Loan</div></li>
<li><p>Review Type:</p> <div class="loanType">Lender Review</div></li>
</ul>

<div class="helpfull-count mobile-view">
<div class="review-type">WAS THIS REVIEW HELPFUL?</div>
<div class="helpfull-section">
<input type="hidden" class="reviewId" name="reviewId" value="5df165acdb03740001f79b73">
<div class="vote-action">
<button class="voteUp hover" id="voteupclick" data-voteupclick=0 aria-label="Mark this review as helpful">
<i class="lt4-ThumbsUp like-icon"></i>
<span class="likes helpfulAction">0</span>
</button>
<span class="visually-hidden hiddenLike">0 People found this helpful</span>
</div>
<div class="vote-action">
<button class="voteDown hover" id="votedownclick" data-votedownclick=0>
<i class="lt4-ThumbsDown dislike-icon"></i>
<span class="dislikes helpfulAction">0</span>
</button>
<span class="visually-hidden hiddenDislike">0 People found this not helpful</span>
</div>
<div class="flagged-review">
<button class="flag" id="m-flag-5df165acdb03740001f79b73" aria-label="Mark this review as flagged">
<img src="https://www.lendingtree.com/content/themes/lt-wp-www-theme/dist/images/lender-review/review-flag-mobile.png" alt="">
</button>
</div>
<div class="review-flag" id="m-review-flag-5df165acdb03740001f79b73">
<div class="review-flag-type">Do you want to flag this review?</div>
<button class="btn btn-secondary-bluelg save">Yes</button>
<button class="btn btn-secondary-bluelg cancel">No</button>
</div>
</div>
</div>

</div>
</div>
<div class="col-xs-12 reviewBtn">
<a class="clsReview" href="#">Full Review</a>
</div>
</div>
<div class="col-xs-12 mainReviews hiddenReviews">
<div class="col-xs-12 starReviews">
<div class="rating-stars-wrapper" itemprop="aggregateRating">
<div class="rating-stars-bottom">
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
</div>
<div class="rating-stars-top">
<div class="rating-stars-bar" style="width:100%;">
<span class="lt4-Star" aria-hidden="true"></span>
 <span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
</div>
</div>
</div>
<div class="recommended">
<div class="numRec">(5 of 5)<span class="visually-hidden">stars</span></div>
<div class="lenderRec">Recommended</div>
</div>
</div>
<div class="col-lg-9 col-sm-8 col-xs-12 reviewDetail">
<p class="reviewTitle">Five Stars in all respects</p>
<p class="reviewText">It was extraordinary, both in terms of its speed and efficiency and also of its highly professional staff</p>
<div class="hideText">
<p class="consumerName">mary <span>from NEW YORK, NY </span></p>
<p class="consumerReviewDate">Reviewed in December 2019</p>
</div>
<div class="helpfull-count desktop-view">
<div class="review-type">WAS THIS REVIEW HELPFUL?</div>
<div class="helpfull-section">
<input type="hidden" class="reviewId" name="reviewId" value="5df161cccb4ee300015ca58c">
<div class="vote-action">
<button class="voteUp hover" id="voteupclick" data-voteupclick=0 aria-label="Mark this review as helpful">
<i class="lt4-ThumbsUp like-icon"></i>
<span class="likes helpfulAction" aria-hidden="true">0</span>
</button>
<span class="visually-hidden hiddenLike">0 People found this helpful</span>
</div>
<div class="vote-action">
<button class="voteDown hover" id="votedownclick" data-votedownclick=0 aria-label="Mark this review as not helpful">
<i class="lt4-ThumbsDown dislike-icon"></i>
<span class="dislikes helpfulAction" aria-hidden="true">0</span>
</button>
<span class="visually-hidden hiddenDislike">0 People found this not helpful</span>
</div>
<div class="flagged-review">
<button class="flag" id="flag-5df161cccb4ee300015ca58c" aria-label="Mark this review as flagged">
<div class='flag-content'>
<img src="https://www.lendingtree.com/content/themes/lt-wp-www-theme/dist/images/lender-review/review-flag-desktop.png" alt="">
<span class="flag-text">Flag review</span>
</div>
</button>
 </div>
</div>
</div>
</div>
<div class="col-lg-3 col-sm-4 col-xs-12 reviewPoints">
<div class="hideText">
<ul>
<li><p>Closed with Lender:</p> <div class="yes">Yes</div></li>
<li><p>Loan Type:</p> <div class="loanType">Personal Loan</div></li>
<li><p>Review Type:</p> <div class="loanType">Lender Review</div></li>
</ul>

<div class="helpfull-count mobile-view">
<div class="review-type">WAS THIS REVIEW HELPFUL?</div>
<div class="helpfull-section">
<input type="hidden" class="reviewId" name="reviewId" value="5df161cccb4ee300015ca58c">
<div class="vote-action">
<button class="voteUp hover" id="voteupclick" data-voteupclick=0 aria-label="Mark this review as helpful">
<i class="lt4-ThumbsUp like-icon"></i>
<span class="likes helpfulAction">0</span>
</button>
<span class="visually-hidden hiddenLike">0 People found this helpful</span>
</div>
<div class="vote-action">
<button class="voteDown hover" id="votedownclick" data-votedownclick=0>
<i class="lt4-ThumbsDown dislike-icon"></i>
<span class="dislikes helpfulAction">0</span>
</button>
<span class="visually-hidden hiddenDislike">0 People found this not helpful</span>
</div>
<div class="flagged-review">
<button class="flag" id="m-flag-5df161cccb4ee300015ca58c" aria-label="Mark this review as flagged">
<img src="https://www.lendingtree.com/content/themes/lt-wp-www-theme/dist/images/lender-review/review-flag-mobile.png" alt="">
</button>
</div>
<div class="review-flag" id="m-review-flag-5df161cccb4ee300015ca58c">
<div class="review-flag-type">Do you want to flag this review?</div>
<button class="btn btn-secondary-bluelg save">Yes</button>
<button class="btn btn-secondary-bluelg cancel">No</button>
</div>
</div>
</div>

 </div>
</div>
<div class="col-xs-12 reviewBtn">
<a class="clsReview" href="#">Full Review</a>
</div>
</div>
<div class="col-xs-12 mainReviews hiddenReviews">
<div class="col-xs-12 starReviews">
<div class="rating-stars-wrapper" itemprop="aggregateRating">
<div class="rating-stars-bottom">
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
</div>
<div class="rating-stars-top">
<div class="rating-stars-bar" style="width:100%;">
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
</div>
</div>
</div>
<div class="recommended">
<div class="numRec">(5 of 5)<span class="visually-hidden">stars</span></div>
<div class="lenderRec">Recommended</div>
</div>
</div>
<div class="col-lg-9 col-sm-8 col-xs-12 reviewDetail">
<p class="reviewTitle">Great experience</p>
<p class="reviewText">The process was very easy and very fast, I highly recommend! Everything was done via email which made me a little worried but after all was said and done, it was the easiest and quickest experience I ever had with a loan!</p>
<div class="hideText">
<p class="consumerName">Denice <span>from MC DOWELL, KY </span></p>
<p class="consumerReviewDate">Reviewed in December 2019</p>
</div>
<div class="helpfull-count desktop-view">
<div class="review-type">WAS THIS REVIEW HELPFUL?</div>
<div class="helpfull-section">
<input type="hidden" class="reviewId" name="reviewId" value="5df1330d29990e0001faa6f8">
<div class="vote-action">
<button class="voteUp hover" id="voteupclick" data-voteupclick=0 aria-label="Mark this review as helpful">
<i class="lt4-ThumbsUp like-icon"></i>
<span class="likes helpfulAction" aria-hidden="true">0</span>
</button>
<span class="visually-hidden hiddenLike">0 People found this helpful</span>
</div>
 <div class="vote-action">
<button class="voteDown hover" id="votedownclick" data-votedownclick=0 aria-label="Mark this review as not helpful">
<i class="lt4-ThumbsDown dislike-icon"></i>
<span class="dislikes helpfulAction" aria-hidden="true">0</span>
</button>
<span class="visually-hidden hiddenDislike">0 People found this not helpful</span>
</div>
<div class="flagged-review">
<button class="flag" id="flag-5df1330d29990e0001faa6f8" aria-label="Mark this review as flagged">
<div class='flag-content'>
<img src="https://www.lendingtree.com/content/themes/lt-wp-www-theme/dist/images/lender-review/review-flag-desktop.png" alt="">
<span class="flag-text">Flag review</span>
</div>
</button>
</div>
</div>
</div>
</div>
<div class="col-lg-3 col-sm-4 col-xs-12 reviewPoints">
<div class="hideText">
<ul>
<li><p>Closed with Lender:</p> <div class="yes">Yes</div></li>
<li><p>Loan Type:</p> <div class="loanType">Personal Loan</div></li>
<li><p>Review Type:</p> <div class="loanType">Lender Review</div></li>
</ul>

<div class="helpfull-count mobile-view">
<div class="review-type">WAS THIS REVIEW HELPFUL?</div>
<div class="helpfull-section">
<input type="hidden" class="reviewId" name="reviewId" value="5df1330d29990e0001faa6f8">
<div class="vote-action">
<button class="voteUp hover" id="voteupclick" data-voteupclick=0 aria-label="Mark this review as helpful">
<i class="lt4-ThumbsUp like-icon"></i>
<span class="likes helpfulAction">0</span>
</button>
<span class="visually-hidden hiddenLike">0 People found this helpful</span>
</div>
<div class="vote-action">
<button class="voteDown hover" id="votedownclick" data-votedownclick=0>
<i class="lt4-ThumbsDown dislike-icon"></i>
<span class="dislikes helpfulAction">0</span>
</button>
 <span class="visually-hidden hiddenDislike">0 People found this not helpful</span>
</div>
<div class="flagged-review">
<button class="flag" id="m-flag-5df1330d29990e0001faa6f8" aria-label="Mark this review as flagged">
<img src="https://www.lendingtree.com/content/themes/lt-wp-www-theme/dist/images/lender-review/review-flag-mobile.png" alt="">
</button>
</div>
<div class="review-flag" id="m-review-flag-5df1330d29990e0001faa6f8">
<div class="review-flag-type">Do you want to flag this review?</div>
<button class="btn btn-secondary-bluelg save">Yes</button>
<button class="btn btn-secondary-bluelg cancel">No</button>
</div>
</div>
</div>

</div>
</div>
<div class="col-xs-12 reviewBtn">
<a class="clsReview" href="#">Full Review</a>
</div>
</div>
<div class="col-xs-12 mainReviews hiddenReviews">
<div class="col-xs-12 starReviews">
<div class="rating-stars-wrapper" itemprop="aggregateRating">
<div class="rating-stars-bottom">
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
</div>
<div class="rating-stars-top">
<div class="rating-stars-bar" style="width:100%;">
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
</div>
</div>
</div>
<div class="recommended">
<div class="numRec">(5 of 5)<span class="visually-hidden">stars</span></div>
<div class="lenderRec">Recommended</div>
</div>
</div>
<div class="col-lg-9 col-sm-8 col-xs-12 reviewDetail">
<p class="reviewTitle">Christine done a great job!!!</p>
<p class="reviewText">Everything went smooth, kept me informed. The whole pross took only a few days. Good job First Midwest Bank. Howard</p>
 <div class="hideText">
<p class="consumerName">Howard <span>from AURORA, IL </span></p>
<p class="consumerReviewDate">Reviewed in December 2019</p>
</div>
<div class="helpfull-count desktop-view">
<div class="review-type">WAS THIS REVIEW HELPFUL?</div>
<div class="helpfull-section">
<input type="hidden" class="reviewId" name="reviewId" value="5df10a57cb4ee300015ca582">
<div class="vote-action">
<button class="voteUp hover" id="voteupclick" data-voteupclick=0 aria-label="Mark this review as helpful">
<i class="lt4-ThumbsUp like-icon"></i>
<span class="likes helpfulAction" aria-hidden="true">0</span>
</button>
<span class="visually-hidden hiddenLike">0 People found this helpful</span>
</div>
<div class="vote-action">
<button class="voteDown hover" id="votedownclick" data-votedownclick=0 aria-label="Mark this review as not helpful">
<i class="lt4-ThumbsDown dislike-icon"></i>
<span class="dislikes helpfulAction" aria-hidden="true">0</span>
</button>
<span class="visually-hidden hiddenDislike">0 People found this not helpful</span>
</div>
<div class="flagged-review">
<button class="flag" id="flag-5df10a57cb4ee300015ca582" aria-label="Mark this review as flagged">
<div class='flag-content'>
<img src="https://www.lendingtree.com/content/themes/lt-wp-www-theme/dist/images/lender-review/review-flag-desktop.png" alt="">
<span class="flag-text">Flag review</span>
</div>
</button>
</div>
</div>
</div>
</div>
<div class="col-lg-3 col-sm-4 col-xs-12 reviewPoints">
<div class="hideText">
<ul>
<li><p>Closed with Lender:</p> <div class="yes">Yes</div></li>
<li><p>Loan Type:</p> <div class="loanType">Personal Loan</div></li>
<li><p>Review Type:</p> <div class="loanType">Lender Review</div></li>
</ul>

<div class="helpfull-count mobile-view">
<div class="review-type">WAS THIS REVIEW HELPFUL?</div>
<div class="helpfull-section">
 <input type="hidden" class="reviewId" name="reviewId" value="5df10a57cb4ee300015ca582">
<div class="vote-action">
<button class="voteUp hover" id="voteupclick" data-voteupclick=0 aria-label="Mark this review as helpful">
<i class="lt4-ThumbsUp like-icon"></i>
<span class="likes helpfulAction">0</span>
</button>
<span class="visually-hidden hiddenLike">0 People found this helpful</span>
</div>
<div class="vote-action">
<button class="voteDown hover" id="votedownclick" data-votedownclick=0>
<i class="lt4-ThumbsDown dislike-icon"></i>
<span class="dislikes helpfulAction">0</span>
</button>
<span class="visually-hidden hiddenDislike">0 People found this not helpful</span>
</div>
<div class="flagged-review">
<button class="flag" id="m-flag-5df10a57cb4ee300015ca582" aria-label="Mark this review as flagged">
<img src="https://www.lendingtree.com/content/themes/lt-wp-www-theme/dist/images/lender-review/review-flag-mobile.png" alt="">
</button>
</div>
<div class="review-flag" id="m-review-flag-5df10a57cb4ee300015ca582">
<div class="review-flag-type">Do you want to flag this review?</div>
<button class="btn btn-secondary-bluelg save">Yes</button>
<button class="btn btn-secondary-bluelg cancel">No</button>
</div>
</div>
</div>

</div>
</div>
<div class="col-xs-12 reviewBtn">
<a class="clsReview" href="#">Full Review</a>
</div>
</div>
<div class="col-xs-12 mainReviews hiddenReviews">
<div class="col-xs-12 starReviews">
<div class="rating-stars-wrapper" itemprop="aggregateRating">
<div class="rating-stars-bottom">
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
</div>
<div class="rating-stars-top">
<div class="rating-stars-bar" style="width:80%;">
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
</div>
</div>
</div>
<div class="recommended">
<div class="numRec">(4 of 5)<span class="visually-hidden">stars</span></div>
<div class="lenderRec">Recommended</div>
</div>
</div>
<div class="col-lg-9 col-sm-8 col-xs-12 reviewDetail">
<p class="reviewTitle">Great service</p>
<p class="reviewText">I have a unique living situation and Marguerite helped make it happen. Thanks very much. Better than a balance transfer </p>
<div class="hideText">
<p class="consumerName">Timothy <span>from OSAGE CITY, KS </span></p>
<p class="consumerReviewDate">Reviewed in December 2019</p>
</div>
<div class="helpfull-count desktop-view">
<div class="review-type">WAS THIS REVIEW HELPFUL?</div>
<div class="helpfull-section">
<input type="hidden" class="reviewId" name="reviewId" value="5df106b1cb4ee300015ca581">
<div class="vote-action">
<button class="voteUp hover" id="voteupclick" data-voteupclick=0 aria-label="Mark this review as helpful">
<i class="lt4-ThumbsUp like-icon"></i>
<span class="likes helpfulAction" aria-hidden="true">0</span>
</button>
<span class="visually-hidden hiddenLike">0 People found this helpful</span>
</div>
<div class="vote-action">
<button class="voteDown hover" id="votedownclick" data-votedownclick=0 aria-label="Mark this review as not helpful">
<i class="lt4-ThumbsDown dislike-icon"></i>
<span class="dislikes helpfulAction" aria-hidden="true">0</span>
</button>
<span class="visually-hidden hiddenDislike">0 People found this not helpful</span>
</div>
<div class="flagged-review">
<button class="flag" id="flag-5df106b1cb4ee300015ca581" aria-label="Mark this review as flagged">
<div class='flag-content'>
<img src="https://www.lendingtree.com/content/themes/lt-wp-www-theme/dist/images/lender-review/review-flag-desktop.png" alt="">
<span class="flag-text">Flag review</span>
 </div>
</button>
</div>
</div>
</div>
</div>
<div class="col-lg-3 col-sm-4 col-xs-12 reviewPoints">
<div class="hideText">
<ul>
<li><p>Closed with Lender:</p> <div class="yes">Yes</div></li>
<li><p>Loan Type:</p> <div class="loanType">Personal Loan</div></li>
<li><p>Review Type:</p> <div class="loanType">Lender Review</div></li>
</ul>

<div class="helpfull-count mobile-view">
<div class="review-type">WAS THIS REVIEW HELPFUL?</div>
<div class="helpfull-section">
<input type="hidden" class="reviewId" name="reviewId" value="5df106b1cb4ee300015ca581">
<div class="vote-action">
<button class="voteUp hover" id="voteupclick" data-voteupclick=0 aria-label="Mark this review as helpful">
<i class="lt4-ThumbsUp like-icon"></i>
<span class="likes helpfulAction">0</span>
</button>
<span class="visually-hidden hiddenLike">0 People found this helpful</span>
</div>
<div class="vote-action">
<button class="voteDown hover" id="votedownclick" data-votedownclick=0>
<i class="lt4-ThumbsDown dislike-icon"></i>
<span class="dislikes helpfulAction">0</span>
</button>
<span class="visually-hidden hiddenDislike">0 People found this not helpful</span>
</div>
<div class="flagged-review">
<button class="flag" id="m-flag-5df106b1cb4ee300015ca581" aria-label="Mark this review as flagged">
<img src="https://www.lendingtree.com/content/themes/lt-wp-www-theme/dist/images/lender-review/review-flag-mobile.png" alt="">
</button>
</div>
<div class="review-flag" id="m-review-flag-5df106b1cb4ee300015ca581">
<div class="review-flag-type">Do you want to flag this review?</div>
<button class="btn btn-secondary-bluelg save">Yes</button>
<button class="btn btn-secondary-bluelg cancel">No</button>
</div>
</div>
</div>
 
</div>
</div>
<div class="col-xs-12 reviewBtn">
<a class="clsReview" href="#">Full Review</a>
</div>
</div>
<div class="col-xs-12 mainReviews hiddenReviews">
<div class="col-xs-12 starReviews">
<div class="rating-stars-wrapper" itemprop="aggregateRating">
<div class="rating-stars-bottom">
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
</div>
<div class="rating-stars-top">
<div class="rating-stars-bar" style="width:100%;">
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
<span class="lt4-Star" aria-hidden="true"></span>
</div>
</div>
</div>
<div class="recommended">
<div class="numRec">(5 of 5)<span class="visually-hidden">stars</span></div>
<div class="lenderRec">Recommended</div>
</div>
</div>
<div class="col-lg-9 col-sm-8 col-xs-12 reviewDetail">
<p class="reviewTitle">Excellent Company</p>
<p class="reviewText">The process was fast and easy. Money was in my account within days. First Midwest offered the best rates. Thanks to Cassie for making the process seamless from start to finish.</p>
<div class="hideText">
<p class="consumerName">Stef <span>from OIL CITY, PA </span></p>
<p class="consumerReviewDate">Reviewed in December 2019</p>
</div>
<div class="helpfull-count desktop-view">
<div class="review-type">WAS THIS REVIEW HELPFUL?</div>
<div class="helpfull-section">
<input type="hidden" class="reviewId" name="reviewId" value="5df08924cb4ee300015ca57f">
<div class="vote-action">
<button class="voteUp hover" id="voteupclick" data-voteupclick=0 aria-label="Mark this review as helpful">
<i class="lt4-ThumbsUp like-icon"></i>
<span class="likes helpfulAction" aria-hidden="true">0</span>
</button>
<span class="visually-hidden hiddenLike">0 People found this helpful</span>
 </div>
<div class="vote-action">
<button class="voteDown hover" id="votedownclick" data-votedownclick=0 aria-label="Mark this review as not helpful">
<i class="lt4-ThumbsDown dislike-icon"></i>
<span class="dislikes helpfulAction" aria-hidden="true">0</span>
</button>
<span class="visually-hidden hiddenDislike">0 People found this not helpful</span>
</div>
<div class="flagged-review">
<button class="flag" id="flag-5df08924cb4ee300015ca57f" aria-label="Mark this review as flagged">
<div class='flag-content'>
<img src="https://www.lendingtree.com/content/themes/lt-wp-www-theme/dist/images/lender-review/review-flag-desktop.png" alt="">
<span class="flag-text">Flag review</span>
</div>
</button>
</div>
</div>
</div>
</div>
<div class="col-lg-3 col-sm-4 col-xs-12 reviewPoints">
<div class="hideText">
<ul>
<li><p>Closed with Lender:</p> <div class="yes">Yes</div></li>
<li><p>Loan Type:</p> <div class="loanType">Personal Loan</div></li>
<li><p>Review Type:</p> <div class="loanType">Lender Review</div></li>
</ul>

<div class="helpfull-count mobile-view">
<div class="review-type">WAS THIS REVIEW HELPFUL?</div>
<div class="helpfull-section">
<input type="hidden" class="reviewId" name="reviewId" value="5df08924cb4ee300015ca57f">
<div class="vote-action">
<button class="voteUp hover" id="voteupclick" data-voteupclick=0 aria-label="Mark this review as helpful">
<i class="lt4-ThumbsUp like-icon"></i>
<span class="likes helpfulAction">0</span>
</button>
<span class="visually-hidden hiddenLike">0 People found this helpful</span>
</div>
<div class="vote-action">
<button class="voteDown hover" id="votedownclick" data-votedownclick=0>
<i class="lt4-ThumbsDown dislike-icon"></i>
<span class="dislikes helpfulAction">0</span>
 </button>
<span class="visually-hidden hiddenDislike">0 People found this not helpful</span>
</div>
<div class="flagged-review">
<button class="flag" id="m-flag-5df08924cb4ee300015ca57f" aria-label="Mark this review as flagged">
<img src="https://www.lendingtree.com/content/themes/lt-wp-www-theme/dist/images/lender-review/review-flag-mobile.png" alt="">
</button>
</div>
<div class="review-flag" id="m-review-flag-5df08924cb4ee300015ca57f">
<div class="review-flag-type">Do you want to flag this review?</div>
<button class="btn btn-secondary-bluelg save">Yes</button>
<button class="btn btn-secondary-bluelg cancel">No</button>
</div>
</div>
</div>

</div>
</div>
<div class="col-xs-12 reviewBtn">
<a class="clsReview" href="#">Full Review</a>
</div>
</div>

<div class="modal fade helpfullSectionModal" role="dialog" tabindex="-1">
<div class="modal-dialog modal-lg helpfull-flag-modal" role="document">
<div class="modal-content">
<div class="modal-body">
<button aria-label="Close" class="close" data-dismiss="modal" type="button">
<span aria-hidden="true">&times;</span>
</button>
<div class="helpfull-modal-content">
<p class="modal-desc">You have flagged this review for having inappropriate or invalid content.<br> This action requires your confirmation.</p>
<div class="modal-actions">
<button class="btn btn-orange save" type="button">Yes, I'd like to flag this review</button>
<button class="btn btn-white cancel" type="button">No, I made an error</button>
</div>
</div>
</div>
</div>
</div>
</div>

</div>
</div>
<div class="container">
<nav class="col-md-12 col-sm-12 col-xs-12 reviewNav glob-marg" aria-label="Pagination for lender reviews">
<ul class="lenderNav pagination">
<li class="pageNum page-item"><a class="page-link" href="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&pid=1" aria-label="Page 1">1</a></li>
<li class="page-item"><a class="page-link" href="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&pid=2" aria-label="Page 2">2</a></li>
<li class="page-item"><a class="page-link" href="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&pid=3" aria-label="Page 3">3</a></li>
<li class="page-item"><a class="page-link" href="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&pid=4" aria-label="Page 4">4</a></li>
<li class="page-item"><a class="page-link" href="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&pid=5" aria-label="Page 5">5</a></li>
<li class="page-item"><a class="page-link" href="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&pid=2" aria-label="Next Page">Next</a></li>
</ul>
</nav>
</div>
<nav class="col-md-9 col-sm-12 col-xs-12 reviewNavMobile glob-marg">
<ul class="lenderNav pagination">
<li class="col-xs-6 pageNum page-item">1 of <a class="pageNum" href="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&pid=226">226</a></li>
<li class="col-xs-6 page-item"><a href="https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&pid=2">Next</a></li>
</ul>
</nav>
<div class="container containerMobilePad">
<a class="moreReviewBtn">View More Reviews</a>
</div>
</section>
<form name="writeLenderReviewForm" id="writeLenderReviewForm" method="post" novalidate="novalidate">
<div class="modal fade lenderModal" id="review" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
<div class="modal-dialog" role="document">
<div class="modal-content">
<div class="modal-header">
<button type="button" class="close review-close" data-dismiss="modal" aria-hidden="true">&times;</button>
<div class="col-xs-12 lenderHeader npad">
<p class="writeRev">Write A Review</p>
<p class="lender">
<span id="lenderDisplayName"></span>
<input type="hidden" name="lenderName" id="lenderName" value="">
<input type="hidden" name="lenderReviewID" id="lenderReviewID" value="">
<input type="hidden" name="lenderId" id="lenderId" value="">
</p>
</div>
<div class="col-md-9 col-sm-12 col-xs-12 glob-marg">
<ul id="navTabs" class="nav nav-tabs nav-justified" role="tablist">
<li role="presentation" class="active singleLine">
<a aria-controls="tab1" data-target="#tab1" role="tab" data-toggle="tab">Reviews</a>
</li>
<li role="presentation" class="">
<a aria-controls="tab2" data-target="#tab2" role="tab" data-toggle="tab">Review Details</a>
</li>
<li role="presentation" class="">
<a aria-controls="tab3" data-target="#tab3" role="tab" data-toggle="tab">Personal Details</a>
</li>
</ul>
</div>
</div> 
<div class="modal-body">
<div class="tab-content">
<div class="tab-pane fade in active" id="tab1" role="tabpanel">
<div class="container tb-padding20">
<div class="row">
<div class="col-xs-12 col-md-8 glob-marg reviewTab">
<div class="rateExperience glob-marg">
<p class="rate">Rate your overall experience</p>
<div class="rating-stars-wrapper" itemprop="aggregateRating">
<div class="editable-rating-bar">
<input type="radio" class="rating-input" id="overallReviewRating-5" name="overallReviewRating" value="5">
<label for="overallReviewRating-5" class="lt4-Star-editable"></label>
<input type="radio" class="rating-input" id="overallReviewRating-4" name="overallReviewRating" value="4">
<label for="overallReviewRating-4" class="lt4-Star-editable"></label>
<input type="radio" class="rating-input" id="overallReviewRating-3" name="overallReviewRating" value="3">
<label for="overallReviewRating-3" class="lt4-Star-editable"></label>
<input type="radio" class="rating-input" id="overallReviewRating-2" name="overallReviewRating" value="2">
<label for="overallReviewRating-2" class="lt4-Star-editable"></label>
<input type="radio" class="rating-input" id="overallReviewRating-1" name="overallReviewRating" value="1">
<label for="overallReviewRating-1" class="lt4-Star-editable"></label>
</div>
<p class="exRating">Select your rating</p>
</div>
</div>
<div class="reviewForm">
<ul>
<li>
<label>Review Title</label>
<input type="text" title="reviewtitle" id="reviewtitle" name="reviewtitle" label="reviewtitle" placeholder="Example: It was a good experience" tabindex="1">
<div class="error reviewtitle-errMsg">Sorry, the maximum character count has been reached.</div>
</li>
<li>
<label>Review Text</label>
<textarea title="reviewtext" id="reviewtext" name="reviewtext" label="reviewtext" rows="7" placeholder="Example: The entire process was pretty easy. I was happy to work with them." tabindex="1"></textarea>
<div class="error reviewtext-errMsg">Your review must be at least 100 characters long.</div>
<div class="counter">(100 characters minimum)</div>
</li>
<li>
<a class="btn btn-blue continueBtn inactive">Continue</a>
<a data-dismiss="modal" aria-hidden="true" class="btn cancelBtn">Cancel</a>
</li>
</ul>
</div>
</div>
</div>
</div>
 </div> 
<div class="tab-pane fade" id="tab2" role="tabpanel">
<div class="container tb-padding20">
<div class="row">
<div class="col-md-8 col-sm-10 col-xs-12 npad glob-marg reviewDetailsTab">
<div class="col-xs-12 npad lenderCertModal container">
<div class="rating-stars-wrapper justify-content-start" itemprop="aggregateRating">
<label class="col-md-3 col-sm-3 col-xs-6 ratingForLabel npad">Interest rates</label>
<div class="editable-rating-bar col-md-4 col-sm-5 col-xs-6">
<input type="radio" class="rating-input interest-input" id="intrestRatesRating-5" name="intrestRatesRating" value="5">
<label for="intrestRatesRating-5" class="lt4-Star-editable"></label>
<input type="radio" class="rating-input interest-input" id="intrestRatesRating-4" name="intrestRatesRating" value="4">
<label for="intrestRatesRating-4" class="lt4-Star-editable"></label>
<input type="radio" class="rating-input interest-input" id="intrestRatesRating-3" name="intrestRatesRating" value="3">
<label for="intrestRatesRating-3" class="lt4-Star-editable"></label>
<input type="radio" class="rating-input interest-input" id="intrestRatesRating-2" name="intrestRatesRating" value="2">
<label for="intrestRatesRating-2" class="lt4-Star-editable"></label>
<input type="radio" class="rating-input interest-input" id="intrestRatesRating-1" name="intrestRatesRating" value="1">
<label for="intrestRatesRating-1" class="lt4-Star-editable"></label>
</div>
<label class="exRating col-md-5 col-sm-12 col-xs-12 npad">&nbsp;</label>
</div>
<div class="rating-stars-wrapper justify-content-start" itemprop="aggregateRating">
<label class="col-md-3 col-sm-3 col-xs-6 ratingForLabel npad">Fees & closing costs</label>
<div class="editable-rating-bar col-md-4 col-sm-5 col-xs-6">
<input type="radio" class="rating-input closing-cost-input" id="closingCostsRating-5" name="closingCostsRating" value="5">
<label for="closingCostsRating-5" class="lt4-Star-editable"></label>
<input type="radio" class="rating-input closing-cost-input" id="closingCostsRating-4" name="closingCostsRating" value="4">
<label for="closingCostsRating-4" class="lt4-Star-editable"></label>
<input type="radio" class="rating-input closing-cost-input" id="closingCostsRating-3" name="closingCostsRating" value="3">
<label for="closingCostsRating-3" class="lt4-Star-editable"></label>
<input type="radio" class="rating-input closing-cost-input" id="closingCostsRating-2" name="closingCostsRating" value="2">
<label for="closingCostsRating-2" class="lt4-Star-editable"></label>
 <input type="radio" class="rating-input closing-cost-input" id="closingCostsRating-1" name="closingCostsRating" value="1">
<label for="closingCostsRating-1" class="lt4-Star-editable"></label>
</div>
<label class="exRating col-md-5 col-sm-12 col-xs-12 npad">&nbsp;</label>
</div>
<div class="rating-stars-wrapper justify-content-start" itemprop="aggregateRating">
<label class="col-md-3 col-sm-3 col-xs-6 ratingForLabel npad">Customer service</label>
<div class="editable-rating-bar col-md-4 col-sm-5 col-xs-6">
<input type="radio" class="rating-input customer-service-input" id="customerServiceRating-5" name="customerServiceRating" value="5">
<label for="customerServiceRating-5" class="lt4-Star-editable"></label>
<input type="radio" class="rating-input customer-service-input" id="customerServiceRating-4" name="customerServiceRating" value="4">
<label for="customerServiceRating-4" class="lt4-Star-editable"></label>
<input type="radio" class="rating-input customer-service-input" id="customerServiceRating-3" name="customerServiceRating" value="3">
<label for="customerServiceRating-3" class="lt4-Star-editable"></label>
<input type="radio" class="rating-input customer-service-input" id="customerServiceRating-2" name="customerServiceRating" value="2">
<label for="customerServiceRating-2" class="lt4-Star-editable"></label>
<input type="radio" class="rating-input customer-service-input" id="customerServiceRating-1" name="customerServiceRating" value="1">
<label for="customerServiceRating-1" class="lt4-Star-editable"></label>
</div>
<label class="exRating col-md-5 col-sm-12 col-xs-12 npad">&nbsp;</label>
</div>
<div class="rating-stars-wrapper justify-content-start" itemprop="aggregateRating">
<label class="col-md-3 col-sm-3 col-xs-6 ratingForLabel npad">Responsiveness</label>
<div class="editable-rating-bar col-md-4 col-sm-5 col-xs-6">
<input type="radio" class="rating-input responsive-input" id="responsivenessRating-5" name="responsivenessRating" value="5">
<label for="responsivenessRating-5" class="lt4-Star-editable"></label>
<input type="radio" class="rating-input responsive-input" id="responsivenessRating-4" name="responsivenessRating" value="4">
<label for="responsivenessRating-4" class="lt4-Star-editable"></label>
<input type="radio" class="rating-input responsive-input" id="responsivenessRating-3" name="responsivenessRating" value="3">
<label for="responsivenessRating-3" class="lt4-Star-editable"></label>
<input type="radio" class="rating-input responsive-input" id="responsivenessRating-2" name="responsivenessRating" value="2">
 <label for="responsivenessRating-2" class="lt4-Star-editable"></label>
<input type="radio" class="rating-input responsive-input" id="responsivenessRating-1" name="responsivenessRating" value="1">
<label for="responsivenessRating-1" class="lt4-Star-editable"></label>
</div>
<label class="exRating col-md-5 col-sm-12 col-xs-12 npad">&nbsp;</label>
</div>
</div>
<div class="col-xs-12 typeLoan npad">
<p>What type of loan was requested?</p>
</div>
<div class="col-xs-12 reviewDetailForm npad">
<div class="clearfix"></div>
<a class="btn btn-blue continueBtn inactive">Continue</a>
<a class="btn cancelBtn">Back</a>
</div>
</div>
</div>
</div>
</div> 
<div class="tab-pane fade" id="tab3" role="tabpanel">
<div class="container tb-padding20">
<div class="row">
<div class="col-xs-12 col-md-8 glob-marg">
<div class="personalDetailForm">
<ul>
<li class="clearfix">
<div class="col-md-7 col-sm-6 col-xs-12 npad">
<p>Did you close with this lender?</p>
</div>
<div class="col-md-2 col-sm-3 col-xs-6">
<input type="radio" id="yes" name="closedWithLender" value="Yes">
<label for="yes">Yes</label>
</div>
<div class="col-md-2 col-sm-3 col-xs-6">
<input type="radio" id="no" name="closedWithLender" value="No">
<label for="no">No</label>
</div>
</li>
<li class="clearfix">
<div class="col-md-7 col-sm-6 col-xs-12 npad">
<p>Would you recommend this lender?</p>
</div>
<div class="col-md-2 col-sm-3 col-xs-6">
<input type="radio" id="yes2" name="recommendThisLender" value="Yes">
<label for="yes2">Yes</label>
</div>
<div class="col-md-2 col-sm-3 col-xs-6">
<input type="radio" id="no2" name="recommendThisLender" value="No">
<label for="no2">No</label>
</div>
</li>
</ul>
 <p class="headerType">Personal Information</p>
<div>
<label>First Name</label>
<input type="text" title="firstname" id="displayname" name="displayname" label="displayname" placeholder="Enter first name only" tabindex="1">
<label for="displayname" generated="true" class="error errorMsg">
<div id="err-displayname"></div>
</label>
</div>
<div id="MyLTAccount">


<label>Enter your email</label>
<input type="text" title="email" id="email" name="email" label="email" placeholder="Enter your email address (It will not appear on the review)" tabindex="1">
<input type="hidden" id="hdnEmail" name="hdnEmail">
<input type="hidden" id="treeAuthId" name="treeAuthId">
<input type="hidden" id="userLoggedIn" name="userLoggedIn">
<label for="email" generated="true" class="error errorMsg">
<div id="err-email"></div>
</label>
</div>
<label>Location</label>
<input type="tel" title="zipcode" id="zipcode" name="zipcode" maxlength="5" label="zipcode" placeholder="Enter your ZIP code" tabindex="1">
<input type="hidden" id="location" name="location">
<label for="zipcode" generated="true" class="error errorMsg">
<div id="err-zipcode"></div>
</label>
<div class="modalDisc row">
<div class="col-xs-12 discpad">
<input type="checkbox" id="disclaimer" name="disclaimer" />
<label for="disclaimer">
I agree to LendingTree <a href=" https://www.lendingtree.com/legal/reviews-ugc-terms-of-use" target="_blank">review guidelines</a> and certify that I am writing this review based on my experience. I understand that I may be emailed by the Lender above in relation to my review.
</label>
</div>
</div>
<div class="clearfix"></div>
<button type="submit" class="btn btn-gray btn-fullwidth btn-arrow button--form-start submitLenderReviewBtn" disabled>Submit</button>
<a class="btn cancelBtn">Back</a>
</div>
</div>
</div>
</div>
</div> 
</div> 
</div> 
</div>
</div>
</div> 
</form>
<div class="experience-model">
<div class="model-body">
<span class="experience-model-close">&times;</span>
<h3>Thank you for sharing your experience</h3>
<h4>Here are a few tips for writing a top-notch review for a company in our marketplace:</h4>
<div class="do-dont-block">
<div class="do-block">
<h5>Do</h5>
<label>Describe your experience with this company. Tell us why you chose this company and explain what you liked most and least about it.</label>
<label>Expect to see a confirmation screen once you submit your review.</label>
<label>Be patient. Your review may take five to eight days to appear on the site.</label>
</div>
<div class="dont-block">
<h5>Don't</h5>
<label>Mention other companies. Your review is about this one specifically. None others.</label>
<label>Include any personal information, such as your first and last name, email address or phone number.</label>
<label>Use profane or offensive language. Keep it clean.</label>
</div>
</div>
<button class="btn btn-blue continue-btn">Continue</button>
</div>
</div>
<div id="review-popup" class="review-thanks-model">
<div>
<i class="lt4-Ex" id="closeReviewPopup"></i>
<h2 id="success-title"></h2>
<p id="success-msg"></p>
<p id="error-msg"></p>
</div>
</div>

<div aria-labelledby="custSatisfactionLabel" class="modal fade" id="custSatisfactionModal" role="dialog" tabindex="-1">
<div class="modal-dialog lender-review" role="document">
<div class="modal-content cust-satisfaction-modal">
<div class="modal-body">
<button aria-label="Close" class="close" data-dismiss="modal" type="button"><span aria-hidden="true">&times;</span></button>
<div>
<p>Customer Satisfaction rating is based directly on customer ratings and reviews. Customers rate lenders on their customer service, interest rates, fees and closing cost and overall experience.</P>
</div>
</div>
</div>
</div>
</div>

<div aria-labelledby="certifiedLenderLabel" class="modal fade" id="certifiedLenderModal" role="dialog" tabindex="-1">
<div class="modal-dialog lender-review" role="document">
<div class="modal-content certified-lender-modal">
<div class="modal-body">
<button aria-label="Close" class="close" data-dismiss="modal" type="button"><span aria-hidden="true">&times;</span></button>
<div>
<label>LendingTree Certification:</label>
<p>The LendingTree Certification Program recognizes Lenders and Loan Officers with outstanding performance on the LendingTree Network, they are committed to providing exceptional customer service and are graduates of LendingTree University.</p>
<label>LendingTree Certification:</label>
<ul>
<li>
<img src="https://lt-scorecard-logo.s3.amazonaws.com/Certified_Lender_2019.png" alt="Certified Lender">
<div class="content">
<b>Certified Lenders</b> have demonstrated their organizational commitment to employee development, at least 50% of their loan professionals have been certified while also providing exemplary service to LendingTree consumers.
</div>
</li>
</ul>
<label>Loan Officer Certifications:</label>
<ul>
<li><img src="https://lt-scorecard-logo.s3.amazonaws.com/Gold_Leaf_2019.png" alt="Certified Gold Leaf">
<div class="content">
<b>Gold Leaf</b> is the cornerstone of the loan officer certification program and is designed to recognize loan officers committed to their own professional development while adhering to LendingTree best practices. Gold Leaf recipients know the fundamentals of LendingTree and online lending, they are equipped with the necessary skills to be best-in-class loan professionals.
</div>
</li>
<li class="mb-none">
<img src="https://lt-scorecard-logo.s3.amazonaws.com/Presidents_Club_2019.png" alt="Certified President's Club">
<div class="content">
<b>President&rsquo;s Club</b> is presented to an elite group of loan officers based on success levels in several areas including adherence to LendingTree best practices, commitment to professional development and dedication to customer excellence. Recipients have also met all Gold Leaf criteria.
</div>
</li>
</ul>
</div>
</div>
</div>
</div>
</div>

<div class="modal gModal fade col-md-4 disclaimer-modal" id="disclaimerModal" tabindex="-1" role="dialog" aria-labelledby="lenderDisclaimerModal" aria-hidden="true">
 <div class="modal-dialog">
<div class="modal-content">
<div class="modal-header">
<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
<h4 class="modal-title">First Midwest Bank</h4>
</div>
<div class="modal-body">
<p>Let's answer a few short questions and see what offers First Midwest Bank and other lenders may have for you.</p>
</div>
<div class="disclaimer-modal-button">
<a class="btn btn-blue" href="/redirect/offers?id=wp-personal&userselectedlender=52903183">Continue</a>
</div>
</div>
</div>
</div>
<script type="5870d3775a1169cbe2c6706a-text/javascript">
    $(document).ready(function() {
        var reviewObj = [];
                reviewObj.push({"reviewId":"5df2654edb03740001f79b8b", "voteUp": "0", "voteDown":"0", "isFlagged": ""  });
                reviewObj.push({"reviewId":"5df23499b527b4000157ea4e", "voteUp": "0", "voteDown":"0", "isFlagged": ""  });
                reviewObj.push({"reviewId":"5df1b258cb4ee300015ca599", "voteUp": "0", "voteDown":"0", "isFlagged": ""  });
                reviewObj.push({"reviewId":"5df18909db03740001f79b7e", "voteUp": "0", "voteDown":"0", "isFlagged": ""  });
                reviewObj.push({"reviewId":"5df165acdb03740001f79b73", "voteUp": "0", "voteDown":"0", "isFlagged": ""  });
                reviewObj.push({"reviewId":"5df161cccb4ee300015ca58c", "voteUp": "0", "voteDown":"0", "isFlagged": ""  });
                reviewObj.push({"reviewId":"5df1330d29990e0001faa6f8", "voteUp": "0", "voteDown":"0", "isFlagged": ""  });
                reviewObj.push({"reviewId":"5df10a57cb4ee300015ca582", "voteUp": "0", "voteDown":"0", "isFlagged": ""  });
                reviewObj.push({"reviewId":"5df106b1cb4ee300015ca581", "voteUp": "0", "voteDown":"0", "isFlagged": ""  });
                reviewObj.push({"reviewId":"5df08924cb4ee300015ca57f", "voteUp": "0", "voteDown":"0", "isFlagged": ""  });
                localStorage.removeItem("reviews_details");
        localStorage.setItem("reviews_details", JSON.stringify(reviewObj));
        var reviewObjVal=JSON.parse(localStorage.getItem("reviews_details"));
        for(var i = 0; i < reviewObjVal.length; i++)
        {
            var reviewId = reviewObjVal[i].reviewId;
            $('.mainReviews .helpfull-section').each(function(j, obj) {
                if($(this).find(".reviewId").val() == reviewId)
                {
                    $(this).find(".likes").text(reviewObjVal[i].voteUp);
                    $(this).find(".dislikes").text(reviewObjVal[i].voteDown);
                    if(reviewObjVal[i].isFlagged)
                    {
                        $(this).find("#flag-" + reviewId ).addClass('flagged flagColor not-allowed');
                        $(this).find("#flag-" + reviewId ).find('.flag-text').text('Flagged');
                    }
                }
             });
        }
                        $("#certifiedLoCarousel").addClass("stop-carousel");
                $("div").removeClass("owl-dots");
                    sessionStorage.removeItem('allReviews');
                    var elm = $("[name='keywords']");
        if(elm.length > 0) {
            elm.attr("content", "keywords");
        }
        else {
            $("head").append("<meta name='keywords' content='First Midwest Bank,First Midwest Bank ratings ,First Midwest Bank reviews,First Midwest Bank scorecard, First Midwest Bank ratings and reviews' >");
        }
        $.getJSON("https://www.lendingtree.com" + "/account/user-info").done(function( userData ) {
            if(userData.IsUserLoggedIn){
                $("#MyLTAccount").hide();
                $('#hdnEmail').val(userData.Email);
                $('#displayname').val(userData.FirstName);
                $('#treeAuthId').val(userData.TreeAuthUid);
                $('input[name=haveLTAccount]:nth(0)').attr('checked',true);
                $('#userLoggedIn').val("Yes");

                // Handles logged in user writing review
                $('#frame').attr('src', 'about:blank');
            }else{
                $("#MyLTAccount").show();
                var iframeSrc = window.location.origin + '/loginproxy?logintheme=mcCommon&url=' + encodeURIComponent(window.location.href.split('?')[0]);
                $('#frame').attr('src', iframeSrc)
            }
        }).fail(function() {
            $("#MyLTAccount").show();
            var iframeSrc = window.location.origin + '/loginproxy?logintheme=mcCommon&url=' + encodeURIComponent(window.location.href.split('?')[0]);
            $('#frame').attr('src', iframeSrc)
        });
    });
    $(".moreReviewBtn").click(function () {
        $(".hiddenReviews").css('display') == 'none' ? sessionStorage.setItem('allReviews', 'true') : sessionStorage.setItem('allReviews', 'false');
    });
    </script> </main>
<footer id="at-footer">
<h2 class="visually-hidden">Footer Navigation</h2>
<div class="main-section">
<div class="footer-nav">
<section class="footer-menu">
<h3 class="h3">About Us</h3>
<ul>
<li><a href="https://www.lendingtree.com/press/" rel="nofollow">About LendingTree</a></li>
<li><a href="https://www.lendingtree.com/blog/">Blog</a></li>
<li><a href="https://www.lendingtree.com/careers/" rel="nofollow">Careers</a></li>
<li><a href="https://www.lendingtree.com/about/contact-us/" rel="nofollow">Contact Us</a></li>
<li><a href="https://investors.lendingtree.com/" rel="nofollow">Investors</a></li>
<li><a href="https://www.lendingtree.com/about/partner-with-us/">Partner with Us</a></li>
<li><a href="https://www.lendingtree.com/press/press-releases/" rel="nofollow">Press Room</a></li>
<li><a href="https://www.lendingtree.com/widget/" rel="nofollow">Widgets</a></li>
</ul>
</section>
<section class="footer-menu">
<h3 class="h3">Legal Information</h3>
<ul>
<li><a href="https://www.lendingtree.com/legal" rel="nofollow">Overview</a></li>
<li><a href="https://www.lendingtree.com/legal/privacy-policy" rel="nofollow">Privacy</a></li>
<li><a href="https://www.lendingtree.com/legal/security" rel="nofollow">Security</a></li>
<li><a href="https://www.lendingtree.com/legal/advertising-disclosures" rel="nofollow">Advertising Disclosures</a></li>
<li><a href="https://www.lendingtree.com/legal/terms-of-use" rel="nofollow">Terms of Use</a></li>
<li><a href="https://www.lendingtree.com/legal/licenses-and-disclosures" rel="nofollow">Licenses & Disclosures</a></li>
<li><a href="https://www.lendingtree.com/publications" rel="nofollow">Unsubscribe</a></li>
</ul>
</section>
<section class="footer-menu">
<h3 class="h3">Other Sites</h3>
<ul>
<li><a href="https://www.comparecards.com/" rel="nofollow noopener" target="_blank">CompareCards</a></li>
<li><a href="https://www.depositaccounts.com/" rel="nofollow noopener" target="_blank">DepositAccounts</a></li>
<li><a href="https://www.magnifymoney.com/" rel="nofollow noopener" target="_blank">MagnifyMoney</a></li>
<li><a href="https://ovationcredit.com/" rel="nofollow noopener" target="_blank">Ovation Credit</a></li>
<li><a href="https://quotewizard.com/" rel="nofollow noopener" target="_blank">QuoteWizard</a></li>
<li><a href="https://www.simpletuition.com/" rel="nofollow noopener" target="_blank">SimpleTuition</a></li>
<li><a href="https://snapcap.com/" rel="nofollow noopener" target="_blank">SnapCap</a></li>
<li><a href="https://studentloanhero.com/" rel="nofollow noopener" target="_blank">Student Loan Hero</a></li>
<li><a href="https://www.valuepenguin.com/" rel="nofollow noopener" target="_blank">ValuePenguin</a></li>
</ul>
</section>
<div class="blank-div">
</div>
<div class="follow-app">
<section class="follow">
<h3 class="h3">Follow Us</h3>
<ul class="follow-us">
<li class="youtube"><a href="https://www.youtube.com/user/lendingtree" target="_blank" rel="noopener" aria-label="LendingTree on YouTube"></a></li>
<li class="twitter"><a href="https://twitter.com/LendingTree" target="_blank" rel="noopener" aria-label="LendingTree on Twitter"></a></li>
<li class="facebook"><a href="https://www.facebook.com/LendingTree" target="_blank" rel="noopener" aria-label="LendingTree on Facebook"></a></li>
<li class="pinterest"><a href="https://www.pinterest.com/lendingtree" target="_blank" rel="noopener" aria-label="LendingTree on Pinterest"></a></li>
<li class="instagram"><a href="https://www.instagram.com/LendingTree" target="_blank" rel="noopener" aria-label="LendingTree on Instagram"></a></li>
</ul>
</section>
<section class="app">
<h3 class="h3">Download Our App</h3>
<ul class="app-download">
<li>
<a href="https://app.adjust.com/hyl2bh?fallback=https://itunes.apple.com/us/app/my-lendingtree/id957868548?mt=8" rel="noopener">
<img src="https://www.lendingtree.com/content/themes/lt-wp-www-theme/dist/images/apple-app-store-badge.svg" id="app-store" alt="Apple App Store" />
</a>
</li>
<li>
<a href="https://app.adjust.com/h5v9i5?fallback=https://play.google.com/store/apps/details?id=com.ltmoneycenter_android.PROD&hl=en" rel="noopener">
<img src="https://www.lendingtree.com/content/themes/lt-wp-www-theme/dist/images/google-play-store-badge.svg" id="google-play" alt="Google Play" />
</a>
</li>
</ul>
</section>
</div>
</div>
<div class="clear-fix"></div>
<div class="footer-terms" id="footerDisclosure">
LendingTree, LLC is a Marketing Lead Generator and is a Duly Licensed Mortgage Broker, as required by law, with its main office located at 11115 Rushmore Dr., Charlotte, NC 28277, Telephone Number 866-501-2397 <a href="https://www.lendingtree.com/tddtty" rel="nofollow">(TDD/TTY)</a>. <a href="http://www.nmlsconsumeraccess.org/EntityDetails.aspx/COMPANY/1136" target="_blank" rel="nofollow noopener">NMLS Unique Identifier #1136</a>. LendingTree, LLC is known as LT Technologies in lieu of true name LendingTree, LLC in NY. LendingTree technology and processes are patented under U.S. Patent Nos. 6,385,594 and 6,611,816 and licensed under U.S. Patent Nos. 5,995,947 and 5,758,328. &copy; 2016 LendingTree, LLC. All Rights Reserved. This site is directed at, and made available to, persons in the continental U.S., Alaska and Hawaii only.
</div>
<div class="security-icons">
<p><strong>Online Security</strong>: <a href="https://www.lendingtree.com/about/onlinesecurity" target="_blank" rel="nofollow noopener">Protect Against Fraud</a></p>
<a class="equal-housing" href="https://www.lendingtree.com/legal/equal-housing-opportunity" target="_blank" rel="nofollow noopener">
<img width="40" height="28" src="https://www.lendingtree.com/content/themes/lt-wp-www-theme/dist/images/icon-equal-housing.svg" alt="Equal Housing Opportunity" />
</a>
<a class="bbb" href="https://www.bbb.org/charlotte/business-reviews/online-loans-referral-services/lendingtree-in-charlotte-nc-109412" target="_blank" rel="nofollow noopener">
<img width="35" height="53" src="https://www.lendingtree.com/content/themes/lt-wp-www-theme/dist/images/icon-bbb.svg" alt="Better Business Bureau" />
</a>
<a href="https://secure.comodo.com/ttb_searcher/trustlogo?v_querytype=W&v_shortname=SC4&v_search=https://www.lendingtree.com/about/onlinesecurity&x=6&y=5" class="comodo" target="_blank" rel="nofollow noopener">
<img width="100" height="26" src="https://www.lendingtree.com/content/themes/lt-wp-www-theme/dist/images/icon-comodo.svg" alt="Comodo Secure" />
</a>
</div>
<div class="clear-fix"></div>
</div>
</footer><script type='application/ld+json'>{"@context":"http:\/\/schema.org","@type":"ProfilePage","name":"First Midwest Bank","description":"At First Midwest, you'll get the financing you want and the momentum you need to tackle whatever is on your to do list. Our Gold Leaf certified bankers will be with you every step of the way with low rates, an easy application process, and quick and convenient closings. Get connected to a First Midwest Banker today. You'll be glad you did.","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.9","reviewCount":2255}}</script>
<script type="5870d3775a1169cbe2c6706a-text/javascript" src='https://nebula-cdn.kampyle.com/wu/65391/onsite/embed.js' async='async'></script>
<script type="5870d3775a1169cbe2c6706a-text/javascript">
/* <![CDATA[ */
var tocplus = {"smooth_scroll":"1"};
/* ]]> */
</script>
<script type="5870d3775a1169cbe2c6706a-text/javascript" src='https://www.lendingtree.com/content/plugins/table-of-contents-plus/front.min.js?ver=1509'></script>
<script type="5870d3775a1169cbe2c6706a-text/javascript">
/* <![CDATA[ */
var LT_TRACKING_CONFIG = {"ltanalyticsIsNonprod":"false","currentId":"","pageTemplate":"","pageIntendedProduct":"Brand"};
/* ]]> */
</script>
<script type="5870d3775a1169cbe2c6706a-text/javascript" src='https://www.lendingtree.com/content/themes/lt-wp-www-theme/dist/scripts/main-3f90693697.js'></script>
<script type="5870d3775a1169cbe2c6706a-text/javascript">
!function(e,t){"function"==typeof define&&define.amd?define([],t):"object"==typeof module&&module.exports?module.exports=t():e.ltReferrerTrack=t()}(this,function(){var t,a="LTNAV_TRACK";return"undefined"!=typeof sessionStorage?{get:function(){return t||(t=JSON.parse(sessionStorage.getItem(a)),sessionStorage.removeItem(a),t)},set:function(e){return sessionStorage.setItem(a,JSON.stringify(e)),t=e,!0}}:{get:function(){return t},set:function(e){return t=e,!0}}});var queryParams=window.ltReferrerTrack&&window.ltReferrerTrack.get(),recommendationID="";function receiveStatus(e){e.data&&e.data.TreeAuthUid&&(window.ltanalytics=window.ltanalytics||[],window.ltanalytics.push(function(){window.adobe&&window.adobe.target&&window.adobe.target.getOffers&&window.adobe.target.getOffers({request:{id:{thirdPartyId:e.data.TreeAuthUid},prefetch:{mboxes:[{index:0,name:"mbox3rdparty-data",profileParameters:{id:e.data.TreeAuthUid}}]}}})}))}queryParams&&"object"==typeof queryParams&&(queryParams.ltwarea||queryParams.ltwpos||queryParams.ltwpid)&&(recommendationID=queryParams.ltwpid+":"+queryParams.ltwarea+":"+LT_TRACKING_CONFIG.currentId+":"+queryParams.ltwpos),window.ltanalytics&&window.ltanalytics.page(location.pathname,{path:location.pathname,isNonProd:LT_TRACKING_CONFIG.ltanalyticsIsNonprod,recommendationids_clicked:recommendationID,isAuthenticated:new RegExp("(^|; )ajs_is_fcs=([^;]*)").test(document.cookie),isFreeCreditScore:(document.cookie.match("(^|; )ajs_is_fcs=([^;]*)")||0)[2]||"",page_intended_product:LT_TRACKING_CONFIG.pageIntendedProduct,ltnav:"object"!=typeof queryParams?queryParams:null,pageTemplate:LT_TRACKING_CONFIG.pageTemplate}),window.addEventListener("message",receiveStatus,!1),function(e,t,d){e.ltanalytics&&0!=d("[data-target-area-name]").length&&d(e).scroll(function(){var a,r,n=d("body").attr("data-item-id"),o=d("[data-target-area-name]").attr("data-target-area-name"),i=[];d.each(d("[data-target-area-name] [data-target-item-position]"),function(e,t){r=d(t).attr("data-target-item-position"),a=d(t).find("a").attr("data-target-item-id"),i.push(n+":"+o+":"+a+":"+r)}),d("[data-target-area-name]").offset().top+d("[data-target-area-name]").outerHeight()-d(e).height()<d(this).scrollTop()&&(e.ltanalytics.track("Recommendations Viewed",{recommendationids_viewed:i.join()}),d(e).off("scroll"))})}(window,document,jQuery);
!function(n,a,l){"use strict";var e=[{id:"homeloans",label:"Home Loans"},{id:"autoloans",label:"Auto Loans"},{id:"personalloans",label:"Personal Loans"},{id:"businessloans",label:"Business Loans"},{id:"studentloans",label:"Student Loans"},{id:"creditcards",label:"Credit Cards"},{id:"freereditscore",label:"Free Credit Score"}];function i(a,n){var e=l(a).text(),i=l(location).attr("href"),t="/"==location.pathname?"/":/.+?\:\/\/.+?(\/.+?)(?:#|\?|$)/.exec(i)[1];n=(n=void 0===n?"":n+"-").replace(/\s+/g,"_"),e=(e=e.replace(/\s+/g,"_")).replace(/[\W]/g,"-"),l(a).addClass("ltnav-track"),l(a).val(n+e+":"+t)}l(a).on("click","a.ltnav-track",function(){ltReferrerTrack.set(l(this).val())}),l(n).on("load",function(){l.each(e,function(a,e){i(l("#"+e.id+" a:first")),l("#"+e.id+" .col-md-3 a").each(function(a,n){l(n).hasClass("btn")||i(n,e.label)})}),l(".mainMenu li").each(function(a){l(this).find("a:not(.menuLinks, .back, .tertiary)").each(function(a){i(l(this))})})}),l(a).on("click",".signin, .sign-in-link",function(){if(n.ltanalytics){var a="Homepage-menu";"signin"===this.className&&(a="Homepage-header"),n.ltanalytics.track("SignIn Clicked",{"signIn-clicked-location":a})}})}(window,document,jQuery);
</script>
<script type="5870d3775a1169cbe2c6706a-text/javascript">
/* <![CDATA[ */
var lender_data = {"lenderId":"52903183","name":"First Midwest Bank","reviewCount":"2255","averageOverallRating":"4.9","logoPath":"https:\/\/lt-scorecard-logo.s3.amazonaws.com\/52903183SEO.gif","vertical":"Personal","certLogo":"","city":"Itasca","state":"IL","postalCode":"60143"};
/* ]]> */
</script>
<script type="5870d3775a1169cbe2c6706a-text/javascript" src='https://www.lendingtree.com/content/themes/lt-wp-www-theme/dist/scripts/track-lender-5b4d7482fb.js'></script>
<script type="5870d3775a1169cbe2c6706a-text/javascript" src='https://www.lendingtree.com/content/themes/lt-wp-www-theme/dist/scripts/lender-e00c72128a.js'></script>
<script type="5870d3775a1169cbe2c6706a-text/javascript">
/* <![CDATA[ */
var reviewPostParameter = {"reviewPostUrl":"https:\/\/www.lendingtree.com\/content\/mu-plugins\/lt-review-api\/review-api-proxy.php"};
/* ]]> */
</script>
<script type="5870d3775a1169cbe2c6706a-text/javascript" src='https://www.lendingtree.com/content/mu-plugins/lt-review-api/assets/scripts/submit-review.js?ver=5.2.4'></script>
<script type="5870d3775a1169cbe2c6706a-text/javascript" src='https://www.lendingtree.com/content/themes/lt-wp-www-theme/dist/scripts/review-068648e2d7.js'></script>
<script type="5870d3775a1169cbe2c6706a-text/javascript">window.lazyLoadOptions = {
                elements_selector: "[loading=lazy],.rocket-lazyload",
                data_src: "lazy-src",
                data_srcset: "lazy-srcset",
                data_sizes: "lazy-sizes",
                class_loading: "lazyloading",
                class_loaded: "lazyloaded",
                threshold: 300,
                callback_loaded: function(element) {
                    if ( element.tagName === "IFRAME" && element.dataset.rocketLazyload == "fitvidscompatible" ) {
                        if (element.classList.contains("lazyloaded") ) {
                            if (typeof window.jQuery != "undefined") {
                                if (jQuery.fn.fitVids) {
                                    jQuery(element).parent().fitVids();
                                }
                            }
                        }
                    }
                },
use_native: true};
        window.addEventListener('LazyLoad::Initialized', function (e) {
            var lazyLoadInstance = e.detail.instance;
        
            if (window.MutationObserver) {
                var observer = new MutationObserver(function(mutations) {
                    var image_count = 0;
                    var iframe_count = 0;
                    var rocketlazy_count = 0;

                    mutations.forEach(function(mutation) {
                        for (i = 0; i < mutation.addedNodes.length; i++) {
                            if (typeof mutation.addedNodes[i].getElementsByTagName !== 'function') {
                                return;
                            }

                           if (typeof mutation.addedNodes[i].getElementsByClassName !== 'function') {
                                return;
                            }

                            images = mutation.addedNodes[i].getElementsByTagName('img');
                            is_image = mutation.addedNodes[i].tagName == "IMG";
                            iframes = mutation.addedNodes[i].getElementsByTagName('iframe');
                            is_iframe = mutation.addedNodes[i].tagName == "IFRAME";
                            rocket_lazy = mutation.addedNodes[i].getElementsByClassName('rocket-lazyload');

                            image_count += images.length;
			                iframe_count += iframes.length;
			                rocketlazy_count += rocket_lazy.length;
                            
                            if(is_image){
                                image_count += 1;
                            }

                            if(is_iframe){
                                iframe_count += 1;
                            }
                        }
                    } );

                    if(image_count > 0 || iframe_count > 0 || rocketlazy_count > 0){
                        lazyLoadInstance.update();
                    }
                } );
                
                var b      = document.getElementsByTagName("body")[0];
                var config = { childList: true, subtree: true };
                
                observer.observe(b, config);
            }
        }, false);</script><script data-no-minify="1" async src="https://www.lendingtree.com/content/plugins/rocket-lazy-load/assets/js/12.0/lazyload.min.js" type="5870d3775a1169cbe2c6706a-text/javascript"></script><script type="5870d3775a1169cbe2c6706a-text/javascript">function lazyLoadThumb(e){var t='<img loading="lazy" data-lazy-src="https://i.ytimg.com/vi/ID/hqdefault.jpg" alt="" width="480" height="360"><noscript><img src="https://i.ytimg.com/vi/ID/hqdefault.jpg" alt="" width="480" height="360"></noscript>',a='<div class="play"></div>';return t.replace("ID",e)+a}function lazyLoadYoutubeIframe(){var e=document.createElement("iframe"),t="https://www.youtube.com/embed/ID?autoplay=1";t+=0===this.dataset.query.length?'':'&'+this.dataset.query;e.setAttribute("src",t.replace("ID",this.dataset.id)),e.setAttribute("frameborder","0"),e.setAttribute("allowfullscreen","1"),e.setAttribute("allow", "accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"),this.parentNode.replaceChild(e,this)}document.addEventListener("DOMContentLoaded",function(){var e,t,a=document.getElementsByClassName("rll-youtube-player");for(t=0;t<a.length;t++)e=document.createElement("div"),e.setAttribute("data-id",a[t].dataset.id),e.setAttribute("data-query", a[t].dataset.query),e.innerHTML=lazyLoadThumb(a[t].dataset.id),e.onclick=lazyLoadYoutubeIframe,a[t].appendChild(e)});</script> <script type="5870d3775a1169cbe2c6706a-text/javascript">window.NREUM||(NREUM={});NREUM.info={"beacon":"bam.nr-data.net","licenseKey":"b6d3a1e0ad","applicationID":"78570423","transactionName":"ZFIHNhMHXkQEBUwICV0YMBAISVlZAQNATxZbRw==","queueTime":0,"applicationTime":2225,"atts":"SBUEQFsdTUo=","errorBeacon":"bam.nr-data.net","agent":""}</script><script src="https://ajax.cloudflare.com/cdn-cgi/scripts/7089c43e/cloudflare-static/rocket-loader.min.js" data-cf-settings="5870d3775a1169cbe2c6706a-|49" defer=""></script></body>
</html>
"""