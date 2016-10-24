<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "https://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="https://www.w3.org/1999/xhtml" lang="sl">
<head>
<link rel="canonical" href="/oglasi-prodaja/ljubljana-mesto/stanovanje/cena-do-200000-eur/20/" /><meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta http-equiv="content-language" content="sl" />
<meta name="msvalidate.01" content="D9C9544A6631C60218BF47FD618F42E5" />

<meta http-equiv="X-UA-Compatible" content="IE=EDGE" />
<meta name="SKYPE_TOOLBAR" content="SKYPE_TOOLBAR_PARSER_COMPATIBLE" />
<meta name="format-detection" content="telephone=no">
<title>Prodaja </title>
<meta name="Keywords" content="" />
<meta name="Description" content="Rezultati iskanja nepremiènin: Prodaja  na Nepremicnine.net" />
<meta property="og:image" content="https://www.nepremicnine.net/apple-touch-icon-144x144-precomposed.png" /><link rel="icon" href="/images/icon_n.gif" type="image/gif" sizes="16x16" />
<link rel="stylesheet" href="/css/font-awesome.min.css?v=3">

<!-- Tooltip -->
<link rel="stylesheet" href="/css/tooltipster.css">
<link rel="stylesheet" href="/css/tooltipster-shadow.css">

<!--<link href="/css/styles.css?v=15.05.22" rel="stylesheet" type="text/css" media="all" />-->

<link href="/css/jqtransform.css" rel="stylesheet"  type="text/css" media="all" />
<link href="/css/jquery-ui.css" rel="stylesheet"  type="text/css" media="all" />
<link rel="stylesheet" type="text/css" href="/css/facet.css" media="all" />
<script type="text/javascript" src="/Scripts/sa.js"></script>
<script type="text/javascript" src="/Scripts/jquery-1.11.1.min.js"></script>
<script type="text/javascript" src="/Scripts/jquery-migrate-1.2.1.min.js"></script>


    <script type="text/javascript" src="/Scripts/jquery-ui-1.11.1.custom.min.js"></script>
    <script type="text/javascript" src="/Scripts/jquery.mobile.custom.min.js"></script>
    <script type="text/javascript" src="/Scripts/jquery.ui.touch-punch.min.js"></script>
    <!--<script type="text/javascript" src="/Scripts/jquery.mobile-1.4.4.min.js"></script>-->
    <!--<script type="text/javascript" src="/Scripts/jquery-ui-1.11.1.custom.min.js"></script>
    <script type="text/javascript" src="/Scripts/jquery.mobile.custom.min.js"></script>
    <script type="text/javascript" src="/Scripts/jquery.ui.touch-punch.min.js"></script>-->

<!--[if (gte IE 6)&(lte IE 8)]>
  <script type="text/javascript" src="/Scripts/selectivizr-min.js"></script>
<![endif]-->

<script type="text/javascript" src="/Scripts/forms.js"></script><!--forms-->
<script type="text/javascript" src="/Scripts/pagination.js"></script>

<link href="/css/colorbox.css" rel="stylesheet" type="text/css" media="all" /><!--galerija litebox-->
<script type="text/javascript" src="/Scripts/jquery.colorbox-min.js"></script><!--galerija litebox-->
<script type="text/javascript" src="/Scripts/autoNumeric-1.9.30.js"></script>
<script type="text/javascript" src="/Scripts/jquery.tooltipster.min.js"></script> <!-- Tooltip -->
<script type="text/javascript" src="/Scripts/noty/js/packaged/jquery.noty.packaged.min.js"></script> <!-- Noty -->
<link href="/Scripts/noty/css/animate.css" rel="stylesheet"  type="text/css" media="all" />
<link href="/Scripts/noty/css/buttons.css" rel="stylesheet"  type="text/css" media="all" />

<script type="text/javascript" src="/Scripts/popover/jquery.webui-popover.min.js"></script> <!-- Webui Popover -->
<link href="/Scripts/popover/jquery.webui-popover.min.css" rel="stylesheet"  type="text/css" media="all" />
<script type="text/javascript" src="/Scripts/scrollbar/js/perfect-scrollbar.jquery.min.js"></script> <!-- Perfect scrollbar -->
<link href="/Scripts/scrollbar/css/perfect-scrollbar.min.css" rel="stylesheet"  type="text/css" media="all" />

<script type="text/javascript" src="/Scripts/dropdown/js/simple.dropdown.js"></script> <!-- Simple Dropdown -->
<link href="/Scripts/dropdown/css/simple.dropdown.css" rel="stylesheet"  type="text/css" media="all" />



<link href="/css/styles-im.css?v=1.1.047b" rel="stylesheet" type="text/css" media="all" />
<script src="https://ok.internetmedia.si/ad-files/runtime.js"></script>
    <script type="text/javascript">
    var ok_swiffy_isLoaded = 1; // variable used in ok.internetmedia.si to prevent multiple load of swiffy.js

    $(document).ready(function() {
    if (self == top) {
            document.documentElement.style.display = 'block';
    } else {
            //document.documentElement.style.display = 'none';
            $('body').html('<h1>Licenca iskalnika je potekla!</h1>').attr('style', 'background:none;');
            window.top.location.href = 'https://www.nepremicnine.net/'
    }

        $('.prot').bind('contextmenu', function(e) {
            return false;
        });
    });

    $(document).ready(function(){
        $("body").keypress(function(e){
            if (e.which == 110 ) {
                if ( !$("input, textarea, select").is(":focus") ) {
                    $("#hitroiskanje").focus();
                    var el = $("#hitroiskanje").get(0);
                    var elemLen = el.value.length;
                    el.selectionStart = elemLen;
                    el.selectionEnd = elemLen;
                    e.defaultPrevented();
                }
            }
        });
    });
        /* AS: search suggestion */
        $(function() {
            var cache = {},
                lastXhr;
            $( "#hitroiskanje" ).appendTo("#hitroiskanje").autocomplete({
                minLength: 0,
                source: function( request, response ) {
                    var term = request.term;

                    if ( term in cache ) {
                        response( cache[ term ] );
                        return;
                    }

                    lastXhr = $.getJSON( "/jq/facet-suggest.php", request, function( data, status, xhr ) {
                        cache[ term ] = data;

                        if ( xhr === lastXhr ) {
                            response( data );
                        }
                    });
                }
            });
        });

                $(document).ready(function(){
            $.ajax({
                url: "/jq/c.php",
                data: '' , //{ cookie : $.cookie('IP') }, // data to send to above script page if any
                async: false,
                cache: false,
                error: function(data){
                    //alert('ERR: ' + data);
                    $("#toperr").css("display", "block").append('<div class="msgE">Nimate omogoèenih piškotkov (cookies). Uporaba je omejena.</div>')
                },
                success: function(data){
                    if (data != '') {
                        //$("#nocookie div").removeClass('msgE').addClass('msgI');
                        //$("#nocookie div").replaceWith('<div class="msgI">Pozdravljeni na strani Nepremicnine.net.</div>')
                    } else {
                        $("#toperr").css("display", "block").append('<div class="msgE">Nimate omogoèenih piškotkov (cookies). Uporaba je omejena.</div>')
                    }

                }
            })
        });
        
        jQuery(function($) {
            $("a.fav").click(function(e){
                e.defaultPrevented(); // this will prevent the anchor tag from going the user off to the link
                var bookmarkUrl = this.href;
                var bookmarkTitle = 'Prodaja ';
                if (navigator.userAgent.toLowerCase().indexOf('chrome') > -1) {
                    alert("This function is not available in Google Chrome. Click the star symbol at the end of the address-bar or hit Ctrl-D (Command+D for Macs) to create a bookmark.");
                } else if (window.sidebar) { // For Mozilla Firefox Bookmark
                    window.sidebar.addPanel(bookmarkTitle, bookmarkUrl,"");
                } else if( window.external || document.all) { // For IE Favorite
                    window.external.AddFavorite( bookmarkUrl, bookmarkTitle);
                } else if(window.opera) { // For Opera Browsers
                    $("a.bookmark").attr("href",bookmarkUrl);
                    $("a.bookmark").attr("title",bookmarkTitle);
                    $("a.bookmark").attr("rel","sidebar");
                } else { // for other browsers which does not support
                    alert('Your browser does not support this bookmark action');
                    return false;
                }
            });
        });

//	$(document).ready(function(){
// example uses the selector "input" with the class "auto" & no options passed
//		jQuery(function($) {
//			$('input.numeric').autoNumeric();
//		});

        // example uses the selector "input" with the class "auto" & with options passed
        // See details below on allowed options
        jQuery(function($) {
            $('input.numeric').autoNumeric({aSep: '.', aDec: ','});
            $('input.intnum').autoNumeric('init', {aSep: '.', aDec: ',', mDec: 0, aForm:false});
            $('input.yearnum').autoNumeric({aSep: '', aDec: ',', mDec: 0, vMin: '0', vMax: '2017'});
        });

        $(document).ready (function () {
            $('.jq-confirm').click (function () {
                return confirm ($(this).attr ("title") + "?") ;
            }) ;
        }) ;
//	}) ;

    //slider zgoraj - moje nepremicnine
    jQuery(function($) {
        $(document).ready(function() {
            $("a.btn-slide").mouseover(function() {
                $("#top-panel").stop(true, true).slideDown("fast");
                $(this).addClass("active");
            });
            $("#moje-nep").mouseleave(function() {
                if ( !$('#moje-nep input[type=text]').is(":focus") ) {
                    $("#top-panel").delay(1000).slideUp("slow");
                    $(this).removeClass("active");
                }
            });
        });
        $(".flogin").bind("keyup change", function () {
          $(this).val(function(i, v) { return v.replace(/  /g," "); });
        });

        $(document).bind('click', function(e) {
            if( $(e.target).closest('#moje-nep').length === 0 ) {
                $("#top-panel").delay(1000).slideUp("slow");
            }
        });
    });

            $('<img src="/images/iskalnik.png"/>');

        jQuery(function($) {
            $(document).ready(function() {
                $("#fqrun").click(function() {
                    $("li.iskalnik").addClass("open");
                     $("#header").css('z-index', 500);
                    $(".iskalnik ul").stop(true, true).slideDown("fast");
                });
                $("li.iskalnik").mouseover(function() {
                     $("#header").css('z-index', 500);
                    $(".iskalnik ul").stop(true, true).slideDown("fast");
                    $(this).addClass("open");
                });
                $("li.iskalnik").mouseleave(function() {
                    if ($('.iskalnik input[type=text]').is(":focus")) {
                        $('input[type=text]').focus(function(){
                            $(this).css({'background-color' : '#FCC'});
                        });
                        $('input[type=text]').blur(function(){
                            $(this).css({'background-color' : '#fff'});
                        });
                    } else {
                        if( /Android|webOS|iPhone|iPad|iPod|BlackBerry/i.test(navigator.userAgent) == false ) {
                            $(".iskalnik ul").delay(500).slideUp("slow", function(){
                                 $("#header").css('z-index', 300);
                            });
                        }
                    }
                    $(".iskalnik select").mouseleave(function(event){
                        event.stopPropagation();
                    });
                    //$(this).removeClass("open");
                });

                $(document).bind('click', function(e) {
                    if( $(e.target).closest('li.iskalnik.open').length === 0 && $(e.target).closest('#moje-nep').length === 0 ) {
                        $("li.iskalnik.open ul").delay(500).slideUp("slow", function(){
                            $("#header").css('z-index', 300);
                        });
                        $("#top-panel").delay(1000).slideUp("slow");
                  }
                });

            });
        });
    
    function rSel (r) {
        $.post("/jq/r-sel.php", {id:r,rsel:'0'}, function(data) {
            $("select#NOr").html(data);
            $("select#NOr").removeAttr("disabled");
        }).done(function(){serialize_search();});
    }

    $(function(){
        $('input:radio[name=d]').change(function() {
            $("select#NOr").attr("disabled","disabled");
            $("select#NOr").html("<option>wait...</option>");

            var id = $("input:radio[name=d]:checked").val();

            $.post("/jq/r-sel.php", {id:id,rsel:'0'}, function(data) {
                $("select#NOr").html(data);
                $("select#NOr").removeAttr("disabled");
            }).done(function(){
                var select = $('#NOr>option');
                select[0].selected = true;
    			serialize_search();
            });
            //$('#NOr')[0].selectedIndex = 0;
            /*var select = $('#NOr>option');
            select[0].selected = true;
			serialize_search();*/
        });
    });

    $(function(){
        $('.uni.clr').click(function() {
            var clr = $(this).attr('data');
            var aClr = clr.split(',');

            for(i = 0; i< aClr.length; i++){
                $( aClr[i]).val('');
            }
        })
    });

    $(function(){
        $('#clr-cena').click(function() {
            $("#NOc1").val('');
            $("#NOc2").val('');
        })
    });

    jQuery(function($) {
        $(document).ready(function() {
            $("#NOreset").click(function() {
//			$('input:radio[value=197]').prop('checked', true);
                $("#NOp option:first").attr('selected','selected');
                $("#NOn option:first").attr('selected','selected');
                $("#NOr option:first").attr('selected','selected');
                $("#NOc1").val('');
                $("#NOc2").val('');
                $("#NOcm2 option:first").attr('selected','selected');
                $('input:radio[value=197]').trigger('click');
                //$.post('/NOpar.php', { name: 'value' });
              //$('#NOsearch').submit();
            });
        });
    });

    $(document).ready(function()
    {
        $("input:text").focus(function()
        {
            if ($(this).val() == $(this)[0].title)
            {
                $(this).removeClass("grey");
                $(this).val("");
            }
        });

        $("input:text").blur(function()
        {
            if ($(this).val() == "")
            {
                $(this).addClass("grey");
                $(this).val($(this)[0].title);
            }
        });

        $("input:text").blur();
    });

    $(document).ready(function(e){
        $(".form-kontakt").on("touchenter touchmove", function(){
            $("html, body").bind(function(e){
                e.defaultPrevented();
            });
        });
    });

    window.mobileAndTabletcheck = function() {
      var check = false;
      (function(a){if(/(android|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|mobile.+firefox|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows ce|xda|xiino|android|ipad|playbook|silk/i.test(a)||/1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-/i.test(a.substr(0,4)))check = true})(navigator.userAgent||navigator.vendor||window.opera);
      return check;
    }

    $(document).ready(function(e){
        $('.contact-tooltip').tooltipster({
            theme: 'tooltipster-shadow',
            contentAsHTML: true,
            position: 'left',
            interactive: true
        });

        if (mobileAndTabletcheck()){
            $('.contact-tooltip').click(function(){
                return false;
            });
        }
    });
</script>
<meta name="google-site-verification" content="fdN5cF2yYubJLN0QzkOj99U-Zw0Xqs0epcAH5U0uty0" />
<style>
	#cookieWarn {
		position:relative;
		z-index:1;
		background:#313131;
		min-height:50px;
		width:auto;
		padding: 0 10px;
		font-size:11px;
		text-align:center;
		border-bottom: 1px solid #888;
	}
	#cookieWarn .inner{
		width:auto;
		margin: 0 auto;
		color:#fff;
		padding:4px 0;
	}
	#cookieWarn .naslov {
		padding:4px 0;
		font-weight:bold;
	}
	#cookieWarn .fl {
		width:800px;
	}
	#cookieTermsagree {
    display: inline-block;
    color: #fff;
    text-decoration: none;
    background: #222;
    padding: 4px 10px;
		border: 1px solid rgb(85, 85, 85);
    border-radius: 3px 3px 3px 3px;
    box-shadow: 0px 0px 2px rgba(0, 0, 0, 0.25);
    text-shadow: 0px -1px 0px rgba(0, 0, 0, 0.35);
    transition: background 0.25s ease-in 0s;
		cursor:pointer;
}

