<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "https://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="https://www.w3.org/1999/xhtml" lang="sl">
<head>
<link rel="canonical" href="/oglasi-prodaja/ljubljana-mesto/stanovanje/cena-do-200000-eur/16/" /><meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta http-equiv="content-language" content="sl" />
<meta name="msvalidate.01" content="D9C9544A6631C60218BF47FD618F42E5" />

<meta http-equiv="X-UA-Compatible" content="IE=EDGE" />
<meta name="SKYPE_TOOLBAR" content="SKYPE_TOOLBAR_PARSER_COMPATIBLE" />
<meta name="format-detection" content="telephone=no">
<title>Prodaja </title>
<meta name="Keywords" content="" />
<meta name="Description" content="Rezultati iskanja nepremi�nin: Prodaja  na Nepremicnine.net" />
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
                    $("#toperr").css("display", "block").append('<div class="msgE">Nimate omogo�enih pi�kotkov (cookies). Uporaba je omejena.</div>')
                },
                success: function(data){
                    if (data != '') {
                        //$("#nocookie div").removeClass('msgE').addClass('msgI');
                        //$("#nocookie div").replaceWith('<div class="msgI">Pozdravljeni na strani Nepremicnine.net.</div>')
                    } else {
                        $("#toperr").css("display", "block").append('<div class="msgE">Nimate omogo�enih pi�kotkov (cookies). Uporaba je omejena.</div>')
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
            $('#notification-message a').webuiPopover({title:'<i class="fa fa-envelope"></i> &nbsp; Sporo�ila',content:'Content',width:250,height:200,placement:'bottom-left',type:'async',url:'/jq/popover_messages.php',cache:false,closeable:true});

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
                <li><a href="http://www.montazne-hise.net" target="_blank">monta�ne hi�e</a></li>
                <li><a href="http://www.podsvojostreho.net" target="_blank">pod<span class="svojo">svojo</span>streho.net</a></li>
                <li><a href="http://www.novogradnje.si" target="_blank">novogradnje.si</a></li>
                <!--<li><a href="http://www.nepremicninar.com" target="_blank">nepremicninar.com</a></li>-->
                                                <li><a class="lang" href="http://www.realestate-slovenia.info/">
                                        <img src="/images/vector-flags/gb.svg" style="height: 18px;">
                                    </a></li>
                                <li><!--<a class="last" href="http://www.facebook.com/pages/NEPREMICNINEnet/181757358510072" target="_blank" title="NEPREMICNINE.net na Facebook-u"><img src="/images/ikona-fb.png" alt="Nepremicnine.net FB" /></a>-->
                    <div class="fb-like" data-href="https://www.facebook.com/NEPREMICNINEnet-181757358510072/" data-colorscheme="light" data-layout="button_count" data-action="like" data-show-faces="false" data-share="false"></div>
                </li>
                <!--<li><a href="/profil.html?m=so&s=37" class="blink last">SPORO�ILO</a></li>-->
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
        <p class="slide"><a href="/profil.html" name="moje-nep" class="btn-slide">Moje nepremi�nine</a></p>            </div>
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
<iframe id='a4e1c538' name='a4e1c538' src='https://ok.internetmedia.si/www/delivery/afr.php?zoneid=1&amp;target=_blank&amp;charset=UTF-8&amp;cb=1301044753&amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5=' frameborder='0' scrolling='no' width='960' height='150'><a href='https://ok.internetmedia.si/www/delivery/ck.php?n=a0fcbf0c&amp;cb=737983567&amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5=' target='_blank'><img src='https://ok.internetmedia.si/www/delivery/avw.php?zoneid=1&amp;charset=UTF-8&amp;cb=1809497812&amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5=&amp;n=a0fcbf0c' border='0' alt='' /></a></iframe>
            </div></div>
        <div class="clearer"></div>

        <div id="content">
                        <div id="header-top">
                                <div id="logo">
                    <a href="/"><img src="/images/logo.gif" width="297" height="37" title="Nepremi�nine, sredi��e ponudbe nepremi�nin v Sloveniji, agencije za nepremi�nine, novogradnje..." alt="Nepremi�nine, sredi��e ponudbe nepremi�nin v Sloveniji, agencije za posredovanje nepremi�nin, novogradnje..." />
                    <strong>Najve�ji slovenski nepremi�ninski portal</strong></a>
                </div>
                <div id="slogan"></div>
                <div id="iskalnik-hitroiskanje" class="ui-widget">
                                        <form action="/nepremicnine.html" method="get" name="searcher" accept-charset="utf-8">
                        <input type="text" name="q" id="hitroiskanje" value="" title="npr. hi�a bled atrij, ref. �t. oglasa ..." size="30" maxlength="160" onclick="if (searcher.q.value.substring(0,3) == 'npr') searcher.q.value='';" />
                        <input type="submit" id="hitroiskanjepotrdi" value="" width="31" height="32" onclick="if ( searcher.q.value=='npr. hi�a bled atrij, ref. �t. oglasa ...' ) return false;" />
                    </form>
                </div>
            </div>
            <div id="header">
                <div id="menu">
                    <ul>
                        <li class="first"><a href="/">nepremi�nine</a></li>
                                                <li class="iskalnik">
                            <div class="menuitem"><a href="#" id="fqrun" class="active">ISKALNIK</a></div>
                            <ul>
	<li>
		<div class="levo">
						<form name="NOsearch" id="NOsearch" action="/nepremicnine.html" class="" method="get">
				<div id="loading">Loading ...</div>
				<table width="350" border="0" cellpadding="3" cellspacing="0">
					<tr>
						<td class="td-levo"><strong>Dr�ava</strong></td>
						<td class="td-desno">
							<input type="radio" class="radio" id="NOd197" name="d" value="197" checked="checked">
							<label for="NOd197" class="radio">Slovenija</label>
							<input type="radio" class="radio" id="NOd55" name="d" value="55" >
							<label for="NOd55" class="radio">Hrva�ka</label>
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
						<td class="td-levo"><strong>Nepremi�nina</strong></td>
						<td class="td-desno">
														<select name="n" id="NOn">
								<option value="1">Stanovanje</option><option value="2">Hi�a</option><option value="4">Vikend</option><option value="3">Posest</option><option value="5">Poslovni prostor</option><option value="6">Gara�a</option><option value="7">Po�itni�ki objekt</option>								</select>
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
							<!--<input type="submit" id="NOsubmit" class="gumb potrdi" value="Prika�i rezultate" />-->
							<a  class="gumb potrdi" href="/oglasi-prodaja/ljubljana-mesto/stanovanje/">Prika�i rezultate</a>
						</td>
					</tr>
				</table>
			</form>
		</div>
		<ul class="desno">
			<li><a href="/ne-spreglejte.html" class="isk-nespreglejte">ne spreglejte</a></li>
			<li><a href="/24ur.html" class="isk-v24ur">24 ur</a></li>
			<li><a href="/znizane-cene.html" class="isk-znizano">zni�ane cene</a></li>
					<li><a href="/nepremicnine-vpis.html?v=1" class="isk-vpis">vpis oglasa</a></li>
			<li><a href="/infonep.html" class="isk-obv">obve��ajte me</a></li>
					<li><a href="/profil.html?m=si" class="isk-si">shranjena iskanja</a></li>
			<li><a href="/profil.html?m=so" class="isk-so">shranjeni oglasi</a></li>
			<li><a href="/javne-drazbe.html" class="isk-jd">javne dra�be</a></li>
			<li><a href="/za-studente.html" class="isk-stu">za �tudente</a></li>
		</ul>
	</li>
</ul>
                        </li>
                        <li class="nav-novogradnje"><a href="/novogradnje.html">Novogradnje</a></li><li class="nav-javne-drazbe"><a href="/javne-drazbe.html">Javne dra�be</a></li><li class="nav-montazne-hise"><a href="/montazne-hise.html">Monta�ne hi�e</a></li><li class="nav-pocitniski-objekti"><a href="/pocitniski-objekti.html">Na po�itnice!</a></li><li class="nav-dom-in-gradnja"><a href="/dom-in-gradnja.html">Dom in gradnja</a></li><li class="nav-nepremicninske-agencije"><a href="/nepremicninske-agencije.html">Podjetja</a></li><li class="nav-energetska-izkaznica"><a href="/energetska-izkaznica.html">E. izkaznica</a></li><li class="nav-trendi"><a href="/trendi.html">Trendi</a></li>                    </ul>
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
                    //data: "wpg=nepremicnine&p=1&arg[]=ljubljana-mesto&arg[]=stanovanje&arg[]=cena-do-200000-eur&pg=16&s=13&uid=", // data to send to above script page if any
                    data: "wpg=nepremicnine&p=1&arg%5B0%5D=ljubljana-mesto&arg%5B1%5D=stanovanje&arg%5B2%5D=cena-do-200000-eur&pg=16&s=13&c2=200000&uid=", // data to send to above script page if any
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
        �t. ustreznih oglasov: <strong>19532</strong><br />    <!--<form action="/nepremicnine.html" method="get" id="sform" name="sform" accept-charset="utf-8">-->
        <form action="/jq/search.php?wpg=nepremicnine&red=1" method="post" id="sform" name="sform" accept-charset="utf-8">
        
                    <a name=""></a><h3>+ Klju�ne besede</h3>
                    <input type="text" name="q" id="q" class="mini" style="width:185px; float: left;" value="" size="30" maxlength="60">
                    <input type="submit" class="fsearch" value=">" /><br />
                <a name=""></a><h3>Osnovni parametri</h3><select name="d" id="dd" class="invisible" onchange="sform.submit()"><option value="0">Vse dr�ave</option><option value="197">Slovenija</option><option value="55">Hrva�ka</option><option value="999">Ostale</option></select><div class="dropdownWrapper">
                          <div class="dropdownLabel">Vse dr�ave<i class="fa fa-caret-down" aria-hidden="true"></i></div>
                          <div class="dropdownPanel">
                            <a href="/oglasi-prodaja/cena-do-200000-eur/?s=13">Vse dr�ave</a><a href="/oglasi-prodaja/slovenija/cena-do-200000-eur/?s=13">Slovenija</a><a href="/oglasi-prodaja/hrvaska/cena-do-200000-eur/?s=13">Hrva�ka</a><a href="/oglasi-prodaja/ostale-drzave/cena-do-200000-eur/?s=13">Ostale</a>
                          </div>
                        </div>
        <select name="n" id="n" class="invisible" onchange="sform.submit()"><option value="0">Vse nepremi�nine</option><option value="1">Stanovanje</option><option value="2">Hi�a</option><option value="4">Vikend</option><option value="3">Posest</option><option value="5">Poslovni prostor</option><option value="6">Gara�a</option><option value="7">Po�itni�ki objekt</option></select><div class="dropdownWrapper">
                          <div class="dropdownLabel">Vse nepremi�nine<i class="fa fa-caret-down" aria-hidden="true"></i></div>
                          <div class="dropdownPanel">
                            <a href="/oglasi-prodaja/cena-do-200000-eur/?s=13">Vse nepremi�nine</a><a href="/oglasi-prodaja/stanovanje/cena-do-200000-eur/?s=13">Stanovanje</a><a href="/oglasi-prodaja/hisa/cena-do-200000-eur/?s=13">Hi�a</a><a href="/oglasi-prodaja/vikend/cena-do-200000-eur/?s=13">Vikend</a><a href="/oglasi-prodaja/posest/cena-do-200000-eur/?s=13">Posest</a><a href="/oglasi-prodaja/poslovni-prostor/cena-do-200000-eur/?s=13">Poslovni prostor</a><a href="/oglasi-prodaja/garaza/cena-do-200000-eur/?s=13">Gara�a</a><a href="/oglasi-prodaja/pocitniski-objekt/cena-do-200000-eur/?s=13">Po�itni�ki objekt</a>
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
                <a name="M2"></a><h3>Velikost (m2)</h3><ul id="facetM2"><li><a href="/oglasi-prodaja/cena-do-200000-eur,velikost-do-2000-m2/?s=13"><div class="cnt">[17928]</div><span class="fnum">do </span>&nbsp;<span class="fnum">2.000</span></a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur,velikost-od-2000-do-4000-m2/?s=13"><div class="cnt">[761]</div><span class="fnum">2.000</span>&nbsp;<span class="fnum">-&nbsp;4.000</span></a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur,velikost-od-4000-do-6000-m2/?s=13"><div class="cnt">[251]</div><span class="fnum">4.000</span>&nbsp;<span class="fnum">-&nbsp;6.000</span></a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur,velikost-od-6000-do-8000-m2/?s=13"><div class="cnt">[131]</div><span class="fnum">6.000</span>&nbsp;<span class="fnum">-&nbsp;8.000</span></a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur,velikost-od-8000-do-10000-m2/?s=13"><div class="cnt">[95]</div><span class="fnum">8.000</span>&nbsp;<span class="fnum">-&nbsp;10.000</span></a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur,velikost-od-10000-m2/?s=13"><div class="cnt">[429]</div><span class="fnum">10.000</span>&nbsp; in ve�</a></li></ul>
                    <div class="more">
                        <div>vnesite poljubno vrednost</div>
                        <input type="text" class="mini intnum" size="10" maxlength="10" name="m1" onchange="CheckCurrency(document.sform.m1,'m1')" value="">
                        -
                        <input type="text" class="mini intnum" size="10" maxlength="10" name="m2" onchange="CheckCurrency(document.sform.m2,'m2')" value="">
                        m2
                        <input type="submit" class="fsearch" value=">" />
                    </div>
                <a name="leto"></a><h3>Leto</h3><ul><li><a href="/oglasi-prodaja/cena-do-200000-eur,letnik-do-1949/?s=13"><div class="cnt">[7782]</div>do  - 1949</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur,letnik-od-1950-do-1959/?s=13"><div class="cnt">[579]</div>1950 - 1959</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur,letnik-od-1960-do-1969/?s=13"><div class="cnt">[1211]</div>1960 - 1969</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur,letnik-od-1970-do-1979/?s=13"><div class="cnt">[1436]</div>1970 - 1979</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur,letnik-od-1980-do-1989/?s=13"><div class="cnt">[1834]</div>1980 - 1989</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur,letnik-od-1990-do-1999/?s=13"><div class="cnt">[1416]</div>1990 - 1999</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur,letnik-od-2000-do-2009/?s=13"><div class="cnt">[2873]</div>2000 - 2009</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur,letnik-od-2010-do-2014/?s=13"><div class="cnt">[1649]</div>2010 - 2014</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur,letnik-od-2015/?s=13"><div class="cnt">[752]</div>2015 in ve�</a></li></ul>
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
        <div class="spacer"></div><div><input type="checkbox" name="f" id="f1" option value="1" onchange="sform.submit()">Zni�ane cene</div><hr/><div class="grey tac">Povpre�na cena najdenih oglasov: <strong>900,09 EUR/m2</strong><br/></div>    </form>
</div></div><div id="vsebina760">
                <div class="headbar"><div id="pagination" class="top fr"><ul>
                    <li><a href="/oglasi-prodaja/cena-do-200000-eur/?s=13" class="first"><<</a></li>
                    <li><a href="/oglasi-prodaja/cena-do-200000-eur/15/?s=13" class="prev"><</a></li>
                <span class="dots3">...</span><li><a href="/oglasi-prodaja/cena-do-200000-eur/13/?s=13">13</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/14/?s=13">14</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/15/?s=13">15</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/16/?s=13" class="active">16</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/17/?s=13">17</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/18/?s=13">18</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/19/?s=13">19</a></li><span class="dots3">...</span><li><a href="/oglasi-prodaja/cena-do-200000-eur/17/?s=13" class="next">></a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/652/?s=13" class="last">>></a></li></ul></div><h1>Prodaja </h1><div class="sort cb">
                    <div class="fl">
                    <strong>Razvrsti:</strong> <a href="/oglasi-prodaja/ljubljana-mesto/stanovanje/cena-do-200000-eur/16/?s=1" class="up">lokacija</a> | <a href="/oglasi-prodaja/ljubljana-mesto/stanovanje/cena-do-200000-eur/16/?s=11" class="down">lokacija</a> | <a href="/oglasi-prodaja/ljubljana-mesto/stanovanje/cena-do-200000-eur/16/?s=3" class="up">cena</a> | <a href="/oglasi-prodaja/ljubljana-mesto/stanovanje/cena-do-200000-eur/16/?s=13" class="down act">cena</a> | <a href="/oglasi-prodaja/ljubljana-mesto/stanovanje/cena-do-200000-eur/16/?s=4" class="up">m2</a> | <a href="/oglasi-prodaja/ljubljana-mesto/stanovanje/cena-do-200000-eur/16/?s=14" class="down">m2</a> | <a href="/oglasi-prodaja/ljubljana-mesto/stanovanje/cena-do-200000-eur/16/?s=5" class="up">ponudnik</a> | <a href="/oglasi-prodaja/ljubljana-mesto/stanovanje/cena-do-200000-eur/16/?s=16" class="down">datum vpisa</a> | </div><a id="si" href="#" class="fr ibl pf i-si" style="padding-right:0">Shrani iskanje</a><div class="clearer"></div></div>
                    </div><div id="slide-thumb">
				<a href="http://www.nepremicnine.net/novogradnje/novo-naselje-med-lipami-v-mengsu.html" target="_blank" class="pt">
					<table border="0" cellpadding="0" cellspacing="0">
						<tr>
							<td>
								<strong>Menge�</strong>
							</td>
						</tr>
						<tr>
							<td class="slika">
								<div><img src="https://picbase.turbosist.si/adads/thumbnails/1144.jpg" /></div>								
							</td>
						</tr>
						<tr>
							<td><span>Soseska Med lipami</span></td>
						</tr>
					</table>
				</a>
			
				<a href="http://www.nepremicnine.net/novogradnje/med-cesnjami-v-crnucah.html" target="_blank" class="pt">
					<table border="0" cellpadding="0" cellspacing="0">
						<tr>
							<td>
								<strong>Lj. �rnu�e</strong>
							</td>
						</tr>
						<tr>
							<td class="slika">
								<div><img src="https://picbase.turbosist.si/adads/thumbnails/1165.jpg" /></div>								
							</td>
						</tr>
						<tr>
							<td><span>Naselje Med �e�njami</span></td>
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
			
				<a href="http://www.nepremicnine.net/novogradnje/soseska-gaj-preserje.html" target="_blank" class="pt">
					<table border="0" cellpadding="0" cellspacing="0">
						<tr>
							<td>
								<strong>Preserje pri Dom�alah</strong>
							</td>
						</tr>
						<tr>
							<td class="slika">
								<div><img src="https://picbase.turbosist.si/adads/thumbnails/785.jpg" /></div>								
							</td>
						</tr>
						<tr>
							<td><span>Soseska Gaj Preserje</span></td>
						</tr>
					</table>
				</a>
			<div class="clearer"></div></div>
<div class="seznam">
                    <div class="oglas_container oglasbold oglas219" id="o6017780">
                        <h2><a href="/oglasi-prodaja/brezovica-pri-ljubljani-log-stanovanje_6017780/" title="6017780"><span class="title">BREZOVICA PRI LJUBLJANI, LOG</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/brezovica-pri-ljubljani-log-stanovanje_6017780/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4540587.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Stanovanje</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Leto: <strong>2015</strong></span><span class="atribut">Zemlji��e: <strong>316 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">161 m2, 4,5-sobno, zgrajeno l. 2015, 316 m2 zemlji��a, polovica dvoj�ka (hi�a-dvoj�ek), gara�a, dodatna parkirna mesta p...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                161 m2, 4,5-sobno, zgrajeno l. 2015, 316 m2 zemlji��a, polovica dvoj�ka (hi�a-dvoj�ek), gara�a, dodatna parkirna mesta p...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">161,00 m2</span><br />
                                <span class="cena">195.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="HIP KA d.o.o."><div class="logo"><a href="/oglasi-prodaja/brezovica-pri-ljubljani-log-stanovanje_6017780/"><img src="https://picbase.turbosist.si/slonep_agenc120/1559.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="6017780"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-6017780" href="#" data-id="6017780" onclick="save_ad(6017780); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fbrezovica-pri-ljubljani-log-stanovanje_6017780%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fbrezovica-pri-ljubljani-log-stanovanje_6017780%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fbrezovica-pri-ljubljani-log-stanovanje_6017780%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fbrezovica-pri-ljubljani-log-stanovanje_6017780%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="6017780"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fbrezovica-pri-ljubljani-log-stanovanje_6017780%2F" class="utility" data-id="6017780"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po�lji prijatelju</span></a>
                            <a href="/oglasi-prodaja/brezovica-pri-ljubljani-log-stanovanje_6017780/" class="utility contact-tooltip" title="01/436-20-83<br />HIP KA d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas191" id="o6037663">
                        <h2><a href="/oglasi-prodaja/kranj-strazisce-hisa_6037663/" title="6037663"><span class="title">KRANJ, STRA�I��E</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/kranj-strazisce-hisa_6037663/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4707292.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hi�a</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Leto: <strong>1960</strong></span><span class="atribut">Zemlji��e: <strong>628 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">136 m2, samostojna, zgrajena l. 1960, adaptirana l. 2009, 628 m2 zemlji��a, na lepi lokaciji, v Stra�i��u prodamo enodru...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                136 m2, samostojna, zgrajena l. 1960, adaptirana l. 2009, 628 m2 zemlji��a, na lepi lokaciji, v Stra�i��u prodamo enodru...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">136,00 m2</span><br />
                                <span class="cena">195.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="JUR-TAN nepremi�nine d.o.o., PE �abnica"><div class="logo"><a href="/oglasi-prodaja/kranj-strazisce-hisa_6037663/"><img src="https://picbase.turbosist.si/slonep_agenc120/262.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="6037663"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-6037663" href="#" data-id="6037663" onclick="save_ad(6037663); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkranj-strazisce-hisa_6037663%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkranj-strazisce-hisa_6037663%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkranj-strazisce-hisa_6037663%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkranj-strazisce-hisa_6037663%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="6037663"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkranj-strazisce-hisa_6037663%2F" class="utility" data-id="6037663"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po�lji prijatelju</span></a>
                            <a href="/oglasi-prodaja/kranj-strazisce-hisa_6037663/" class="utility contact-tooltip" title="041/451-857<br />JUR-TAN nepremi�nine d.o.o., PE �abnica"><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas593" id="o6000262">
                        <h2><a href="/oglasi-prodaja/visnja-gora-kriska-vas-hisa_6000262/" title="6000262"><span class="title">VI�NJA GORA, KRI�KA VAS</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/visnja-gora-kriska-vas-hisa_6000262/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4401058.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hi�a</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Nadstropje: <strong>K+P+M</strong></span><span class="atribut">Leto: <strong>2011</strong></span><span class="atribut">Zemlji��e: <strong>500 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">180 m2, samostojna, zgrajena l. 2011, 500 m2 zemlji��a, K+P+M, V Kri�ki vasi prodamo samostojno hi�o v izmeri 180 m2, pa...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                180 m2, samostojna, zgrajena l. 2011, 500 m2 zemlji��a, K+P+M, V Kri�ki vasi prodamo samostojno hi�o v izmeri 180 m2, pa...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">180,00 m2</span><br />
                                <span class="cena">195.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Miklji�-Hribar Company d.o.o."><div class="logo"><a href="/oglasi-prodaja/visnja-gora-kriska-vas-hisa_6000262/"><img src="https://picbase.turbosist.si/slonep_agenc120/868.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="6000262"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-6000262" href="#" data-id="6000262" onclick="save_ad(6000262); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fvisnja-gora-kriska-vas-hisa_6000262%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fvisnja-gora-kriska-vas-hisa_6000262%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fvisnja-gora-kriska-vas-hisa_6000262%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fvisnja-gora-kriska-vas-hisa_6000262%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="6000262"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fvisnja-gora-kriska-vas-hisa_6000262%2F" class="utility" data-id="6000262"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po�lji prijatelju</span></a>
                            <a href="/oglasi-prodaja/visnja-gora-kriska-vas-hisa_6000262/" class="utility contact-tooltip" title="041/359-265<br />Miklji�-Hribar Company d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
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
            //]]>--></script><noscript><a href='https://ok.internetmedia.si/www/delivery/ck.php?n=a280490d&amp;cb=510364512&amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5=' target='_blank'><img src='https://ok.internetmedia.si/www/delivery/avw.php?zoneid=5&amp;cb=678157858&amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5=&amp;n=a280490d' border='0' alt='' /></a></noscript>
                </div>
            
                    <div class="oglas_container oglasbold oglas625" id="o5970365">
                        <h2><a href="/oglasi-prodaja/trbovlje-hisa_5970365/" title="5970365"><span class="title">TRBOVLJE</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/trbovlje-hisa_5970365/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4175055.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hi�a</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Leto: <strong>1970</strong></span><span class="atribut">Zemlji��e: <strong>694 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">220 m2, samostojna, zgrajena l. 1970, adaptirana l. 2008, 694 m2 zemlji��a, V zgormjem delu centra Trbovelj, na lepi lok...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                220 m2, samostojna, zgrajena l. 1970, adaptirana l. 2008, 694 m2 zemlji��a, V zgormjem delu centra Trbovelj, na lepi lok...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">220,00 m2</span><br />
                                <span class="cena">195.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="NeSta d.o.o."><div class="logo"><a href="/oglasi-prodaja/trbovlje-hisa_5970365/"><img src="https://picbase.turbosist.si/slonep_agenc120/199.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5970365"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-5970365" href="#" data-id="5970365" onclick="save_ad(5970365); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Ftrbovlje-hisa_5970365%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Ftrbovlje-hisa_5970365%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Ftrbovlje-hisa_5970365%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Ftrbovlje-hisa_5970365%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="5970365"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Ftrbovlje-hisa_5970365%2F" class="utility" data-id="5970365"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po�lji prijatelju</span></a>
                            <a href="/oglasi-prodaja/trbovlje-hisa_5970365/" class="utility contact-tooltip" title="01/898-11-56<br />NeSta d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas15" id="o6047596">
                        <h2><a href="/oglasi-prodaja/novo-mesto-2-km-od-centra-mesta-hisa_6047596/" title="6047596"><span class="title">NOVO MESTO, 2 KM OD CENTRA MESTA</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/novo-mesto-2-km-od-centra-mesta-hisa_6047596/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4792034.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hi�a</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Leto: <strong>2016</strong></span><span class="atribut">Zemlji��e: <strong>503 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">155 m2, samostojna, zgrajena l. 2016, 503 m2 zemlji��a, nizko energijska hi�a v urejenem naselju, zgrajena do 3. podalj�...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                155 m2, samostojna, zgrajena l. 2016, 503 m2 zemlji��a, nizko energijska hi�a v urejenem naselju, zgrajena do 3. podalj�...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">155,00 m2</span><br />
                                <span class="cena">195.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Kvadrat nepremi�nine d.o.o."><div class="logo"><a href="/oglasi-prodaja/novo-mesto-2-km-od-centra-mesta-hisa_6047596/"><img src="/images/ponudba-podjetja.png" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="6047596"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-6047596" href="#" data-id="6047596" onclick="save_ad(6047596); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fnovo-mesto-2-km-od-centra-mesta-hisa_6047596%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fnovo-mesto-2-km-od-centra-mesta-hisa_6047596%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fnovo-mesto-2-km-od-centra-mesta-hisa_6047596%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fnovo-mesto-2-km-od-centra-mesta-hisa_6047596%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="6047596"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fnovo-mesto-2-km-od-centra-mesta-hisa_6047596%2F" class="utility" data-id="6047596"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po�lji prijatelju</span></a>
                            <a href="/oglasi-prodaja/novo-mesto-2-km-od-centra-mesta-hisa_6047596/" class="utility contact-tooltip" title="07/337-50-03<br />Kvadrat nepremi�nine d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas365" id="o6048256">
                        <h2><a href="/oglasi-prodaja/lj-moste-malo-trebeljevo-prezganje-hisa_6048256/" title="6048256"><span class="title">LJ. MOSTE, MALO TREBELJEVO, PRE�GANJE</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/lj-moste-malo-trebeljevo-prezganje-hisa_6048256/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4796316.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hi�a<span class="new-label">novo</span></span>
                            <!--<div class="new-container">
                            <div class="new sl"><i class="fa fa-certificate"></i><span>novo</span></div>
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Nadstropje: <strong>K+P+1</strong></span><span class="atribut">Leto: <strong>1985</strong></span><span class="atribut">Zemlji��e: <strong>889 m2</strong></span>
                            </div>
                            <!--<div class="new sl"><i class="fa fa-certificate"></i><span>novo</span></div>-->
                            

                            <div class="kratek_container">
                                <div class="kratek">150 m2, samostojna, zgrajena l. 1985, 889 m2 zemlji��a, K+P+1, prodamo. Cena: 195.000,00 EUR</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                150 m2, samostojna, zgrajena l. 1985, 889 m2 zemlji��a, K+P+1, prodamo. Cena: 195.000,00 EUR
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">150,00 m2</span><br />
                                <span class="cena">195.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Visa d.o.o., Ljubljana"><div class="logo"><a href="/oglasi-prodaja/lj-moste-malo-trebeljevo-prezganje-hisa_6048256/"><img src="https://picbase.turbosist.si/slonep_agenc120/436.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="6048256"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-6048256" href="#" data-id="6048256" onclick="save_ad(6048256); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-moste-malo-trebeljevo-prezganje-hisa_6048256%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-moste-malo-trebeljevo-prezganje-hisa_6048256%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-moste-malo-trebeljevo-prezganje-hisa_6048256%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-moste-malo-trebeljevo-prezganje-hisa_6048256%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="6048256"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-moste-malo-trebeljevo-prezganje-hisa_6048256%2F" class="utility" data-id="6048256"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po�lji prijatelju</span></a>
                            <a href="/oglasi-prodaja/lj-moste-malo-trebeljevo-prezganje-hisa_6048256/" class="utility contact-tooltip" title="040/900-101<br />Visa d.o.o., Ljubljana"><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas622" id="o5981240">
                        <h2><a href="/oglasi-prodaja/crna-gora-bar-pecurica-hisa_5981240/" title="5981240"><span class="title">�RNA GORA, BAR, PE�URICA</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/crna-gora-bar-pecurica-hisa_5981240/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4255739.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hi�a</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Leto: <strong>2015</strong></span><span class="atribut">Zemlji��e: <strong>200 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">152 m2, samostojna, zgrajena l. 2015, 200 m2 zemlji��a, nedale� iz bara, �rna gora, prodamo samostojno hi�o v dveh eta�a...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                152 m2, samostojna, zgrajena l. 2015, 200 m2 zemlji��a, nedale� iz bara, �rna gora, prodamo samostojno hi�o v dveh eta�a...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">152,00 m2</span><br />
                                <span class="cena">195.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="�ardi&Co. nepremi�nine, dru�ba za posredovanje v prometu z nepremi�ninami, d.o.o."><div class="logo"><a href="/oglasi-prodaja/crna-gora-bar-pecurica-hisa_5981240/"><img src="https://picbase.turbosist.si/slonep_agenc120/1733.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5981240"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-5981240" href="#" data-id="5981240" onclick="save_ad(5981240); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fcrna-gora-bar-pecurica-hisa_5981240%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fcrna-gora-bar-pecurica-hisa_5981240%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fcrna-gora-bar-pecurica-hisa_5981240%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fcrna-gora-bar-pecurica-hisa_5981240%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="5981240"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fcrna-gora-bar-pecurica-hisa_5981240%2F" class="utility" data-id="5981240"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po�lji prijatelju</span></a>
                            <a href="/oglasi-prodaja/crna-gora-bar-pecurica-hisa_5981240/" class="utility contact-tooltip" title="041/477-795<br />�ardi&Co. nepremi�nine, dru�ba za posredovanje v prometu z nepremi�ninami, d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas958" id="o5937993">
                        <h2><a href="/oglasi-prodaja/kranjska-gora-gozd-martuljek-hisa_5937993/" title="5937993"><span class="title">KRANJSKA GORA, GOZD MARTULJEK</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/kranjska-gora-gozd-martuljek-hisa_5937993/"><img src="https://picbase.turbosist.si/slonep_oglasi2/3948148.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hi�a</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Nadstropje: <strong>P+1+M</strong></span><span class="atribut">Leto: <strong>1990</strong></span><span class="atribut">Zemlji��e: <strong>821 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">198 m2, dvoj�ek, zgrajen l. 1990, 821 m2 zemlji��a, P+1+M, v staro me��anskem stilu, zelo prijetno opremljena, prostorna...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                198 m2, dvoj�ek, zgrajen l. 1990, 821 m2 zemlji��a, P+1+M, v staro me��anskem stilu, zelo prijetno opremljena, prostorna...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">198,00 m2</span><br />
                                <span class="cena">195.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Ceres nepremi�nine d.o.o."><div class="logo"><a href="/oglasi-prodaja/kranjska-gora-gozd-martuljek-hisa_5937993/"><img src="https://picbase.turbosist.si/slonep_agenc120/244.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5937993"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-5937993" href="#" data-id="5937993" onclick="save_ad(5937993); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkranjska-gora-gozd-martuljek-hisa_5937993%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkranjska-gora-gozd-martuljek-hisa_5937993%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkranjska-gora-gozd-martuljek-hisa_5937993%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkranjska-gora-gozd-martuljek-hisa_5937993%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="5937993"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkranjska-gora-gozd-martuljek-hisa_5937993%2F" class="utility" data-id="5937993"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po�lji prijatelju</span></a>
                            <a href="/oglasi-prodaja/kranjska-gora-gozd-martuljek-hisa_5937993/" class="utility contact-tooltip" title="051/608-030<br />Ceres nepremi�nine d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas927" id="o6003598">
                        <h2><a href="/oglasi-prodaja/kranjska-gora-hisa_6003598/" title="6003598"><span class="title">KRANJSKA GORA</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/kranjska-gora-hisa_6003598/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4427460.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hi�a</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Leto: <strong>1990</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">170 m2, dvostanovanjska, adaptirana l. 1990, adaptirana l. 1990, prodamo. Cena: 195.000,00 EUR</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                170 m2, dvostanovanjska, adaptirana l. 1990, adaptirana l. 1990, prodamo. Cena: 195.000,00 EUR
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">170,00 m2</span><br />
                                <span class="cena">195.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="INF-ING d.o.o."><div class="logo"><a href="/oglasi-prodaja/kranjska-gora-hisa_6003598/"><img src="/images/ponudba-podjetja.png" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="6003598"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-6003598" href="#" data-id="6003598" onclick="save_ad(6003598); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkranjska-gora-hisa_6003598%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkranjska-gora-hisa_6003598%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkranjska-gora-hisa_6003598%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkranjska-gora-hisa_6003598%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="6003598"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkranjska-gora-hisa_6003598%2F" class="utility" data-id="6003598"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po�lji prijatelju</span></a>
                            <a href="/oglasi-prodaja/kranjska-gora-hisa_6003598/" class="utility contact-tooltip" title="041/429-330<br />INF-ING d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
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
            //]]>--></script><noscript><a href='https://ok.internetmedia.si/www/delivery/ck.php?n=a280490d&amp;cb=351933874&amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5=' target='_blank'><img src='https://ok.internetmedia.si/www/delivery/avw.php?zoneid=5&amp;cb=1446182505&amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5=&amp;n=a280490d' border='0' alt='' /></a></noscript>
                </div>
            
                    <div class="oglas_container oglasbold oglas507" id="o5911155">
                        <h2><a href="/oglasi-prodaja/crna-pri-kamniku-kisovec-pocitniski-objekt_5911155/" title="5911155"><span class="title">�RNA PRI KAMNIKU, KISOVEC</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/crna-pri-kamniku-kisovec-pocitniski-objekt_5911155/"><img src="https://picbase.turbosist.si/slonep_oglasi2/3751609.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Po�itni�ki objekt</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Leto: <strong>1950</strong></span><span class="atribut">Zemlji��e: <strong>1800 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">600 m2, ko�a, zgrajena l. 1950, adaptirana l. 2006, 1.800 m2 zemlji��a, planinski dom na odli�ni dobro obiskani lokaciji...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                600 m2, ko�a, zgrajena l. 1950, adaptirana l. 2006, 1.800 m2 zemlji��a, planinski dom na odli�ni dobro obiskani lokaciji...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">600,00 m2</span><br />
                                <span class="cena">195.000,00 &euro;<span class="cena-old">230.000,00 &euro;</span><div class="znizano"><i class="fa fa-arrow-circle-down"></i></div></span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="MA - nepremi�ninska dru�ba, Marko Ali� s.p."><div class="logo"><a href="/oglasi-prodaja/crna-pri-kamniku-kisovec-pocitniski-objekt_5911155/"><img src="https://picbase.turbosist.si/slonep_agenc120/171.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5911155"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-5911155" href="#" data-id="5911155" onclick="save_ad(5911155); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fcrna-pri-kamniku-kisovec-pocitniski-objekt_5911155%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fcrna-pri-kamniku-kisovec-pocitniski-objekt_5911155%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fcrna-pri-kamniku-kisovec-pocitniski-objekt_5911155%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fcrna-pri-kamniku-kisovec-pocitniski-objekt_5911155%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="5911155"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fcrna-pri-kamniku-kisovec-pocitniski-objekt_5911155%2F" class="utility" data-id="5911155"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po�lji prijatelju</span></a>
                            <a href="/oglasi-prodaja/crna-pri-kamniku-kisovec-pocitniski-objekt_5911155/" class="utility contact-tooltip" title="041/466-053<br />MA - nepremi�ninska dru�ba, Marko Ali� s.p."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas362" id="o5981645">
                        <h2><a href="/oglasi-prodaja/rudnik-stanovanje_5981645/" title="5981645"><span class="title">RUDNIK</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/rudnik-stanovanje_5981645/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4258822.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Stanovanje</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Nadstropje: <strong>P</strong></span><span class="atribut">Leto: <strong>1910</strong></span><span class="atribut">Zemlji��e: <strong>104 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">73 m2, 3-sobno, zgrajeno l. 1910, adaptirano l. 2013, 104 m2 zemlji��a, pritli�je, Stanovanje v 4 stanovanjski hi�i v bl...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                73 m2, 3-sobno, zgrajeno l. 1910, adaptirano l. 2013, 104 m2 zemlji��a, pritli�je, Stanovanje v 4 stanovanjski hi�i v bl...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">73,00 m2</span><br />
                                <span class="cena">195.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="LJUBLJANA NEPREMI�NINE d.o.o."><div class="logo"><a href="/oglasi-prodaja/rudnik-stanovanje_5981645/"><img src="https://picbase.turbosist.si/slonep_agenc120/242.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5981645"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-5981645" href="#" data-id="5981645" onclick="save_ad(5981645); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Frudnik-stanovanje_5981645%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Frudnik-stanovanje_5981645%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Frudnik-stanovanje_5981645%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Frudnik-stanovanje_5981645%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="5981645"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Frudnik-stanovanje_5981645%2F" class="utility" data-id="5981645"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po�lji prijatelju</span></a>
                            <a href="/oglasi-prodaja/rudnik-stanovanje_5981645/" class="utility contact-tooltip" title="030/253-000<br />LJUBLJANA NEPREMI�NINE d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas196" id="o6049339">
                        <h2><a href="/oglasi-prodaja/koper-blizina-centra-in-sodisca-poslovni-prostor_6049339/" title="6049339"><span class="title">KOPER, BLI�INA CENTRA IN SODI��A</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/koper-blizina-centra-in-sodisca-poslovni-prostor_6049339/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4806573.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Poslovni prostor<span class="new-label">novo</span></span>
                            <!--<div class="new-container">
                            <div class="new sl"><i class="fa fa-certificate"></i><span>novo</span></div>
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Nadstropje: <strong>1</strong></span><span class="atribut">Leto: <strong>1980</strong></span>
                            </div>
                            <!--<div class="new sl"><i class="fa fa-certificate"></i><span>novo</span></div>-->
                            

                            <div class="kratek_container">
                                <div class="kratek">85 m2, pisarna, zgrajena l. 1980, 1. nad., Prodamo pisarni�ke prostore na frekventni lokaciji v neposredni bli�ini centr...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                85 m2, pisarna, zgrajena l. 1980, 1. nad., Prodamo pisarni�ke prostore na frekventni lokaciji v neposredni bli�ini centr...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">85,00 m2</span><br />
                                <span class="cena">195.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Apertura, poslovanje z nepremi�ninami, d.o.o."><div class="logo"><a href="/oglasi-prodaja/koper-blizina-centra-in-sodisca-poslovni-prostor_6049339/"><img src="https://picbase.turbosist.si/slonep_agenc120/86.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="6049339"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-6049339" href="#" data-id="6049339" onclick="save_ad(6049339); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkoper-blizina-centra-in-sodisca-poslovni-prostor_6049339%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkoper-blizina-centra-in-sodisca-poslovni-prostor_6049339%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkoper-blizina-centra-in-sodisca-poslovni-prostor_6049339%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkoper-blizina-centra-in-sodisca-poslovni-prostor_6049339%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="6049339"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkoper-blizina-centra-in-sodisca-poslovni-prostor_6049339%2F" class="utility" data-id="6049339"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po�lji prijatelju</span></a>
                            <a href="/oglasi-prodaja/koper-blizina-centra-in-sodisca-poslovni-prostor_6049339/" class="utility contact-tooltip" title="0590/35-211<br />Apertura, poslovanje z nepremi�ninami, d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas242" id="o5926326">
                        <h2><a href="/oglasi-prodaja/lj-vic-stanovanje_5926326/" title="5926326"><span class="title">LJ. VI�</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/lj-vic-stanovanje_5926326/"><img src="https://picbase.turbosist.si/slonep_oglasi2/3861132.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Stanovanje</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Nadstropje: <strong>2</strong>/2</span><span class="atribut">Leto: <strong>1976</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">140 m2, 4-sobno, zgrajeno l. 1976, adaptirano l. 2005, 2/2 nad., prostorno in popolnoma prenovljeno, na odli�ni lokaciji...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                140 m2, 4-sobno, zgrajeno l. 1976, adaptirano l. 2005, 2/2 nad., prostorno in popolnoma prenovljeno, na odli�ni lokaciji...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">140,00 m2</span><br />
                                <span class="cena">195.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="LJUBLJANA NEPREMI�NINE d.o.o."><div class="logo"><a href="/oglasi-prodaja/lj-vic-stanovanje_5926326/"><img src="https://picbase.turbosist.si/slonep_agenc120/242.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5926326"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-5926326" href="#" data-id="5926326" onclick="save_ad(5926326); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-vic-stanovanje_5926326%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-vic-stanovanje_5926326%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-vic-stanovanje_5926326%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-vic-stanovanje_5926326%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="5926326"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-vic-stanovanje_5926326%2F" class="utility" data-id="5926326"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po�lji prijatelju</span></a>
                            <a href="/oglasi-prodaja/lj-vic-stanovanje_5926326/" class="utility contact-tooltip" title="030/313-004<br />LJUBLJANA NEPREMI�NINE d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas450" id="o5483302">
                        <h2><a href="/oglasi-prodaja/piran-prvomajski-trg-stanovanje_5483302/" title="5483302"><span class="title">PIRAN, PRVOMAJSKI TRG</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/piran-prvomajski-trg-stanovanje_5483302/"><img src="https://picbase.turbosist.si/slonep_oglasi2/1469000.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Stanovanje</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Nadstropje: <strong>3</strong>/M</span><span class="atribut">Leto: <strong>2010</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">73,35 m2, 3-sobno, adaptirano l. 2010, zgrajeno l. 1900, 3/M, atraktivno in svetlo dvoeta�no stanovanje 3. nadstropje in...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                73,35 m2, 3-sobno, adaptirano l. 2010, zgrajeno l. 1900, 3/M, atraktivno in svetlo dvoeta�no stanovanje 3. nadstropje in...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">73,35 m2</span><br />
                                <span class="cena">195.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Casabela d.o.o./s.r.l."><div class="logo"><a href="/oglasi-prodaja/piran-prvomajski-trg-stanovanje_5483302/"><img src="/images/ponudba-podjetja.png" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5483302"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-5483302" href="#" data-id="5483302" onclick="save_ad(5483302); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fpiran-prvomajski-trg-stanovanje_5483302%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fpiran-prvomajski-trg-stanovanje_5483302%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fpiran-prvomajski-trg-stanovanje_5483302%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fpiran-prvomajski-trg-stanovanje_5483302%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="5483302"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fpiran-prvomajski-trg-stanovanje_5483302%2F" class="utility" data-id="5483302"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po�lji prijatelju</span></a>
                            <a href="/oglasi-prodaja/piran-prvomajski-trg-stanovanje_5483302/" class="utility contact-tooltip" title="05/673-02-50<br />Casabela d.o.o./s.r.l."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas440" id="o5828623">
                        <h2><a href="/oglasi-prodaja/radovljica-poslovni-prostor_5828623/" title="5828623"><span class="title">RADOVLJICA</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/radovljica-poslovni-prostor_5828623/"><img src="https://picbase.turbosist.si/slonep_oglasi2/3203062.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Poslovni prostor</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Leto: <strong>1990</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">151,8 m2, gostinski lokal, zgrajen l. 1990, Gostinski prostor v pritli�ju poslovno-stanovanjske stavbe, v obratovanju, p...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                151,8 m2, gostinski lokal, zgrajen l. 1990, Gostinski prostor v pritli�ju poslovno-stanovanjske stavbe, v obratovanju, p...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">151,80 m2</span><br />
                                <span class="cena">195.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="K 3 Kern d.o.o."><div class="logo"><a href="/oglasi-prodaja/radovljica-poslovni-prostor_5828623/"><img src="https://picbase.turbosist.si/slonep_agenc120/887.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5828623"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-5828623" href="#" data-id="5828623" onclick="save_ad(5828623); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fradovljica-poslovni-prostor_5828623%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fradovljica-poslovni-prostor_5828623%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fradovljica-poslovni-prostor_5828623%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fradovljica-poslovni-prostor_5828623%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="5828623"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fradovljica-poslovni-prostor_5828623%2F" class="utility" data-id="5828623"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po�lji prijatelju</span></a>
                            <a href="/oglasi-prodaja/radovljica-poslovni-prostor_5828623/" class="utility contact-tooltip" title="051/320-700<br />K 3 Kern d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
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
            //]]>--></script><noscript><a href='https://ok.internetmedia.si/www/delivery/ck.php?n=a280490d&amp;cb=499379580&amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5=' target='_blank'><img src='https://ok.internetmedia.si/www/delivery/avw.php?zoneid=5&amp;cb=1334812269&amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5=&amp;n=a280490d' border='0' alt='' /></a></noscript>
                </div>
            
                    <div class="oglas_container oglasbold oglas867" id="o5885995">
                        <h2><a href="/oglasi-prodaja/log-pri-brezovici-hisa_5885995/" title="5885995"><span class="title">LOG PRI BREZOVICI</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/log-pri-brezovici-hisa_5885995/"><img src="https://picbase.turbosist.si/slonep_oglasi2/3581962.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hi�a</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Leto: <strong>2007</strong></span><span class="atribut">Zemlji��e: <strong>81 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">221,5 m2, vrstna, zgrajena l. 2007, 81 m2 zemlji��a, prodamo. Cena: 195.000,00 EUR</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                221,5 m2, vrstna, zgrajena l. 2007, 81 m2 zemlji��a, prodamo. Cena: 195.000,00 EUR
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">221,50 m2</span><br />
                                <span class="cena">195.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Nepremi�nine Land d.o.o."><div class="logo"><a href="/oglasi-prodaja/log-pri-brezovici-hisa_5885995/"><img src="https://picbase.turbosist.si/slonep_agenc120/891.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5885995"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-5885995" href="#" data-id="5885995" onclick="save_ad(5885995); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flog-pri-brezovici-hisa_5885995%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flog-pri-brezovici-hisa_5885995%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flog-pri-brezovici-hisa_5885995%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flog-pri-brezovici-hisa_5885995%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="5885995"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flog-pri-brezovici-hisa_5885995%2F" class="utility" data-id="5885995"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po�lji prijatelju</span></a>
                            <a href="/oglasi-prodaja/log-pri-brezovici-hisa_5885995/" class="utility contact-tooltip" title="051/833-000<br />Nepremi�nine Land d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas163" id="o6049654">
                        <h2><a href="/oglasi-prodaja/malinska-150m-od-morja-stanovanje_6049654/" title="6049654"><span class="title">MALINSKA, 150M OD MORJA</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/malinska-150m-od-morja-stanovanje_6049654/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4809256.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Stanovanje<span class="new-label">novo</span></span>
                            <!--<div class="new-container">
                            <div class="new sl"><i class="fa fa-certificate"></i><span>novo</span></div>
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Nadstropje: <strong>2</strong></span><span class="atribut">Leto: <strong>2013</strong></span>
                            </div>
                            <!--<div class="new sl"><i class="fa fa-certificate"></i><span>novo</span></div>-->
                            

                            <div class="kratek_container">
                                <div class="kratek">112 m2, apartma, zgrajen l. 2013, 2. nad., malinska, apartma od 112 m2 150 m od morja. prilo�nost., prodamo. Cena: max. ...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                112 m2, apartma, zgrajen l. 2013, 2. nad., malinska, apartma od 112 m2 150 m od morja. prilo�nost., prodamo. Cena: max. ...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">112,00 m2</span><br />
                                <span class="cena">195.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Premium SM d.o.o."><div class="logo"><a href="/oglasi-prodaja/malinska-150m-od-morja-stanovanje_6049654/"><img src="https://picbase.turbosist.si/slonep_agenc120/2242.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="6049654"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-6049654" href="#" data-id="6049654" onclick="save_ad(6049654); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmalinska-150m-od-morja-stanovanje_6049654%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmalinska-150m-od-morja-stanovanje_6049654%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmalinska-150m-od-morja-stanovanje_6049654%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmalinska-150m-od-morja-stanovanje_6049654%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="6049654"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmalinska-150m-od-morja-stanovanje_6049654%2F" class="utility" data-id="6049654"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po�lji prijatelju</span></a>
                            <a href="/oglasi-prodaja/malinska-150m-od-morja-stanovanje_6049654/" class="utility contact-tooltip" title="+385 51 858364<br />Premium SM d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas738" id="o6049701">
                        <h2><a href="/oglasi-prodaja/koper-center-novejsi-dupleks-stanovanje_6049701/" title="6049701"><span class="title">KOPER, CENTER - NOVEJ�I DUPLEKS</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/koper-center-novejsi-dupleks-stanovanje_6049701/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4809598.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Stanovanje<span class="new-label">novo</span></span>
                            <!--<div class="new-container">
                            <div class="new sl"><i class="fa fa-certificate"></i><span>novo</span></div>
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Nadstropje: <strong>2</strong>/2</span><span class="atribut">Leto: <strong>2005</strong></span>
                            </div>
                            <!--<div class="new sl"><i class="fa fa-certificate"></i><span>novo</span></div>-->
                            

                            <div class="kratek_container">
                                <div class="kratek">110 m2, 4,5-sobno, dupleks, zgrajeno l. 2005, 2/2 nad., novej�i dupleks v Centru Kopra, prodamo. Cena: cca 195.000,00 EU...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                110 m2, 4,5-sobno, dupleks, zgrajeno l. 2005, 2/2 nad., novej�i dupleks v Centru Kopra, prodamo. Cena: cca 195.000,00 EU...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">110,00 m2</span><br />
                                <span class="cena">195.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="1A nepremi�nine, Ervin Bu�an, s.p."><div class="logo"><a href="/oglasi-prodaja/koper-center-novejsi-dupleks-stanovanje_6049701/"><img src="https://picbase.turbosist.si/slonep_agenc120/1933.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="6049701"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-6049701" href="#" data-id="6049701" onclick="save_ad(6049701); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkoper-center-novejsi-dupleks-stanovanje_6049701%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkoper-center-novejsi-dupleks-stanovanje_6049701%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkoper-center-novejsi-dupleks-stanovanje_6049701%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkoper-center-novejsi-dupleks-stanovanje_6049701%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="6049701"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkoper-center-novejsi-dupleks-stanovanje_6049701%2F" class="utility" data-id="6049701"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po�lji prijatelju</span></a>
                            <a href="/oglasi-prodaja/koper-center-novejsi-dupleks-stanovanje_6049701/" class="utility contact-tooltip" title="030/350-360<br />1A nepremi�nine, Ervin Bu�an, s.p."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas417" id="o6049805">
                        <h2><a href="/oglasi-prodaja/crikvenica-stanovanje_6049805/" title="6049805"><span class="title">CRIKVENICA</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/crikvenica-stanovanje_6049805/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4810588.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Stanovanje<span class="new-label">novo</span></span>
                            <!--<div class="new-container">
                            <div class="new sl"><i class="fa fa-certificate"></i><span>novo</span></div>
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Nadstropje: <strong>P</strong></span><span class="atribut">Leto: <strong>2014</strong></span>
                            </div>
                            <!--<div class="new sl"><i class="fa fa-certificate"></i><span>novo</span></div>-->
                            

                            <div class="kratek_container">
                                <div class="kratek">95 m2, 2,5-sobno, dupleks, novogradnja - zgr. l. 2014, pritli�je, prodamo. Cena: 195.000,00 EUR</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                95 m2, 2,5-sobno, dupleks, novogradnja - zgr. l. 2014, pritli�je, prodamo. Cena: 195.000,00 EUR
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">95,00 m2</span><br />
                                <span class="cena">195.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Casa de mar nekretnine d.o.o."><div class="logo"><a href="/oglasi-prodaja/crikvenica-stanovanje_6049805/"><img src="https://picbase.turbosist.si/slonep_agenc120/1522.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="6049805"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-6049805" href="#" data-id="6049805" onclick="save_ad(6049805); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fcrikvenica-stanovanje_6049805%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fcrikvenica-stanovanje_6049805%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fcrikvenica-stanovanje_6049805%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fcrikvenica-stanovanje_6049805%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="6049805"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fcrikvenica-stanovanje_6049805%2F" class="utility" data-id="6049805"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po�lji prijatelju</span></a>
                            <a href="/oglasi-prodaja/crikvenica-stanovanje_6049805/" class="utility contact-tooltip" title="+385 51 633 700<br />Casa de mar nekretnine d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas628" id="o6037102">
                        <h2><a href="/oglasi-prodaja/vir-hisa_6037102/" title="6037102"><span class="title">VIR</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/vir-hisa_6037102/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4702236.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hi�a</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Leto: <strong>1987</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">100,64 m2, samostojna, zgrajena l. 1987, prodamo. Cena: 195.000,00 EUR</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                100,64 m2, samostojna, zgrajena l. 1987, prodamo. Cena: 195.000,00 EUR
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">100,64 m2</span><br />
                                <span class="cena">195.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Mre�a nepremi�nin d.o.o."><div class="logo"><a href="/oglasi-prodaja/vir-hisa_6037102/"><img src="https://picbase.turbosist.si/slonep_agenc120/1940.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="6037102"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-6037102" href="#" data-id="6037102" onclick="save_ad(6037102); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fvir-hisa_6037102%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fvir-hisa_6037102%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fvir-hisa_6037102%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fvir-hisa_6037102%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="6037102"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fvir-hisa_6037102%2F" class="utility" data-id="6037102"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po�lji prijatelju</span></a>
                            <a href="/oglasi-prodaja/vir-hisa_6037102/" class="utility contact-tooltip" title="01/560-30-50<br />Mre�a nepremi�nin d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas841" id="o6027919">
                        <h2><a href="/oglasi-prodaja/ilovik-otok-hisa_6027919/" title="6027919"><span class="title">ILOVIK, OTOK</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/ilovik-otok-hisa_6027919/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4625168.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hi�a</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Nadstropje: <strong>P+1</strong></span><span class="atribut">Leto: <strong>1978</strong></span><span class="atribut">Zemlji��e: <strong>230 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">160 m2, samostojna, adaptirana l. 1978, 230 m2 zemlji��a, P+1, prodamo. Cena: 195.000,00 EUR</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                160 m2, samostojna, adaptirana l. 1978, 230 m2 zemlji��a, P+1, prodamo. Cena: 195.000,00 EUR
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">160,00 m2</span><br />
                                <span class="cena">195.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Zasebna ponudba"><div class="logo"><a href="/oglasi-prodaja/ilovik-otok-hisa_6027919/"><img src="/images/zasebna-ponudba.png" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="6027919"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-6027919" href="#" data-id="6027919" onclick="save_ad(6027919); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Filovik-otok-hisa_6027919%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Filovik-otok-hisa_6027919%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Filovik-otok-hisa_6027919%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Filovik-otok-hisa_6027919%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="6027919"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Filovik-otok-hisa_6027919%2F" class="utility" data-id="6027919"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po�lji prijatelju</span></a>
                            <a href="/oglasi-prodaja/ilovik-otok-hisa_6027919/" class="utility contact-tooltip" title="041/229-110<br />"><i class="fa fa-phone"></i><span>O ponudniku</span></a>
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
            //]]>--></script><noscript><a href='https://ok.internetmedia.si/www/delivery/ck.php?n=a280490d&amp;cb=49633550&amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5=' target='_blank'><img src='https://ok.internetmedia.si/www/delivery/avw.php?zoneid=5&amp;cb=2087411910&amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5=&amp;n=a280490d' border='0' alt='' /></a></noscript>
                </div>
            
                    <div class="oglas_container oglasbold oglas684" id="o6037528">
                        <h2><a href="/oglasi-prodaja/koper-ferrarska-12-ogrlica-poslovni-prostor_6037528/" title="6037528"><span class="title">KOPER, FERRARSKA 12 OGRLICA</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/koper-ferrarska-12-ogrlica-poslovni-prostor_6037528/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4706023.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Poslovni prostor</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Nadstropje: <strong>1</strong></span><span class="atribut">Leto: <strong>1995</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">85 m2, pisarna, zgrajena l. 1995, 1. nad., Poslovni prostor obsega dve pisarne, predprostor in WC, prodamo. Cena: 195.00...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                85 m2, pisarna, zgrajena l. 1995, 1. nad., Poslovni prostor obsega dve pisarne, predprostor in WC, prodamo. Cena: 195.00...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">85,00 m2</span><br />
                                <span class="cena">195.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Zasebna ponudba"><div class="logo"><a href="/oglasi-prodaja/koper-ferrarska-12-ogrlica-poslovni-prostor_6037528/"><img src="/images/zasebna-ponudba.png" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="6037528"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-6037528" href="#" data-id="6037528" onclick="save_ad(6037528); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkoper-ferrarska-12-ogrlica-poslovni-prostor_6037528%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkoper-ferrarska-12-ogrlica-poslovni-prostor_6037528%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkoper-ferrarska-12-ogrlica-poslovni-prostor_6037528%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkoper-ferrarska-12-ogrlica-poslovni-prostor_6037528%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="6037528"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkoper-ferrarska-12-ogrlica-poslovni-prostor_6037528%2F" class="utility" data-id="6037528"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po�lji prijatelju</span></a>
                            <a href="/oglasi-prodaja/koper-ferrarska-12-ogrlica-poslovni-prostor_6037528/" class="utility contact-tooltip" title="041/753-198<br />"><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas241" id="o6023819">
                        <h2><a href="/oglasi-prodaja/mali-losinj-haraciceva-ulica-hisa_6023819/" title="6023819"><span class="title">MALI LO�INJ, HARA�I�EVA ULICA</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/mali-losinj-haraciceva-ulica-hisa_6023819/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4590249.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hi�a</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Nadstropje: <strong>P+1</strong></span><span class="atribut">Leto: <strong>1987</strong></span><span class="atribut">Zemlji��e: <strong>177 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">100 m2, samostojna, zgrajena l. 1987, 177 m2 zemlji��a, P+1, Hi�a ima 4 bivalne enote. Vse enote so opremljene, v vsaki ...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                100 m2, samostojna, zgrajena l. 1987, 177 m2 zemlji��a, P+1, Hi�a ima 4 bivalne enote. Vse enote so opremljene, v vsaki ...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">100,00 m2</span><br />
                                <span class="cena">195.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Zasebna ponudba"><div class="logo"><a href="/oglasi-prodaja/mali-losinj-haraciceva-ulica-hisa_6023819/"><img src="/images/zasebna-ponudba.png" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="6023819"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-6023819" href="#" data-id="6023819" onclick="save_ad(6023819); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmali-losinj-haraciceva-ulica-hisa_6023819%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmali-losinj-haraciceva-ulica-hisa_6023819%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmali-losinj-haraciceva-ulica-hisa_6023819%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmali-losinj-haraciceva-ulica-hisa_6023819%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="6023819"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmali-losinj-haraciceva-ulica-hisa_6023819%2F" class="utility" data-id="6023819"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po�lji prijatelju</span></a>
                            <a href="/oglasi-prodaja/mali-losinj-haraciceva-ulica-hisa_6023819/" class="utility contact-tooltip" title="02/818-14-84<br />"><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas191" id="o5888762">
                        <h2><a href="/oglasi-prodaja/maribor-center-stanovanje_5888762/" title="5888762"><span class="title">MARIBOR, CENTER</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/maribor-center-stanovanje_5888762/"><img src="https://picbase.turbosist.si/slonep_oglasi2/3598952.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Stanovanje</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Nadstropje: <strong>P</strong>/2</span><span class="atribut">Leto: <strong>1997</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">153,5 m2, 4-sobno, zgrajeno l. 1997, P/2 nad., Novej�e - pritli�no, 4 sobno stanovanje z atrijem, v dveh eta�ah. V stano...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                153,5 m2, 4-sobno, zgrajeno l. 1997, P/2 nad., Novej�e - pritli�no, 4 sobno stanovanje z atrijem, v dveh eta�ah. V stano...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">153,50 m2</span><br />
                                <span class="cena">195.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Zasebna ponudba"><div class="logo"><a href="/oglasi-prodaja/maribor-center-stanovanje_5888762/"><img src="/images/zasebna-ponudba.png" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5888762"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-5888762" href="#" data-id="5888762" onclick="save_ad(5888762); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmaribor-center-stanovanje_5888762%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmaribor-center-stanovanje_5888762%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmaribor-center-stanovanje_5888762%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmaribor-center-stanovanje_5888762%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="5888762"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmaribor-center-stanovanje_5888762%2F" class="utility" data-id="5888762"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po�lji prijatelju</span></a>
                            <a href="/oglasi-prodaja/maribor-center-stanovanje_5888762/" class="utility contact-tooltip" title="041/675-951<br />"><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas874" id="o5842284">
                        <h2><a href="/oglasi-prodaja/cepno-hisa_5842284/" title="5842284"><span class="title">�EPNO</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/cepno-hisa_5842284/"><img src="https://picbase.turbosist.si/slonep_oglasi2/3294682.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hi�a</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Leto: <strong>1973</strong></span><span class="atribut">Zemlji��e: <strong>80000 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">840 m2, samostojna, zgrajena l. 1973, 80.000 m2 zemlji��a, Kmetija v �epnem, odli�na prilo�nost za postavitev EKO OAZE n...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                840 m2, samostojna, zgrajena l. 1973, 80.000 m2 zemlji��a, Kmetija v �epnem, odli�na prilo�nost za postavitev EKO OAZE n...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">840,00 m2</span><br />
                                <span class="cena">195.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Makler Bled d.o.o."><div class="logo"><a href="/oglasi-prodaja/cepno-hisa_5842284/"><img src="https://picbase.turbosist.si/slonep_agenc120/246.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5842284"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-5842284" href="#" data-id="5842284" onclick="save_ad(5842284); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fcepno-hisa_5842284%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fcepno-hisa_5842284%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fcepno-hisa_5842284%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fcepno-hisa_5842284%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="5842284"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fcepno-hisa_5842284%2F" class="utility" data-id="5842284"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po�lji prijatelju</span></a>
                            <a href="/oglasi-prodaja/cepno-hisa_5842284/" class="utility contact-tooltip" title="041/647-974<br />Makler Bled d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas833" id="o6008846">
                        <h2><a href="/oglasi-prodaja/rakitna-na-soncni-strani-hisa_6008846/" title="6008846"><span class="title">RAKITNA, NA SON�NI STRANI</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/rakitna-na-soncni-strani-hisa_6008846/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4467345.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hi�a</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Nadstropje: <strong>P+1+M</strong></span><span class="atribut">Leto: <strong>1992</strong></span><span class="atribut">Zemlji��e: <strong>647 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">166,2 m2, samostojna, zgrajena l. 1992, adaptirana l. 2006, 647 m2 zemlji��a, P+1+M, Vsi priklju�ki, CK na olje, kamin n...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                166,2 m2, samostojna, zgrajena l. 1992, adaptirana l. 2006, 647 m2 zemlji��a, P+1+M, Vsi priklju�ki, CK na olje, kamin n...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">166,20 m2</span><br />
                                <span class="cena">195.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Zasebna ponudba"><div class="logo"><a href="/oglasi-prodaja/rakitna-na-soncni-strani-hisa_6008846/"><img src="/images/zasebna-ponudba.png" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="6008846"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-6008846" href="#" data-id="6008846" onclick="save_ad(6008846); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Frakitna-na-soncni-strani-hisa_6008846%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Frakitna-na-soncni-strani-hisa_6008846%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Frakitna-na-soncni-strani-hisa_6008846%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Frakitna-na-soncni-strani-hisa_6008846%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="6008846"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Frakitna-na-soncni-strani-hisa_6008846%2F" class="utility" data-id="6008846"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po�lji prijatelju</span></a>
                            <a href="/oglasi-prodaja/rakitna-na-soncni-strani-hisa_6008846/" class="utility contact-tooltip" title="041/462-959<br />"><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas428" id="o6042945">
                        <h2><a href="/oglasi-prodaja/lj-bezigrad-savski-breg-stanovanje_6042945/" title="6042945"><span class="title">LJ. BE�IGRAD, SAVSKI BREG</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/lj-bezigrad-savski-breg-stanovanje_6042945/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4751944.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Stanovanje</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Nadstropje: <strong>5</strong>/5</span><span class="atribut">Leto: <strong>2009</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">116 m2, 2,5-sobno, &quot;penthouse&quot;, zgrajeno l. 2009, adaptirano l. 2016, 5/5 nad., Moderno zasnovano in opremljen...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                116 m2, 2,5-sobno, &quot;penthouse&quot;, zgrajeno l. 2009, adaptirano l. 2016, 5/5 nad., Moderno zasnovano in opremljen...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">116,00 m2</span><br />
                                <span class="cena">195.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Zasebna ponudba"><div class="logo"><a href="/oglasi-prodaja/lj-bezigrad-savski-breg-stanovanje_6042945/"><img src="/images/zasebna-ponudba.png" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="6042945"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-6042945" href="#" data-id="6042945" onclick="save_ad(6042945); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-bezigrad-savski-breg-stanovanje_6042945%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-bezigrad-savski-breg-stanovanje_6042945%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-bezigrad-savski-breg-stanovanje_6042945%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-bezigrad-savski-breg-stanovanje_6042945%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="6042945"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-bezigrad-savski-breg-stanovanje_6042945%2F" class="utility" data-id="6042945"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po�lji prijatelju</span></a>
                            <a href="/oglasi-prodaja/lj-bezigrad-savski-breg-stanovanje_6042945/" class="utility contact-tooltip" title="041/613-251<br />"><i class="fa fa-phone"></i><span>O ponudniku</span></a>
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
            //]]>--></script><noscript><a href='https://ok.internetmedia.si/www/delivery/ck.php?n=a280490d&amp;cb=409221441&amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5=' target='_blank'><img src='https://ok.internetmedia.si/www/delivery/avw.php?zoneid=5&amp;cb=986240611&amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5=&amp;n=a280490d' border='0' alt='' /></a></noscript>
                </div>
            
                    <div class="oglas_container oglasbold oglas443" id="o6027334">
                        <h2><a href="/oglasi-prodaja/potocnica-151-hisa_6027334/" title="6027334"><span class="title">POTO�NICA, 151</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/potocnica-151-hisa_6027334/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4620592.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hi�a</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Leto: <strong>1995</strong></span><span class="atribut">Zemlji��e: <strong>616 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">130 m2, dvostanovanjska, zgrajena l. 1995, adaptirana l. 2015, 616 m2 zemlji��a, Razgled na morje - le 90m od morja, zal...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                130 m2, dvostanovanjska, zgrajena l. 1995, adaptirana l. 2015, 616 m2 zemlji��a, Razgled na morje - le 90m od morja, zal...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">130,00 m2</span><br />
                                <span class="cena">195.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Zasebna ponudba"><div class="logo"><a href="/oglasi-prodaja/potocnica-151-hisa_6027334/"><img src="/images/zasebna-ponudba.png" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="6027334"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-6027334" href="#" data-id="6027334" onclick="save_ad(6027334); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fpotocnica-151-hisa_6027334%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fpotocnica-151-hisa_6027334%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fpotocnica-151-hisa_6027334%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fpotocnica-151-hisa_6027334%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="6027334"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fpotocnica-151-hisa_6027334%2F" class="utility" data-id="6027334"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po�lji prijatelju</span></a>
                            <a href="/oglasi-prodaja/potocnica-151-hisa_6027334/" class="utility contact-tooltip" title="+386 41 707 408<br />"><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas555" id="o6030022">
                        <h2><a href="/oglasi-prodaja/sentvid-stanovanje_6030022/" title="6030022"><span class="title">�ENTVID</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/sentvid-stanovanje_6030022/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4643064.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Stanovanje</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Nadstropje: <strong>P</strong>/4</span><span class="atribut">Leto: <strong>1939</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">112,8 m2, 5 in ve�sobno, dupleks, zgrajeno l. 1939, adaptirano l. 2006, P/4 nad., lasten vhod, prostorno, 2 kopalnici, 2...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                112,8 m2, 5 in ve�sobno, dupleks, zgrajeno l. 1939, adaptirano l. 2006, P/4 nad., lasten vhod, prostorno, 2 kopalnici, 2...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">112,80 m2</span><br />
                                <span class="cena">195.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Zasebna ponudba"><div class="logo"><a href="/oglasi-prodaja/sentvid-stanovanje_6030022/"><img src="/images/zasebna-ponudba.png" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="6030022"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-6030022" href="#" data-id="6030022" onclick="save_ad(6030022); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsentvid-stanovanje_6030022%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsentvid-stanovanje_6030022%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsentvid-stanovanje_6030022%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsentvid-stanovanje_6030022%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="6030022"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsentvid-stanovanje_6030022%2F" class="utility" data-id="6030022"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po�lji prijatelju</span></a>
                            <a href="/oglasi-prodaja/sentvid-stanovanje_6030022/" class="utility contact-tooltip" title="041/686-091<br />"><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas82" id="o5973243">
                        <h2><a href="/oglasi-prodaja/sentvid-hisa_5973243/" title="5973243"><span class="title">�ENTVID</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/sentvid-hisa_5973243/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4713570.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hi�a</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Nadstropje: <strong>P+1</strong></span><span class="atribut">Leto: <strong>2016</strong></span><span class="atribut">Zemlji��e: <strong>254 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">128 m2, dvoj�ek, zgrajen l. 2016, 254 m2 zemlji��a, P+1, prodamo. Cena: 195.000,00 EUR</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                128 m2, dvoj�ek, zgrajen l. 2016, 254 m2 zemlji��a, P+1, prodamo. Cena: 195.000,00 EUR
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">128,00 m2</span><br />
                                <span class="cena">195.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Zasebna ponudba"><div class="logo"><a href="/oglasi-prodaja/sentvid-hisa_5973243/"><img src="/images/zasebna-ponudba.png" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5973243"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-5973243" href="#" data-id="5973243" onclick="save_ad(5973243); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsentvid-hisa_5973243%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsentvid-hisa_5973243%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsentvid-hisa_5973243%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsentvid-hisa_5973243%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="5973243"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsentvid-hisa_5973243%2F" class="utility" data-id="5973243"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po�lji prijatelju</span></a>
                            <a href="/oglasi-prodaja/sentvid-hisa_5973243/" class="utility contact-tooltip" title="031/666-017<br />"><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                </div><div class="spacer"></div><div id="pagination" class="fr"><ul>
                    <li><a href="/oglasi-prodaja/cena-do-200000-eur/?s=13" class="first"><<</a></li>
                    <li><a href="/oglasi-prodaja/cena-do-200000-eur/15/?s=13" class="prev"><</a></li>
                <span class="dots3">...</span><li><a href="/oglasi-prodaja/cena-do-200000-eur/13/?s=13">13</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/14/?s=13">14</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/15/?s=13">15</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/16/?s=13" class="active">16</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/17/?s=13">17</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/18/?s=13">18</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/19/?s=13">19</a></li><span class="dots3">...</span><li><a href="/oglasi-prodaja/cena-do-200000-eur/17/?s=13" class="next">></a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/652/?s=13" class="last">>></a></li></ul></div>
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
		<strong>MEGANET d.o.o. � 1998 - 2016</strong><br />
		Kontakt: 03/567-91-10<br />
		E-po�ta: <a href="mailto:info@nepremicnine.net" class="nn">info@nepremicnine.net</a>
	</div>
	<div class="spacer"></div>
	<div class="spacer"></div>
	<div class="block">
		<strong>Tehni�na podpora: </strong><br />
		INTERNET MEDIA d.o.o.<br />
				E-po�ta: <a href="mailto:podpora@nepremicnine.net" class="nn">podpora@nepremicnine.net</a>
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
			<li><a href="/nepremicnine.html?q=menjava nepremi�nine" title="menjava nepremi�nine"><strong>Menjava nepremi�nine</strong></a></li>
			<li><a href="/pravno-pojasnilo.html">Pravno pojasnilo</a></li>
			<li><a href="/nepremicnine-oglasevanje.html">Ogla�evanje</a></li>
			<li><a href="/cookies.html">O pi�kotkih</a></li>
			<li class="last"><a href="/pomoc-in-svetovanje.html">Pomo�</a></li>		</ul>
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



