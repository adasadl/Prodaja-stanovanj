<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "https://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="https://www.w3.org/1999/xhtml" lang="sl">
<head>
<link rel="canonical" href="/oglasi-prodaja/ljubljana-mesto/stanovanje/cena-do-200000-eur/2/" /><meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
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
<iframe id='a4e1c538' name='a4e1c538' src='https://ok.internetmedia.si/www/delivery/afr.php?zoneid=1&amp;target=_blank&amp;charset=UTF-8&amp;cb=1596738158&amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5=' frameborder='0' scrolling='no' width='960' height='150'><a href='https://ok.internetmedia.si/www/delivery/ck.php?n=a0fcbf0c&amp;cb=1279978271&amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5=' target='_blank'><img src='https://ok.internetmedia.si/www/delivery/avw.php?zoneid=1&amp;charset=UTF-8&amp;cb=170182172&amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5=&amp;n=a0fcbf0c' border='0' alt='' /></a></iframe>
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
                    //data: "wpg=nepremicnine&p=1&arg[]=ljubljana-mesto&arg[]=stanovanje&arg[]=cena-do-200000-eur&pg=2&s=13&uid=", // data to send to above script page if any
                    data: "wpg=nepremicnine&p=1&arg%5B0%5D=ljubljana-mesto&arg%5B1%5D=stanovanje&arg%5B2%5D=cena-do-200000-eur&pg=2&s=13&c2=200000&uid=", // data to send to above script page if any
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
                    <li><a href="/oglasi-prodaja/cena-do-200000-eur/?s=13" class="prev"><</a></li>
                <li><a href="/oglasi-prodaja/cena-do-200000-eur/?s=13">1</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/2/?s=13" class="active">2</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/3/?s=13">3</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/4/?s=13">4</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/5/?s=13">5</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/6/?s=13">6</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/7/?s=13">7</a></li><span class="dots3">...</span><li><a href="/oglasi-prodaja/cena-do-200000-eur/3/?s=13" class="next">></a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/652/?s=13" class="last">>></a></li></ul></div><h1>Prodaja </h1><div class="sort cb">
                    <div class="fl">
                    <strong>Razvrsti:</strong> <a href="/oglasi-prodaja/ljubljana-mesto/stanovanje/cena-do-200000-eur/2/?s=1" class="up">lokacija</a> | <a href="/oglasi-prodaja/ljubljana-mesto/stanovanje/cena-do-200000-eur/2/?s=11" class="down">lokacija</a> | <a href="/oglasi-prodaja/ljubljana-mesto/stanovanje/cena-do-200000-eur/2/?s=3" class="up">cena</a> | <a href="/oglasi-prodaja/ljubljana-mesto/stanovanje/cena-do-200000-eur/2/?s=13" class="down act">cena</a> | <a href="/oglasi-prodaja/ljubljana-mesto/stanovanje/cena-do-200000-eur/2/?s=4" class="up">m2</a> | <a href="/oglasi-prodaja/ljubljana-mesto/stanovanje/cena-do-200000-eur/2/?s=14" class="down">m2</a> | <a href="/oglasi-prodaja/ljubljana-mesto/stanovanje/cena-do-200000-eur/2/?s=5" class="up">ponudnik</a> | <a href="/oglasi-prodaja/ljubljana-mesto/stanovanje/cena-do-200000-eur/2/?s=16" class="down">datum vpisa</a> | </div><a id="si" href="#" class="fr ibl pf i-si" style="padding-right:0">Shrani iskanje</a><div class="clearer"></div></div>
                    </div><div id="slide-thumb">
				<a href="http://www.sonce-nepremicnine.si/sl/Nepremicninski-oglasi/prodaja.k1/stanovanje.v1/vse_drzave.d0/oglas3096198.html" target="_blank" class="pt">
					<table border="0" cellpadding="0" cellspacing="0">
						<tr>
							<td>
								<strong>Barbariga</strong>
							</td>
						</tr>
						<tr>
							<td class="slika">
								<div><img src="https://picbase.turbosist.si/adads/thumbnails/1290.jpg" /></div>								
							</td>
						</tr>
						<tr>
							<td><span>Dvosobno stanovanje z atrijem</span></td>
						</tr>
					</table>
				</a>
			
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
			
				<a href="http://www.nepremicnine.net/novogradnje/cudovito-naselje-retece-le-streljaj-od-ljubljane.html" target="_blank" class="pt">
					<table border="0" cellpadding="0" cellspacing="0">
						<tr>
							<td>
								<strong>Reteèe</strong>
							</td>
						</tr>
						<tr>
							<td class="slika">
								<div><img src="https://picbase.turbosist.si/adads/thumbnails/672.jpg" /></div>								
							</td>
						</tr>
						<tr>
							<td><span>Izjemna priložnost!</span></td>
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
			<div class="clearer"></div></div>