</style>
<script>
jQuery(function() {
	
  $.fn.cookieChecker = function(options) {
    
    //maintain chainability
    return this.each(function() {
    
			// Create some defaults, extending them with any options that were provided
			var settings = $.extend( {
				'cookieName': 'cookieOK',
				'msgFile'   : '/ext/cookieOK.php',
				'duration'   : '3'
			}, options);
			
			var cName = settings.cookieName;
			var msgFile = settings.msgFile;
			var duration = Number(settings.duration);
			
			//check for the cookie
			function readCookie(name) {
				var nameEQ = name + "=";
				var ca = document.cookie.split(';');
					for(var i=0;i < ca.length;i++) {
						var c = ca[i];
						while (c.charAt(0)==' ') c = c.substring(1,c.length);
						if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
					}
				return null;
			}
		
		
		if (readCookie(cName) != null){
			//console.info('cookies present');
		} else {
//			$('#bar-top-wrapper').append($('<div id="cookieWarn"></div'));
			$('#toperr').prepend($('<div id="cookieWarn"></div'));
			$('#cookieWarn').load(msgFile, function(){
				$(this).slideDown();
				$('#cookieTermsagree').on('click', function(){
				// create one year duration cookie
				var theDate = new Date();
				var oneYearLater = new Date( theDate.getTime() + (31536000000 * duration));
				var expiryDate = oneYearLater.toGMTString();
				document.cookie = cName+'=1;expires='+expiryDate;
				$('#cookieWarn').slideUp('fast',function(){
					$('#cookieWarn').empty().remove();
				});
				});
			});		
		};
  
  // end chainability
  });
  
  // end cookieChecker
  }
  
  // end plugin
});

	$(document).ready(function(){
		$('body').cookieChecker();
	});
</script>
<script type="text/javascript">
window.middle_h_screen = (screen.width/2)-300;
window.middle_v_screen = (screen.height/2)-175;

function popupCenter(url, title, w, h) {
    // Fixes dual-screen position Most browsers Firefox
    var dualScreenLeft = window.screenLeft != undefined ? window.screenLeft : screen.left;
    var dualScreenTop = window.screenTop != undefined ? window.screenTop : screen.top;
    width = window.innerWidth ? window.innerWidth : document.documentElement.clientWidth ? document.documentElement.clientWidth : screen.width;
    height = window.innerHeight ? window.innerHeight : document.documentElement.clientHeight ? document.documentElement.clientHeight : screen.height;

    var left = ((width / 2) - (w / 2)) + dualScreenLeft;
    var top = ((height / 2) - (h / 2)) + dualScreenTop;
    var newWindow = window.open(url, title, 'scrollbars=yes, width=' + w + ', height=' + h + ', top=' + top + ', left=' + left);

    // Puts focus on the newWindow
    if (window.focus) {
    newWindow.focus();
    }
}

// generate notes
function generate(type, text, id) {

            var n = noty({
                text        : text,
                type        : type,
                dismissQueue: true,
                layout      : 'bottomLeft',
                closeWith   : ['button'],
                theme       : 'relax',
                maxVisible  : 5,
                animation   : {
                    open  : 'animated bounceInLeft',
                    close : 'animated bounceOutLeft',
                    easing: 'swing',
                    speed : 500
                },
                callback: {
                    onClose: function() {
                        $.ajax({ url: '/jq/set_noted.php?id=' + id });
                    }
                }
            });
            //console.log('html: ' + n.options.id);
        }

        function generateAll() {
            /*generate('warning', 'txt tukaj');
            generate('error', 'txt tukaj');
            generate('information', 'txt tukaj');
            generate('success', 'txt tukaj');*/
                        //generate('success');
        }

        $(document).ready(function () {

            setTimeout(function() {
                generateAll();
            }, 500);

            setInterval(function() {
                var exclude = '?';
                $( ".notification-identifier" ).each(function( index ) {
                    //console.log( index + ": " + $( this ).text() );
                    exclude += 'exclude[]=' + $( this ).text() + '&';
                });
                $.get( "/jq/check_notifications.php" + exclude, function( data ) {
                    $( "body" ).append( data );
                });
            }, 1000 * 60 * 1); // refresh every minute


            $('#notification-bell a').webuiPopover({title:'<i class="fa fa-bell"></i> &nbsp; Obvestila',content:'Content',width:250,height:200,placement:'bottom-left',type:'async',url:'/jq/popover_notifications.php',cache:false,closeable:true});
            $('#notification-message a').webuiPopover({title:'<i class="fa fa-envelope"></i> &nbsp; Sporoèila',content:'Content',width:250,height:200,placement:'bottom-left',type:'async',url:'/jq/popover_messages.php',cache:false,closeable:true});

            // messaging
            $(".inquiry-form").submit(function(event){
                event.preventDefault();
                event.stopPropagation();
                /*var id = $(".inquiry-form #ad_id").val();
                var conversation = $(".inquiry-form #conversation").val();
                var message = $(".inquiry-form textarea").val();*/
                var id = $(this).find("#ad_id").val();
                var owner = $(this).find("#owner").val();
                var conversation = $(this).find("#conversation").val();
                var message = $(this).find("textarea").val();
                if (id && message){
                    $.post( "/jq/message_send.php", { id: id, owner: owner, message: message, conversation: conversation }, function(data){
                        //console.log(data.answer);
                        if (data.answer == 'success')
                        {
                            //var last_message = $("#conversation-" + conversation + " .messages-list").find("li").last().attr("key");
                            var last_message = data.last_message;
                            //var new_message = last_message*1 + 1;
                            //$("#conversation-" + conversation + " .messages-list").append('<li class="me" key="' + last_message + '"><img src="' + data.image + '" /><h4>' + data.username + '<br /><small> poslano ' + data.time + '</small></h4>' + data.message + '</li>');
                            if ($("#conversation-" + conversation + " .messages-list li").length){
                                $("#conversation-" + conversation + " .messages-list li[key='" + (last_message*1 - 1) + "']").after('<li class="me" key="' + last_message + '"><img src="' + data.image + '" /><h4>' + data.username + '<br /><small> poslano ' + data.time + '</small></h4>' + data.message + '</li>');
                            } else {
                                $("#conversation-" + conversation + " .messages-list").append('<li class="me" key="' + last_message + '"><img src="' + data.image + '" /><h4>' + data.username + '<br /><small> poslano ' + data.time + '</small></h4>' + data.message + '</li>');
                            }
                            $(".inquiry-form textarea").val('');
                            $("#conversation-" + conversation + " .messages-list").perfectScrollbar('update');
                            $("#conversation-" + conversation + " .messages-list").animate({ scrollTop: $("#conversation-" + conversation + " .messages-list")[0].scrollHeight}, 1000);
                        }
                    } );
                }
                //event.preventDefault();
            });

            // check for messages
            
            // initialise scrollbar
            if ($(".messages-list").length){
                $(".messages-list").perfectScrollbar();
                $('.messages-list').scrollTop($('.messages-list')[0].scrollHeight); // scroll to the bottom
            }

            if ($(".sender-info").length){
                $(".sender-info").each(function(index){
                    var conversation_id = $(this).attr("conversation");
                    var ad_id = $(this).attr("ad_id");
                    var owner = $("#conversation-" + conversation_id + " #owner").val();
                    $(this).click(function(){
                        $(".conversation-container").not("#conversation-" + conversation_id).slideUp("fast");
                        $(".conversation-ad-info").not("#conversation-info-" + conversation_id).slideUp("fast");
                        $("#conversation-" + conversation_id).slideDown("fast", function(){
                            $("#conversation-" + conversation_id + " .messages-list").scrollTop($("#conversation-" + conversation_id + " .messages-list")[0].scrollHeight); // scroll to the bottom
                        });
                        $("#conversation-info-" + conversation_id).slideDown("fast");
                        $(this).removeClass("unread");
                        $(this).parent().removeClass("unread");
                        $.post( "/jq/message_update.php", { id: ad_id, owner: owner, conversation: conversation_id, update_change: 'read' }, function(data){
                            //console.log(data.answer);
                            if (data.answer == 'success')
                            {
                                if (data.message_count)
                                {
                                    if ($("#notification-message a").find('span').length)
                                    {
                                        $("#notification-message a").find('span').text(data.message_count);
                                    } else {
                                        $("#notification-message a").append('<span>' + data.message_count + '</span>');
                                    }
                                    $("#notification-message a").addClass('active');

                                    $(".html-msg-count").text('(' + data.message_count + ')');
                                } else {
                                    $("#notification-message a").find('span').remove();
                                    $("#notification-message a").removeClass('active');

                                    $(".html-msg-count").text('');
                                }
                            }
                        } );
                    });
                });
            }

            // get message hash values
            var hash_value = window.location.hash.substr(1);
            if (hash_value){
                //alert(hash_value);
                if (hash_value.indexOf(":") > -1)
                {
                    var split_value = hash_value.split(":")
                    var action_value = split_value[0];
                    var m_value = split_value[1];
                } else {
                    var action_value = hash_value;
                    var m_value = 0;
                }


                window.messages_updated = false;

                if (action_value == 'scroll_messages' && !m_value){
                    $('html, body').animate({
                        scrollTop: $("#get-info").offset().top
                    }, 1000, 'swing', function(){
                        if (!window.messages_updated)
                        {
                            window.messages_updated = true;
                            var ad_id = $("#ad_id").val();
                            var owner = $("#owner").val();
                            var conversation_id = $("#conversation").val();

                            $.post( "/jq/message_update.php", { id: ad_id, owner: owner, conversation: conversation_id, update_change: 'read' }, function(data){
                                //console.log(data.answer);
                                if (data.answer == 'success')
                                {
                                    //alert('yay');

                                    if (data.message_count)
                                    {
                                        if ($("#notification-message a").find('span').length)
                                        {
                                            $("#notification-message a").find('span').text(data.message_count);
                                        } else {
                                            $("#notification-message a").append('<span>' + data.message_count + '</span>');
                                        }
                                        $("#notification-message a").addClass('active');

                                        $(".html-msg-count").text('(' + data.message_count + ')');
                                    } else {
                                        $("#notification-message a").find('span').remove();
                                        $("#notification-message a").removeClass('active');

                                        $(".html-msg-count").text('');
                                    }
                                }

                            } );
                        }
                    });
                }

                if (action_value == 'scroll_messages' && m_value){
                    var conversation_id = m_value;
                    $('html, body').animate({
                        //scrollTop: $("#get-info").offset().top
                        scrollTop: $("#sender-conversation-" + m_value).offset().top
                    }, 1000, 'swing', function(){
                        $(".conversation-container").not("#conversation-" + conversation_id).slideUp("fast");
                        $(".conversation-ad-info").not("#conversation-info-" + conversation_id).slideUp("fast");
                        $("#conversation-" + conversation_id).slideDown("fast", function(){
                            $("#conversation-" + conversation_id + " .messages-list").scrollTop($("#conversation-" + conversation_id + " .messages-list")[0].scrollHeight); // scroll to the bottom
                            $("#sender-conversation-" + conversation_id).removeClass("unread");
                            $("#sender-conversation-" + conversation_id).parent().removeClass("unread");
                            var ad_id = $("#sender-conversation-" + conversation_id).attr('ad_id');
                            var owner = $("#conversation-" + conversation_id + " #owner").val();

                            if (!window.messages_updated)
                            {
                                window.messages_updated = true;
                                $.post( "/jq/message_update.php", { id: ad_id, owner: owner, conversation: conversation_id, update_change: 'read' }, function(data){
                                    //console.log(data.answer);
                                    if (data.answer == 'success')
                                    {
                                        //alert('yay');
                                        if (data.message_count)
                                        {
                                            if ($("#notification-message a").find('span').length)
                                            {
                                                $("#notification-message a").find('span').text(data.message_count);
                                            } else {
                                                $("#notification-message a").append('<span>' + data.message_count + '</span>');
                                            }
                                            $("#notification-message a").addClass('active');

                                            $(".html-msg-count").text('(' + data.message_count + ')');
                                        } else {
                                            $("#notification-message a").find('span').remove();
                                            $("#notification-message a").removeClass('active');

                                            $(".html-msg-count").text('');
                                        }
                                    }

                                } );
                            }
                        });
                        $("#conversation-info-" + conversation_id).slideDown("fast");
                    });
                }
            }
        });

        function update_read(element){
            var ad_id = $(element).parent().find("#ad_id").val();
            var owner = $(element).parent().find("#owner").val();
            var conversation_id = $(element).parent().find("#conversation").val();
            $.post( "/jq/message_update.php", { id: ad_id, owner: owner, conversation: conversation_id, update_change: 'read' }, function(data){
                //console.log(data.answer);
                if (data.answer == 'success')
                {
                    if (data.message_count)
                    {
                        if ($("#notification-message a").find('span').length)
                        {
                            $("#notification-message a").find('span').text(data.message_count);
                        } else {
                            $("#notification-message a").append('<span>' + data.message_count + '</span>');
                        }
                        $("#notification-message a").addClass('active');

                        $(".html-msg-count").text('(' + data.message_count + ')');
                    } else {
                        $("#notification-message a").find('span').remove();
                        $("#notification-message a").removeClass('active');

                        $(".html-msg-count").text('');
                    }
                }
            } );
        }

        function txt_auto_grow(element) {
            element.style.height = "5px";
            element.style.height = (element.scrollHeight)+"px";
        }

            var $dropdown = $('div.dropdownWrapper'),
              $drpBtn   = $dropdown.find('div.dropdownLabel');

          /*$drpBtn.on('click', function(e){
            e.stopPropagation();
            var $element = $(this).parent();
            $element.find('.dropdownPanel').fadeToggle(200);
        });*/

          /*$("body").click(function(){
            $('.dropdownPanel').hide(200);
        });*/

        // search form
        $( document ).ready(function() {
            $("#NOsearch input").keyup(function(){
                serialize_search();
            });
            $("#NOsearch input[type='radio'], #NOsearch select").change(function(){
                serialize_search();
            });
        });

        function serialize_search()
        {
            var s_data = $("#NOsearch").serialize();
            $.post( "/jq/search.php?wpg=nepremicnine&" + s_data, function( data ) {
              //$( ".result" ).html( data );
              $("#NOsearch a.gumb.potrdi").attr('href', data);
            });
        }

</script>

<script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-15972954-1']);
  _gaq.push(['_setDomainName', 'nepremicnine.net']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'https://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>
</head>
<body class="sl  -2" id="nepremicnine">
    <div id="fb-root"></div>
<script>
//$(window).load(
(function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return;
  js = d.createElement(s); js.id = id;
  js.src = "//connect.facebook.net/sl_SI/sdk.js#xfbml=1&version=v2.6&appId=218433478210947";
  fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));
//);
</script>

    <div id="bar-top-wrapper">
        <div id="bar-top">
            <!--<ul id="bar-top-right">
                <li><a class="fav" href="#" title="Dodaj v Priljubljene"></a></li>
                <li><a class="kontakt" href="/nepremicnine-oglasevanje.html" title="Kontakt"></a></li>
                                <li><a class="lang en" href="http://www.realestate-slovenia.info/"></a></li>-->
                <!--
                                <li><a class="lang hr" href="/?lang=hr"></a></li>
                                <li><a class="lang de" href="/?lang=de"></a></li>
                                <li><a class="lang it" href="/?lang=it"></a></li>
                -->
                <!--            </ul>-->

            
            
            <ul id="bar-top-right">
                <li id="notification-bell">
                    <a href="#" >
                        <i class="fa fa-bell"></i>
                                            </a>
                </li>
                <li id="notification-message">
                    <a href="#" >
                        <i class="fa fa-envelope"></i>
                                            </a>
                </li>
            </ul>
            <ul>
                <li class="first"><a href="http://www.slonep.net" target="_blank">slonep.net</a></li>
                <li><a href="http://www.montazne-hise.net" target="_blank">montažne hiše</a></li>
                <li><a href="http://www.podsvojostreho.net" target="_blank">pod<span class="svojo">svojo</span>streho.net</a></li>
                <li><a href="http://www.novogradnje.si" target="_blank">novogradnje.si</a></li>
                <!--<li><a href="http://www.nepremicninar.com" target="_blank">nepremicninar.com</a></li>-->
                                                <li><a class="lang" href="http://www.realestate-slovenia.info/">
                                        <img src="/images/vector-flags/gb.svg" style="height: 18px;">
                                    </a></li>
                                <li><!--<a class="last" href="http://www.facebook.com/pages/NEPREMICNINEnet/181757358510072" target="_blank" title="NEPREMICNINE.net na Facebook-u"><img src="/images/ikona-fb.png" alt="Nepremicnine.net FB" /></a>-->
                    <div class="fb-like" data-href="https://www.facebook.com/NEPREMICNINEnet-181757358510072/" data-colorscheme="light" data-layout="button_count" data-action="like" data-show-faces="false" data-share="false"></div>
                </li>
                <!--<li><a href="/profil.html?m=so&s=37" class="blink last">SPOROÈILO</a></li>-->
            </ul>
            <div id="moje-nep">
                
            <div id="top-panel" class="panel inact">
                <div><strong>Niste prijavljeni.</strong></div>
                    <div class="clearer"></div>
                    <div class="items">
        
                <!--<a href="/profil.html?set=ins" class="pf i-adduser">Nov uporabnik</a>-->
                <a href="/nepremicnine-vpis.html?v=1" class="pf i-addad">Vpis oglasa</a>
                <div class="clearer"></div>
            
                    <form method="post" action="/profil.html">
                        <label for="user">Upor. ime:</label><input name="user" type="text" value="" maxlength="50" class="flogin" style="width: 180px;" /><br />
                        <label for="pswd">Geslo:</label><input name="pswd" type="password" value="" maxlength="50" class="flogin" style="width: 180px;" /><br />
                        <div class="spacer"></div>
                        <input name="go" type="submit" value="Prijavi" class="gumb potrdi" />
                        <a href="/profil.html?set=ins" class="pf i-adduser" style="float:left; width: auto;">Nov uporabnik</a>
                        <a href="/profil.html?prijava=1&geslo=2" class="bl fr" style="float:left; width: auto; margin-left: 22px;">Pozabljeno geslo</a>

                        <div class="spacer clearer"></div>
                        <div>
                            <a class="social-login facebook" onclick="popupCenter('/SocialLogin/?platform=Facebook', 'Facebook', 500, 400)"><i class="fa fa-facebook"></i> Prijava preko Facebooka</a>
                    <a class="social-login google" onclick="popupCenter('/SocialLogin/?platform=Google', 'Google', 600, 570)"><i class="fa fa-google"></i>Prijava preko Googla</a>
                            <div class="clearer"></div>
                        </div>
                        <div class="spacer"></div>
                    </form>
                    <div class="clearer"></div>
                	<a href="/profil.html?m=so" class="pf i-so">Shranjeni oglasi</a>
                        <a href="/profil.html?m=si" class="pf i-si">Shranjena iskanja</a>
                        <div class="clearer"></div>
                    </div>
            </div>
        <p class="slide"><a href="/profil.html" name="moje-nep" class="btn-slide">Moje nepremiènine</a></p>            </div>
        </div>
    </div>
    <div id="ad-bg"><style>
#ad-bg div{
	position:fixed;
	top:-10px;
	height:100%;
	width:100%;
	margin:auto;
}
#ad-bg a {
	display:block;
	position:fixed;
	height:100%;
	width:100%;
	left:0;
	top:23px;
	z-index:0;
}
</style>

<script type='text/javascript'><!--//<![CDATA[
   var m3_u = (location.protocol=='https:'?'https://ok.internetmedia.si/www/delivery/ajs.php':'https://ok.internetmedia.si/www/delivery/ajs.php');
   var m3_r = Math.floor(Math.random()*99999999999);
   if (!document.MAX_used) document.MAX_used = ',';
   document.write ("<scr"+"ipt type='text/javascript' src='"+m3_u);
   document.write ("?zoneid=30&amp;target=_blank&amp;withtext=1");
   document.write ('&amp;cb=' + m3_r);
   if (document.MAX_used != ',') document.write ("&amp;exclude=" + document.MAX_used);
   document.write (document.charset ? '&amp;charset='+document.charset : (document.characterSet ? '&amp;charset='+document.characterSet : ''));
   document.write ("&amp;loc=" + escape(window.location));
   if (document.referrer) document.write ("&amp;referer=" + escape(document.referrer));
   if (document.context) document.write ("&context=" + escape(document.context));
   if (document.mmm_fo) document.write ("&amp;mmm_fo=1");
   document.write ("'><\/scr"+"ipt>");
//]]>--></script>

<script>
$('#ad-bg a').css('background','url('+$('#ad-bg a img').attr('src')+') top no-repeat');
$('#ad-bg a img').remove();
</script>

<script>

(function($){
	$.fn.extend({
		fixcenter: function () {
			return this.each(function() {
				var left = (  ( $(window).width() - $(this).outerWidth() ) / 2  );
				//alert($(window).width() + ' - ' + $(this).outerWidth() + ' : ' + left);
				$('#k17').append(' | ' + $(window).width() + ' - ' + $(this).outerWidth() + ' : ' + left);
				$(this).css({position:'fixed', left: (left < 0 ? left : 0)+'px'});
			});
		}
	}); 
})(jQuery);

$('#ad-bg div:first').fixcenter();
$(document).ready(function(){
	$('#ad-bg div:first').fixcenter();
	$(window).resize(function(){
		$('#ad-bg div:first').fixcenter();
	});
});
</script>
</div>
    <div id="all">
    <div id="toperr"></div>
    <div id="wrapper">
        <script src="/Scripts/swfobject_modified.js" type="text/javascript"></script>
        <div id="ad-top-wrapper"><div id="ad-top">
<iframe id='a4e1c538' name='a4e1c538' src='https://ok.internetmedia.si/www/delivery/afr.php?zoneid=1&amp;target=_blank&amp;charset=UTF-8&amp;cb=488536049&amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5=' frameborder='0' scrolling='no' width='960' height='150'><a href='https://ok.internetmedia.si/www/delivery/ck.php?n=a0fcbf0c&amp;cb=953810028&amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5=' target='_blank'><img src='https://ok.internetmedia.si/www/delivery/avw.php?zoneid=1&amp;charset=UTF-8&amp;cb=387671497&amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5=&amp;n=a0fcbf0c' border='0' alt='' /></a></iframe>
            </div></div>
        <div class="clearer"></div>

        <div id="content">
                        <div id="header-top">
                                <div id="logo">
                    <a href="/"><img src="/images/logo.gif" width="297" height="37" title="Nepremiènine, središèe ponudbe nepremiènin v Sloveniji, agencije za nepremiènine, novogradnje..." alt="Nepremiènine, središèe ponudbe nepremiènin v Sloveniji, agencije za posredovanje nepremiènin, novogradnje..." />
                    <strong>Najveèji slovenski nepremièninski portal</strong></a>
                </div>
                <div id="slogan"></div>
                <div id="iskalnik-hitroiskanje" class="ui-widget">
                                        <form action="/nepremicnine.html" method="get" name="searcher" accept-charset="utf-8">
                        <input type="text" name="q" id="hitroiskanje" value="" title="npr. hiša bled atrij, ref. št. oglasa ..." size="30" maxlength="160" onclick="if (searcher.q.value.substring(0,3) == 'npr') searcher.q.value='';" />
                        <input type="submit" id="hitroiskanjepotrdi" value="" width="31" height="32" onclick="if ( searcher.q.value=='npr. hiša bled atrij, ref. št. oglasa ...' ) return false;" />
                    </form>
                </div>
            </div>
            <div id="header">
                <div id="menu">
                    <ul>
                        <li class="first"><a href="/">nepremiènine</a></li>
                                                <li class="iskalnik">
                            <div class="menuitem"><a href="#" id="fqrun" class="active">ISKALNIK</a></div>
                            <ul>
	<li>
		<div class="levo">
						<form name="NOsearch" id="NOsearch" action="/nepremicnine.html" class="" method="get">
				<div id="loading">Loading ...</div>
				<table width="350" border="0" cellpadding="3" cellspacing="0">
					<tr>
						<td class="td-levo"><strong>Država</strong></td>
						<td class="td-desno">
							<input type="radio" class="radio" id="NOd197" name="d" value="197" checked="checked">
							<label for="NOd197" class="radio">Slovenija</label>
							<input type="radio" class="radio" id="NOd55" name="d" value="55" >
							<label for="NOd55" class="radio">Hrvaška</label>
							<input type="radio" class="radio" id="NOd999" name="d" value="999" >
							<label for="NOd999" class="radio">Druge</label>
							</td>
					</tr>

					<tr>
						<td class="td-levo"><strong>Posredovanje</strong></td>
						<td class="td-desno">
							
							<select name="p" id="NOp">
								<option value="1" selected="selected">Prodaja</option><option value="2">Nakup</option><option value="3">Oddaja</option><option value="4">Najem</option>							</select>
						</td>
					</tr>

					<tr>
						<td class="td-levo"><strong>Nepremiènina</strong></td>
						<td class="td-desno">
														<select name="n" id="NOn">
								<option value="1">Stanovanje</option><option value="2">Hiša</option><option value="4">Vikend</option><option value="3">Posest</option><option value="5">Poslovni prostor</option><option value="6">Garaža</option><option value="7">Poèitniški objekt</option>								</select>
						</td>
					</tr>

					<tr>
						<td class="td-levo"><strong>Regija</strong></td>
						<td class="td-desno">
							
							<select name="r" id="NOr">
															</select>
						</td>
					</tr>


			<script>
				//alert( $("#NOr option:selected").text() );
				$(document).ready(function(e) {
					//if ( $("input:radio[name=d]:checked").val() != 197 ) {
						rSel( $("input:radio[name=d]:checked").val() );
					//}
				});
			</script>
							<tr>
						<td class="td-levo">
							<strong>Cena</strong>:
							<div id="clr-cena" class="icon clr fr" title="Ostrani omejitev po ceni"></div>
						</td>
						<td class="td-desno">
														<input name="c1" type="text" class="intnum mini" id="NOc1" size="7" value="" /><span class="minus">-</span><input name="c2" type="text" class="intnum mini" id="NOc2" size="7" value="200000" />
							<select name="cm2" id="NOcm2" class="cm2 mini">
								<option value="0">&euro;</option>
								<option value="1">&euro;/m2</option>
							</select>
						</td>
					</tr>
			<!--						<tr>
						<td class="td-levo"><strong>Velikost</strong>:</td>
						<td class="td-desno">
														<input name="m1" type="text" id="m1" size="7" value="" /><span class="minus">-</span><input name="m2" type="text" id="m2" size="7" value="" />
							<span class="minus">m<span class="m2">2</span></span>
						</td>
					</tr>
			-->
					<tr>
						<td>
							<a href="/nepremicnine.html" id="isk-map" class="fl div-ricon bl fmap rdeca" style="margin-left:7px;">Podrobno<br />iskanje</a>						</td>
						<td class="td-desno">
							<input type="button" id="NOreset" class="gumb ponastavi" value="Ponastavi">
							<!--<input type="submit" id="NOsubmit" class="gumb potrdi" value="Prikaži rezultate" />-->
							<a  class="gumb potrdi" href="/oglasi-prodaja/ljubljana-mesto/stanovanje/">Prikaži rezultate</a>
						</td>
					</tr>
				</table>
			</form>
		</div>
		<ul class="desno">
			<li><a href="/ne-spreglejte.html" class="isk-nespreglejte">ne spreglejte</a></li>
			<li><a href="/24ur.html" class="isk-v24ur">24 ur</a></li>
			<li><a href="/znizane-cene.html" class="isk-znizano">znižane cene</a></li>
					<li><a href="/nepremicnine-vpis.html?v=1" class="isk-vpis">vpis oglasa</a></li>
			<li><a href="/infonep.html" class="isk-obv">obvešèajte me</a></li>
					<li><a href="/profil.html?m=si" class="isk-si">shranjena iskanja</a></li>
			<li><a href="/profil.html?m=so" class="isk-so">shranjeni oglasi</a></li>
			<li><a href="/javne-drazbe.html" class="isk-jd">javne dražbe</a></li>
			<li><a href="/za-studente.html" class="isk-stu">za študente</a></li>
		</ul>
	</li>
</ul>
                        </li>
                        <li class="nav-novogradnje"><a href="/novogradnje.html">Novogradnje</a></li><li class="nav-javne-drazbe"><a href="/javne-drazbe.html">Javne dražbe</a></li><li class="nav-montazne-hise"><a href="/montazne-hise.html">Montažne hiše</a></li><li class="nav-pocitniski-objekti"><a href="/pocitniski-objekti.html">Na poèitnice!</a></li><li class="nav-dom-in-gradnja"><a href="/dom-in-gradnja.html">Dom in gradnja</a></li><li class="nav-nepremicninske-agencije"><a href="/nepremicninske-agencije.html">Podjetja</a></li><li class="nav-energetska-izkaznica"><a href="/energetska-izkaznica.html">E. izkaznica</a></li><li class="nav-trendi"><a href="/trendi.html">Trendi</a></li>                    </ul>
                    <div class="clearer"></div>
                </div>
                <div class="clearer"></div>
                            </div>
            <!-- vsebina -->
            <div class="clearer"></div>
            <div id="vsebina980">
                <!-- 980 -->
                
<script type="text/javascript">
    jQuery(function($) {
        $( '#facetUE' ).on( 'click', 'input:checkbox', function () {
             $( this ).parent().toggleClass( 'act', this.checked );
             $('#sform').submit();
        });
    });