<div class="seznam">
                    <div class="oglas_container oglasbold oglas195" id="o5533808">
                        <h2><a href="/oglasi-prodaja/ilirska-bistrica-poslovni-prostor_5533808/" title="5533808"><span class="title">ILIRSKA BISTRICA</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/ilirska-bistrica-poslovni-prostor_5533808/"><img src="/images/n-5.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Poslovni prostor</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Nadstropje: <strong>P</strong></span><span class="atribut">Leto: <strong>1968</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">307,35 m2, prostor za storitve, zgrajen l. 1968, pritlièje, prodamo. Cena: 200.000,00 EUR</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                307,35 m2, prostor za storitve, zgrajen l. 1968, pritlièje, prodamo. Cena: 200.000,00 EUR
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">307,35 m2</span><br />
                                <span class="cena">200.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Mercator, d.d., Sektor razvoj in dezinvestije"><div class="logo"><a href="/oglasi-prodaja/ilirska-bistrica-poslovni-prostor_5533808/"><img src="https://picbase.turbosist.si/slonep_agenc120/716.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5533808"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-5533808" href="#" data-id="5533808" onclick="save_ad(5533808); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Filirska-bistrica-poslovni-prostor_5533808%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Filirska-bistrica-poslovni-prostor_5533808%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Filirska-bistrica-poslovni-prostor_5533808%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Filirska-bistrica-poslovni-prostor_5533808%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="5533808"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Filirska-bistrica-poslovni-prostor_5533808%2F" class="utility" data-id="5533808"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/ilirska-bistrica-poslovni-prostor_5533808/" class="utility contact-tooltip" title="01/560-63-90<br />Mercator, d.d., Sektor razvoj in dezinvestije"><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas20" id="o5731099">
                        <h2><a href="/oglasi-prodaja/zirovnica-breznica-6a-poslovni-prostor_5731099/" title="5731099"><span class="title">ŽIROVNICA, BREZNICA 6A</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/zirovnica-breznica-6a-poslovni-prostor_5731099/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4388707.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Poslovni prostor</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Nadstropje: <strong>P+1</strong></span><span class="atribut">Leto: <strong>1880</strong></span><span class="atribut">Zemljišèe: <strong>542 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">465,5 m2, živilska trgovina, zgrajena l. 1880, adaptirana l. 2008, 542 m2 zemljišèa, P+1, prodamo. Cena: 200.000,00 EUR</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                465,5 m2, živilska trgovina, zgrajena l. 1880, adaptirana l. 2008, 542 m2 zemljišèa, P+1, prodamo. Cena: 200.000,00 EUR
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">465,50 m2</span><br />
                                <span class="cena">200.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Mercator, d.d., Sektor razvoj in dezinvestije"><div class="logo"><a href="/oglasi-prodaja/zirovnica-breznica-6a-poslovni-prostor_5731099/"><img src="https://picbase.turbosist.si/slonep_agenc120/716.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5731099"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-5731099" href="#" data-id="5731099" onclick="save_ad(5731099); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fzirovnica-breznica-6a-poslovni-prostor_5731099%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fzirovnica-breznica-6a-poslovni-prostor_5731099%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fzirovnica-breznica-6a-poslovni-prostor_5731099%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fzirovnica-breznica-6a-poslovni-prostor_5731099%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="5731099"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fzirovnica-breznica-6a-poslovni-prostor_5731099%2F" class="utility" data-id="5731099"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/zirovnica-breznica-6a-poslovni-prostor_5731099/" class="utility contact-tooltip" title="01/560-63-90<br />Mercator, d.d., Sektor razvoj in dezinvestije"><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas22" id="o5991508">
                        <h2><a href="/oglasi-prodaja/solkan-hisa_5991508/" title="5991508"><span class="title">SOLKAN</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/solkan-hisa_5991508/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4332903.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hiša</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Nadstropje: <strong>P+1</strong></span><span class="atribut">Leto: <strong>2015</strong></span><span class="atribut">Zemljišèe: <strong>650 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">190 m2, samostojna, zgrajena l. 2015, 650 m2 zemljišèa, P+1, prodamo. Cena: 200.000,00 EUR</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                190 m2, samostojna, zgrajena l. 2015, 650 m2 zemljišèa, P+1, prodamo. Cena: 200.000,00 EUR
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">190,00 m2</span><br />
                                <span class="cena">200.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="MISTRAL NEPREMIÈNINE, Valter Vodopivec s.p."><div class="logo"><a href="/oglasi-prodaja/solkan-hisa_5991508/"><img src="https://picbase.turbosist.si/slonep_agenc120/2004.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5991508"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-5991508" href="#" data-id="5991508" onclick="save_ad(5991508); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsolkan-hisa_5991508%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsolkan-hisa_5991508%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsolkan-hisa_5991508%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsolkan-hisa_5991508%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="5991508"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsolkan-hisa_5991508%2F" class="utility" data-id="5991508"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/solkan-hisa_5991508/" class="utility contact-tooltip" title="031/640-215<br />MISTRAL NEPREMIÈNINE, Valter Vodopivec s.p."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
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
            //]]>--></script><noscript><a href='https://ok.internetmedia.si/www/delivery/ck.php?n=a280490d&amp;cb=1845724593&amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5=' target='_blank'><img src='https://ok.internetmedia.si/www/delivery/avw.php?zoneid=5&amp;cb=1322419831&amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5=&amp;n=a280490d' border='0' alt='' /></a></noscript>
                </div>
            
                    <div class="oglas_container oglasbold oglas253" id="o6019725">
                        <h2><a href="/oglasi-prodaja/savudrija-hisa_6019725/" title="6019725"><span class="title">SAVUDRIJA</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/savudrija-hisa_6019725/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4557139.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hiša</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Leto: <strong>1978</strong></span><span class="atribut">Zemljišèe: <strong>494 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">120 m2, samostojna, zgrajena l. 1978, adaptirana l. 2015, 494 m2 zemljišèa, na lepi lokaciji v neposredni bližini morja,...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                120 m2, samostojna, zgrajena l. 1978, adaptirana l. 2015, 494 m2 zemljišèa, na lepi lokaciji v neposredni bližini morja,...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">120,00 m2</span><br />
                                <span class="cena">200.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Malis nepremiènine d.o.o."><div class="logo"><a href="/oglasi-prodaja/savudrija-hisa_6019725/"><img src="https://picbase.turbosist.si/slonep_agenc120/433.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="6019725"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-6019725" href="#" data-id="6019725" onclick="save_ad(6019725); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsavudrija-hisa_6019725%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsavudrija-hisa_6019725%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsavudrija-hisa_6019725%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsavudrija-hisa_6019725%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="6019725"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsavudrija-hisa_6019725%2F" class="utility" data-id="6019725"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/savudrija-hisa_6019725/" class="utility contact-tooltip" title="041/345-544<br />Malis nepremiènine d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas595" id="o5989976">
                        <h2><a href="/oglasi-prodaja/lj-siska-vizmarje-hisa_5989976/" title="5989976"><span class="title">LJ. ŠIŠKA, VIŽMARJE</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/lj-siska-vizmarje-hisa_5989976/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4321468.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hiša</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Nadstropje: <strong>K+P+1+M</strong></span><span class="atribut">Leto: <strong>1964</strong></span><span class="atribut">Zemljišèe: <strong>240 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">169,7 m2, trojèek, zgrajen l. 1964, adaptiran l. 2010, 240 m2 zemljišèa, K+P+1+M, vmesna hiša z lahkim dostopom in garaž...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                169,7 m2, trojèek, zgrajen l. 1964, adaptiran l. 2010, 240 m2 zemljišèa, K+P+1+M, vmesna hiša z lahkim dostopom in garaž...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">169,70 m2</span><br />
                                <span class="cena">200.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="MESTO NEPREMIÈNIN d.o.o."><div class="logo"><a href="/oglasi-prodaja/lj-siska-vizmarje-hisa_5989976/"><img src="https://picbase.turbosist.si/slonep_agenc120/1939.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5989976"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-5989976" href="#" data-id="5989976" onclick="save_ad(5989976); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-siska-vizmarje-hisa_5989976%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-siska-vizmarje-hisa_5989976%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-siska-vizmarje-hisa_5989976%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-siska-vizmarje-hisa_5989976%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="5989976"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-siska-vizmarje-hisa_5989976%2F" class="utility" data-id="5989976"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/lj-siska-vizmarje-hisa_5989976/" class="utility contact-tooltip" title="040/551-818<br />MESTO NEPREMIÈNIN d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas241" id="o5842549">
                        <h2><a href="/oglasi-prodaja/ankaran-posest_5842549/" title="5842549"><span class="title">ANKARAN</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/ankaran-posest_5842549/"><img src="https://picbase.turbosist.si/slonep_oglasi2/3296446.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Posest</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">2.207 m2, zazidljiva, prodamo. Cena: 200.000,00 EUR</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                2.207 m2, zazidljiva, prodamo. Cena: 200.000,00 EUR
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">2.207,00 m2</span><br />
                                <span class="cena">200.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Marketing Galeb d.o.o."><div class="logo"><a href="/oglasi-prodaja/ankaran-posest_5842549/"><img src="https://picbase.turbosist.si/slonep_agenc120/220.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5842549"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-5842549" href="#" data-id="5842549" onclick="save_ad(5842549); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fankaran-posest_5842549%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fankaran-posest_5842549%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fankaran-posest_5842549%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fankaran-posest_5842549%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="5842549"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fankaran-posest_5842549%2F" class="utility" data-id="5842549"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/ankaran-posest_5842549/" class="utility contact-tooltip" title="05/663-09-07<br />Marketing Galeb d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas268" id="o6004989">
                        <h2><a href="/oglasi-prodaja/resnik-vikend_6004989/" title="6004989"><span class="title">RESNIK</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/resnik-vikend_6004989/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4438294.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Vikend</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Nadstropje: <strong>K+P+1</strong></span><span class="atribut">Leto: <strong>2005</strong></span><span class="atribut">Zemljišèe: <strong>400 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">140 m2, bivalen, zgrajen l. 2005, 400 m2 zemljišèa, K+P+1, prodamo. Cena: cca 200.000,00 EUR</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                140 m2, bivalen, zgrajen l. 2005, 400 m2 zemljišèa, K+P+1, prodamo. Cena: cca 200.000,00 EUR
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">140,00 m2</span><br />
                                <span class="cena">200.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Monema d.o.o."><div class="logo"><a href="/oglasi-prodaja/resnik-vikend_6004989/"><img src="https://picbase.turbosist.si/slonep_agenc120/2106.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="6004989"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-6004989" href="#" data-id="6004989" onclick="save_ad(6004989); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fresnik-vikend_6004989%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fresnik-vikend_6004989%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fresnik-vikend_6004989%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fresnik-vikend_6004989%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="6004989"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fresnik-vikend_6004989%2F" class="utility" data-id="6004989"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/resnik-vikend_6004989/" class="utility contact-tooltip" title="040/662-255<br />Monema d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas95" id="o5999765">
                        <h2><a href="/oglasi-prodaja/golnik-hisa_5999765/" title="5999765"><span class="title">GOLNIK</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/golnik-hisa_5999765/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4396467.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hiša</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Nadstropje: <strong>P+1+M</strong></span><span class="atribut">Leto: <strong>2001</strong></span><span class="atribut">Zemljišèe: <strong>664 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">300 m2, samostojna, zgrajena l. 2001, 664 m2 zemljišèa, P+1+M, mirna lokacija, na voljo po dogovoru, prodamo. Cena: 200....</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                300 m2, samostojna, zgrajena l. 2001, 664 m2 zemljišèa, P+1+M, mirna lokacija, na voljo po dogovoru, prodamo. Cena: 200....
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">300,00 m2</span><br />
                                <span class="cena">200.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Nepremiènine ambient, Mojca Piršiè s.p."><div class="logo"><a href="/oglasi-prodaja/golnik-hisa_5999765/"><img src="https://picbase.turbosist.si/slonep_agenc120/1826.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5999765"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-5999765" href="#" data-id="5999765" onclick="save_ad(5999765); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fgolnik-hisa_5999765%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fgolnik-hisa_5999765%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fgolnik-hisa_5999765%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fgolnik-hisa_5999765%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="5999765"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fgolnik-hisa_5999765%2F" class="utility" data-id="5999765"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/golnik-hisa_5999765/" class="utility contact-tooltip" title="040/172-800<br />Nepremiènine ambient, Mojca Piršiè s.p."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas56" id="o5855386">
                        <h2><a href="/oglasi-prodaja/zupanciceva-jama-terasa-stanovanje_5855386/" title="5855386"><span class="title">ZUPANÈIÈEVA JAMA, TERASA</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/zupanciceva-jama-terasa-stanovanje_5855386/"><img src="https://picbase.turbosist.si/slonep_oglasi2/3378230.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Stanovanje</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Nadstropje: <strong>VP</strong></span><span class="atribut">Leto: <strong>2007</strong></span><span class="atribut">Zemljišèe: <strong>110 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">58 m2, 2-sobno, zgrajeno l. 2007, 110 m2 zemljišèa, visoko pritlièje, opremljeno stanovanje s 110 m2 terase + klet + par...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                58 m2, 2-sobno, zgrajeno l. 2007, 110 m2 zemljišèa, visoko pritlièje, opremljeno stanovanje s 110 m2 terase + klet + par...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">58,00 m2</span><br />
                                <span class="cena">200.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Nepremiènine Plus d.o.o."><div class="logo"><a href="/oglasi-prodaja/zupanciceva-jama-terasa-stanovanje_5855386/"><img src="https://picbase.turbosist.si/slonep_agenc120/266.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5855386"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-5855386" href="#" data-id="5855386" onclick="save_ad(5855386); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fzupanciceva-jama-terasa-stanovanje_5855386%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fzupanciceva-jama-terasa-stanovanje_5855386%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fzupanciceva-jama-terasa-stanovanje_5855386%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fzupanciceva-jama-terasa-stanovanje_5855386%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="5855386"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fzupanciceva-jama-terasa-stanovanje_5855386%2F" class="utility" data-id="5855386"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/zupanciceva-jama-terasa-stanovanje_5855386/" class="utility contact-tooltip" title="01/565-31-20<br />Nepremiènine Plus d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
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
            //]]>--></script><noscript><a href='https://ok.internetmedia.si/www/delivery/ck.php?n=a280490d&amp;cb=1756757965&amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5=' target='_blank'><img src='https://ok.internetmedia.si/www/delivery/avw.php?zoneid=5&amp;cb=865699583&amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5=&amp;n=a280490d' border='0' alt='' /></a></noscript>
                </div>
            
                    <div class="oglas_container oglasbold oglas287" id="o6002715">
                        <h2><a href="/oglasi-prodaja/jesenice-poslovna-cona-sp-plavz-poslovni-prostor_6002715/" title="6002715"><span class="title">JESENICE, POSLOVNA CONA SP. PLAVŽ</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/jesenice-poslovna-cona-sp-plavz-poslovni-prostor_6002715/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4420696.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Poslovni prostor</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Leto: <strong>2012</strong></span><span class="atribut">Zemljišèe: <strong>1630 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">471,4 m2, kombiniran prostor, zgrajen l. 2012, 1.630 m2 zemljišèa, V kompleksu se lahko opravlja trgovska, proizvodna in...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                471,4 m2, kombiniran prostor, zgrajen l. 2012, 1.630 m2 zemljišèa, V kompleksu se lahko opravlja trgovska, proizvodna in...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">471,40 m2</span><br />
                                <span class="cena">200.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Nepremiènine Smuk – NSKG d.o.o."><div class="logo"><a href="/oglasi-prodaja/jesenice-poslovna-cona-sp-plavz-poslovni-prostor_6002715/"><img src="https://picbase.turbosist.si/slonep_agenc120/1643.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="6002715"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-6002715" href="#" data-id="6002715" onclick="save_ad(6002715); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fjesenice-poslovna-cona-sp-plavz-poslovni-prostor_6002715%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fjesenice-poslovna-cona-sp-plavz-poslovni-prostor_6002715%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fjesenice-poslovna-cona-sp-plavz-poslovni-prostor_6002715%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fjesenice-poslovna-cona-sp-plavz-poslovni-prostor_6002715%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="6002715"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fjesenice-poslovna-cona-sp-plavz-poslovni-prostor_6002715%2F" class="utility" data-id="6002715"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/jesenice-poslovna-cona-sp-plavz-poslovni-prostor_6002715/" class="utility contact-tooltip" title="04/581-36-10<br />Nepremiènine Smuk – NSKG d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas279" id="o5925299">
                        <h2><a href="/oglasi-prodaja/novo-mesto-slavka-gruma-hisa_5925299/" title="5925299"><span class="title">NOVO MESTO, SLAVKA GRUMA</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/novo-mesto-slavka-gruma-hisa_5925299/"><img src="/images/n-2.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hiša</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Leto: <strong>1980</strong></span><span class="atribut">Zemljišèe: <strong>1511 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">152 m2, samostojna, adaptirana l. 1980, 1.511 m2 zemljišèa, prodamo. Cena: 200.000,00 EUR</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                152 m2, samostojna, adaptirana l. 1980, 1.511 m2 zemljišèa, prodamo. Cena: 200.000,00 EUR
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">152,00 m2</span><br />
                                <span class="cena">200.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Prenova Marko Bele s.p. Novo mesto"><div class="logo"><a href="/oglasi-prodaja/novo-mesto-slavka-gruma-hisa_5925299/"><img src="https://picbase.turbosist.si/slonep_agenc120/146.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5925299"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-5925299" href="#" data-id="5925299" onclick="save_ad(5925299); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fnovo-mesto-slavka-gruma-hisa_5925299%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fnovo-mesto-slavka-gruma-hisa_5925299%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fnovo-mesto-slavka-gruma-hisa_5925299%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fnovo-mesto-slavka-gruma-hisa_5925299%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="5925299"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fnovo-mesto-slavka-gruma-hisa_5925299%2F" class="utility" data-id="5925299"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/novo-mesto-slavka-gruma-hisa_5925299/" class="utility contact-tooltip" title="051/324-658<br />Prenova Marko Bele s.p. Novo mesto"><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas501" id="o5777222">
                        <h2><a href="/oglasi-prodaja/ptuj-posest_5777222/" title="5777222"><span class="title">PTUJ</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/ptuj-posest_5777222/"><img src="https://picbase.turbosist.si/slonep_oglasi2/2891847.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Posest</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">38.811 m2, kmetija, prodamo posest-kmetijo na mirni lokaciji na ptuju, prodamo. Cena: 200.000,00 EUR</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                38.811 m2, kmetija, prodamo posest-kmetijo na mirni lokaciji na ptuju, prodamo. Cena: 200.000,00 EUR
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">38.811,00 m2</span><br />
                                <span class="cena">200.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="RE/MAX Poetovio, Nepremièninska družba d.o.o."><div class="logo"><a href="/oglasi-prodaja/ptuj-posest_5777222/"><img src="https://picbase.turbosist.si/slonep_agenc120/772.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5777222"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-5777222" href="#" data-id="5777222" onclick="save_ad(5777222); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fptuj-posest_5777222%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fptuj-posest_5777222%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fptuj-posest_5777222%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fptuj-posest_5777222%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="5777222"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fptuj-posest_5777222%2F" class="utility" data-id="5777222"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/ptuj-posest_5777222/" class="utility contact-tooltip" title="051/455-010<br />RE/MAX Poetovio, Nepremièninska družba d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas20" id="o5925799">
                        <h2><a href="/oglasi-prodaja/maribor-parmova-ulica-hisa_5925799/" title="5925799"><span class="title">MARIBOR, PARMOVA ULICA</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/maribor-parmova-ulica-hisa_5925799/"><img src="https://picbase.turbosist.si/slonep_oglasi2/3856948.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hiša</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Nadstropje: <strong>K+P+1</strong></span><span class="atribut">Leto: <strong>1965</strong></span><span class="atribut">Zemljišèe: <strong>497 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">236 m2, samostojna, zgrajena l. 1965, 497 m2 zemljišèa, K+P+1, prodamo. Cena: 200.000,00 EUR</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                236 m2, samostojna, zgrajena l. 1965, 497 m2 zemljišèa, K+P+1, prodamo. Cena: 200.000,00 EUR
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">236,00 m2</span><br />
                                <span class="cena">200.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Real integral d.o.o."><div class="logo"><a href="/oglasi-prodaja/maribor-parmova-ulica-hisa_5925799/"><img src="https://picbase.turbosist.si/slonep_agenc120/551.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5925799"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-5925799" href="#" data-id="5925799" onclick="save_ad(5925799); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmaribor-parmova-ulica-hisa_5925799%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmaribor-parmova-ulica-hisa_5925799%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmaribor-parmova-ulica-hisa_5925799%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmaribor-parmova-ulica-hisa_5925799%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="5925799"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmaribor-parmova-ulica-hisa_5925799%2F" class="utility" data-id="5925799"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/maribor-parmova-ulica-hisa_5925799/" class="utility contact-tooltip" title="02/252-65-79<br />Real integral d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas881" id="o5652784">
                        <h2><a href="/oglasi-prodaja/kamno-odlicna-lokacija-na-robu-vasi-hisa_5652784/" title="5652784"><span class="title">KAMNO, ODLIÈNA LOKACIJA NA ROBU VASI</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/kamno-odlicna-lokacija-na-robu-vasi-hisa_5652784/"><img src="https://picbase.turbosist.si/slonep_oglasi2/2266473.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hiša</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Leto: <strong>1988</strong></span><span class="atribut">Zemljišèe: <strong>4802 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">217 m2, samostojna, zgrajena l. 1988, adaptirana l. 2005, 4.802 m2 zemljišèa, Mirna in sonèna lokacija, dvorišèe pred hi...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                217 m2, samostojna, zgrajena l. 1988, adaptirana l. 2005, 4.802 m2 zemljišèa, Mirna in sonèna lokacija, dvorišèe pred hi...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">217,00 m2</span><br />
                                <span class="cena">200.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="REMAX Vogal, Nepremièninska družba, d.o.o."><div class="logo"><a href="/oglasi-prodaja/kamno-odlicna-lokacija-na-robu-vasi-hisa_5652784/"><img src="https://picbase.turbosist.si/slonep_agenc120/1297.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5652784"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-5652784" href="#" data-id="5652784" onclick="save_ad(5652784); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkamno-odlicna-lokacija-na-robu-vasi-hisa_5652784%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkamno-odlicna-lokacija-na-robu-vasi-hisa_5652784%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkamno-odlicna-lokacija-na-robu-vasi-hisa_5652784%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkamno-odlicna-lokacija-na-robu-vasi-hisa_5652784%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="5652784"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkamno-odlicna-lokacija-na-robu-vasi-hisa_5652784%2F" class="utility" data-id="5652784"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/kamno-odlicna-lokacija-na-robu-vasi-hisa_5652784/" class="utility contact-tooltip" title="030/248-247<br />REMAX Vogal, Nepremièninska družba, d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas291" id="o5793539">
                        <h2><a href="/oglasi-prodaja/vir-hisa_5793539/" title="5793539"><span class="title">VIR</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/vir-hisa_5793539/"><img src="https://picbase.turbosist.si/slonep_oglasi2/2992539.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hiša</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Leto: <strong>2013</strong></span><span class="atribut">Zemljišèe: <strong>254 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">175 m2, samostojna, adaptirana l. 2013, 254 m2 zemljišèa, Prodamo poèitniško hišo na otoku Vir, Zadar. Pogled na otok Pa...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                175 m2, samostojna, adaptirana l. 2013, 254 m2 zemljišèa, Prodamo poèitniško hišo na otoku Vir, Zadar. Pogled na otok Pa...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">175,00 m2</span><br />
                                <span class="cena">200.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="REMAX Vogal, Nepremièninska družba, d.o.o."><div class="logo"><a href="/oglasi-prodaja/vir-hisa_5793539/"><img src="https://picbase.turbosist.si/slonep_agenc120/1297.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5793539"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-5793539" href="#" data-id="5793539" onclick="save_ad(5793539); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fvir-hisa_5793539%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fvir-hisa_5793539%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fvir-hisa_5793539%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fvir-hisa_5793539%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="5793539"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fvir-hisa_5793539%2F" class="utility" data-id="5793539"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/vir-hisa_5793539/" class="utility contact-tooltip" title="041/617-066<br />REMAX Vogal, Nepremièninska družba, d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
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
            //]]>--></script><noscript><a href='https://ok.internetmedia.si/www/delivery/ck.php?n=a280490d&amp;cb=1480488659&amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5=' target='_blank'><img src='https://ok.internetmedia.si/www/delivery/avw.php?zoneid=5&amp;cb=1375679088&amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5=&amp;n=a280490d' border='0' alt='' /></a></noscript>
                </div>
            
                    <div class="oglas_container oglasbold oglas116" id="o5572213">
                        <h2><a href="/oglasi-prodaja/pula-medulin-hisa_5572213/" title="5572213"><span class="title">PULA, MEDULIN</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/pula-medulin-hisa_5572213/"><img src="https://picbase.turbosist.si/slonep_oglasi2/1879112.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hiša</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Leto: <strong>2008</strong></span><span class="atribut">Zemljišèe: <strong>179 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">117 m2, samostojna, novogradnja - zgr. l. 2008, 179 m2 zemljišèa, Zelo blizu morja(caa.900m)se nahaja izjemna nova hiša ...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                117 m2, samostojna, novogradnja - zgr. l. 2008, 179 m2 zemljišèa, Zelo blizu morja(caa.900m)se nahaja izjemna nova hiša ...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">117,00 m2</span><br />
                                <span class="cena">200.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="REMAX Vogal, Nepremièninska družba, d.o.o."><div class="logo"><a href="/oglasi-prodaja/pula-medulin-hisa_5572213/"><img src="https://picbase.turbosist.si/slonep_agenc120/1297.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5572213"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-5572213" href="#" data-id="5572213" onclick="save_ad(5572213); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fpula-medulin-hisa_5572213%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fpula-medulin-hisa_5572213%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fpula-medulin-hisa_5572213%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fpula-medulin-hisa_5572213%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="5572213"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fpula-medulin-hisa_5572213%2F" class="utility" data-id="5572213"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/pula-medulin-hisa_5572213/" class="utility contact-tooltip" title="070/900-340<br />REMAX Vogal, Nepremièninska družba, d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas461" id="o5617741">
                        <h2><a href="/oglasi-prodaja/pula-vodnjan-pritlicna-hisa-ugodno-hisa_5617741/" title="5617741"><span class="title">PULA, VODNJAN, PRITLIÈNA HIŠA, UGODNO</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/pula-vodnjan-pritlicna-hisa-ugodno-hisa_5617741/"><img src="https://picbase.turbosist.si/slonep_oglasi2/2081618.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hiša</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Leto: <strong>2009</strong></span><span class="atribut">Zemljišèe: <strong>459 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">147 m2, samostojna, novogradnja - zgr. l. 2009, 459 m2 zemljišèa, Na obrobju Vodnjana se v mirnem okolju nahaja èudovita...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                147 m2, samostojna, novogradnja - zgr. l. 2009, 459 m2 zemljišèa, Na obrobju Vodnjana se v mirnem okolju nahaja èudovita...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">147,00 m2</span><br />
                                <span class="cena">200.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="REMAX Vogal, Nepremièninska družba, d.o.o."><div class="logo"><a href="/oglasi-prodaja/pula-vodnjan-pritlicna-hisa-ugodno-hisa_5617741/"><img src="https://picbase.turbosist.si/slonep_agenc120/1297.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5617741"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-5617741" href="#" data-id="5617741" onclick="save_ad(5617741); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fpula-vodnjan-pritlicna-hisa-ugodno-hisa_5617741%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fpula-vodnjan-pritlicna-hisa-ugodno-hisa_5617741%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fpula-vodnjan-pritlicna-hisa-ugodno-hisa_5617741%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fpula-vodnjan-pritlicna-hisa-ugodno-hisa_5617741%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="5617741"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fpula-vodnjan-pritlicna-hisa-ugodno-hisa_5617741%2F" class="utility" data-id="5617741"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/pula-vodnjan-pritlicna-hisa-ugodno-hisa_5617741/" class="utility contact-tooltip" title="070/900-340<br />REMAX Vogal, Nepremièninska družba, d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas371" id="o6022840">
                        <h2><a href="/oglasi-prodaja/lj-bezigrad-zupanciceva-jama-poslovni-prostor_6022840/" title="6022840"><span class="title">LJ. BEŽIGRAD, ŽUPANÈIÈEVA JAMA</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/lj-bezigrad-zupanciceva-jama-poslovni-prostor_6022840/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4582259.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Poslovni prostor</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Nadstropje: <strong>P</strong></span><span class="atribut">Leto: <strong>1990</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">131 m2, pisarna, zgrajena l. 1990, pritlièje, Na odlièni lokaciji v Županèièevi jami se nahaja odlièen poslovni prostor,...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                131 m2, pisarna, zgrajena l. 1990, pritlièje, Na odlièni lokaciji v Županèièevi jami se nahaja odlièen poslovni prostor,...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">131,00 m2</span><br />
                                <span class="cena">200.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Rocco nepremiènine d.o.o."><div class="logo"><a href="/oglasi-prodaja/lj-bezigrad-zupanciceva-jama-poslovni-prostor_6022840/"><img src="https://picbase.turbosist.si/slonep_agenc120/1883.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="6022840"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-6022840" href="#" data-id="6022840" onclick="save_ad(6022840); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-bezigrad-zupanciceva-jama-poslovni-prostor_6022840%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-bezigrad-zupanciceva-jama-poslovni-prostor_6022840%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-bezigrad-zupanciceva-jama-poslovni-prostor_6022840%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-bezigrad-zupanciceva-jama-poslovni-prostor_6022840%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="6022840"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-bezigrad-zupanciceva-jama-poslovni-prostor_6022840%2F" class="utility" data-id="6022840"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/lj-bezigrad-zupanciceva-jama-poslovni-prostor_6022840/" class="utility contact-tooltip" title="040/867-847<br />Rocco nepremiènine d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas303" id="o6037690">
                        <h2><a href="/oglasi-prodaja/kranj-blizina-mesta-hisa_6037690/" title="6037690"><span class="title">KRANJ, BLIŽINA MESTA</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/kranj-blizina-mesta-hisa_6037690/"><img src="/images/n-2.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hiša</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Nadstropje: <strong>P+1</strong></span><span class="atribut">Leto: <strong>1982</strong></span><span class="atribut">Zemljišèe: <strong>424 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">200 m2, samostojna, zgrajena l. 1982, adaptirana l. 2005, 424 m2 zemljišèa, P+1, Kranj - Bližina mesta, Samostojne hiša ...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                200 m2, samostojna, zgrajena l. 1982, adaptirana l. 2005, 424 m2 zemljišèa, P+1, Kranj - Bližina mesta, Samostojne hiša ...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">200,00 m2</span><br />
                                <span class="cena">200.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Oaza nepremiènine d.o.o."><div class="logo"><a href="/oglasi-prodaja/kranj-blizina-mesta-hisa_6037690/"><img src="https://picbase.turbosist.si/slonep_agenc120/602.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="6037690"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-6037690" href="#" data-id="6037690" onclick="save_ad(6037690); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkranj-blizina-mesta-hisa_6037690%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkranj-blizina-mesta-hisa_6037690%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkranj-blizina-mesta-hisa_6037690%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkranj-blizina-mesta-hisa_6037690%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="6037690"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkranj-blizina-mesta-hisa_6037690%2F" class="utility" data-id="6037690"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/kranj-blizina-mesta-hisa_6037690/" class="utility contact-tooltip" title="0590/22-512<br />Oaza nepremiènine d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas473" id="o6022521">
                        <h2><a href="/oglasi-prodaja/sveti-lovrec-pazenaticki-hisa_6022521/" title="6022521"><span class="title">SVETI LOVREÈ PAZENATIÈKI</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/sveti-lovrec-pazenaticki-hisa_6022521/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4579409.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hiša</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Nadstropje: <strong>K+P+1</strong></span><span class="atribut">Leto: <strong>1967</strong></span><span class="atribut">Zemljišèe: <strong>4126 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">230 m2, samostojna, zgrajena l. 1967, 4.126 m2 zemljišèa, K+P+1, prodamo. Cena: 200.000,00 EUR</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                230 m2, samostojna, zgrajena l. 1967, 4.126 m2 zemljišèa, K+P+1, prodamo. Cena: 200.000,00 EUR
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">230,00 m2</span><br />
                                <span class="cena">200.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Panorama Real Estate d.o.o."><div class="logo"><a href="/oglasi-prodaja/sveti-lovrec-pazenaticki-hisa_6022521/"><img src="https://picbase.turbosist.si/slonep_agenc120/2165.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="6022521"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-6022521" href="#" data-id="6022521" onclick="save_ad(6022521); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsveti-lovrec-pazenaticki-hisa_6022521%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsveti-lovrec-pazenaticki-hisa_6022521%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsveti-lovrec-pazenaticki-hisa_6022521%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsveti-lovrec-pazenaticki-hisa_6022521%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="6022521"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsveti-lovrec-pazenaticki-hisa_6022521%2F" class="utility" data-id="6022521"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/sveti-lovrec-pazenaticki-hisa_6022521/" class="utility contact-tooltip" title="+385 95 8278253<br />Panorama Real Estate d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas334" id="o5936254">
                        <h2><a href="/oglasi-prodaja/klimno-200-m-od-morja-posest_5936254/" title="5936254"><span class="title">KLIMNO, 200 M OD MORJA</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/klimno-200-m-od-morja-posest_5936254/"><img src="https://picbase.turbosist.si/slonep_oglasi2/3935993.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Posest</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">2.000 m2, zazidljiva, Otok Krk, Soline, gradbeno zemljišèe s pogledom na morje, atraktivna lokacija le 200 m od morja, p...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                2.000 m2, zazidljiva, Otok Krk, Soline, gradbeno zemljišèe s pogledom na morje, atraktivna lokacija le 200 m od morja, p...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">2.000,00 m2</span><br />
                                <span class="cena">100,00 &euro;/m2</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Premium SM d.o.o."><div class="logo"><a href="/oglasi-prodaja/klimno-200-m-od-morja-posest_5936254/"><img src="https://picbase.turbosist.si/slonep_agenc120/2242.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5936254"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-5936254" href="#" data-id="5936254" onclick="save_ad(5936254); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fklimno-200-m-od-morja-posest_5936254%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fklimno-200-m-od-morja-posest_5936254%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fklimno-200-m-od-morja-posest_5936254%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fklimno-200-m-od-morja-posest_5936254%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="5936254"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fklimno-200-m-od-morja-posest_5936254%2F" class="utility" data-id="5936254"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/klimno-200-m-od-morja-posest_5936254/" class="utility contact-tooltip" title="+385 51 858364<br />Premium SM d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
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
            //]]>--></script><noscript><a href='https://ok.internetmedia.si/www/delivery/ck.php?n=a280490d&amp;cb=99376967&amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5=' target='_blank'><img src='https://ok.internetmedia.si/www/delivery/avw.php?zoneid=5&amp;cb=149190180&amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5=&amp;n=a280490d' border='0' alt='' /></a></noscript>
                </div>
            
                    <div class="oglas_container oglasbold oglas413" id="o6019607">
                        <h2><a href="/oglasi-prodaja/silba-hisa_6019607/" title="6019607"><span class="title">SILBA</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/silba-hisa_6019607/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4556332.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hiša</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Leto: <strong>1890</strong></span><span class="atribut">Zemljišèe: <strong>120 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">132 m2, dvojèek, zgrajen l. 1890, adaptiran l. 2006, 120 m2 zemljišèa, prodamo. Cena: 200.000,00 EUR</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                132 m2, dvojèek, zgrajen l. 1890, adaptiran l. 2006, 120 m2 zemljišèa, prodamo. Cena: 200.000,00 EUR
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">132,00 m2</span><br />
                                <span class="cena">200.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Novi list d.o.o."><div class="logo"><a href="/oglasi-prodaja/silba-hisa_6019607/"><img src="https://picbase.turbosist.si/slonep_agenc120/707.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="6019607"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-6019607" href="#" data-id="6019607" onclick="save_ad(6019607); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsilba-hisa_6019607%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsilba-hisa_6019607%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsilba-hisa_6019607%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsilba-hisa_6019607%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="6019607"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsilba-hisa_6019607%2F" class="utility" data-id="6019607"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/silba-hisa_6019607/" class="utility contact-tooltip" title="051/622-444<br />Novi list d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas211" id="o6043409">
                        <h2><a href="/oglasi-prodaja/grosuplje-do-centra-2-km-hisa_6043409/" title="6043409"><span class="title">GROSUPLJE, DO CENTRA 2 KM</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/grosuplje-do-centra-2-km-hisa_6043409/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4755714.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hiša</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Nadstropje: <strong>K+P+1</strong></span><span class="atribut">Leto: <strong>1952</strong></span><span class="atribut">Zemljišèe: <strong>789 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">250 m2, samostojna, zgrajena l. 1952, adaptirana l. 1999, 789 m2 zemljišèa, K+P+1, prodamo. Cena: 200.000,00 EUR</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                250 m2, samostojna, zgrajena l. 1952, adaptirana l. 1999, 789 m2 zemljišèa, K+P+1, prodamo. Cena: 200.000,00 EUR
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">250,00 m2</span><br />
                                <span class="cena">200.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Roni nepremiènine d.o.o."><div class="logo"><a href="/oglasi-prodaja/grosuplje-do-centra-2-km-hisa_6043409/"><img src="https://picbase.turbosist.si/slonep_agenc120/1451.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="6043409"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-6043409" href="#" data-id="6043409" onclick="save_ad(6043409); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fgrosuplje-do-centra-2-km-hisa_6043409%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fgrosuplje-do-centra-2-km-hisa_6043409%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fgrosuplje-do-centra-2-km-hisa_6043409%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fgrosuplje-do-centra-2-km-hisa_6043409%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="6043409"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fgrosuplje-do-centra-2-km-hisa_6043409%2F" class="utility" data-id="6043409"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/grosuplje-do-centra-2-km-hisa_6043409/" class="utility contact-tooltip" title="041/707-284<br />Roni nepremiènine d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas265" id="o5819767">
                        <h2><a href="/oglasi-prodaja/dole-pri-litiji-selce-hisa_5819767/" title="5819767"><span class="title">DOLE PRI LITIJI, SELCE</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/dole-pri-litiji-selce-hisa_5819767/"><img src="https://picbase.turbosist.si/slonep_oglasi2/3146077.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hiša</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Leto: <strong>1996</strong></span><span class="atribut">Zemljišèe: <strong>62.67 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">300 m2, samostojna, zgrajena l. 1996, 62,67 m2 zemljišèa, CENA ZNIŽANA Z 225000 EUR NA 202500 EUR. Kmeèka hiša leži na s...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                300 m2, samostojna, zgrajena l. 1996, 62,67 m2 zemljišèa, CENA ZNIŽANA Z 225000 EUR NA 202500 EUR. Kmeèka hiša leži na s...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">300,00 m2</span><br />
                                <span class="cena">200.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Think Slovenia, TS1 d.o.o."><div class="logo"><a href="/oglasi-prodaja/dole-pri-litiji-selce-hisa_5819767/"><img src="https://picbase.turbosist.si/slonep_agenc120/325.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5819767"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-5819767" href="#" data-id="5819767" onclick="save_ad(5819767); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fdole-pri-litiji-selce-hisa_5819767%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fdole-pri-litiji-selce-hisa_5819767%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fdole-pri-litiji-selce-hisa_5819767%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fdole-pri-litiji-selce-hisa_5819767%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="5819767"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fdole-pri-litiji-selce-hisa_5819767%2F" class="utility" data-id="5819767"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/dole-pri-litiji-selce-hisa_5819767/" class="utility contact-tooltip" title="051/725-345<br />Think Slovenia, TS1 d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas433" id="o5936066">
                        <h2><a href="/oglasi-prodaja/krk-stanovanje_5936066/" title="5936066"><span class="title">KRK</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/krk-stanovanje_5936066/"><img src="https://picbase.turbosist.si/slonep_oglasi2/3934411.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Stanovanje</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Nadstropje: <strong>1</strong>/2</span><span class="atribut">Leto: <strong>2014</strong></span><span class="atribut">Zemljišèe: <strong>60 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">88 m2, 3-sobno, zgrajeno l. 2014, 60 m2 zemljišèa, 1/2 nad., prodamo. Cena: max. 200.000,00 EUR</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                88 m2, 3-sobno, zgrajeno l. 2014, 60 m2 zemljišèa, 1/2 nad., prodamo. Cena: max. 200.000,00 EUR
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">88,00 m2</span><br />
                                <span class="cena">200.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Vitus d.o.o."><div class="logo"><a href="/oglasi-prodaja/krk-stanovanje_5936066/"><img src="https://picbase.turbosist.si/slonep_agenc120/130.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5936066"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-5936066" href="#" data-id="5936066" onclick="save_ad(5936066); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkrk-stanovanje_5936066%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkrk-stanovanje_5936066%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkrk-stanovanje_5936066%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkrk-stanovanje_5936066%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="5936066"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkrk-stanovanje_5936066%2F" class="utility" data-id="5936066"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/krk-stanovanje_5936066/" class="utility contact-tooltip" title="+385 51 858 405<br />Vitus d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas233" id="o5934550">
                        <h2><a href="/oglasi-prodaja/kras-hisa_5934550/" title="5934550"><span class="title">KRAS</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/kras-hisa_5934550/"><img src="https://picbase.turbosist.si/slonep_oglasi2/3923917.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hiša</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Nadstropje: <strong>P+1+2</strong></span><span class="atribut">Leto: <strong>1900</strong></span><span class="atribut">Zemljišèe: <strong>1404 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">108 m2, dvojèek, zgrajen l. 1900, 1.404 m2 zemljišèa, P+1+2, prodamo. Cena: max. 200.000,00 EUR</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                108 m2, dvojèek, zgrajen l. 1900, 1.404 m2 zemljišèa, P+1+2, prodamo. Cena: max. 200.000,00 EUR
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">108,00 m2</span><br />
                                <span class="cena">200.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Vitus d.o.o."><div class="logo"><a href="/oglasi-prodaja/kras-hisa_5934550/"><img src="https://picbase.turbosist.si/slonep_agenc120/130.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5934550"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-5934550" href="#" data-id="5934550" onclick="save_ad(5934550); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkras-hisa_5934550%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkras-hisa_5934550%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkras-hisa_5934550%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkras-hisa_5934550%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="5934550"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkras-hisa_5934550%2F" class="utility" data-id="5934550"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/kras-hisa_5934550/" class="utility contact-tooltip" title="+385 51 858 405<br />Vitus d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas124" id="o5940008">
                        <h2><a href="/oglasi-prodaja/kras-hisa_5940008/" title="5940008"><span class="title">KRAS</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/kras-hisa_5940008/"><img src="https://picbase.turbosist.si/slonep_oglasi2/3962969.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hiša</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Nadstropje: <strong>P+1</strong></span><span class="atribut">Leto: <strong>2012</strong></span><span class="atribut">Zemljišèe: <strong>420 m2</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">120 m2, dvojèek, zgrajen l. 2012, 420 m2 zemljišèa, P+1, KRAS, 120 m2, dvojèek, zaè. grad. l. 2012,300 m2 zemljišèa, pro...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                120 m2, dvojèek, zgrajen l. 2012, 420 m2 zemljišèa, P+1, KRAS, 120 m2, dvojèek, zaè. grad. l. 2012,300 m2 zemljišèa, pro...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">120,00 m2</span><br />
                                <span class="cena">200.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Vitus d.o.o."><div class="logo"><a href="/oglasi-prodaja/kras-hisa_5940008/"><img src="https://picbase.turbosist.si/slonep_agenc120/130.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5940008"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-5940008" href="#" data-id="5940008" onclick="save_ad(5940008); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkras-hisa_5940008%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkras-hisa_5940008%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkras-hisa_5940008%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkras-hisa_5940008%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="5940008"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkras-hisa_5940008%2F" class="utility" data-id="5940008"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/kras-hisa_5940008/" class="utility contact-tooltip" title="+385 51 858 405<br />Vitus d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
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
            //]]>--></script><noscript><a href='https://ok.internetmedia.si/www/delivery/ck.php?n=a280490d&amp;cb=103900872&amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5=' target='_blank'><img src='https://ok.internetmedia.si/www/delivery/avw.php?zoneid=5&amp;cb=1040812326&amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5=&amp;n=a280490d' border='0' alt='' /></a></noscript>
                </div>
            
                    <div class="oglas_container oglasbold oglas719" id="o5943908">
                        <h2><a href="/oglasi-prodaja/krk-stanovanje_5943908/" title="5943908"><span class="title">KRK</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/krk-stanovanje_5943908/"><img src="https://picbase.turbosist.si/slonep_oglasi2/3992196.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Stanovanje</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Nadstropje: <strong>2</strong>/2</span><span class="atribut">Leto: <strong>2014</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">88 m2, stanovanje, zgrajeno l. 2014, 2/2 nad., prodamo. Cena: max. 200.000,00 EUR</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                88 m2, stanovanje, zgrajeno l. 2014, 2/2 nad., prodamo. Cena: max. 200.000,00 EUR
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">88,00 m2</span><br />
                                <span class="cena">200.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Vitus d.o.o."><div class="logo"><a href="/oglasi-prodaja/krk-stanovanje_5943908/"><img src="https://picbase.turbosist.si/slonep_agenc120/130.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5943908"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-5943908" href="#" data-id="5943908" onclick="save_ad(5943908); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkrk-stanovanje_5943908%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkrk-stanovanje_5943908%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkrk-stanovanje_5943908%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkrk-stanovanje_5943908%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="5943908"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkrk-stanovanje_5943908%2F" class="utility" data-id="5943908"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/krk-stanovanje_5943908/" class="utility contact-tooltip" title="+385 51 858 405<br />Vitus d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas289" id="o5898703">
                        <h2><a href="/oglasi-prodaja/krk-okolica-na-mirni-lokaciji-hisa_5898703/" title="5898703"><span class="title">KRK, OKOLICA, NA MIRNI LOKACIJI</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/krk-okolica-na-mirni-lokaciji-hisa_5898703/"><img src="https://picbase.turbosist.si/slonep_oglasi2/3665096.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hiša</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Nadstropje: <strong>P+1</strong></span><span class="atribut">Leto: <strong>2015</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">140,49 m2, dvojèek, novogradnja - zgr. l. 2015, P+1, prodaja novo hišo 140,49 m2 na mirni lokaciji. Hiša je sestavljena ...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                140,49 m2, dvojèek, novogradnja - zgr. l. 2015, P+1, prodaja novo hišo 140,49 m2 na mirni lokaciji. Hiša je sestavljena ...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">140,49 m2</span><br />
                                <span class="cena">200.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Vitus d.o.o."><div class="logo"><a href="/oglasi-prodaja/krk-okolica-na-mirni-lokaciji-hisa_5898703/"><img src="https://picbase.turbosist.si/slonep_agenc120/130.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5898703"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-5898703" href="#" data-id="5898703" onclick="save_ad(5898703); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkrk-okolica-na-mirni-lokaciji-hisa_5898703%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkrk-okolica-na-mirni-lokaciji-hisa_5898703%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkrk-okolica-na-mirni-lokaciji-hisa_5898703%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkrk-okolica-na-mirni-lokaciji-hisa_5898703%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="5898703"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkrk-okolica-na-mirni-lokaciji-hisa_5898703%2F" class="utility" data-id="5898703"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/krk-okolica-na-mirni-lokaciji-hisa_5898703/" class="utility contact-tooltip" title="+385 51 858 405<br />Vitus d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                
                    <div class="oglas_container oglasbold oglas752" id="o5899611">
                        <h2><a href="/oglasi-prodaja/krk-okolica-na-mirni-lokaciji-hisa_5899611/" title="5899611"><span class="title">KRK, OKOLICA, NA MIRNI LOKACIJI</span></a></h2>
                        <a class="slika" href="/oglasi-prodaja/krk-okolica-na-mirni-lokaciji-hisa_5899611/"><img src="https://picbase.turbosist.si/slonep_oglasi2/3671670.jpg" /><div class="vec"></div></a>
                        <div class="teksti_container">
                            <span class="posr">Prodaja: Hiša</span>
                            <!--<div class="new-container">
                            
                            </div>-->
                            <div class="atributi">
                                <span class="atribut">Nadstropje: <strong>P+1</strong></span><span class="atribut">Leto: <strong>2015</strong></span>
                            </div>
                            <!---->
                            

                            <div class="kratek_container">
                                <div class="kratek">140 m2, dvojèek, novogradnja - zgr. l. 2015, P+1, prodaja novo hišo v gradnji od 140,09 m2 na mirni lokaciji. Hiša je se...</div>
                            </div>
                            <!--<div class="kratek_container">
                                <table>
                                <tr>
                                <td>
                                140 m2, dvojèek, novogradnja - zgr. l. 2015, P+1, prodaja novo hišo v gradnji od 140,09 m2 na mirni lokaciji. Hiša je se...
                                </td>
                                </tr>
                                </table>
                            </div>-->

                            <div class="main-data">
                                <span class="velikost">140,00 m2</span><br />
                                <span class="cena">200.000,00 &euro;</span>
                            </div>
                        </div>
                        <div class="logo_container">
                            <div class="povezave">
                                <div class="prodajalec_o" title="Vitus d.o.o."><div class="logo"><a href="/oglasi-prodaja/krk-okolica-na-mirni-lokaciji-hisa_5899611/"><img src="https://picbase.turbosist.si/slonep_agenc120/130.jpg?v=20161017" /></a></div></div>
                            </div>
                            <div class="clearer"></div>
                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5899611"></span>-->
                            <a class="ikona-sh3 utility" id="save-ad-5899611" href="#" data-id="5899611" onclick="save_ad(5899611); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>
                            <span class="utility" style="cursor: default;">
                                <i class="fa fa-share-square-o"></i>Deli na:
                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkrk-okolica-na-mirni-lokaciji-hisa_5899611%2F"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"
   target="_blank" title="Facebook">-->
                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkrk-okolica-na-mirni-lokaciji-hisa_5899611%2F', 'Facebook',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-facebook-square"></i>
                                </a>
                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkrk-okolica-na-mirni-lokaciji-hisa_5899611%2F', 'Twitter',600,300);" href="javascript:void(0);">
                                    <i class="fa fa-twitter"></i>
                                </a>
                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkrk-okolica-na-mirni-lokaciji-hisa_5899611%2F', 'Google',500,350);" href="javascript:void(0);">
                                    <i class="fa fa-google-plus-square"></i>
                                </a>
                            </span>
                            <!--<a class="utility" data-id="5899611"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->
                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkrk-okolica-na-mirni-lokaciji-hisa_5899611%2F" class="utility" data-id="5899611"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Pošlji prijatelju</span></a>
                            <a href="/oglasi-prodaja/krk-okolica-na-mirni-lokaciji-hisa_5899611/" class="utility contact-tooltip" title="+385 51 858 405<br />Vitus d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>
                        </div>
                        <div class="clearer"></div>
                    </div>
                </div><div class="spacer"></div><div id="pagination" class="fr"><ul>
                    <li><a href="/oglasi-prodaja/cena-do-200000-eur/?s=13" class="first"><<</a></li>
                    <li><a href="/oglasi-prodaja/cena-do-200000-eur/?s=13" class="prev"><</a></li>
                <li><a href="/oglasi-prodaja/cena-do-200000-eur/?s=13">1</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/2/?s=13" class="active">2</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/3/?s=13">3</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/4/?s=13">4</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/5/?s=13">5</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/6/?s=13">6</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/7/?s=13">7</a></li><span class="dots3">...</span><li><a href="/oglasi-prodaja/cena-do-200000-eur/3/?s=13" class="next">></a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/652/?s=13" class="last">>></a></li></ul></div>
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