</script>

    <script type="text/javascript">
        jQuery(function($) {
            $('#si').click( function () {
                $.ajax({
                    type: "POST",
                    url: "/jq/si.php",
                    //data: "wpg=nepremicnine&p=1&arg[]=ljubljana-mesto&arg[]=stanovanje&arg[]=cena-do-200000-eur&pg=20&s=13&uid=", // data to send to above script page if any
                    data: "wpg=nepremicnine&p=1&arg%5B0%5D=ljubljana-mesto&arg%5B1%5D=stanovanje&arg%5B2%5D=cena-do-200000-eur&pg=20&s=13&c2=200000&uid=", // data to send to above script page if any
                    async: true,
                    cache: false,
                    error: function(response)
                    {
                        alert(response);
                        $('#si').css("background-color","red");
                    },
                    success: function(data){
                        $('#si').removeAttr("href");
                        $('#si').replaceWith($('<span id="si" class="ibl fr">' + $('#si').html() + '</span>'));
                        if(data == 'true') {
                            $('#si').removeClass("pf");
                            $('#si').html("Parametri so shranjeni.").addClass("msgI");
                            //$("#si").delay(8000).hide();
                        } else {
                            $('#si').removeClass("pf");
                            $('#si').html(data);
                            //$('#si').html(data).addClass("msgW");
                        }
                    }
                })
                setTimeout(function() { $('#si').remove().hide('slow'); }, 4000);
                //$(this).delay(4000).hide('slow');
                //.done(function() { alert("success"); })
                //.fail(function() { alert("error"); })
            });
        });

        $(document).ready(function() {
            $('.ikona-sh').click( function () {
                savethis = $(this);
                $.ajax({
                    type: "POST",
                    url: "/jq/so.php",
                    data: {id:$(this).attr('data-id')},
                    async: true,
                    cache: false,
                    error: function(response)
                    {
                        alert(response);
                    },
                    success: function(data){
                        if(data == 'true') {
                            savethis.addClass('ikona-ok').delay(4000).hide('slow');
                        } else {
                            alert(data);
                        }
                    }
                })
            });

            $('.ikona-sh2').click( function () {
                savethis = $(this);
                $.ajax({
                    type: "POST",
                    url: "/jq/so.php",
                    data: {id:$(this).attr('data-id')},
                    async: true,
                    cache: false,
                    error: function(response)
                    {
                        alert(response);
                    },
                    success: function(data){
                        if(data == 'true') {
                            //savethis.addClass('ikona-ok').delay(4000).hide('slow');
                            savethis.delay(150).fadeOut('slow');
                        } else {
                            alert(data);
                        }
                    }
                })
            });
        });

        function save_ad(data_id){
            $.ajax({
                type: "POST",
                url: "/jq/so.php",
                data: {id:data_id},
                async: true,
                cache: false,
                error: function(response)
                {
                    alert(response);
                },
                success: function(data){
                    if(data == 'true') {
                        //savethis.addClass('ikona-ok').delay(4000).hide('slow');
                        $("#save-ad-" + data_id).delay(150).fadeOut('slow');
                    } else {
                        alert(data);
                    }
                }
            });
        }
    </script>
    <div id="vsebina200"><div class="facet">
<script type="text/javascript">
    jQuery(function($) {
        $(document).ready(function() {
            $(".facet .more").mouseover(function() {
                $(this).addClass("open");
            });
            $(".facet .more").mouseleave(function() {
                if ( $(this).find('input[type=text]').is(":focus") ) {
                    if( /Android|webOS|iPhone|iPad|iPod|BlackBerry/i.test(navigator.userAgent) == false ) {
                        $(".facet .more").not(this).removeClass("open");
                    }
                } else {
                    if( /Android|webOS|iPhone|iPad|iPod|BlackBerry/i.test(navigator.userAgent) == false ) {
                        $(".facet .more").removeClass("open");
                    }
                }
            });
            $(".facet select").mouseleave(function(event){
                event.stopPropagation();
            });
        });
    });
</script>


            <div class="params">
                <strong class="fftitle">Parametri iskanja:</strong>
                <div><br /><a href="/oglasi/cena-do-200000-eur/?s=13" class="icon clr"></a>Posredovanje: <strong>Prodaja</strong><br /><a href="/oglasi-prodaja/?s=13" class="icon clr"></a>Cena: <strong> do 200.000 &euro;</strong><br /></div>
                <a href="/nepremicnine.html" class="icon clr ur" style="margin:7px;"></a>
                <div class="clearer"></div>
            </div>
        Št. ustreznih oglasov: <strong>19532</strong><br />    <!--<form action="/nepremicnine.html" method="get" id="sform" name="sform" accept-charset="utf-8">-->
        <form action="/jq/search.php?wpg=nepremicnine&red=1" method="post" id="sform" name="sform" accept-charset="utf-8">
        
                    <a name=""></a><h3>+ Kljuène besede</h3>
                    <input type="text" name="q" id="q" class="mini" style="width:185px; float: left;" value="" size="30" maxlength="60">
                    <input type="submit" class="fsearch" value=">" /><br />
                <a name=""></a><h3>Osnovni parametri</h3><select name="d" id="dd" class="invisible" onchange="sform.submit()"><option value="0">Vse države</option><option value="197">Slovenija</option><option value="55">Hrvaška</option><option value="999">Ostale</option></select><div class="dropdownWrapper">
                          <div class="dropdownLabel">Vse države<i class="fa fa-caret-down" aria-hidden="true"></i></div>
                          <div class="dropdownPanel">
                            <a href="/oglasi-prodaja/cena-do-200000-eur/?s=13">Vse države</a><a href="/oglasi-prodaja/slovenija/cena-do-200000-eur/?s=13">Slovenija</a><a href="/oglasi-prodaja/hrvaska/cena-do-200000-eur/?s=13">Hrvaška</a><a href="/oglasi-prodaja/ostale-drzave/cena-do-200000-eur/?s=13">Ostale</a>
                          </div>
                        </div>
        <select name="n" id="n" class="invisible" onchange="sform.submit()"><option value="0">Vse nepremiènine</option><option value="1">Stanovanje</option><option value="2">Hiša</option><option value="4">Vikend</option><option value="3">Posest</option><option value="5">Poslovni prostor</option><option value="6">Garaža</option><option value="7">Poèitniški objekt</option></select><div class="dropdownWrapper">
                          <div class="dropdownLabel">Vse nepremiènine<i class="fa fa-caret-down" aria-hidden="true"></i></div>
                          <div class="dropdownPanel">
                            <a href="/oglasi-prodaja/cena-do-200000-eur/?s=13">Vse nepremiènine</a><a href="/oglasi-prodaja/stanovanje/cena-do-200000-eur/?s=13">Stanovanje</a><a href="/oglasi-prodaja/hisa/cena-do-200000-eur/?s=13">Hiša</a><a href="/oglasi-prodaja/vikend/cena-do-200000-eur/?s=13">Vikend</a><a href="/oglasi-prodaja/posest/cena-do-200000-eur/?s=13">Posest</a><a href="/oglasi-prodaja/poslovni-prostor/cena-do-200000-eur/?s=13">Poslovni prostor</a><a href="/oglasi-prodaja/garaza/cena-do-200000-eur/?s=13">Garaža</a><a href="/oglasi-prodaja/pocitniski-objekt/cena-do-200000-eur/?s=13">Poèitniški objekt</a>
                          </div>
                        </div>
        
        
        <input type="hidden" name="p" value="1" /><a name="Cena"></a><h3>Cena (&euro;)</h3><ul id="facetCena"><li><a href="/oglasi-prodaja/cena-do-50000-eur/?s=13"><div class="cnt">[5075]</div><span class="fnum">do </span>&nbsp;<span class="fnum">50.000</span></a></li><li><a href="/oglasi-prodaja/cena-od-50000-do-100000-eur/?s=13"><div class="cnt">[6981]</div><span class="fnum">50.000</span>&nbsp;<span class="fnum">-&nbsp;100.000</span></a></li><li><a href="/oglasi-prodaja/cena-od-100000-do-150000-eur/?s=13"><div class="cnt">[4806]</div><span class="fnum">100.000</span>&nbsp;<span class="fnum">-&nbsp;150.000</span></a></li><li><a href="/oglasi-prodaja/cena-od-150000-do-200000-eur/?s=13"><div class="cnt">[3268]</div><span class="fnum">150.000</span>&nbsp;<span class="fnum">-&nbsp;200.000</span></a></li> <a href="/oglasi-prodaja/?s=13" class="icon clr ur" title="Izbris omejitve po ceni"></a></ul>
                    <div class="more">
                        <div>vnesite poljubno vrednost</div>
                        <input type="text" class="mini intnum" size="10" maxlength="10" name="c1" value="">
                        -
                        <input type="text" class="mini intnum" size="10" maxlength="10" name="c2" value="200000">
                        <select name="cm2" class="cm2">
                            <option value="0">&euro;</option>
                            <option value="1">&euro;/m2</option>
                        </select>
                        <input type="submit" class="fsearch" value=">" /><br />
                    </div>
                <a name="M2"></a><h3>Velikost (m2)</h3><ul id="facetM2"><li><a href="/oglasi-prodaja/cena-do-200000-eur,velikost-do-2000-m2/?s=13"><div class="cnt">[17928]</div><span class="fnum">do </span>&nbsp;<span class="fnum">2.000</span></a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur,velikost-od-2000-do-4000-m2/?s=13"><div class="cnt">[761]</div><span class="fnum">2.000</span>&nbsp;<span class="fnum">-&nbsp;4.000</span></a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur,velikost-od-4000-do-6000-m2/?s=13"><div class="cnt">[251]</div><span class="fnum">4.000</span>&nbsp;<span class="fnum">-&nbsp;6.000</span></a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur,velikost-od-6000-do-8000-m2/?s=13"><div class="cnt">[131]</div><span class="fnum">6.000</span>&nbsp;<span class="fnum">-&nbsp;8.000</span></a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur,velikost-od-8000-do-10000-m2/?s=13"><div class="cnt">[95]</div><span class="fnum">8.000</span>&nbsp;<span class="fnum">-&nbsp;10.000</span></a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur,velikost-od-10000-m2/?s=13"><div class="cnt">[429]</div><span class="fnum">10.000</span>&nbsp; in veè</a></li></ul>
                    <div class="more">
                        <div>vnesite poljubno vrednost</div>
                        <input type="text" class="mini intnum" size="10" maxlength="10" name="m1" onchange="CheckCurrency(document.sform.m1,'m1')" value="">
                        -
                        <input type="text" class="mini intnum" size="10" maxlength="10" name="m2" onchange="CheckCurrency(document.sform.m2,'m2')" value="">
                        m2
                        <input type="submit" class="fsearch" value=">" />
                    </div>
                <a name="leto"></a><h3>Leto</h3><ul><li><a href="/oglasi-prodaja/cena-do-200000-eur,letnik-do-1949/?s=13"><div class="cnt">[7782]</div>do  - 1949</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur,letnik-od-1950-do-1959/?s=13"><div class="cnt">[579]</div>1950 - 1959</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur,letnik-od-1960-do-1969/?s=13"><div class="cnt">[1211]</div>1960 - 1969</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur,letnik-od-1970-do-1979/?s=13"><div class="cnt">[1436]</div>1970 - 1979</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur,letnik-od-1980-do-1989/?s=13"><div class="cnt">[1834]</div>1980 - 1989</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur,letnik-od-1990-do-1999/?s=13"><div class="cnt">[1416]</div>1990 - 1999</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur,letnik-od-2000-do-2009/?s=13"><div class="cnt">[2873]</div>2000 - 2009</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur,letnik-od-2010-do-2014/?s=13"><div class="cnt">[1649]</div>2010 - 2014</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur,letnik-od-2015/?s=13"><div class="cnt">[752]</div>2015 in veè</a></li></ul>
                        <div class="more">
                        <div>vnesite poljubno vrednost</div>
                            <input type="text" class="mini" size="10" maxlength="4" name="l1" value="">
                            -
                            <input type="text" class="mini" size="10" maxlength="4" name="l2" value="">
                            l.
                            <input type="submit" class="fsearch" value=">" />
                        </div>
                    
        <h3>Datum vpisa</h3>
        <select name="last" onchange="document.sform.submit();">
            <option value="" selected="selected">Vsi objekti</option>
            <option value="1">Zadnjih 24 ur</option><option value="2">Zadnja 2 dneva</option><option value="3">Zadnje 3 dni</option><option value="7">Zadnji teden</option><option value="31">Zadnji mesec</option>        </select>
        <div class="spacer"></div><div><input type="checkbox" name="f" id="f1" option value="1" onchange="sform.submit()">Znižane cene</div><hr/><div class="grey tac">Povpreèna cena najdenih oglasov: <strong>900,09 EUR/m2</strong><br/></div>    </form>
</div></div><div id="vsebina760">
                <div class="headbar"><div id="pagination" class="top fr"><ul>
                    <li><a href="/oglasi-prodaja/cena-do-200000-eur/?s=13" class="first"><<</a></li>
                    <li><a href="/oglasi-prodaja/cena-do-200000-eur/19/?s=13" class="prev"><</a></li>
                <span class="dots3">...</span><li><a href="/oglasi-prodaja/cena-do-200000-eur/17/?s=13">17</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/18/?s=13">18</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/19/?s=13">19</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/20/?s=13" class="active">20</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/21/?s=13">21</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/22/?s=13">22</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/23/?s=13">23</a></li><span class="dots3">...</span><li><a href="/oglasi-prodaja/cena-do-200000-eur/21/?s=13" class="next">></a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/652/?s=13" class="last">>></a></li></ul></div><h1>Prodaja </h1><div class="sort cb">
                    <div class="fl">
                    <strong>Razvrsti:</strong> <a href="/oglasi-prodaja/ljubljana-mesto/stanovanje/cena-do-200000-eur/20/?s=1" class="up">lokacija</a> | <a href="/oglasi-prodaja/ljubljana-mesto/stanovanje/cena-do-200000-eur/20/?s=11" class="down">lokacija</a> | <a href="/oglasi-prodaja/ljubljana-mesto/stanovanje/cena-do-200000-eur/20/?s=3" class="up">cena</a> | <a href="/oglasi-prodaja/ljubljana-mesto/stanovanje/cena-do-200000-eur/20/?s=13" class="down act">cena</a> | <a href="/oglasi-prodaja/ljubljana-mesto/stanovanje/cena-do-200000-eur/20/?s=4" class="up">m2</a> | <a href="/oglasi-prodaja/ljubljana-mesto/stanovanje/cena-do-200000-eur/20/?s=14" class="down">m2</a> | <a href="/oglasi-prodaja/ljubljana-mesto/stanovanje/cena-do-200000-eur/20/?s=5" class="up">ponudnik</a> | <a href="/oglasi-prodaja/ljubljana-mesto/stanovanje/cena-do-200000-eur/20/?s=16" class="down">datum vpisa</a> | </div><a id="si" href="#" class="fr ibl pf i-si" style="padding-right:0">Shrani iskanje</a><div class="clearer"></div></div>
                    </div><div id="slide-thumb">
				<a href="http://www.premium-nekretnine.com/hr/prodaja/kuca/3088/vile-Malinska-Dubasnica-Malinska" target="_blank" class="pt">
					<table border="0" cellpadding="0" cellspacing="0">
						<tr>
							<td>
								<strong>Dobrinj</strong>
							</td>
						</tr>
						<tr>
							<td class="slika">
								<div><img src="https://picbase.turbosist.si/adads/thumbnails/1298.jpg" /></div>								
							</td>
						</tr>
						<tr>
							<td><span>Luksuzna kamnita hiša</span></td>
						</tr>
					</table>
				</a>
			
				<a href="http://www.sonce-nepremicnine.si/sl/Nepremicninski-oglasi/prodaja.k1/stanovanje.v1/Hrvaska.d54/Primorsko-goranska_zup..r28/Apartma_Crikvenica_Hrvaska_obala_nakup_53fb12741de9a_55c8c49,Sonce_nepremicnine.html" target="_blank" class="pt">
					<table border="0" cellpadding="0" cellspacing="0">
						<tr>
							<td>
								<strong>Crikvenica</strong>
							</td>
						</tr>
						<tr>
							<td class="slika">
								<div><img src="https://picbase.turbosist.si/adads/thumbnails/1253.jpg" /></div>								
							</td>
						</tr>
						<tr>
							<td><span>Stanovanje trisobno</span></td>
						</tr>
					</table>
				</a>
			
				<a href="http://www.sonce-nepremicnine.si/sl/Nepremicninski-oglasi/prodaja.k1/hisa.v2/Hrvaska.d54/Istarska_zupanija.r38/Vila_z_bazenom_Motovun_Hrvaska,Sonce_nepremicnine.html" target="_blank" class="pt">
					<table border="0" cellpadding="0" cellspacing="0">
						<tr>
							<td>
								<strong>Motovun</strong>
							</td>
						</tr>
						<tr>
							<td class="slika">
								<div><img src="https://picbase.turbosist.si/adads/thumbnails/1286.jpg" /></div>								
							</td>
						</tr>
						<tr>
							<td><span>Vila z bazenom</span></td>
						</tr>
					</table>
				</a>
			
				<a href="http://www.premium-nekretnine.com/hr/prodaja/stan/3167/apartmani-Krk-Krk" target="_blank" class="pt">
					<table border="0" cellpadding="0" cellspacing="0">
						<tr>
							<td>
								<strong>Mesto Krk</strong>
							</td>
						</tr>
						<tr>
							<td class="slika">
								<div><img src="https://picbase.turbosist.si/adads/thumbnails/1294.jpg" /></div>								
							</td>
						</tr>
						<tr>
							<td><span>Apartma z bazenom</span></td>
						</tr>
					</table>
				</a>
			<div class="clearer"></div></div>
<div class="seznam">
                    <div class="oglas_container oglasbold oglas597" id="o5585947">
                        <h2><a href="/oglasi-prodaja/secovlje-na-vrhu-naselja-posest_5585947/" title="5585947"><span class="title">SEÈOVLJE, NA VRHU NASELJA</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/secovlje-na-vrhu-naselja-posest_5585947/"><img src="https://picbase.turbosist.si/slonep_oglasi2/1943781.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Posest</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">704 m2, zazidljiva, Na vrhu Seèovelj se prodaja gradbena parcela v izmeri 704 m2. Parcela je pravokotne oblike in vsi ko...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                704 m2, zazidljiva, Na vrhu Seèovelj se prodaja gradbena parcela v izmeri 704 m2. Parcela je pravokotne oblike in vsi ko...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">704,00 m2</span><br />
                                <span class="cena">190.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Dodoma d.o.o., PE Koper, Pristaniška 5, 6000 Koper"><div class="logo"><a href="/oglasi-prodaja/secovlje-na-vrhu-naselja-posest_5585947/"><img src="https://picbase.turbosist.si/slonep_agenc120/598.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5585947"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-5585947" href="#" data-id="5585947" onclick="save_ad(5585947); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsecovlje-na-vrhu-naselja-posest_5585947%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsecovlje-na-vrhu-naselja-posest_5585947%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsecovlje-na-vrhu-naselja-posest_5585947%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsecovlje-na-vrhu-naselja-posest_5585947%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="5585947"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsecovlje-na-vrhu-naselja-posest_5585947%2F" class="utility" data-id="5585947"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/secovlje-na-vrhu-naselja-posest_5585947/" class="utility contact-tooltip" title="031/775-008<br />Dodoma d.o.o., PE Koper, Pristaniška 5, 6000 Koper"><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas775" id="o6020381">
                        <h2><a href="/oglasi-prodaja/portoroz-stanovanje_6020381/" title="6020381"><span class="title">PORTOROŽ</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/portoroz-stanovanje_6020381/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4562633.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Stanovanje</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Nadstropje: <strong>2</strong>/M</span><span class="atribut">Leto: <strong>1980</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">100,8 m2, 3-sobno, zgrajeno l. 1980, adaptirano l. 2014, 2/M, V centru Portoroža le par minut hoje do plaže, stanovanje ...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                100,8 m2, 3-sobno, zgrajeno l. 1980, adaptirano l. 2014, 2/M, V centru Portoroža le par minut hoje do plaže, stanovanje ...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">100,80 m2</span><br />
                                <span class="cena">190.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Focus nepremiènine, Eva Lukin s.p."><div class="logo"><a href="/oglasi-prodaja/portoroz-stanovanje_6020381/"><img src="https://picbase.turbosist.si/slonep_agenc120/77.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="6020381"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-6020381" href="#" data-id="6020381" onclick="save_ad(6020381); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fportoroz-stanovanje_6020381%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fportoroz-stanovanje_6020381%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fportoroz-stanovanje_6020381%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fportoroz-stanovanje_6020381%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="6020381"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fportoroz-stanovanje_6020381%2F" class="utility" data-id="6020381"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/portoroz-stanovanje_6020381/" class="utility contact-tooltip" title="051/609-603<br />Focus nepremiènine, Eva Lukin s.p."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas205" id="o6007311">
                        <h2><a href="/oglasi-prodaja/lj-center-levstikov-trg-poslovni-prostor_6007311/" title="6007311"><span class="title">LJ. CENTER, LEVSTIKOV TRG</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/lj-center-levstikov-trg-poslovni-prostor_6007311/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4455289.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Poslovni prostor</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Nadstropje: <strong>P</strong>/2</span><span class="atribut">Leto: <strong>1700</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">82,36 m2, prostor za storitve, zgrajen l. 1700, adaptiran l. 2011, P/2 nad., poslovni prostor z izložbo, primeren za raz...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                82,36 m2, prostor za storitve, zgrajen l. 1700, adaptiran l. 2011, P/2 nad., poslovni prostor z izložbo, primeren za raz...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">82,36 m2</span><br />
                                <span class="cena">190.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Infostan, Radiša Miljakoviæ s.p."><div class="logo"><a href="/oglasi-prodaja/lj-center-levstikov-trg-poslovni-prostor_6007311/"><img src="https://picbase.turbosist.si/slonep_agenc120/125.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="6007311"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-6007311" href="#" data-id="6007311" onclick="save_ad(6007311); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-center-levstikov-trg-poslovni-prostor_6007311%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-center-levstikov-trg-poslovni-prostor_6007311%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-center-levstikov-trg-poslovni-prostor_6007311%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-center-levstikov-trg-poslovni-prostor_6007311%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="6007311"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-center-levstikov-trg-poslovni-prostor_6007311%2F" class="utility" data-id="6007311"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/lj-center-levstikov-trg-poslovni-prostor_6007311/" class="utility contact-tooltip" title="031/306-706<br />Infostan, Radiša Miljakoviæ s.p."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                <div class="midad shadow">
                <script type='text/javascript'><!--//<![CDATA[
                 var m3_u = (location.protocol=='https:'?'https://ok.internetmedia.si/www/delivery/ajs.php':'https://ok.internetmedia.si/www/delivery/ajs.php');
                 var m3_r = Math.floor(Math.random()*99999999999);
                 if (!document.MAX_used) document.MAX_used = ',';
                 document.write ("<scr"+"ipt type='text/javascript' src='"+m3_u);
                 document.write ("?zoneid=5&amp;target=_blank&amp;block=1&amp;blockcampaign=1 . &amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5= . ");
                 document.write ('&amp;cb=' + m3_r);
                 if (document.MAX_used != ',') document.write ("&amp;exclude=" + document.MAX_used);
                 document.write (document.charset ? '&amp;charset='+document.charset : (document.characterSet ? '&amp;charset='+document.characterSet : ''));
                 document.write ("&amp;loc=" + escape(window.location));
                 if (document.referrer) document.write ("&amp;referer=" + escape(document.referrer));
                 if (document.context) document.write ("&context=" + escape(document.context));
                 if (document.mmm_fo) document.write ("&amp;mmm_fo=1");
                 document.write ("'><\/scr"+"ipt>");
            //]]>--></script><noscript><a href='https://ok.internetmedia.si/www/delivery/ck.php?n=a280490d&amp;cb=998527209&amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5=' target='_blank'><img src='https://ok.internetmedia.si/www/delivery/avw.php?zoneid=5&amp;cb=1770527493&amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5=&amp;n=a280490d' border='0' alt='' /></a></noscript>
                </div>
            
                    <div class="oglas_container oglasbold oglas166" id="o6007374">
                        <h2><a href="/oglasi-prodaja/lj-center-levstikov-trg-poslovni-prostor_6007374/" title="6007374"><span class="title">LJ. CENTER, LEVSTIKOV TRG</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/lj-center-levstikov-trg-poslovni-prostor_6007374/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4455644.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Poslovni prostor</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Nadstropje: <strong>P</strong>/2</span><span class="atribut">Leto: <strong>1700</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">82,36 m2, neživilska trgovina, zgrajena l. 1700, adaptirana l. 2011, P/2 nad., poslovni prostor - lokal z izložbo, prime...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                82,36 m2, neživilska trgovina, zgrajena l. 1700, adaptirana l. 2011, P/2 nad., poslovni prostor - lokal z izložbo, prime...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">82,36 m2</span><br />
                                <span class="cena">190.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Infostan, Radiša Miljakoviæ s.p."><div class="logo"><a href="/oglasi-prodaja/lj-center-levstikov-trg-poslovni-prostor_6007374/"><img src="https://picbase.turbosist.si/slonep_agenc120/125.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="6007374"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-6007374" href="#" data-id="6007374" onclick="save_ad(6007374); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-center-levstikov-trg-poslovni-prostor_6007374%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-center-levstikov-trg-poslovni-prostor_6007374%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-center-levstikov-trg-poslovni-prostor_6007374%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-center-levstikov-trg-poslovni-prostor_6007374%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="6007374"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-center-levstikov-trg-poslovni-prostor_6007374%2F" class="utility" data-id="6007374"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/lj-center-levstikov-trg-poslovni-prostor_6007374/" class="utility contact-tooltip" title="031/306-706<br />Infostan, Radiša Miljakoviæ s.p."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas168" id="o6038733">
                        <h2><a href="/oglasi-prodaja/radovljica-predtrg-poslovni-prostor_6038733/" title="6038733"><span class="title">RADOVLJICA, PREDTRG</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/radovljica-predtrg-poslovni-prostor_6038733/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4716161.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Poslovni prostor</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Nadstropje: <strong>P</strong></span><span class="atribut">Leto: <strong>1977</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">177,6 m2, živilska trgovina, zgrajena l. 1977, pritlièje, PREDTRG, RADOVLJICA, živilska trgovina. Poslovna stavba se nah...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                177,6 m2, živilska trgovina, zgrajena l. 1977, pritlièje, PREDTRG, RADOVLJICA, živilska trgovina. Poslovna stavba se nah...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">177,60 m2</span><br />
                                <span class="cena">190.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Gaberit nepremiènine Matija Ceket s.p."><div class="logo"><a href="/oglasi-prodaja/radovljica-predtrg-poslovni-prostor_6038733/"><img src="https://picbase.turbosist.si/slonep_agenc120/1445.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="6038733"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-6038733" href="#" data-id="6038733" onclick="save_ad(6038733); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fradovljica-predtrg-poslovni-prostor_6038733%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fradovljica-predtrg-poslovni-prostor_6038733%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fradovljica-predtrg-poslovni-prostor_6038733%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fradovljica-predtrg-poslovni-prostor_6038733%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="6038733"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fradovljica-predtrg-poslovni-prostor_6038733%2F" class="utility" data-id="6038733"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/radovljica-predtrg-poslovni-prostor_6038733/" class="utility contact-tooltip" title="0599/28-075<br />Gaberit nepremiènine Matija Ceket s.p."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas730" id="o6004556">
                        <h2><a href="/oglasi-prodaja/lj-siska-nad-gostilno-kaval-posest_6004556/" title="6004556"><span class="title">LJ. ŠIŠKA, NAD GOSTILNO KAVAL</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/lj-siska-nad-gostilno-kaval-posest_6004556/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4444593.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Posest</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">878 m2, zazidljiva, èudovit razgled, ob kmetijskem pasu, sonèna, mirna lokacija, prodamo. Cena: 190.000,00 EUR</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                878 m2, zazidljiva, èudovit razgled, ob kmetijskem pasu, sonèna, mirna lokacija, prodamo. Cena: 190.000,00 EUR
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">878,00 m2</span><br />
                                <span class="cena">190.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Harmonija nepremiènine Ksenja Kokalj s.p."><div class="logo"><a href="/oglasi-prodaja/lj-siska-nad-gostilno-kaval-posest_6004556/"><img src="https://picbase.turbosist.si/slonep_agenc120/1266.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="6004556"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-6004556" href="#" data-id="6004556" onclick="save_ad(6004556); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-siska-nad-gostilno-kaval-posest_6004556%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-siska-nad-gostilno-kaval-posest_6004556%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-siska-nad-gostilno-kaval-posest_6004556%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-siska-nad-gostilno-kaval-posest_6004556%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="6004556"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-siska-nad-gostilno-kaval-posest_6004556%2F" class="utility" data-id="6004556"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/lj-siska-nad-gostilno-kaval-posest_6004556/" class="utility contact-tooltip" title="041/750-407<br />Harmonija nepremiènine Ksenja Kokalj s.p."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas771" id="o5579439">
                        <h2><a href="/oglasi-prodaja/premantura-hisa_5579439/" title="5579439"><span class="title">PREMANTURA</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/premantura-hisa_5579439/"><img src="https://picbase.turbosist.si/slonep_oglasi2/1913728.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hiša</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Leto: <strong>2007</strong></span><span class="atribut">Zemljišèe: <strong>236 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">90 m2, dvojèek, zgrajen l. 2007, 236 m2 zemljišèa, Prekrasna hiša v okolici Premanture, površine 90 m2, z vrtom 236 m2, ...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                90 m2, dvojèek, zgrajen l. 2007, 236 m2 zemljišèa, Prekrasna hiša v okolici Premanture, površine 90 m2, z vrtom 236 m2, ...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">90,00 m2</span><br />
                                <span class="cena">190.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Istra-immobilien obrt za poslovanje nekretninama"><div class="logo"><a href="/oglasi-prodaja/premantura-hisa_5579439/"><img src="https://picbase.turbosist.si/slonep_agenc120/1195.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5579439"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-5579439" href="#" data-id="5579439" onclick="save_ad(5579439); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fpremantura-hisa_5579439%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fpremantura-hisa_5579439%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fpremantura-hisa_5579439%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fpremantura-hisa_5579439%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="5579439"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fpremantura-hisa_5579439%2F" class="utility" data-id="5579439"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/premantura-hisa_5579439/" class="utility contact-tooltip" title="+385989161212<br />Istra-immobilien obrt za poslovanje nekretninama"><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas891" id="o5903193">
                        <h2><a href="/oglasi-prodaja/fazana-istra-hisa_5903193/" title="5903193"><span class="title">FAŽANA, ISTRA</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/fazana-istra-hisa_5903193/"><img src="https://picbase.turbosist.si/slonep_oglasi2/3695893.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hiša</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Leto: <strong>2008</strong></span><span class="atribut">Zemljišèe: <strong>750 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">200 m2, samostojna, zgrajena l. 2008, 750 m2 zemljišèa, prodamo. Cena: 190.000,00 EUR</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                200 m2, samostojna, zgrajena l. 2008, 750 m2 zemljišèa, prodamo. Cena: 190.000,00 EUR
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">200,00 m2</span><br />
                                <span class="cena">190.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Istra-immobilien obrt za poslovanje nekretninama"><div class="logo"><a href="/oglasi-prodaja/fazana-istra-hisa_5903193/"><img src="https://picbase.turbosist.si/slonep_agenc120/1195.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5903193"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-5903193" href="#" data-id="5903193" onclick="save_ad(5903193); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Ffazana-istra-hisa_5903193%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Ffazana-istra-hisa_5903193%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Ffazana-istra-hisa_5903193%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Ffazana-istra-hisa_5903193%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="5903193"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Ffazana-istra-hisa_5903193%2F" class="utility" data-id="5903193"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/fazana-istra-hisa_5903193/" class="utility contact-tooltip" title="+385989161212<br />Istra-immobilien obrt za poslovanje nekretninama"><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas445" id="o5908480">
                        <h2><a href="/oglasi-prodaja/fazana-istra-brioni-hisa_5908480/" title="5908480"><span class="title">FAŽANA, ISTRA, BRIONI.</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/fazana-istra-brioni-hisa_5908480/"><img src="https://picbase.turbosist.si/slonep_oglasi2/3733037.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hiša</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Nadstropje: <strong>P+1</strong></span><span class="atribut">Leto: <strong>2010</strong></span><span class="atribut">Zemljišèe: <strong>750 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">200 m2, samostojna, zgrajena l. 2010, 750 m2 zemljišèa, P+1, prodamo. Cena: 190.000,00 EUR</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                200 m2, samostojna, zgrajena l. 2010, 750 m2 zemljišèa, P+1, prodamo. Cena: 190.000,00 EUR
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">200,00 m2</span><br />
                                <span class="cena">190.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Istra-immobilien obrt za poslovanje nekretninama"><div class="logo"><a href="/oglasi-prodaja/fazana-istra-brioni-hisa_5908480/"><img src="https://picbase.turbosist.si/slonep_agenc120/1195.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5908480"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-5908480" href="#" data-id="5908480" onclick="save_ad(5908480); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Ffazana-istra-brioni-hisa_5908480%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Ffazana-istra-brioni-hisa_5908480%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Ffazana-istra-brioni-hisa_5908480%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Ffazana-istra-brioni-hisa_5908480%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="5908480"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Ffazana-istra-brioni-hisa_5908480%2F" class="utility" data-id="5908480"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/fazana-istra-brioni-hisa_5908480/" class="utility contact-tooltip" title="+385989161212<br />Istra-immobilien obrt za poslovanje nekretninama"><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                <div class="midad shadow">
                <script type='text/javascript'><!--//<![CDATA[
                 var m3_u = (location.protocol=='https:'?'https://ok.internetmedia.si/www/delivery/ajs.php':'https://ok.internetmedia.si/www/delivery/ajs.php');
                 var m3_r = Math.floor(Math.random()*99999999999);
                 if (!document.MAX_used) document.MAX_used = ',';
                 document.write ("<scr"+"ipt type='text/javascript' src='"+m3_u);
                 document.write ("?zoneid=5&amp;target=_blank&amp;block=1&amp;blockcampaign=1 . &amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5= . ");
                 document.write ('&amp;cb=' + m3_r);
                 if (document.MAX_used != ',') document.write ("&amp;exclude=" + document.MAX_used);
                 document.write (document.charset ? '&amp;charset='+document.charset : (document.characterSet ? '&amp;charset='+document.characterSet : ''));
                 document.write ("&amp;loc=" + escape(window.location));
                 if (document.referrer) document.write ("&amp;referer=" + escape(document.referrer));
                 if (document.context) document.write ("&context=" + escape(document.context));
                 if (document.mmm_fo) document.write ("&amp;mmm_fo=1");
                 document.write ("'><\/scr"+"ipt>");
            //]]>--></script><noscript><a href='https://ok.internetmedia.si/www/delivery/ck.php?n=a280490d&amp;cb=978393988&amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5=' target='_blank'><img src='https://ok.internetmedia.si/www/delivery/avw.php?zoneid=5&amp;cb=1362630713&amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5=&amp;n=a280490d' border='0' alt='' /></a></noscript>
                </div>
            
                    <div class="oglas_container oglasbold oglas487" id="o5765667">
                        <h2><a href="/oglasi-prodaja/soline-stanovanje_5765667/" title="5765667"><span class="title">SOLINE</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/soline-stanovanje_5765667/"><img src="https://picbase.turbosist.si/slonep_oglasi2/2821380.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Stanovanje</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Nadstropje: <strong>P</strong></span><span class="atribut">Leto: <strong>2005</strong></span><span class="atribut">Zemljišèe: <strong>132 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">64 m2, 2,5-sobno, zgrajeno l. 2005, 132 m2 zemljišèa, pritlièje, uvala soline - opremljen apartma s pogledom na morje in...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                64 m2, 2,5-sobno, zgrajeno l. 2005, 132 m2 zemljišèa, pritlièje, uvala soline - opremljen apartma s pogledom na morje in...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">64,00 m2</span><br />
                                <span class="cena">190.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Kvarner imobilije d.o.o. Njivice"><div class="logo"><a href="/oglasi-prodaja/soline-stanovanje_5765667/"><img src="https://picbase.turbosist.si/slonep_agenc120/167.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5765667"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-5765667" href="#" data-id="5765667" onclick="save_ad(5765667); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsoline-stanovanje_5765667%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsoline-stanovanje_5765667%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsoline-stanovanje_5765667%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsoline-stanovanje_5765667%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="5765667"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsoline-stanovanje_5765667%2F" class="utility" data-id="5765667"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/soline-stanovanje_5765667/" class="utility contact-tooltip" title="+385 (0)51 847 074<br />Kvarner imobilije d.o.o. Njivice"><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas788" id="o6015049">
                        <h2><a href="/oglasi-prodaja/malinska-hisa_6015049/" title="6015049"><span class="title">MALINSKA</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/malinska-hisa_6015049/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4518905.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hiša</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Leto: <strong>2006</strong></span><span class="atribut">Zemljišèe: <strong>145 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">100 m2, dvojèek, zgrajen l. 2006, 145 m2 zemljišèa, Opremljena hiša z garažo na mirni lokaciji, oddaljena 350 m od plaže...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                100 m2, dvojèek, zgrajen l. 2006, 145 m2 zemljišèa, Opremljena hiša z garažo na mirni lokaciji, oddaljena 350 m od plaže...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">100,00 m2</span><br />
                                <span class="cena">190.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Kvarner imobilije d.o.o. Njivice"><div class="logo"><a href="/oglasi-prodaja/malinska-hisa_6015049/"><img src="https://picbase.turbosist.si/slonep_agenc120/167.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="6015049"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-6015049" href="#" data-id="6015049" onclick="save_ad(6015049); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmalinska-hisa_6015049%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmalinska-hisa_6015049%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmalinska-hisa_6015049%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmalinska-hisa_6015049%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="6015049"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmalinska-hisa_6015049%2F" class="utility" data-id="6015049"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/malinska-hisa_6015049/" class="utility contact-tooltip" title="+385 (0)51 847 074<br />Kvarner imobilije d.o.o. Njivice"><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas263" id="o6035233">
                        <h2><a href="/oglasi-prodaja/dobrinj-hisa_6035233/" title="6035233"><span class="title">DOBRINJ</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/dobrinj-hisa_6035233/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4687169.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hiša</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Leto: <strong>2008</strong></span><span class="atribut">Zemljišèe: <strong>900 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">100 m2, dvojèek, zgrajen l. 2008, 900 m2 zemljišèa, PRILOŽNOST, nova dvojna kamnita hiša z lepo urejenim vrtom na mirni ...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                100 m2, dvojèek, zgrajen l. 2008, 900 m2 zemljišèa, PRILOŽNOST, nova dvojna kamnita hiša z lepo urejenim vrtom na mirni ...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">100,00 m2</span><br />
                                <span class="cena">190.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Kvarner imobilije d.o.o. Njivice"><div class="logo"><a href="/oglasi-prodaja/dobrinj-hisa_6035233/"><img src="https://picbase.turbosist.si/slonep_agenc120/167.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="6035233"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-6035233" href="#" data-id="6035233" onclick="save_ad(6035233); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fdobrinj-hisa_6035233%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fdobrinj-hisa_6035233%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fdobrinj-hisa_6035233%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fdobrinj-hisa_6035233%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="6035233"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fdobrinj-hisa_6035233%2F" class="utility" data-id="6035233"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/dobrinj-hisa_6035233/" class="utility contact-tooltip" title="+385 (0)51 847 074<br />Kvarner imobilije d.o.o. Njivice"><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas193" id="o6016350">
                        <h2><a href="/oglasi-prodaja/dobrinj-hisa_6016350/" title="6016350"><span class="title">DOBRINJ</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/dobrinj-hisa_6016350/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4529053.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hiša</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Leto: <strong>1900</strong></span><span class="atribut">Zemljišèe: <strong>1700 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">96 m2, dvojèek, zgrajen l. 1900, adaptiran l. 2005, 1.700 m2 zemljišèa, Kamniti dvojèek na mirni lokaciji z velikim vrto...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                96 m2, dvojèek, zgrajen l. 1900, adaptiran l. 2005, 1.700 m2 zemljišèa, Kamniti dvojèek na mirni lokaciji z velikim vrto...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">96,00 m2</span><br />
                                <span class="cena">190.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Kvarner imobilije d.o.o. Njivice"><div class="logo"><a href="/oglasi-prodaja/dobrinj-hisa_6016350/"><img src="https://picbase.turbosist.si/slonep_agenc120/167.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="6016350"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-6016350" href="#" data-id="6016350" onclick="save_ad(6016350); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fdobrinj-hisa_6016350%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fdobrinj-hisa_6016350%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fdobrinj-hisa_6016350%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fdobrinj-hisa_6016350%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="6016350"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fdobrinj-hisa_6016350%2F" class="utility" data-id="6016350"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/dobrinj-hisa_6016350/" class="utility contact-tooltip" title="+385 (0)51 847 074<br />Kvarner imobilije d.o.o. Njivice"><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas292" id="o6019282">
                        <h2><a href="/oglasi-prodaja/lucija-parecag-posest_6019282/" title="6019282"><span class="title">LUCIJA, PARECAG</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/lucija-parecag-posest_6019282/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4553755.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Posest</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">828 m2, zazidljiva, zemljišèe se nahaja ob cesti, s pogledom na morje, na parceli vsa komunalna infrastruktura, izdelan ...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                828 m2, zazidljiva, zemljišèe se nahaja ob cesti, s pogledom na morje, na parceli vsa komunalna infrastruktura, izdelan ...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">828,00 m2</span><br />
                                <span class="cena">190.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Malis nepremiènine d.o.o."><div class="logo"><a href="/oglasi-prodaja/lucija-parecag-posest_6019282/"><img src="https://picbase.turbosist.si/slonep_agenc120/433.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="6019282"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-6019282" href="#" data-id="6019282" onclick="save_ad(6019282); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flucija-parecag-posest_6019282%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flucija-parecag-posest_6019282%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flucija-parecag-posest_6019282%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flucija-parecag-posest_6019282%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="6019282"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flucija-parecag-posest_6019282%2F" class="utility" data-id="6019282"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/lucija-parecag-posest_6019282/" class="utility contact-tooltip" title="041/345-544<br />Malis nepremiènine d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas818" id="o5982319">
                        <h2><a href="/oglasi-prodaja/zapotok-hisa_5982319/" title="5982319"><span class="title">ZAPOTOK</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/zapotok-hisa_5982319/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4263871.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hiša</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Nadstropje: <strong>P+M</strong></span><span class="atribut">Leto: <strong>2008</strong></span><span class="atribut">Zemljišèe: <strong>1125 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">200 m2, samostojna, zgrajena l. 2008, 1.125 m2 zemljišèa, P+M, P:120 m2, neizdelana man.80 m2 upor. p. Lahko dvostanovan...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                200 m2, samostojna, zgrajena l. 2008, 1.125 m2 zemljišèa, P+M, P:120 m2, neizdelana man.80 m2 upor. p. Lahko dvostanovan...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">200,00 m2</span><br />
                                <span class="cena">190.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="METKA HANUNA s.p."><div class="logo"><a href="/oglasi-prodaja/zapotok-hisa_5982319/"><img src="/images/ponudba-podjetja.png" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5982319"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-5982319" href="#" data-id="5982319" onclick="save_ad(5982319); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fzapotok-hisa_5982319%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fzapotok-hisa_5982319%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fzapotok-hisa_5982319%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fzapotok-hisa_5982319%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="5982319"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fzapotok-hisa_5982319%2F" class="utility" data-id="5982319"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/zapotok-hisa_5982319/" class="utility contact-tooltip" title="041/203-861<br />METKA HANUNA s.p."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                <div class="midad shadow">
                <script type='text/javascript'><!--//<![CDATA[
                 var m3_u = (location.protocol=='https:'?'https://ok.internetmedia.si/www/delivery/ajs.php':'https://ok.internetmedia.si/www/delivery/ajs.php');
                 var m3_r = Math.floor(Math.random()*99999999999);
                 if (!document.MAX_used) document.MAX_used = ',';
                 document.write ("<scr"+"ipt type='text/javascript' src='"+m3_u);
                 document.write ("?zoneid=5&amp;target=_blank&amp;block=1&amp;blockcampaign=1 . &amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5= . ");
                 document.write ('&amp;cb=' + m3_r);
                 if (document.MAX_used != ',') document.write ("&amp;exclude=" + document.MAX_used);
                 document.write (document.charset ? '&amp;charset='+document.charset : (document.characterSet ? '&amp;charset='+document.characterSet : ''));
                 document.write ("&amp;loc=" + escape(window.location));
                 if (document.referrer) document.write ("&amp;referer=" + escape(document.referrer));
                 if (document.context) document.write ("&context=" + escape(document.context));
                 if (document.mmm_fo) document.write ("&amp;mmm_fo=1");
                 document.write ("'><\/scr"+"ipt>");
            //]]>--></script><noscript><a href='https://ok.internetmedia.si/www/delivery/ck.php?n=a280490d&amp;cb=1429678965&amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5=' target='_blank'><img src='https://ok.internetmedia.si/www/delivery/avw.php?zoneid=5&amp;cb=471677069&amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5=&amp;n=a280490d' border='0' alt='' /></a></noscript>
                </div>
            
                    <div class="oglas_container oglasbold oglas290" id="o5989344">
                        <h2><a href="/oglasi-prodaja/bled-koritenska-cesta-hisa_5989344/" title="5989344"><span class="title">BLED, KORITENSKA CESTA</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/bled-koritenska-cesta-hisa_5989344/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4317265.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hiša</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Leto: <strong>1976</strong></span><span class="atribut">Zemljišèe: <strong>590 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">269 m2, dvostanovanjska, zgrajena l. 1976, 590 m2 zemljišèa, prodamo. Cena: 190.000,00 EUR</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                269 m2, dvostanovanjska, zgrajena l. 1976, 590 m2 zemljišèa, prodamo. Cena: 190.000,00 EUR
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">269,00 m2</span><br />
                                <span class="cena">190.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Koncepti d.o.o."><div class="logo"><a href="/oglasi-prodaja/bled-koritenska-cesta-hisa_5989344/"><img src="https://picbase.turbosist.si/slonep_agenc120/360.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5989344"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-5989344" href="#" data-id="5989344" onclick="save_ad(5989344); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fbled-koritenska-cesta-hisa_5989344%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fbled-koritenska-cesta-hisa_5989344%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fbled-koritenska-cesta-hisa_5989344%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fbled-koritenska-cesta-hisa_5989344%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="5989344"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fbled-koritenska-cesta-hisa_5989344%2F" class="utility" data-id="5989344"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/bled-koritenska-cesta-hisa_5989344/" class="utility contact-tooltip" title="04/574-35-14<br />Koncepti d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas92" id="o5951129">
                        <h2><a href="/oglasi-prodaja/lj-siska-sentvid-hisa_5951129/" title="5951129"><span class="title">LJ. ŠIŠKA, ŠENTVID</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/lj-siska-sentvid-hisa_5951129/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4045397.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hiša</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Nadstropje: <strong>K+P+M</strong></span><span class="atribut">Leto: <strong>1960</strong></span><span class="atribut">Zemljišèe: <strong>414 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">183 m2, samostojna, zgrajena l. 1960, 414 m2 zemljišèa, K+P+M, Prodamo samostojno stanovanjsko hišo na parceli 414 m2 po...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                183 m2, samostojna, zgrajena l. 1960, 414 m2 zemljišèa, K+P+M, Prodamo samostojno stanovanjsko hišo na parceli 414 m2 po...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">183,00 m2</span><br />
                                <span class="cena">190.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Nepremiènine M8, Lea Kavaliè s.p."><div class="logo"><a href="/oglasi-prodaja/lj-siska-sentvid-hisa_5951129/"><img src="https://picbase.turbosist.si/slonep_agenc120/1915.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5951129"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-5951129" href="#" data-id="5951129" onclick="save_ad(5951129); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-siska-sentvid-hisa_5951129%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-siska-sentvid-hisa_5951129%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-siska-sentvid-hisa_5951129%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-siska-sentvid-hisa_5951129%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="5951129"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-siska-sentvid-hisa_5951129%2F" class="utility" data-id="5951129"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/lj-siska-sentvid-hisa_5951129/" class="utility contact-tooltip" title="041/499-652<br />Nepremiènine M8, Lea Kavaliè s.p."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas478" id="o6017831">
                        <h2><a href="/oglasi-prodaja/gostinjac-hisa_6017831/" title="6017831"><span class="title">GOSTINJAC</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/gostinjac-hisa_6017831/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4541060.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hiša</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Nadstropje: <strong>K+P</strong></span><span class="atribut">Leto: <strong>2005</strong></span><span class="atribut">Zemljišèe: <strong>1700 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">185 m2, samostojna, adaptirana l. 2005, 1.700 m2 zemljišèa, K+P, Stara kamnita hiša, popolnoma obnovljena leta 2005, se ...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                185 m2, samostojna, adaptirana l. 2005, 1.700 m2 zemljišèa, K+P, Stara kamnita hiša, popolnoma obnovljena leta 2005, se ...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">185,00 m2</span><br />
                                <span class="cena">190.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="NOTE posredništvo z nepremièninami Polona Bobera s.p., PE Ljubljana"><div class="logo"><a href="/oglasi-prodaja/gostinjac-hisa_6017831/"><img src="https://picbase.turbosist.si/slonep_agenc120/103.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="6017831"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-6017831" href="#" data-id="6017831" onclick="save_ad(6017831); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fgostinjac-hisa_6017831%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fgostinjac-hisa_6017831%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fgostinjac-hisa_6017831%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fgostinjac-hisa_6017831%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="6017831"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fgostinjac-hisa_6017831%2F" class="utility" data-id="6017831"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/gostinjac-hisa_6017831/" class="utility contact-tooltip" title="051/624-753<br />NOTE posredništvo z nepremièninami Polona Bobera s.p., PE Ljubljana"><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas729" id="o6013427">
                        <h2><a href="/oglasi-prodaja/col-hisa_6013427/" title="6013427"><span class="title">COL</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/col-hisa_6013427/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4504734.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hiša</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Leto: <strong>1954</strong></span><span class="atribut">Zemljišèe: <strong>3710 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">342 m2, samostojna, zgrajena l. 1954, 3.710 m2 zemljišèa, Mirna in urejena lokacija s pogledom na tržaški zaliv, prodamo...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                342 m2, samostojna, zgrajena l. 1954, 3.710 m2 zemljišèa, Mirna in urejena lokacija s pogledom na tržaški zaliv, prodamo...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">342,00 m2</span><br />
                                <span class="cena">190.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Oridom nepremiènine, Ivan Orešnik s.p."><div class="logo"><a href="/oglasi-prodaja/col-hisa_6013427/"><img src="https://picbase.turbosist.si/slonep_agenc120/1083.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="6013427"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-6013427" href="#" data-id="6013427" onclick="save_ad(6013427); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fcol-hisa_6013427%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fcol-hisa_6013427%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fcol-hisa_6013427%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fcol-hisa_6013427%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="6013427"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fcol-hisa_6013427%2F" class="utility" data-id="6013427"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/col-hisa_6013427/" class="utility contact-tooltip" title="031/256-560<br />Oridom nepremiènine, Ivan Orešnik s.p."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas190" id="o5883112">
                        <h2><a href="/oglasi-prodaja/radece-poslovni-prostor_5883112/" title="5883112"><span class="title">RADEÈE</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/radece-poslovni-prostor_5883112/"><img src="https://picbase.turbosist.si/slonep_oglasi2/3563783.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Poslovni prostor</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Nadstropje: <strong>1</strong>/1</span><span class="atribut">Leto: <strong>2012</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">675 m2, neživilska trgovina, adaptirana l. 2012, 1/1 nad., možna tudi oddaja ali poslovno partnerstvo, prodamo. Cena: cc...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                675 m2, neživilska trgovina, adaptirana l. 2012, 1/1 nad., možna tudi oddaja ali poslovno partnerstvo, prodamo. Cena: cc...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">675,00 m2</span><br />
                                <span class="cena">190.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Oridom nepremiènine, Ivan Orešnik s.p."><div class="logo"><a href="/oglasi-prodaja/radece-poslovni-prostor_5883112/"><img src="https://picbase.turbosist.si/slonep_agenc120/1083.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5883112"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-5883112" href="#" data-id="5883112" onclick="save_ad(5883112); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fradece-poslovni-prostor_5883112%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fradece-poslovni-prostor_5883112%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fradece-poslovni-prostor_5883112%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fradece-poslovni-prostor_5883112%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="5883112"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fradece-poslovni-prostor_5883112%2F" class="utility" data-id="5883112"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/radece-poslovni-prostor_5883112/" class="utility contact-tooltip" title="031/256-560<br />Oridom nepremiènine, Ivan Orešnik s.p."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas320" id="o5746742">
                        <h2><a href="/oglasi-prodaja/njivice-atraktivna-lokacija-hisa_5746742/" title="5746742"><span class="title">NJIVICE, ATRAKTIVNA LOKACIJA</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/njivice-atraktivna-lokacija-hisa_5746742/"><img src="https://picbase.turbosist.si/slonep_oglasi2/2708843.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hiša</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Leto: <strong>1965</strong></span><span class="atribut">Zemljišèe: <strong>364 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">60 m2, samostojna, zgrajena l. 1965, 364 m2 zemljišèa, poèitniška hiša, 60 m2 z lepo urejenim vrtom površino 304 m2, pog...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                60 m2, samostojna, zgrajena l. 1965, 364 m2 zemljišèa, poèitniška hiša, 60 m2 z lepo urejenim vrtom površino 304 m2, pog...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">60,00 m2</span><br />
                                <span class="cena">190.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Premium SM d.o.o."><div class="logo"><a href="/oglasi-prodaja/njivice-atraktivna-lokacija-hisa_5746742/"><img src="https://picbase.turbosist.si/slonep_agenc120/2242.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5746742"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-5746742" href="#" data-id="5746742" onclick="save_ad(5746742); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fnjivice-atraktivna-lokacija-hisa_5746742%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fnjivice-atraktivna-lokacija-hisa_5746742%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fnjivice-atraktivna-lokacija-hisa_5746742%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fnjivice-atraktivna-lokacija-hisa_5746742%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="5746742"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fnjivice-atraktivna-lokacija-hisa_5746742%2F" class="utility" data-id="5746742"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/njivice-atraktivna-lokacija-hisa_5746742/" class="utility contact-tooltip" title="+385 51 858364<br />Premium SM d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                <div class="midad shadow">
                <script type='text/javascript'><!--//<![CDATA[
                 var m3_u = (location.protocol=='https:'?'https://ok.internetmedia.si/www/delivery/ajs.php':'https://ok.internetmedia.si/www/delivery/ajs.php');
                 var m3_r = Math.floor(Math.random()*99999999999);
                 if (!document.MAX_used) document.MAX_used = ',';
                 document.write ("<scr"+"ipt type='text/javascript' src='"+m3_u);
                 document.write ("?zoneid=5&amp;target=_blank&amp;block=1&amp;blockcampaign=1 . &amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5= . ");
                 document.write ('&amp;cb=' + m3_r);
                 if (document.MAX_used != ',') document.write ("&amp;exclude=" + document.MAX_used);
                 document.write (document.charset ? '&amp;charset='+document.charset : (document.characterSet ? '&amp;charset='+document.characterSet : ''));
                 document.write ("&amp;loc=" + escape(window.location));
                 if (document.referrer) document.write ("&amp;referer=" + escape(document.referrer));
                 if (document.context) document.write ("&context=" + escape(document.context));
                 if (document.mmm_fo) document.write ("&amp;mmm_fo=1");
                 document.write ("'><\/scr"+"ipt>");
            //]]>--></script><noscript><a href='https://ok.internetmedia.si/www/delivery/ck.php?n=a280490d&amp;cb=2055242497&amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5=' target='_blank'><img src='https://ok.internetmedia.si/www/delivery/avw.php?zoneid=5&amp;cb=1361930471&amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5=&amp;n=a280490d' border='0' alt='' /></a></noscript>
                </div>
            
                    <div class="oglas_container oglasbold oglas500" id="o5979973">
                        <h2><a href="/oglasi-prodaja/omisalj-200-od-morja-hisa_5979973/" title="5979973"><span class="title">OMIŠALJ, 200 OD MORJA</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/omisalj-200-od-morja-hisa_5979973/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4246257.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hiša</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Nadstropje: <strong>P+1</strong></span><span class="atribut">Leto: <strong>1992</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">135 m2, samostojna, zgrajena l. 1992, P+1, Krk, Omišalj, samostojna hiša 135 m2 s pogledom na morje, prodamo. Cena: max....</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                135 m2, samostojna, zgrajena l. 1992, P+1, Krk, Omišalj, samostojna hiša 135 m2 s pogledom na morje, prodamo. Cena: max....
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">135,00 m2</span><br />
                                <span class="cena">190.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Premium SM d.o.o."><div class="logo"><a href="/oglasi-prodaja/omisalj-200-od-morja-hisa_5979973/"><img src="https://picbase.turbosist.si/slonep_agenc120/2242.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5979973"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-5979973" href="#" data-id="5979973" onclick="save_ad(5979973); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fomisalj-200-od-morja-hisa_5979973%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fomisalj-200-od-morja-hisa_5979973%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fomisalj-200-od-morja-hisa_5979973%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fomisalj-200-od-morja-hisa_5979973%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="5979973"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fomisalj-200-od-morja-hisa_5979973%2F" class="utility" data-id="5979973"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/omisalj-200-od-morja-hisa_5979973/" class="utility contact-tooltip" title="+385 51 858364<br />Premium SM d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas758" id="o5635829">
                        <h2><a href="/oglasi-prodaja/malinska-samostojna-hiza-hisa_5635829/" title="5635829"><span class="title">MALINSKA, SAMOSTOJNA HIŽA</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/malinska-samostojna-hiza-hisa_5635829/"><img src="https://picbase.turbosist.si/slonep_oglasi2/2171931.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hiša</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Leto: <strong>2004</strong></span><span class="atribut">Zemljišèe: <strong>600 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">250 m2, samostojna, zgrajena l. 2004, 600 m2 zemljišèa, okolica, samostojna hiša, 250 m2, zgrajena leta 2004.Na parceli ...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                250 m2, samostojna, zgrajena l. 2004, 600 m2 zemljišèa, okolica, samostojna hiša, 250 m2, zgrajena leta 2004.Na parceli ...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">250,00 m2</span><br />
                                <span class="cena">190.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Premium SM d.o.o."><div class="logo"><a href="/oglasi-prodaja/malinska-samostojna-hiza-hisa_5635829/"><img src="https://picbase.turbosist.si/slonep_agenc120/2242.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5635829"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-5635829" href="#" data-id="5635829" onclick="save_ad(5635829); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmalinska-samostojna-hiza-hisa_5635829%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmalinska-samostojna-hiza-hisa_5635829%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmalinska-samostojna-hiza-hisa_5635829%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmalinska-samostojna-hiza-hisa_5635829%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="5635829"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmalinska-samostojna-hiza-hisa_5635829%2F" class="utility" data-id="5635829"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/malinska-samostojna-hiza-hisa_5635829/" class="utility contact-tooltip" title="+385 51 858364<br />Premium SM d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas232" id="o5699220">
                        <h2><a href="/oglasi-prodaja/njivice-hisa_5699220/" title="5699220"><span class="title">NJIVICE</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/njivice-hisa_5699220/"><img src="https://picbase.turbosist.si/slonep_oglasi2/2455608.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hiša</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Leto: <strong>1971</strong></span><span class="atribut">Zemljišèe: <strong>120 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">82 m2, samostojna, zgrajena l. 1971, 120 m2 zemljišèa, hiša z dvema apartmajema in vrt. 82 m2 z vrtom 120 m2. Hiša je se...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                82 m2, samostojna, zgrajena l. 1971, 120 m2 zemljišèa, hiša z dvema apartmajema in vrt. 82 m2 z vrtom 120 m2. Hiša je se...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">82,00 m2</span><br />
                                <span class="cena">190.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Premium SM d.o.o."><div class="logo"><a href="/oglasi-prodaja/njivice-hisa_5699220/"><img src="https://picbase.turbosist.si/slonep_agenc120/2242.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5699220"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-5699220" href="#" data-id="5699220" onclick="save_ad(5699220); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fnjivice-hisa_5699220%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fnjivice-hisa_5699220%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fnjivice-hisa_5699220%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fnjivice-hisa_5699220%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="5699220"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fnjivice-hisa_5699220%2F" class="utility" data-id="5699220"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/njivice-hisa_5699220/" class="utility contact-tooltip" title="+385 51 858364<br />Premium SM d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas276" id="o6039918">
                        <h2><a href="/oglasi-prodaja/malinska-350-m-od-morja-stanovanje_6039918/" title="6039918"><span class="title">MALINSKA, 350 M OD MORJA</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/malinska-350-m-od-morja-stanovanje_6039918/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4725703.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Stanovanje</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Leto: <strong>2010</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">99 m2, apartma, zgrajen l. 2010, Malinska- center, stanovanje 100 m2,350 m od morja, prodamo. Cena: max. 190.000,00 EUR</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                99 m2, apartma, zgrajen l. 2010, Malinska- center, stanovanje 100 m2,350 m od morja, prodamo. Cena: max. 190.000,00 EUR
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">99,00 m2</span><br />
                                <span class="cena">190.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Premium SM d.o.o."><div class="logo"><a href="/oglasi-prodaja/malinska-350-m-od-morja-stanovanje_6039918/"><img src="https://picbase.turbosist.si/slonep_agenc120/2242.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="6039918"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-6039918" href="#" data-id="6039918" onclick="save_ad(6039918); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmalinska-350-m-od-morja-stanovanje_6039918%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmalinska-350-m-od-morja-stanovanje_6039918%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmalinska-350-m-od-morja-stanovanje_6039918%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmalinska-350-m-od-morja-stanovanje_6039918%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="6039918"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmalinska-350-m-od-morja-stanovanje_6039918%2F" class="utility" data-id="6039918"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/malinska-350-m-od-morja-stanovanje_6039918/" class="utility contact-tooltip" title="+385 51 858364<br />Premium SM d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas962" id="o5995730">
                        <h2><a href="/oglasi-prodaja/celje-kukovceva-ulica-hisa_5995730/" title="5995730"><span class="title">CELJE, KUKOVÈEVA ULICA</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/celje-kukovceva-ulica-hisa_5995730/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4365134.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hiša</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Leto: <strong>1967</strong></span><span class="atribut">Zemljišèe: <strong>986 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">264,5 m2, samostojna, zgrajena l. 1967, adaptirana l. 2010, 986 m2 zemljišèa, vsi prikljuèki, odlièen pogled na Stari gr...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                264,5 m2, samostojna, zgrajena l. 1967, adaptirana l. 2010, 986 m2 zemljišèa, vsi prikljuèki, odlièen pogled na Stari gr...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">264,50 m2</span><br />
                                <span class="cena">190.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Real-fin posredovanje z nepremièninami d.o.o., PE Celje"><div class="logo"><a href="/oglasi-prodaja/celje-kukovceva-ulica-hisa_5995730/"><img src="/images/ponudba-podjetja.png" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5995730"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-5995730" href="#" data-id="5995730" onclick="save_ad(5995730); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fcelje-kukovceva-ulica-hisa_5995730%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fcelje-kukovceva-ulica-hisa_5995730%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fcelje-kukovceva-ulica-hisa_5995730%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fcelje-kukovceva-ulica-hisa_5995730%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="5995730"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fcelje-kukovceva-ulica-hisa_5995730%2F" class="utility" data-id="5995730"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/celje-kukovceva-ulica-hisa_5995730/" class="utility contact-tooltip" title="041/740-994<br />Real-fin posredovanje z nepremièninami d.o.o., PE Celje"><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas696" id="o6038063">
                        <h2><a href="/oglasi-prodaja/senozece-center-poslovni-prostor_6038063/" title="6038063"><span class="title">SENOŽEÈE, CENTER</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/senozece-center-poslovni-prostor_6038063/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4710559.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Poslovni prostor</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Nadstropje: <strong>P</strong>/M</span><span class="atribut">Leto: <strong>1900</strong></span><span class="atribut">Zemljišèe: <strong>1942 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">880 m2, prostor za storitve, zgrajen l. 1900, adaptiran l. 2015, 1.942 m2 zemljišèa, P/M, delno adaptirano 2015, potrebn...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                880 m2, prostor za storitve, zgrajen l. 1900, adaptiran l. 2015, 1.942 m2 zemljišèa, P/M, delno adaptirano 2015, potrebn...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">880,00 m2</span><br />
                                <span class="cena">190.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Rebernik nepremiènine, Samo Rebernik s.p."><div class="logo"><a href="/oglasi-prodaja/senozece-center-poslovni-prostor_6038063/"><img src="https://picbase.turbosist.si/slonep_agenc120/506.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="6038063"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-6038063" href="#" data-id="6038063" onclick="save_ad(6038063); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsenozece-center-poslovni-prostor_6038063%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsenozece-center-poslovni-prostor_6038063%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsenozece-center-poslovni-prostor_6038063%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsenozece-center-poslovni-prostor_6038063%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="6038063"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsenozece-center-poslovni-prostor_6038063%2F" class="utility" data-id="6038063"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/senozece-center-poslovni-prostor_6038063/" class="utility contact-tooltip" title="041/714-830<br />Rebernik nepremiènine, Samo Rebernik s.p."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                <div class="midad shadow">
                <script type='text/javascript'><!--//<![CDATA[
                 var m3_u = (location.protocol=='https:'?'https://ok.internetmedia.si/www/delivery/ajs.php':'https://ok.internetmedia.si/www/delivery/ajs.php');
                 var m3_r = Math.floor(Math.random()*99999999999);
                 if (!document.MAX_used) document.MAX_used = ',';
                 document.write ("<scr"+"ipt type='text/javascript' src='"+m3_u);
                 document.write ("?zoneid=5&amp;target=_blank&amp;block=1&amp;blockcampaign=1 . &amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5= . ");
                 document.write ('&amp;cb=' + m3_r);
                 if (document.MAX_used != ',') document.write ("&amp;exclude=" + document.MAX_used);
                 document.write (document.charset ? '&amp;charset='+document.charset : (document.characterSet ? '&amp;charset='+document.characterSet : ''));
                 document.write ("&amp;loc=" + escape(window.location));
                 if (document.referrer) document.write ("&amp;referer=" + escape(document.referrer));
                 if (document.context) document.write ("&context=" + escape(document.context));
                 if (document.mmm_fo) document.write ("&amp;mmm_fo=1");
                 document.write ("'><\/scr"+"ipt>");
            //]]>--></script><noscript><a href='https://ok.internetmedia.si/www/delivery/ck.php?n=a280490d&amp;cb=215023799&amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5=' target='_blank'><img src='https://ok.internetmedia.si/www/delivery/avw.php?zoneid=5&amp;cb=275337610&amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5=&amp;n=a280490d' border='0' alt='' /></a></noscript>
                </div>
            
                    <div class="oglas_container oglasbold oglas864" id="o5744586">
                        <h2><a href="/oglasi-prodaja/krtina-izjemno-lepa-lokacija-3km-od-ac-hisa_5744586/" title="5744586"><span class="title">KRTINA, IZJEMNO LEPA LOKACIJA, 3KM OD AC</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/krtina-izjemno-lepa-lokacija-3km-od-ac-hisa_5744586/"><img src="https://picbase.turbosist.si/slonep_oglasi2/2695927.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hiša</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Leto: <strong>2009</strong></span><span class="atribut">Zemljišèe: <strong>249 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">158 m2, dvojèek, zgrajen l. 2009, 249 m2 zemljišèa, Na izjemno lepi lokaciji se nahaja dvojèek hiše velikosti 157,65mz z...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                158 m2, dvojèek, zgrajen l. 2009, 249 m2 zemljišèa, Na izjemno lepi lokaciji se nahaja dvojèek hiše velikosti 157,65mz z...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">158,00 m2</span><br />
                                <span class="cena">190.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="REMAX Vogal, Nepremièninska družba, d.o.o."><div class="logo"><a href="/oglasi-prodaja/krtina-izjemno-lepa-lokacija-3km-od-ac-hisa_5744586/"><img src="https://picbase.turbosist.si/slonep_agenc120/1297.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5744586"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-5744586" href="#" data-id="5744586" onclick="save_ad(5744586); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkrtina-izjemno-lepa-lokacija-3km-od-ac-hisa_5744586%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkrtina-izjemno-lepa-lokacija-3km-od-ac-hisa_5744586%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkrtina-izjemno-lepa-lokacija-3km-od-ac-hisa_5744586%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkrtina-izjemno-lepa-lokacija-3km-od-ac-hisa_5744586%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="5744586"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkrtina-izjemno-lepa-lokacija-3km-od-ac-hisa_5744586%2F" class="utility" data-id="5744586"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/krtina-izjemno-lepa-lokacija-3km-od-ac-hisa_5744586/" class="utility contact-tooltip" title="070/900-340<br />REMAX Vogal, Nepremièninska družba, d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas830" id="o6036743">
                        <h2><a href="/oglasi-prodaja/krtina-le-3km-od-ac-prikljucka-hisa_6036743/" title="6036743"><span class="title">KRTINA, LE 3KM OD AC PRIKLJUÈKA</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/krtina-le-3km-od-ac-prikljucka-hisa_6036743/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4699287.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hiša</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Nadstropje: <strong>K+P+M</strong></span><span class="atribut">Leto: <strong>2009</strong></span><span class="atribut">Zemljišèe: <strong>249 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">158 m2, dvojèek, zgrajen l. 2009, 249 m2 zemljišèa, K+P+M, Na izjemno lepi mirni lokaciji se prodaja dvojèek hiše veliko...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                158 m2, dvojèek, zgrajen l. 2009, 249 m2 zemljišèa, K+P+M, Na izjemno lepi mirni lokaciji se prodaja dvojèek hiše veliko...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">158,00 m2</span><br />
                                <span class="cena">190.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="REMAX Vogal, Nepremièninska družba, d.o.o."><div class="logo"><a href="/oglasi-prodaja/krtina-le-3km-od-ac-prikljucka-hisa_6036743/"><img src="https://picbase.turbosist.si/slonep_agenc120/1297.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="6036743"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-6036743" href="#" data-id="6036743" onclick="save_ad(6036743); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkrtina-le-3km-od-ac-prikljucka-hisa_6036743%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkrtina-le-3km-od-ac-prikljucka-hisa_6036743%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkrtina-le-3km-od-ac-prikljucka-hisa_6036743%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkrtina-le-3km-od-ac-prikljucka-hisa_6036743%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="6036743"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkrtina-le-3km-od-ac-prikljucka-hisa_6036743%2F" class="utility" data-id="6036743"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/krtina-le-3km-od-ac-prikljucka-hisa_6036743/" class="utility contact-tooltip" title="070/900-340<br />REMAX Vogal, Nepremièninska družba, d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas899" id="o5866562">
                        <h2><a href="/oglasi-prodaja/kozarsce-pri-tolminu-hisa_5866562/" title="5866562"><span class="title">KOZARŠÈE, PRI TOLMINU</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/kozarsce-pri-tolminu-hisa_5866562/"><img src="https://picbase.turbosist.si/slonep_oglasi2/3450573.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hiša</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Leto: <strong>1923</strong></span><span class="atribut">Zemljišèe: <strong>15575 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">215 m2, samostojna, zgrajena l. 1923, adaptirana l. 2009, 15.575 m2 zemljišèa, Hiša z gospodarskim poslopjem na lepi pos...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                215 m2, samostojna, zgrajena l. 1923, adaptirana l. 2009, 15.575 m2 zemljišèa, Hiša z gospodarskim poslopjem na lepi pos...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">215,00 m2</span><br />
                                <span class="cena">190.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="REMAX Vogal, Nepremièninska družba, d.o.o."><div class="logo"><a href="/oglasi-prodaja/kozarsce-pri-tolminu-hisa_5866562/"><img src="https://picbase.turbosist.si/slonep_agenc120/1297.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5866562"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-5866562" href="#" data-id="5866562" onclick="save_ad(5866562); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkozarsce-pri-tolminu-hisa_5866562%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkozarsce-pri-tolminu-hisa_5866562%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkozarsce-pri-tolminu-hisa_5866562%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkozarsce-pri-tolminu-hisa_5866562%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="5866562"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkozarsce-pri-tolminu-hisa_5866562%2F" class="utility" data-id="5866562"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/kozarsce-pri-tolminu-hisa_5866562/" class="utility contact-tooltip" title="030/248-247<br />REMAX Vogal, Nepremièninska družba, d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                </div><div class="spacer"></div><div id="pagination" class="fr"><ul>
                    <li><a href="/oglasi-prodaja/cena-do-200000-eur/?s=13" class="first"><<</a></li>
                    <li><a href="/oglasi-prodaja/cena-do-200000-eur/19/?s=13" class="prev"><</a></li>
                <span class="dots3">...</span><li><a href="/oglasi-prodaja/cena-do-200000-eur/17/?s=13">17</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/18/?s=13">18</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/19/?s=13">19</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/20/?s=13" class="active">20</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/21/?s=13">21</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/22/?s=13">22</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/23/?s=13">23</a></li><span class="dots3">...</span><li><a href="/oglasi-prodaja/cena-do-200000-eur/21/?s=13" class="next">></a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/652/?s=13" class="last">>></a></li></ul></div>
                <div class="clearer"></div>
            </div>
            
                <div class="clearer"></div>
            </div><!-- /980 -->
            <div class="clearer"></div>
        </div>
        <div class="clearer"></div>
    </div>

    <div id="footer-wrapper">
        <div id="footer">
            <div class="fl">
	<div class="block">
		<strong>MEGANET d.o.o. © 1998 - 2016</strong><br />
		Kontakt: 03/567-91-10<br />
		E-pošta: <a href="mailto:info@nepremicnine.net" class="nn">info@nepremicnine.net</a>
	</div>
	<div class="spacer"></div>
	<div class="spacer"></div>
	<div class="block">
		<strong>Tehnièna podpora: </strong><br />
		INTERNET MEDIA d.o.o.<br />
				E-pošta: <a href="mailto:podpora@nepremicnine.net" class="nn">podpora@nepremicnine.net</a>
			</div>
</div>
<div class="block">
	<ul>
		<li><a href="https://www.nepremicnine.net" target="_blank">www.nepremicnine.net</a></li>
		<li><a href="http://www.slonep.net" target="_blank">www.slonep.net</a></li>
		<li><a href="http://www.montazne-hise.net" target="_blank">www.montazne-hise.net</a></li>
		<li><a href="http://www.podsvojostreho.net" target="_blank">www.podsvojostreho.net</a></li>
		<li><a href="http://www.novogradnje.si" target="_blank">www.novogradnje.si</a></li>
		<li><a href="http://www.nepremicninar.com" target="_blank">www.nepremicninar.com</a></li>
		<li class="last"><a href="http://www.samsvojmajstor.com" target="_blank">www.samsvojmajstor.com</a></li>
	</ul>
</div>
<div class="fl">
	<div class="block">
		<ul>
			<li><a href="/nepremicnine-rubrike.html"><strong>Rubrike oglasov</strong></a></li>
			<li><a href="/nepremicnine.html?q=menjava nepremiènine" title="menjava nepremiènine"><strong>Menjava nepremiènine</strong></a></li>
			<li><a href="/pravno-pojasnilo.html">Pravno pojasnilo</a></li>
			<li><a href="/nepremicnine-oglasevanje.html">Oglaševanje</a></li>
			<li><a href="/cookies.html">O piškotkih</a></li>
			<li class="last"><a href="/pomoc-in-svetovanje.html">Pomoè</a></li>		</ul>
	</div>
</div>

<div class="fr tac">
	<!--<div class="obisk">
		<script type="text/javascript" src="https://www.obisk.net/obisk/top.js"></script><script type="text/javascript">obisk(119,"g")</script>
	</div>-->
</div>
        </div>
        <div class="clearer"></div>
    </div>
    </div>
    <script type="text/javascript">
    $(".web-opis a").attr('target', '_blank');

    </script>
</body>



</html>



