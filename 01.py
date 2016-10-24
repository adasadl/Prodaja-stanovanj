<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "https://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

<html xmlns="https://www.w3.org/1999/xhtml" lang="sl">

<head>

<link rel="canonical" href="/oglasi-prodaja/ljubljana-mesto/stanovanje/cena-do-200000-eur/1/" /><meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

<meta http-equiv="content-language" content="sl" />

<meta name="msvalidate.01" content="D9C9544A6631C60218BF47FD618F42E5" />



<meta http-equiv="X-UA-Compatible" content="IE=EDGE" />

<meta name="SKYPE_TOOLBAR" content="SKYPE_TOOLBAR_PARSER_COMPATIBLE" />

<meta name="format-detection" content="telephone=no">

<title>Prodaja </title>

<meta name="Keywords" content="" />

<meta name="Description" content="Rezultati iskanja nepremi?nin: Prodaja  na Nepremicnine.net" />

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

                    $("#toperr").css("display", "block").append('<div class="msgE">Nimate omogo?enih pi?kotkov (cookies). Uporaba je omejena.</div>')

                },

                success: function(data){

                    if (data != '') {

                        //$("#nocookie div").removeClass('msgE').addClass('msgI');

                        //$("#nocookie div").replaceWith('<div class="msgI">Pozdravljeni na strani Nepremicnine.net.</div>')

                    } else {

                        $("#toperr").css("display", "block").append('<div class="msgE">Nimate omogo?enih pi?kotkov (cookies). Uporaba je omejena.</div>')

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

            $('#notification-message a').webuiPopover({title:'<i class="fa fa-envelope"></i> &nbsp; Sporo?ila',content:'Content',width:250,height:200,placement:'bottom-left',type:'async',url:'/jq/popover_messages.php',cache:false,closeable:true});



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

                <li><a href="http://www.montazne-hise.net" target="_blank">monta?ne hi?e</a></li>

                <li><a href="http://www.podsvojostreho.net" target="_blank">pod<span class="svojo">svojo</span>streho.net</a></li>

                <li><a href="http://www.novogradnje.si" target="_blank">novogradnje.si</a></li>

                <!--<li><a href="http://www.nepremicninar.com" target="_blank">nepremicninar.com</a></li>-->

                                                <li><a class="lang" href="http://www.realestate-slovenia.info/">

                                        <img src="/images/vector-flags/gb.svg" style="height: 18px;">

                                    </a></li>

                                <li><!--<a class="last" href="http://www.facebook.com/pages/NEPREMICNINEnet/181757358510072" target="_blank" title="NEPREMICNINE.net na Facebook-u"><img src="/images/ikona-fb.png" alt="Nepremicnine.net FB" /></a>-->

                    <div class="fb-like" data-href="https://www.facebook.com/NEPREMICNINEnet-181757358510072/" data-colorscheme="light" data-layout="button_count" data-action="like" data-show-faces="false" data-share="false"></div>

                </li>

                <!--<li><a href="/profil.html?m=so&s=37" class="blink last">SPORO?ILO</a></li>-->

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

        <p class="slide"><a href="/profil.html" name="moje-nep" class="btn-slide">Moje nepremi?nine</a></p>            </div>

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

<iframe id='a4e1c538' name='a4e1c538' src='https://ok.internetmedia.si/www/delivery/afr.php?zoneid=1&amp;target=_blank&amp;charset=UTF-8&amp;cb=809413712&amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5=' frameborder='0' scrolling='no' width='960' height='150'><a href='https://ok.internetmedia.si/www/delivery/ck.php?n=a0fcbf0c&amp;cb=1761716090&amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5=' target='_blank'><img src='https://ok.internetmedia.si/www/delivery/avw.php?zoneid=1&amp;charset=UTF-8&amp;cb=319821666&amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5=&amp;n=a0fcbf0c' border='0' alt='' /></a></iframe>

            </div></div>

        <div class="clearer"></div>



        <div id="content">

                        <div id="header-top">

                                <div id="logo">

                    <a href="/"><img src="/images/logo.gif" width="297" height="37" title="Nepremi?nine, sredi??e ponudbe nepremi?nin v Sloveniji, agencije za nepremi?nine, novogradnje..." alt="Nepremi?nine, sredi??e ponudbe nepremi?nin v Sloveniji, agencije za posredovanje nepremi?nin, novogradnje..." />

                    <strong>Najve?ji slovenski nepremi?ninski portal</strong></a>

                </div>

                <div id="slogan"></div>

                <div id="iskalnik-hitroiskanje" class="ui-widget">

                                        <form action="/nepremicnine.html" method="get" name="searcher" accept-charset="utf-8">

                        <input type="text" name="q" id="hitroiskanje" value="" title="npr. hi?a bled atrij, ref. ?t. oglasa ..." size="30" maxlength="160" onclick="if (searcher.q.value.substring(0,3) == 'npr') searcher.q.value='';" />

                        <input type="submit" id="hitroiskanjepotrdi" value="" width="31" height="32" onclick="if ( searcher.q.value=='npr. hi?a bled atrij, ref. ?t. oglasa ...' ) return false;" />

                    </form>

                </div>

            </div>

            <div id="header">

                <div id="menu">

                    <ul>

                        <li class="first"><a href="/">nepremi?nine</a></li>

                                                <li class="iskalnik">

                            <div class="menuitem"><a href="#" id="fqrun" class="active">ISKALNIK</a></div>

                            <ul>

	<li>

		<div class="levo">

						<form name="NOsearch" id="NOsearch" action="/nepremicnine.html" class="" method="get">

				<div id="loading">Loading ...</div>

				<table width="350" border="0" cellpadding="3" cellspacing="0">

					<tr>

						<td class="td-levo"><strong>Dr?ava</strong></td>

						<td class="td-desno">

							<input type="radio" class="radio" id="NOd197" name="d" value="197" checked="checked">

							<label for="NOd197" class="radio">Slovenija</label>

							<input type="radio" class="radio" id="NOd55" name="d" value="55" >

							<label for="NOd55" class="radio">Hrva?ka</label>

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

						<td class="td-levo"><strong>Nepremi?nina</strong></td>

						<td class="td-desno">

														<select name="n" id="NOn">

								<option value="1">Stanovanje</option><option value="2">Hi?a</option><option value="4">Vikend</option><option value="3">Posest</option><option value="5">Poslovni prostor</option><option value="6">Gara?a</option><option value="7">Po?itni?ki objekt</option>								</select>

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

							<!--<input type="submit" id="NOsubmit" class="gumb potrdi" value="Prika?i rezultate" />-->

							<a  class="gumb potrdi" href="/oglasi-prodaja/ljubljana-mesto/stanovanje/">Prika?i rezultate</a>

						</td>

					</tr>

				</table>

			</form>

		</div>

		<ul class="desno">

			<li><a href="/ne-spreglejte.html" class="isk-nespreglejte">ne spreglejte</a></li>

			<li><a href="/24ur.html" class="isk-v24ur">24 ur</a></li>

			<li><a href="/znizane-cene.html" class="isk-znizano">zni?ane cene</a></li>

					<li><a href="/nepremicnine-vpis.html?v=1" class="isk-vpis">vpis oglasa</a></li>

			<li><a href="/infonep.html" class="isk-obv">obve??ajte me</a></li>

					<li><a href="/profil.html?m=si" class="isk-si">shranjena iskanja</a></li>

			<li><a href="/profil.html?m=so" class="isk-so">shranjeni oglasi</a></li>

			<li><a href="/javne-drazbe.html" class="isk-jd">javne dra?be</a></li>

			<li><a href="/za-studente.html" class="isk-stu">za ?tudente</a></li>

		</ul>

	</li>

</ul>

                        </li>

                        <li class="nav-novogradnje"><a href="/novogradnje.html">Novogradnje</a></li><li class="nav-javne-drazbe"><a href="/javne-drazbe.html">Javne dra?be</a></li><li class="nav-montazne-hise"><a href="/montazne-hise.html">Monta?ne hi?e</a></li><li class="nav-pocitniski-objekti"><a href="/pocitniski-objekti.html">Na po?itnice!</a></li><li class="nav-dom-in-gradnja"><a href="/dom-in-gradnja.html">Dom in gradnja</a></li><li class="nav-nepremicninske-agencije"><a href="/nepremicninske-agencije.html">Podjetja</a></li><li class="nav-energetska-izkaznica"><a href="/energetska-izkaznica.html">E. izkaznica</a></li><li class="nav-trendi"><a href="/trendi.html">Trendi</a></li>                    </ul>

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

                    //data: "wpg=nepremicnine&p=1&arg[]=ljubljana-mesto&arg[]=stanovanje&arg[]=cena-do-200000-eur&pg=1&s=13&uid=", // data to send to above script page if any

                    data: "wpg=nepremicnine&p=1&arg%5B0%5D=ljubljana-mesto&arg%5B1%5D=stanovanje&arg%5B2%5D=cena-do-200000-eur&pg=1&s=13&c2=200000&uid=", // data to send to above script page if any

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

        ?t. ustreznih oglasov: <strong>19532</strong><br />    <!--<form action="/nepremicnine.html" method="get" id="sform" name="sform" accept-charset="utf-8">-->

        <form action="/jq/search.php?wpg=nepremicnine&red=1" method="post" id="sform" name="sform" accept-charset="utf-8">

        

                    <a name=""></a><h3>+ Klju?ne besede</h3>

                    <input type="text" name="q" id="q" class="mini" style="width:185px; float: left;" value="" size="30" maxlength="60">

                    <input type="submit" class="fsearch" value=">" /><br />

                <a name=""></a><h3>Osnovni parametri</h3><select name="d" id="dd" class="invisible" onchange="sform.submit()"><option value="0">Vse dr?ave</option><option value="197">Slovenija</option><option value="55">Hrva?ka</option><option value="999">Ostale</option></select><div class="dropdownWrapper">

                          <div class="dropdownLabel">Vse dr?ave<i class="fa fa-caret-down" aria-hidden="true"></i></div>

                          <div class="dropdownPanel">

                            <a href="/oglasi-prodaja/cena-do-200000-eur/?s=13">Vse dr?ave</a><a href="/oglasi-prodaja/slovenija/cena-do-200000-eur/?s=13">Slovenija</a><a href="/oglasi-prodaja/hrvaska/cena-do-200000-eur/?s=13">Hrva?ka</a><a href="/oglasi-prodaja/ostale-drzave/cena-do-200000-eur/?s=13">Ostale</a>

                          </div>

                        </div>

        <select name="n" id="n" class="invisible" onchange="sform.submit()"><option value="0">Vse nepremi?nine</option><option value="1">Stanovanje</option><option value="2">Hi?a</option><option value="4">Vikend</option><option value="3">Posest</option><option value="5">Poslovni prostor</option><option value="6">Gara?a</option><option value="7">Po?itni?ki objekt</option></select><div class="dropdownWrapper">

                          <div class="dropdownLabel">Vse nepremi?nine<i class="fa fa-caret-down" aria-hidden="true"></i></div>

                          <div class="dropdownPanel">

                            <a href="/oglasi-prodaja/cena-do-200000-eur/?s=13">Vse nepremi?nine</a><a href="/oglasi-prodaja/stanovanje/cena-do-200000-eur/?s=13">Stanovanje</a><a href="/oglasi-prodaja/hisa/cena-do-200000-eur/?s=13">Hi?a</a><a href="/oglasi-prodaja/vikend/cena-do-200000-eur/?s=13">Vikend</a><a href="/oglasi-prodaja/posest/cena-do-200000-eur/?s=13">Posest</a><a href="/oglasi-prodaja/poslovni-prostor/cena-do-200000-eur/?s=13">Poslovni prostor</a><a href="/oglasi-prodaja/garaza/cena-do-200000-eur/?s=13">Gara?a</a><a href="/oglasi-prodaja/pocitniski-objekt/cena-do-200000-eur/?s=13">Po?itni?ki objekt</a>

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

                <a name="M2"></a><h3>Velikost (m2)</h3><ul id="facetM2"><li><a href="/oglasi-prodaja/cena-do-200000-eur,velikost-do-2000-m2/?s=13"><div class="cnt">[17928]</div><span class="fnum">do </span>&nbsp;<span class="fnum">2.000</span></a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur,velikost-od-2000-do-4000-m2/?s=13"><div class="cnt">[761]</div><span class="fnum">2.000</span>&nbsp;<span class="fnum">-&nbsp;4.000</span></a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur,velikost-od-4000-do-6000-m2/?s=13"><div class="cnt">[251]</div><span class="fnum">4.000</span>&nbsp;<span class="fnum">-&nbsp;6.000</span></a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur,velikost-od-6000-do-8000-m2/?s=13"><div class="cnt">[131]</div><span class="fnum">6.000</span>&nbsp;<span class="fnum">-&nbsp;8.000</span></a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur,velikost-od-8000-do-10000-m2/?s=13"><div class="cnt">[95]</div><span class="fnum">8.000</span>&nbsp;<span class="fnum">-&nbsp;10.000</span></a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur,velikost-od-10000-m2/?s=13"><div class="cnt">[429]</div><span class="fnum">10.000</span>&nbsp; in ve?</a></li></ul>

                    <div class="more">

                        <div>vnesite poljubno vrednost</div>

                        <input type="text" class="mini intnum" size="10" maxlength="10" name="m1" onchange="CheckCurrency(document.sform.m1,'m1')" value="">

                        -

                        <input type="text" class="mini intnum" size="10" maxlength="10" name="m2" onchange="CheckCurrency(document.sform.m2,'m2')" value="">

                        m2

                        <input type="submit" class="fsearch" value=">" />

                    </div>

                <a name="leto"></a><h3>Leto</h3><ul><li><a href="/oglasi-prodaja/cena-do-200000-eur,letnik-do-1949/?s=13"><div class="cnt">[7782]</div>do  - 1949</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur,letnik-od-1950-do-1959/?s=13"><div class="cnt">[579]</div>1950 - 1959</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur,letnik-od-1960-do-1969/?s=13"><div class="cnt">[1211]</div>1960 - 1969</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur,letnik-od-1970-do-1979/?s=13"><div class="cnt">[1436]</div>1970 - 1979</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur,letnik-od-1980-do-1989/?s=13"><div class="cnt">[1834]</div>1980 - 1989</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur,letnik-od-1990-do-1999/?s=13"><div class="cnt">[1416]</div>1990 - 1999</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur,letnik-od-2000-do-2009/?s=13"><div class="cnt">[2873]</div>2000 - 2009</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur,letnik-od-2010-do-2014/?s=13"><div class="cnt">[1649]</div>2010 - 2014</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur,letnik-od-2015/?s=13"><div class="cnt">[752]</div>2015 in ve?</a></li></ul>

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

        <div class="spacer"></div><div><input type="checkbox" name="f" id="f1" option value="1" onchange="sform.submit()">Zni?ane cene</div><hr/><div class="grey tac">Povpre?na cena najdenih oglasov: <strong>900,09 EUR/m2</strong><br/></div>    </form>

</div></div><div id="vsebina760">

                <div class="headbar"><div id="pagination" class="top fr"><ul><li><a href="/oglasi-prodaja/cena-do-200000-eur/?s=13" class="active">1</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/2/?s=13">2</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/3/?s=13">3</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/4/?s=13">4</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/5/?s=13">5</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/6/?s=13">6</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/7/?s=13">7</a></li><span class="dots3">...</span><li><a href="/oglasi-prodaja/cena-do-200000-eur/2/?s=13" class="next">></a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/652/?s=13" class="last">>></a></li></ul></div><h1>Prodaja </h1><div class="sort cb">

                    <div class="fl">

                    <strong>Razvrsti:</strong> <a href="/oglasi-prodaja/ljubljana-mesto/stanovanje/cena-do-200000-eur/1/?s=1" class="up">lokacija</a> | <a href="/oglasi-prodaja/ljubljana-mesto/stanovanje/cena-do-200000-eur/1/?s=11" class="down">lokacija</a> | <a href="/oglasi-prodaja/ljubljana-mesto/stanovanje/cena-do-200000-eur/1/?s=3" class="up">cena</a> | <a href="/oglasi-prodaja/ljubljana-mesto/stanovanje/cena-do-200000-eur/1/?s=13" class="down act">cena</a> | <a href="/oglasi-prodaja/ljubljana-mesto/stanovanje/cena-do-200000-eur/1/?s=4" class="up">m2</a> | <a href="/oglasi-prodaja/ljubljana-mesto/stanovanje/cena-do-200000-eur/1/?s=14" class="down">m2</a> | <a href="/oglasi-prodaja/ljubljana-mesto/stanovanje/cena-do-200000-eur/1/?s=5" class="up">ponudnik</a> | <a href="/oglasi-prodaja/ljubljana-mesto/stanovanje/cena-do-200000-eur/1/?s=16" class="down">datum vpisa</a> | </div><a id="si" href="#" class="fr ibl pf i-si" style="padding-right:0">Shrani iskanje</a><div class="clearer"></div></div>

                    </div><div id="slide-thumb">

				<a href="http://www.premium-nekretnine.com/hr/prodaja/stan/3008/apartmani-Malinska-Dubasnica-Malinska" target="_blank" class="pt">

					<table border="0" cellpadding="0" cellspacing="0">

						<tr>

							<td>

								<strong>Malinska-Duba?nica</strong>

							</td>

						</tr>

						<tr>

							<td class="slika">

								<div><img src="https://picbase.turbosist.si/adads/thumbnails/1293.jpg" /></div>								

							</td>

						</tr>

						<tr>

							<td><span>Apartma 100m od morja</span></td>

						</tr>

					</table>

				</a>

			

				<a href="http://www.sonce-nepremicnine.si/sl/Nepremicninski-oglasi/prodaja.k1/hisa.v2/Hrvaska.d54/Zadarska_zupanija.r33/Otok_Ugljan_hisa_prodaja,Sonce_nepremicnine.html" target="_blank" class="pt">

					<table border="0" cellpadding="0" cellspacing="0">

						<tr>

							<td>

								<strong>Zadar</strong>

							</td>

						</tr>

						<tr>

							<td class="slika">

								<div><img src="https://picbase.turbosist.si/adads/thumbnails/1261.jpg" /></div>								

							</td>

						</tr>

						<tr>

							<td><span>Hi?a samostojna</span></td>

						</tr>

					</table>

				</a>

			

				<a href="http://www.sonce-nepremicnine.si/sl/Nepremicninski-oglasi/prodaja.k1/stanovanje.v1/vse_drzave.d0/Nepremicnine-hrvaska-prodaja-stanovanja-ob-mor_57ab9704a8efb,Sonce_nepremicnine.html" target="_blank" class="pt">

					<table border="0" cellpadding="0" cellspacing="0">

						<tr>

							<td>

								<strong>Novigrad</strong>

							</td>

						</tr>

						<tr>

							<td class="slika">

								<div><img src="https://picbase.turbosist.si/adads/thumbnails/1288.jpg" /></div>								

							</td>

						</tr>

						<tr>

							<td><span>Stanovanje - 100 m od morja</span></td>

						</tr>

					</table>

				</a>

			

				<a href="http://www.nepremicnine.net/novogradnje/dvojcek-v-3-pgf-l-2015.html" target="_blank" class="pt">

					<table border="0" cellpadding="0" cellspacing="0">

						<tr>

							<td>

								<strong>Naklo - okolica</strong>

							</td>

						</tr>

						<tr>

							<td class="slika">

								<div><img src="https://picbase.turbosist.si/adads/thumbnails/1246.jpg" /></div>								

							</td>

						</tr>

						<tr>

							<td><span>Dvoj?ek v 3.PGF, l.2015</span></td>

						</tr>

					</table>

				</a>

			<div class="clearer"></div></div>

<div class="seznam">

                    <div class="oglas_container oglasbold oglas576" id="o6033659">

                        <h2><a href="/oglasi-prodaja/koper-zg-skofije-stanovanje_6033659/" title="6033659"><span class="title">KOPER, ZG. ?KOFIJE</span></a></h2>

                        <a class="slika" href="/oglasi-prodaja/koper-zg-skofije-stanovanje_6033659/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4674308.jpg" /><div class="vec"></div></a>

                        <div class="teksti_container">

                            <span class="posr">Prodaja: Stanovanje</span>

                            <!--<div class="new-container">

                            

                            </div>-->

                            <div class="atributi">

                                <span class="atribut">Nadstropje: <strong>1</strong>/1</span><span class="atribut">Leto: <strong>2014</strong></span>

                            </div>

                            <!---->

                            



                            <div class="kratek_container">

                                <div class="kratek">100,8 m2, 2,5-sobno, v stavbi zgrajeni l. 2014, 1/1 nad., prodamo. Cena: 200.000,00 EUR</div>

                            </div>

                            <!--<div class="kratek_container">

                                <table>

                                <tr>

                                <td>

                                100,8 m2, 2,5-sobno, v stavbi zgrajeni l. 2014, 1/1 nad., prodamo. Cena: 200.000,00 EUR

                                </td>

                                </tr>

                                </table>

                            </div>-->



                            <div class="main-data">

                                <span class="velikost">100,80 m2</span><br />

                                <span class="cena">200.000,00 &euro;</span>

                            </div>

                        </div>

                        <div class="logo_container">

                            <div class="povezave">

                                <div class="prodajalec_o" title="C-nep agencija, d.o.o."><div class="logo"><a href="/oglasi-prodaja/koper-zg-skofije-stanovanje_6033659/"><img src="https://picbase.turbosist.si/slonep_agenc120/2086.jpg?v=20161017" /></a></div></div>

                            </div>

                            <div class="clearer"></div>

                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="6033659"></span>-->

                            <a class="ikona-sh3 utility" id="save-ad-6033659" href="#" data-id="6033659" onclick="save_ad(6033659); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>

                            <span class="utility" style="cursor: default;">

                                <i class="fa fa-share-square-o"></i>Deli na:

                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkoper-zg-skofije-stanovanje_6033659%2F"

   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"

   target="_blank" title="Facebook">-->

                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkoper-zg-skofije-stanovanje_6033659%2F', 'Facebook',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-facebook-square"></i>

                                </a>

                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkoper-zg-skofije-stanovanje_6033659%2F', 'Twitter',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-twitter"></i>

                                </a>

                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkoper-zg-skofije-stanovanje_6033659%2F', 'Google',500,350);" href="javascript:void(0);">

                                    <i class="fa fa-google-plus-square"></i>

                                </a>

                            </span>

                            <!--<a class="utility" data-id="6033659"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->

                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkoper-zg-skofije-stanovanje_6033659%2F" class="utility" data-id="6033659"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po?lji prijatelju</span></a>

                            <a href="/oglasi-prodaja/koper-zg-skofije-stanovanje_6033659/" class="utility contact-tooltip" title="041/988-937<br />C-nep agencija, d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>

                        </div>

                        <div class="clearer"></div>

                    </div>

                

                    <div class="oglas_container oglasbold oglas701" id="o5804381">

                        <h2><a href="/oglasi-prodaja/brezovica-pri-ljubljani-poslovni-prostor_5804381/" title="5804381"><span class="title">BREZOVICA PRI LJUBLJANI</span></a></h2>

                        <a class="slika" href="/oglasi-prodaja/brezovica-pri-ljubljani-poslovni-prostor_5804381/"><img src="https://picbase.turbosist.si/slonep_oglasi2/3047950.jpg" /><div class="vec"></div></a>

                        <div class="teksti_container">

                            <span class="posr">Prodaja: Poslovni prostor</span>

                            <!--<div class="new-container">

                            

                            </div>-->

                            <div class="atributi">

                                <span class="atribut">Nadstropje: <strong>P</strong>/1</span><span class="atribut">Leto: <strong>1985</strong></span><span class="atribut">Zemlji??e: <strong>470 m2</strong></span>

                            </div>

                            <!---->

                            



                            <div class="kratek_container">

                                <div class="kratek">220 m2, delavnica, zgrajena l. 1985, adaptirana l. 2006, 470 m2 zemlji??a, P/1 nad., vrstna poslovna stanovanjska stavba...</div>

                            </div>

                            <!--<div class="kratek_container">

                                <table>

                                <tr>

                                <td>

                                220 m2, delavnica, zgrajena l. 1985, adaptirana l. 2006, 470 m2 zemlji??a, P/1 nad., vrstna poslovna stanovanjska stavba...

                                </td>

                                </tr>

                                </table>

                            </div>-->



                            <div class="main-data">

                                <span class="velikost">220,00 m2</span><br />

                                <span class="cena">200.000,00 &euro;</span>

                            </div>

                        </div>

                        <div class="logo_container">

                            <div class="povezave">

                                <div class="prodajalec_o" title="CIMER, MAKSIMILJAN REMIC s.p."><div class="logo"><a href="/oglasi-prodaja/brezovica-pri-ljubljani-poslovni-prostor_5804381/"><img src="https://picbase.turbosist.si/slonep_agenc120/1471.jpg?v=20161017" /></a></div></div>

                            </div>

                            <div class="clearer"></div>

                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5804381"></span>-->

                            <a class="ikona-sh3 utility" id="save-ad-5804381" href="#" data-id="5804381" onclick="save_ad(5804381); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>

                            <span class="utility" style="cursor: default;">

                                <i class="fa fa-share-square-o"></i>Deli na:

                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fbrezovica-pri-ljubljani-poslovni-prostor_5804381%2F"

   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"

   target="_blank" title="Facebook">-->

                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fbrezovica-pri-ljubljani-poslovni-prostor_5804381%2F', 'Facebook',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-facebook-square"></i>

                                </a>

                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fbrezovica-pri-ljubljani-poslovni-prostor_5804381%2F', 'Twitter',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-twitter"></i>

                                </a>

                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fbrezovica-pri-ljubljani-poslovni-prostor_5804381%2F', 'Google',500,350);" href="javascript:void(0);">

                                    <i class="fa fa-google-plus-square"></i>

                                </a>

                            </span>

                            <!--<a class="utility" data-id="5804381"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->

                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fbrezovica-pri-ljubljani-poslovni-prostor_5804381%2F" class="utility" data-id="5804381"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po?lji prijatelju</span></a>

                            <a href="/oglasi-prodaja/brezovica-pri-ljubljani-poslovni-prostor_5804381/" class="utility contact-tooltip" title="041/873-580<br />CIMER, MAKSIMILJAN REMIC s.p."><i class="fa fa-phone"></i><span>O ponudniku</span></a>

                        </div>

                        <div class="clearer"></div>

                    </div>

                

                    <div class="oglas_container oglasbold oglas887" id="o6023215">

                        <h2><a href="/oglasi-prodaja/zgornje-radvanje-hisa_6023215/" title="6023215"><span class="title">ZGORNJE RADVANJE</span></a></h2>

                        <a class="slika" href="/oglasi-prodaja/zgornje-radvanje-hisa_6023215/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4585112.jpg" /><div class="vec"></div></a>

                        <div class="teksti_container">

                            <span class="posr">Prodaja: Hi?a</span>

                            <!--<div class="new-container">

                            

                            </div>-->

                            <div class="atributi">

                                <span class="atribut">Leto: <strong>2012</strong></span><span class="atribut">Zemlji??e: <strong>431 m2</strong></span>

                            </div>

                            <!---->

                            



                            <div class="kratek_container">

                                <div class="kratek">200 m2, vrstna, zgrajena l. 2012, 431 m2 zemlji??a, prodamo. Cena: 200.000,00 EUR</div>

                            </div>

                            <!--<div class="kratek_container">

                                <table>

                                <tr>

                                <td>

                                200 m2, vrstna, zgrajena l. 2012, 431 m2 zemlji??a, prodamo. Cena: 200.000,00 EUR

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

                                <div class="prodajalec_o" title="C-nep agencija, d.o.o."><div class="logo"><a href="/oglasi-prodaja/zgornje-radvanje-hisa_6023215/"><img src="https://picbase.turbosist.si/slonep_agenc120/2086.jpg?v=20161017" /></a></div></div>

                            </div>

                            <div class="clearer"></div>

                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="6023215"></span>-->

                            <a class="ikona-sh3 utility" id="save-ad-6023215" href="#" data-id="6023215" onclick="save_ad(6023215); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>

                            <span class="utility" style="cursor: default;">

                                <i class="fa fa-share-square-o"></i>Deli na:

                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fzgornje-radvanje-hisa_6023215%2F"

   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"

   target="_blank" title="Facebook">-->

                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fzgornje-radvanje-hisa_6023215%2F', 'Facebook',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-facebook-square"></i>

                                </a>

                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fzgornje-radvanje-hisa_6023215%2F', 'Twitter',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-twitter"></i>

                                </a>

                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fzgornje-radvanje-hisa_6023215%2F', 'Google',500,350);" href="javascript:void(0);">

                                    <i class="fa fa-google-plus-square"></i>

                                </a>

                            </span>

                            <!--<a class="utility" data-id="6023215"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->

                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fzgornje-radvanje-hisa_6023215%2F" class="utility" data-id="6023215"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po?lji prijatelju</span></a>

                            <a href="/oglasi-prodaja/zgornje-radvanje-hisa_6023215/" class="utility contact-tooltip" title="031/360-190<br />C-nep agencija, d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>

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

            //]]>--></script><noscript><a href='https://ok.internetmedia.si/www/delivery/ck.php?n=a280490d&amp;cb=523931924&amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5=' target='_blank'><img src='https://ok.internetmedia.si/www/delivery/avw.php?zoneid=5&amp;cb=2108645058&amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5=&amp;n=a280490d' border='0' alt='' /></a></noscript>

                </div>

            

                    <div class="oglas_container oglasbold oglas100" id="o6017813">

                        <h2><a href="/oglasi-prodaja/zgornje-radvanje-hisa_6017813/" title="6017813"><span class="title">ZGORNJE RADVANJE</span></a></h2>

                        <a class="slika" href="/oglasi-prodaja/zgornje-radvanje-hisa_6017813/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4540835.jpg" /><div class="vec"></div></a>

                        <div class="teksti_container">

                            <span class="posr">Prodaja: Hi?a</span>

                            <!--<div class="new-container">

                            

                            </div>-->

                            <div class="atributi">

                                <span class="atribut">Leto: <strong>1982</strong></span><span class="atribut">Zemlji??e: <strong>759 m2</strong></span>

                            </div>

                            <!---->

                            



                            <div class="kratek_container">

                                <div class="kratek">146,3 m2, samostojna, zgrajena l. 1982, adaptirana l. 2008, 759 m2 zemlji??a, prodamo. Cena: 200.000,00 EUR</div>

                            </div>

                            <!--<div class="kratek_container">

                                <table>

                                <tr>

                                <td>

                                146,3 m2, samostojna, zgrajena l. 1982, adaptirana l. 2008, 759 m2 zemlji??a, prodamo. Cena: 200.000,00 EUR

                                </td>

                                </tr>

                                </table>

                            </div>-->



                            <div class="main-data">

                                <span class="velikost">146,30 m2</span><br />

                                <span class="cena">200.000,00 &euro;</span>

                            </div>

                        </div>

                        <div class="logo_container">

                            <div class="povezave">

                                <div class="prodajalec_o" title="C-nep agencija, d.o.o."><div class="logo"><a href="/oglasi-prodaja/zgornje-radvanje-hisa_6017813/"><img src="https://picbase.turbosist.si/slonep_agenc120/2086.jpg?v=20161017" /></a></div></div>

                            </div>

                            <div class="clearer"></div>

                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="6017813"></span>-->

                            <a class="ikona-sh3 utility" id="save-ad-6017813" href="#" data-id="6017813" onclick="save_ad(6017813); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>

                            <span class="utility" style="cursor: default;">

                                <i class="fa fa-share-square-o"></i>Deli na:

                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fzgornje-radvanje-hisa_6017813%2F"

   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"

   target="_blank" title="Facebook">-->

                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fzgornje-radvanje-hisa_6017813%2F', 'Facebook',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-facebook-square"></i>

                                </a>

                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fzgornje-radvanje-hisa_6017813%2F', 'Twitter',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-twitter"></i>

                                </a>

                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fzgornje-radvanje-hisa_6017813%2F', 'Google',500,350);" href="javascript:void(0);">

                                    <i class="fa fa-google-plus-square"></i>

                                </a>

                            </span>

                            <!--<a class="utility" data-id="6017813"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->

                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fzgornje-radvanje-hisa_6017813%2F" class="utility" data-id="6017813"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po?lji prijatelju</span></a>

                            <a href="/oglasi-prodaja/zgornje-radvanje-hisa_6017813/" class="utility contact-tooltip" title="031/819-152<br />C-nep agencija, d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>

                        </div>

                        <div class="clearer"></div>

                    </div>

                

                    <div class="oglas_container oglasbold oglas529" id="o5812617">

                        <h2><a href="/oglasi-prodaja/novigrad-saini-u-stanovanje_5812617/" title="5812617"><span class="title">NOVIGRAD, ?AINI U</span></a></h2>

                        <a class="slika" href="/oglasi-prodaja/novigrad-saini-u-stanovanje_5812617/"><img src="https://picbase.turbosist.si/slonep_oglasi2/3098977.jpg" /><div class="vec"></div></a>

                        <div class="teksti_container">

                            <span class="posr">Prodaja: Stanovanje</span>

                            <!--<div class="new-container">

                            

                            </div>-->

                            <div class="atributi">

                                <span class="atribut">Nadstropje: <strong>P</strong>/2</span><span class="atribut">Leto: <strong>2007</strong></span>

                            </div>

                            <!---->

                            



                            <div class="kratek_container">

                                <div class="kratek">80 m2, 3-sobno, zgrajeno l. 2007, P/2 nad., izredno lepo pritli?no stanovanje, v zgradbi, v kateri je samo 6stanovanj, z...</div>

                            </div>

                            <!--<div class="kratek_container">

                                <table>

                                <tr>

                                <td>

                                80 m2, 3-sobno, zgrajeno l. 2007, P/2 nad., izredno lepo pritli?no stanovanje, v zgradbi, v kateri je samo 6stanovanj, z...

                                </td>

                                </tr>

                                </table>

                            </div>-->



                            <div class="main-data">

                                <span class="velikost">80,00 m2</span><br />

                                <span class="cena">200.000,00 &euro;</span>

                            </div>

                        </div>

                        <div class="logo_container">

                            <div class="povezave">

                                <div class="prodajalec_o" title="D5 invest d.o.o."><div class="logo"><a href="/oglasi-prodaja/novigrad-saini-u-stanovanje_5812617/"><img src="/images/ponudba-podjetja.png" /></a></div></div>

                            </div>

                            <div class="clearer"></div>

                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5812617"></span>-->

                            <a class="ikona-sh3 utility" id="save-ad-5812617" href="#" data-id="5812617" onclick="save_ad(5812617); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>

                            <span class="utility" style="cursor: default;">

                                <i class="fa fa-share-square-o"></i>Deli na:

                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fnovigrad-saini-u-stanovanje_5812617%2F"

   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"

   target="_blank" title="Facebook">-->

                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fnovigrad-saini-u-stanovanje_5812617%2F', 'Facebook',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-facebook-square"></i>

                                </a>

                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fnovigrad-saini-u-stanovanje_5812617%2F', 'Twitter',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-twitter"></i>

                                </a>

                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fnovigrad-saini-u-stanovanje_5812617%2F', 'Google',500,350);" href="javascript:void(0);">

                                    <i class="fa fa-google-plus-square"></i>

                                </a>

                            </span>

                            <!--<a class="utility" data-id="5812617"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->

                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fnovigrad-saini-u-stanovanje_5812617%2F" class="utility" data-id="5812617"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po?lji prijatelju</span></a>

                            <a href="/oglasi-prodaja/novigrad-saini-u-stanovanje_5812617/" class="utility contact-tooltip" title="01/230-98-80<br />D5 invest d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>

                        </div>

                        <div class="clearer"></div>

                    </div>

                

                    <div class="oglas_container oglasbold oglas523" id="o6043730">

                        <h2><a href="/oglasi-prodaja/logatec-ioc-posest_6043730/" title="6043730"><span class="title">LOGATEC, IOC</span></a></h2>

                        <a class="slika" href="/oglasi-prodaja/logatec-ioc-posest_6043730/"><img src="/images/n-3.jpg" /><div class="vec"></div></a>

                        <div class="teksti_container">

                            <span class="posr">Prodaja: Posest</span>

                            <!--<div class="new-container">

                            

                            </div>-->

                            <div class="atributi">

                                

                            </div>

                            <!---->

                            



                            <div class="kratek_container">

                                <div class="kratek">5.000 m2, zazidljiva, Prodaja se tudi parcela 10.000 m2. Kupec ne pla?a provizije, prodamo. Cena: 40,00 EUR/m2</div>

                            </div>

                            <!--<div class="kratek_container">

                                <table>

                                <tr>

                                <td>

                                5.000 m2, zazidljiva, Prodaja se tudi parcela 10.000 m2. Kupec ne pla?a provizije, prodamo. Cena: 40,00 EUR/m2

                                </td>

                                </tr>

                                </table>

                            </div>-->



                            <div class="main-data">

                                <span class="velikost">5.000,00 m2</span><br />

                                <span class="cena">40,00 &euro;/m2</span>

                            </div>

                        </div>

                        <div class="logo_container">

                            <div class="povezave">

                                <div class="prodajalec_o" title="DARMAL d.o.o."><div class="logo"><a href="/oglasi-prodaja/logatec-ioc-posest_6043730/"><img src="/images/ponudba-podjetja.png" /></a></div></div>

                            </div>

                            <div class="clearer"></div>

                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="6043730"></span>-->

                            <a class="ikona-sh3 utility" id="save-ad-6043730" href="#" data-id="6043730" onclick="save_ad(6043730); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>

                            <span class="utility" style="cursor: default;">

                                <i class="fa fa-share-square-o"></i>Deli na:

                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flogatec-ioc-posest_6043730%2F"

   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"

   target="_blank" title="Facebook">-->

                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flogatec-ioc-posest_6043730%2F', 'Facebook',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-facebook-square"></i>

                                </a>

                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flogatec-ioc-posest_6043730%2F', 'Twitter',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-twitter"></i>

                                </a>

                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flogatec-ioc-posest_6043730%2F', 'Google',500,350);" href="javascript:void(0);">

                                    <i class="fa fa-google-plus-square"></i>

                                </a>

                            </span>

                            <!--<a class="utility" data-id="6043730"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->

                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flogatec-ioc-posest_6043730%2F" class="utility" data-id="6043730"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po?lji prijatelju</span></a>

                            <a href="/oglasi-prodaja/logatec-ioc-posest_6043730/" class="utility contact-tooltip" title="040/863-000<br />DARMAL d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>

                        </div>

                        <div class="clearer"></div>

                    </div>

                

                    <div class="oglas_container oglasbold oglas196" id="o5946923">

                        <h2><a href="/oglasi-prodaja/koper-dolina-reke-dragonje-krkavce-posest_5946923/" title="5946923"><span class="title">KOPER, DOLINA REKE DRAGONJE KRKAV?E</span></a></h2>

                        <a class="slika" href="/oglasi-prodaja/koper-dolina-reke-dragonje-krkavce-posest_5946923/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4014466.jpg" /><div class="vec"></div></a>

                        <div class="teksti_container">

                            <span class="posr">Prodaja: Posest</span>

                            <!--<div class="new-container">

                            

                            </div>-->

                            <div class="atributi">

                                

                            </div>

                            <!---->

                            



                            <div class="kratek_container">

                                <div class="kratek">4.800 m2, zazidljiva, Prodaja se zanimiva parcela na mirnem podro?ju doline reke Dragonje. Parcelo sestavlja stavbni del...</div>

                            </div>

                            <!--<div class="kratek_container">

                                <table>

                                <tr>

                                <td>

                                4.800 m2, zazidljiva, Prodaja se zanimiva parcela na mirnem podro?ju doline reke Dragonje. Parcelo sestavlja stavbni del...

                                </td>

                                </tr>

                                </table>

                            </div>-->



                            <div class="main-data">

                                <span class="velikost">4.800,00 m2</span><br />

                                <span class="cena">200.000,00 &euro;</span>

                            </div>

                        </div>

                        <div class="logo_container">

                            <div class="povezave">

                                <div class="prodajalec_o" title="Apertura, poslovanje z nepremi?ninami, d.o.o."><div class="logo"><a href="/oglasi-prodaja/koper-dolina-reke-dragonje-krkavce-posest_5946923/"><img src="https://picbase.turbosist.si/slonep_agenc120/86.jpg?v=20161017" /></a></div></div>

                            </div>

                            <div class="clearer"></div>

                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5946923"></span>-->

                            <a class="ikona-sh3 utility" id="save-ad-5946923" href="#" data-id="5946923" onclick="save_ad(5946923); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>

                            <span class="utility" style="cursor: default;">

                                <i class="fa fa-share-square-o"></i>Deli na:

                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkoper-dolina-reke-dragonje-krkavce-posest_5946923%2F"

   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"

   target="_blank" title="Facebook">-->

                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkoper-dolina-reke-dragonje-krkavce-posest_5946923%2F', 'Facebook',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-facebook-square"></i>

                                </a>

                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkoper-dolina-reke-dragonje-krkavce-posest_5946923%2F', 'Twitter',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-twitter"></i>

                                </a>

                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkoper-dolina-reke-dragonje-krkavce-posest_5946923%2F', 'Google',500,350);" href="javascript:void(0);">

                                    <i class="fa fa-google-plus-square"></i>

                                </a>

                            </span>

                            <!--<a class="utility" data-id="5946923"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->

                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkoper-dolina-reke-dragonje-krkavce-posest_5946923%2F" class="utility" data-id="5946923"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po?lji prijatelju</span></a>

                            <a href="/oglasi-prodaja/koper-dolina-reke-dragonje-krkavce-posest_5946923/" class="utility contact-tooltip" title="0590/35-211<br />Apertura, poslovanje z nepremi?ninami, d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>

                        </div>

                        <div class="clearer"></div>

                    </div>

                

                    <div class="oglas_container oglasbold oglas299" id="o6024576">

                        <h2><a href="/oglasi-prodaja/skofljica-reber-pri-skofljici-posest_6024576/" title="6024576"><span class="title">?KOFLJICA, REBER PRI ?KOFLJICI</span></a></h2>

                        <a class="slika" href="/oglasi-prodaja/skofljica-reber-pri-skofljici-posest_6024576/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4596585.jpg" /><div class="vec"></div></a>

                        <div class="teksti_container">

                            <span class="posr">Prodaja: Posest</span>

                            <!--<div class="new-container">

                            

                            </div>-->

                            <div class="atributi">

                                

                            </div>

                            <!---->

                            



                            <div class="kratek_container">

                                <div class="kratek">5.000 m2, zazidljiva, Mo?nost nakupa manj?e parcele. Mo?nost postavitve in izdelave objekta po ?elji kupca, prodamo. Cen...</div>

                            </div>

                            <!--<div class="kratek_container">

                                <table>

                                <tr>

                                <td>

                                5.000 m2, zazidljiva, Mo?nost nakupa manj?e parcele. Mo?nost postavitve in izdelave objekta po ?elji kupca, prodamo. Cen...

                                </td>

                                </tr>

                                </table>

                            </div>-->



                            <div class="main-data">

                                <span class="velikost">5.000,00 m2</span><br />

                                <span class="cena">40,00 &euro;/m2</span>

                            </div>

                        </div>

                        <div class="logo_container">

                            <div class="povezave">

                                <div class="prodajalec_o" title="A?ur Trading, d.o.o."><div class="logo"><a href="/oglasi-prodaja/skofljica-reber-pri-skofljici-posest_6024576/"><img src="https://picbase.turbosist.si/slonep_agenc120/483.jpg?v=20161017" /></a></div></div>

                            </div>

                            <div class="clearer"></div>

                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="6024576"></span>-->

                            <a class="ikona-sh3 utility" id="save-ad-6024576" href="#" data-id="6024576" onclick="save_ad(6024576); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>

                            <span class="utility" style="cursor: default;">

                                <i class="fa fa-share-square-o"></i>Deli na:

                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fskofljica-reber-pri-skofljici-posest_6024576%2F"

   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"

   target="_blank" title="Facebook">-->

                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fskofljica-reber-pri-skofljici-posest_6024576%2F', 'Facebook',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-facebook-square"></i>

                                </a>

                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fskofljica-reber-pri-skofljici-posest_6024576%2F', 'Twitter',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-twitter"></i>

                                </a>

                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fskofljica-reber-pri-skofljici-posest_6024576%2F', 'Google',500,350);" href="javascript:void(0);">

                                    <i class="fa fa-google-plus-square"></i>

                                </a>

                            </span>

                            <!--<a class="utility" data-id="6024576"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->

                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fskofljica-reber-pri-skofljici-posest_6024576%2F" class="utility" data-id="6024576"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po?lji prijatelju</span></a>

                            <a href="/oglasi-prodaja/skofljica-reber-pri-skofljici-posest_6024576/" class="utility contact-tooltip" title="01/786-08-80<br />A?ur Trading, d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>

                        </div>

                        <div class="clearer"></div>

                    </div>

                

                    <div class="oglas_container oglasbold oglas364" id="o5414192">

                        <h2><a href="/oglasi-prodaja/izola-hisa_5414192/" title="5414192"><span class="title">IZOLA</span></a></h2>

                        <a class="slika" href="/oglasi-prodaja/izola-hisa_5414192/"><img src="https://picbase.turbosist.si/slonep_oglasi2/1236952.jpg" /><div class="vec"></div></a>

                        <div class="teksti_container">

                            <span class="posr">Prodaja: Hi?a</span>

                            <!--<div class="new-container">

                            

                            </div>-->

                            <div class="atributi">

                                <span class="atribut">Leto: <strong>2008</strong></span><span class="atribut">Zemlji??e: <strong>3249 m2</strong></span>

                            </div>

                            <!---->

                            



                            <div class="kratek_container">

                                <div class="kratek">42 m2, samostojna, adaptirana l. 2008, 3.249 m2 zemlji??a, Izola, okolica, smer ?ared, mo?nost nadgradnje, dvori??e, par...</div>

                            </div>

                            <!--<div class="kratek_container">

                                <table>

                                <tr>

                                <td>

                                42 m2, samostojna, adaptirana l. 2008, 3.249 m2 zemlji??a, Izola, okolica, smer ?ared, mo?nost nadgradnje, dvori??e, par...

                                </td>

                                </tr>

                                </table>

                            </div>-->



                            <div class="main-data">

                                <span class="velikost">42,00 m2</span><br />

                                <span class="cena">200.000,00 &euro;</span>

                            </div>

                        </div>

                        <div class="logo_container">

                            <div class="povezave">

                                <div class="prodajalec_o" title="Agencija Stenat 2000, Jagoda Nikoli? s.p."><div class="logo"><a href="/oglasi-prodaja/izola-hisa_5414192/"><img src="https://picbase.turbosist.si/slonep_agenc120/144.jpg?v=20161017" /></a></div></div>

                            </div>

                            <div class="clearer"></div>

                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5414192"></span>-->

                            <a class="ikona-sh3 utility" id="save-ad-5414192" href="#" data-id="5414192" onclick="save_ad(5414192); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>

                            <span class="utility" style="cursor: default;">

                                <i class="fa fa-share-square-o"></i>Deli na:

                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fizola-hisa_5414192%2F"

   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"

   target="_blank" title="Facebook">-->

                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fizola-hisa_5414192%2F', 'Facebook',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-facebook-square"></i>

                                </a>

                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fizola-hisa_5414192%2F', 'Twitter',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-twitter"></i>

                                </a>

                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fizola-hisa_5414192%2F', 'Google',500,350);" href="javascript:void(0);">

                                    <i class="fa fa-google-plus-square"></i>

                                </a>

                            </span>

                            <!--<a class="utility" data-id="5414192"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->

                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fizola-hisa_5414192%2F" class="utility" data-id="5414192"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po?lji prijatelju</span></a>

                            <a href="/oglasi-prodaja/izola-hisa_5414192/" class="utility contact-tooltip" title="05/6279-222<br />Agencija Stenat 2000, Jagoda Nikoli? s.p."><i class="fa fa-phone"></i><span>O ponudniku</span></a>

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

            //]]>--></script><noscript><a href='https://ok.internetmedia.si/www/delivery/ck.php?n=a280490d&amp;cb=803169081&amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5=' target='_blank'><img src='https://ok.internetmedia.si/www/delivery/avw.php?zoneid=5&amp;cb=937138689&amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5=&amp;n=a280490d' border='0' alt='' /></a></noscript>

                </div>

            

                    <div class="oglas_container oglasbold oglas242" id="o6017904">

                        <h2><a href="/oglasi-prodaja/lj-center-stanovanje_6017904/" title="6017904"><span class="title">LJ. CENTER</span></a></h2>

                        <a class="slika" href="/oglasi-prodaja/lj-center-stanovanje_6017904/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4541607.jpg" /><div class="vec"></div></a>

                        <div class="teksti_container">

                            <span class="posr">Prodaja: Stanovanje</span>

                            <!--<div class="new-container">

                            

                            </div>-->

                            <div class="atributi">

                                <span class="atribut">Leto: <strong>1500</strong></span>

                            </div>

                            <!---->

                            



                            <div class="kratek_container">

                                <div class="kratek">107 m2, 4-sobno, zgrajeno l. 1500, prodamo. Cena: 200.000,00 EUR</div>

                            </div>

                            <!--<div class="kratek_container">

                                <table>

                                <tr>

                                <td>

                                107 m2, 4-sobno, zgrajeno l. 1500, prodamo. Cena: 200.000,00 EUR

                                </td>

                                </tr>

                                </table>

                            </div>-->



                            <div class="main-data">

                                <span class="velikost">107,00 m2</span><br />

                                <span class="cena">200.000,00 &euro;</span>

                            </div>

                        </div>

                        <div class="logo_container">

                            <div class="povezave">

                                <div class="prodajalec_o" title="Agencija Elite d.o.o."><div class="logo"><a href="/oglasi-prodaja/lj-center-stanovanje_6017904/"><img src="https://picbase.turbosist.si/slonep_agenc120/895.jpg?v=20161017" /></a></div></div>

                            </div>

                            <div class="clearer"></div>

                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="6017904"></span>-->

                            <a class="ikona-sh3 utility" id="save-ad-6017904" href="#" data-id="6017904" onclick="save_ad(6017904); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>

                            <span class="utility" style="cursor: default;">

                                <i class="fa fa-share-square-o"></i>Deli na:

                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-center-stanovanje_6017904%2F"

   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"

   target="_blank" title="Facebook">-->

                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-center-stanovanje_6017904%2F', 'Facebook',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-facebook-square"></i>

                                </a>

                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-center-stanovanje_6017904%2F', 'Twitter',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-twitter"></i>

                                </a>

                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-center-stanovanje_6017904%2F', 'Google',500,350);" href="javascript:void(0);">

                                    <i class="fa fa-google-plus-square"></i>

                                </a>

                            </span>

                            <!--<a class="utility" data-id="6017904"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->

                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-center-stanovanje_6017904%2F" class="utility" data-id="6017904"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po?lji prijatelju</span></a>

                            <a href="/oglasi-prodaja/lj-center-stanovanje_6017904/" class="utility contact-tooltip" title="040/319-100<br />Agencija Elite d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>

                        </div>

                        <div class="clearer"></div>

                    </div>

                

                    <div class="oglas_container oglasbold oglas20" id="o6038709">

                        <h2><a href="/oglasi-prodaja/lj-bezigrad-dunajska-cesta-blizina-gr-stanovanje_6038709/" title="6038709"><span class="title">LJ. BE?IGRAD, DUNAJSKA CESTA, BLI?INA GR</span></a></h2>

                        <a class="slika" href="/oglasi-prodaja/lj-bezigrad-dunajska-cesta-blizina-gr-stanovanje_6038709/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4715962.jpg" /><div class="vec"></div></a>

                        <div class="teksti_container">

                            <span class="posr">Prodaja: Stanovanje</span>

                            <!--<div class="new-container">

                            

                            </div>-->

                            <div class="atributi">

                                <span class="atribut">Nadstropje: <strong>4</strong>/4</span><span class="atribut">Leto: <strong>1939</strong></span>

                            </div>

                            <!---->

                            



                            <div class="kratek_container">

                                <div class="kratek">98,7 m2, 3-sobno, zgrajeno l. 1939, 4/4 nad., v me??anskem bloku blizu mestnega sredi??a, lega V-Z, uporabne povr?ine 84...</div>

                            </div>

                            <!--<div class="kratek_container">

                                <table>

                                <tr>

                                <td>

                                98,7 m2, 3-sobno, zgrajeno l. 1939, 4/4 nad., v me??anskem bloku blizu mestnega sredi??a, lega V-Z, uporabne povr?ine 84...

                                </td>

                                </tr>

                                </table>

                            </div>-->



                            <div class="main-data">

                                <span class="velikost">98,70 m2</span><br />

                                <span class="cena">200.000,00 &euro;</span>

                            </div>

                        </div>

                        <div class="logo_container">

                            <div class="povezave">

                                <div class="prodajalec_o" title="Abstract nepremi?nine, Igor Kerin s.p."><div class="logo"><a href="/oglasi-prodaja/lj-bezigrad-dunajska-cesta-blizina-gr-stanovanje_6038709/"><img src="https://picbase.turbosist.si/slonep_agenc120/116.jpg?v=20161017" /></a></div></div>

                            </div>

                            <div class="clearer"></div>

                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="6038709"></span>-->

                            <a class="ikona-sh3 utility" id="save-ad-6038709" href="#" data-id="6038709" onclick="save_ad(6038709); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>

                            <span class="utility" style="cursor: default;">

                                <i class="fa fa-share-square-o"></i>Deli na:

                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-bezigrad-dunajska-cesta-blizina-gr-stanovanje_6038709%2F"

   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"

   target="_blank" title="Facebook">-->

                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-bezigrad-dunajska-cesta-blizina-gr-stanovanje_6038709%2F', 'Facebook',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-facebook-square"></i>

                                </a>

                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-bezigrad-dunajska-cesta-blizina-gr-stanovanje_6038709%2F', 'Twitter',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-twitter"></i>

                                </a>

                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-bezigrad-dunajska-cesta-blizina-gr-stanovanje_6038709%2F', 'Google',500,350);" href="javascript:void(0);">

                                    <i class="fa fa-google-plus-square"></i>

                                </a>

                            </span>

                            <!--<a class="utility" data-id="6038709"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->

                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-bezigrad-dunajska-cesta-blizina-gr-stanovanje_6038709%2F" class="utility" data-id="6038709"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po?lji prijatelju</span></a>

                            <a href="/oglasi-prodaja/lj-bezigrad-dunajska-cesta-blizina-gr-stanovanje_6038709/" class="utility contact-tooltip" title="041/694-482<br />Abstract nepremi?nine, Igor Kerin s.p."><i class="fa fa-phone"></i><span>O ponudniku</span></a>

                        </div>

                        <div class="clearer"></div>

                    </div>

                

                    <div class="oglas_container oglasbold oglas369" id="o6016589">

                        <h2><a href="/oglasi-prodaja/bertoki-posest_6016589/" title="6016589"><span class="title">BERTOKI</span></a></h2>

                        <a class="slika" href="/oglasi-prodaja/bertoki-posest_6016589/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4530842.jpg" /><div class="vec"></div></a>

                        <div class="teksti_container">

                            <span class="posr">Prodaja: Posest</span>

                            <!--<div class="new-container">

                            

                            </div>-->

                            <div class="atributi">

                                

                            </div>

                            <!---->

                            



                            <div class="kratek_container">

                                <div class="kratek">17.036 m2, kmetijsko zemlji??e, prodamo. Cena: 200.000,00 EUR</div>

                            </div>

                            <!--<div class="kratek_container">

                                <table>

                                <tr>

                                <td>

                                17.036 m2, kmetijsko zemlji??e, prodamo. Cena: 200.000,00 EUR

                                </td>

                                </tr>

                                </table>

                            </div>-->



                            <div class="main-data">

                                <span class="velikost">17.036,00 m2</span><br />

                                <span class="cena">200.000,00 &euro;</span>

                            </div>

                        </div>

                        <div class="logo_container">

                            <div class="povezave">

                                <div class="prodajalec_o" title="De?elna banka Slovenije d.d."><div class="logo"><a href="/oglasi-prodaja/bertoki-posest_6016589/"><img src="https://picbase.turbosist.si/slonep_agenc120/1092.jpg?v=20161017" /></a></div></div>

                            </div>

                            <div class="clearer"></div>

                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="6016589"></span>-->

                            <a class="ikona-sh3 utility" id="save-ad-6016589" href="#" data-id="6016589" onclick="save_ad(6016589); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>

                            <span class="utility" style="cursor: default;">

                                <i class="fa fa-share-square-o"></i>Deli na:

                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fbertoki-posest_6016589%2F"

   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"

   target="_blank" title="Facebook">-->

                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fbertoki-posest_6016589%2F', 'Facebook',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-facebook-square"></i>

                                </a>

                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fbertoki-posest_6016589%2F', 'Twitter',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-twitter"></i>

                                </a>

                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fbertoki-posest_6016589%2F', 'Google',500,350);" href="javascript:void(0);">

                                    <i class="fa fa-google-plus-square"></i>

                                </a>

                            </span>

                            <!--<a class="utility" data-id="6016589"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->

                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fbertoki-posest_6016589%2F" class="utility" data-id="6016589"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po?lji prijatelju</span></a>

                            <a href="/oglasi-prodaja/bertoki-posest_6016589/" class="utility contact-tooltip" title="01/472-73-42<br />De?elna banka Slovenije d.d."><i class="fa fa-phone"></i><span>O ponudniku</span></a>

                        </div>

                        <div class="clearer"></div>

                    </div>

                

                    <div class="oglas_container oglasbold oglas921" id="o5747505">

                        <h2><a href="/oglasi-prodaja/pag-s-pogledom-na-morje-pocitniski-objekt_5747505/" title="5747505"><span class="title">PAG, S POGLEDOM NA MORJE</span></a></h2>

                        <a class="slika" href="/oglasi-prodaja/pag-s-pogledom-na-morje-pocitniski-objekt_5747505/"><img src="https://picbase.turbosist.si/slonep_oglasi2/3088292.jpg" /><div class="vec"></div></a>

                        <div class="teksti_container">

                            <span class="posr">Prodaja: Po?itni?ki objekt</span>

                            <!--<div class="new-container">

                            

                            </div>-->

                            <div class="atributi">

                                <span class="atribut">Leto: <strong>1989</strong></span><span class="atribut">Zemlji??e: <strong>500 m2</strong></span>

                            </div>

                            <!---->

                            



                            <div class="kratek_container">

                                <div class="kratek">200 m2, hi?a, zgrajena l. 1989, 500 m2 zemlji??a, hi?o z dvema apartmajema, s ?udovitim razgledom, prodamo. apartmaja st...</div>

                            </div>

                            <!--<div class="kratek_container">

                                <table>

                                <tr>

                                <td>

                                200 m2, hi?a, zgrajena l. 1989, 500 m2 zemlji??a, hi?o z dvema apartmajema, s ?udovitim razgledom, prodamo. apartmaja st...

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

                                <div class="prodajalec_o" title="Dividenda d.o.o., PE Ptuj"><div class="logo"><a href="/oglasi-prodaja/pag-s-pogledom-na-morje-pocitniski-objekt_5747505/"><img src="/images/ponudba-podjetja.png" /></a></div></div>

                            </div>

                            <div class="clearer"></div>

                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5747505"></span>-->

                            <a class="ikona-sh3 utility" id="save-ad-5747505" href="#" data-id="5747505" onclick="save_ad(5747505); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>

                            <span class="utility" style="cursor: default;">

                                <i class="fa fa-share-square-o"></i>Deli na:

                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fpag-s-pogledom-na-morje-pocitniski-objekt_5747505%2F"

   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"

   target="_blank" title="Facebook">-->

                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fpag-s-pogledom-na-morje-pocitniski-objekt_5747505%2F', 'Facebook',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-facebook-square"></i>

                                </a>

                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fpag-s-pogledom-na-morje-pocitniski-objekt_5747505%2F', 'Twitter',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-twitter"></i>

                                </a>

                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fpag-s-pogledom-na-morje-pocitniski-objekt_5747505%2F', 'Google',500,350);" href="javascript:void(0);">

                                    <i class="fa fa-google-plus-square"></i>

                                </a>

                            </span>

                            <!--<a class="utility" data-id="5747505"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->

                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fpag-s-pogledom-na-morje-pocitniski-objekt_5747505%2F" class="utility" data-id="5747505"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po?lji prijatelju</span></a>

                            <a href="/oglasi-prodaja/pag-s-pogledom-na-morje-pocitniski-objekt_5747505/" class="utility contact-tooltip" title="051/848-241<br />Dividenda d.o.o., PE Ptuj"><i class="fa fa-phone"></i><span>O ponudniku</span></a>

                        </div>

                        <div class="clearer"></div>

                    </div>

                

                    <div class="oglas_container oglasbold oglas577" id="o5908439">

                        <h2><a href="/oglasi-prodaja/izola-korte-hisa_5908439/" title="5908439"><span class="title">IZOLA, KORTE</span></a></h2>

                        <a class="slika" href="/oglasi-prodaja/izola-korte-hisa_5908439/"><img src="https://picbase.turbosist.si/slonep_oglasi2/3732761.jpg" /><div class="vec"></div></a>

                        <div class="teksti_container">

                            <span class="posr">Prodaja: Hi?a</span>

                            <!--<div class="new-container">

                            

                            </div>-->

                            <div class="atributi">

                                <span class="atribut">Leto: <strong>1900</strong></span><span class="atribut">Zemlji??e: <strong>205 m2</strong></span>

                            </div>

                            <!---->

                            



                            <div class="kratek_container">

                                <div class="kratek">169,1 m2, vrstna, zgrajena l. 1900, 205 m2 zemlji??a, V Korath prodamo istrsko, dvostanovanjsko hi?o na son?ni lokaciji....</div>

                            </div>

                            <!--<div class="kratek_container">

                                <table>

                                <tr>

                                <td>

                                169,1 m2, vrstna, zgrajena l. 1900, 205 m2 zemlji??a, V Korath prodamo istrsko, dvostanovanjsko hi?o na son?ni lokaciji....

                                </td>

                                </tr>

                                </table>

                            </div>-->



                            <div class="main-data">

                                <span class="velikost">169,10 m2</span><br />

                                <span class="cena">200.000,00 &euro;</span>

                            </div>

                        </div>

                        <div class="logo_container">

                            <div class="povezave">

                                <div class="prodajalec_o" title="Dodoma d.o.o., PE Koper, Pristani?ka 5, 6000 Koper"><div class="logo"><a href="/oglasi-prodaja/izola-korte-hisa_5908439/"><img src="https://picbase.turbosist.si/slonep_agenc120/598.jpg?v=20161017" /></a></div></div>

                            </div>

                            <div class="clearer"></div>

                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5908439"></span>-->

                            <a class="ikona-sh3 utility" id="save-ad-5908439" href="#" data-id="5908439" onclick="save_ad(5908439); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>

                            <span class="utility" style="cursor: default;">

                                <i class="fa fa-share-square-o"></i>Deli na:

                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fizola-korte-hisa_5908439%2F"

   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"

   target="_blank" title="Facebook">-->

                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fizola-korte-hisa_5908439%2F', 'Facebook',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-facebook-square"></i>

                                </a>

                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fizola-korte-hisa_5908439%2F', 'Twitter',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-twitter"></i>

                                </a>

                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fizola-korte-hisa_5908439%2F', 'Google',500,350);" href="javascript:void(0);">

                                    <i class="fa fa-google-plus-square"></i>

                                </a>

                            </span>

                            <!--<a class="utility" data-id="5908439"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->

                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fizola-korte-hisa_5908439%2F" class="utility" data-id="5908439"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po?lji prijatelju</span></a>

                            <a href="/oglasi-prodaja/izola-korte-hisa_5908439/" class="utility contact-tooltip" title="031/775-008<br />Dodoma d.o.o., PE Koper, Pristani?ka 5, 6000 Koper"><i class="fa fa-phone"></i><span>O ponudniku</span></a>

                        </div>

                        <div class="clearer"></div>

                    </div>

                

                    <div class="oglas_container oglasbold oglas782" id="o5839191">

                        <h2><a href="/oglasi-prodaja/sneberje-sneberska-cesta-hisa_5839191/" title="5839191"><span class="title">SNEBERJE, SNEBERSKA CESTA</span></a></h2>

                        <a class="slika" href="/oglasi-prodaja/sneberje-sneberska-cesta-hisa_5839191/"><img src="https://picbase.turbosist.si/slonep_oglasi2/3274101.jpg" /><div class="vec"></div></a>

                        <div class="teksti_container">

                            <span class="posr">Prodaja: Hi?a</span>

                            <!--<div class="new-container">

                            

                            </div>-->

                            <div class="atributi">

                                <span class="atribut">Leto: <strong>1946</strong></span>

                            </div>

                            <!---->

                            



                            <div class="kratek_container">

                                <div class="kratek">240 m2, samostojna, zgrajena l. 1946, prodamo. Cena: 200.000,00 EUR</div>

                            </div>

                            <!--<div class="kratek_container">

                                <table>

                                <tr>

                                <td>

                                240 m2, samostojna, zgrajena l. 1946, prodamo. Cena: 200.000,00 EUR

                                </td>

                                </tr>

                                </table>

                            </div>-->



                            <div class="main-data">

                                <span class="velikost">240,00 m2</span><br />

                                <span class="cena">200.000,00 &euro;</span>

                            </div>

                        </div>

                        <div class="logo_container">

                            <div class="povezave">

                                <div class="prodajalec_o" title="Domplan d.d."><div class="logo"><a href="/oglasi-prodaja/sneberje-sneberska-cesta-hisa_5839191/"><img src="https://picbase.turbosist.si/slonep_agenc120/415.jpg?v=20161017" /></a></div></div>

                            </div>

                            <div class="clearer"></div>

                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5839191"></span>-->

                            <a class="ikona-sh3 utility" id="save-ad-5839191" href="#" data-id="5839191" onclick="save_ad(5839191); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>

                            <span class="utility" style="cursor: default;">

                                <i class="fa fa-share-square-o"></i>Deli na:

                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsneberje-sneberska-cesta-hisa_5839191%2F"

   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"

   target="_blank" title="Facebook">-->

                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsneberje-sneberska-cesta-hisa_5839191%2F', 'Facebook',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-facebook-square"></i>

                                </a>

                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsneberje-sneberska-cesta-hisa_5839191%2F', 'Twitter',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-twitter"></i>

                                </a>

                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsneberje-sneberska-cesta-hisa_5839191%2F', 'Google',500,350);" href="javascript:void(0);">

                                    <i class="fa fa-google-plus-square"></i>

                                </a>

                            </span>

                            <!--<a class="utility" data-id="5839191"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->

                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsneberje-sneberska-cesta-hisa_5839191%2F" class="utility" data-id="5839191"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po?lji prijatelju</span></a>

                            <a href="/oglasi-prodaja/sneberje-sneberska-cesta-hisa_5839191/" class="utility contact-tooltip" title="04/206-87-73<br />Domplan d.d."><i class="fa fa-phone"></i><span>O ponudniku</span></a>

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

            //]]>--></script><noscript><a href='https://ok.internetmedia.si/www/delivery/ck.php?n=a280490d&amp;cb=848538779&amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5=' target='_blank'><img src='https://ok.internetmedia.si/www/delivery/avw.php?zoneid=5&amp;cb=1789335643&amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5=&amp;n=a280490d' border='0' alt='' /></a></noscript>

                </div>

            

                    <div class="oglas_container oglasbold oglas957" id="o5999990">

                        <h2><a href="/oglasi-prodaja/maribor-studenci-stanovanje_5999990/" title="5999990"><span class="title">MARIBOR, STUDENCI</span></a></h2>

                        <a class="slika" href="/oglasi-prodaja/maribor-studenci-stanovanje_5999990/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4398487.jpg" /><div class="vec"></div></a>

                        <div class="teksti_container">

                            <span class="posr">Prodaja: Stanovanje</span>

                            <!--<div class="new-container">

                            

                            </div>-->

                            <div class="atributi">

                                <span class="atribut">Nadstropje: <strong>P</strong>/1</span><span class="atribut">Leto: <strong>1980</strong></span>

                            </div>

                            <!---->

                            



                            <div class="kratek_container">

                                <div class="kratek">147 m2, 3,5-sobno, zgrajeno l. 1980, adaptirano l. 2007, P/1 nad., Eta?a hi?e (3,5-sobno stanovanje) z dvojno gara?o, kl...</div>

                            </div>

                            <!--<div class="kratek_container">

                                <table>

                                <tr>

                                <td>

                                147 m2, 3,5-sobno, zgrajeno l. 1980, adaptirano l. 2007, P/1 nad., Eta?a hi?e (3,5-sobno stanovanje) z dvojno gara?o, kl...

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

                                <div class="prodajalec_o" title="Idila nepremi?nine, Damijan Kokol s.p."><div class="logo"><a href="/oglasi-prodaja/maribor-studenci-stanovanje_5999990/"><img src="/images/ponudba-podjetja.png" /></a></div></div>

                            </div>

                            <div class="clearer"></div>

                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5999990"></span>-->

                            <a class="ikona-sh3 utility" id="save-ad-5999990" href="#" data-id="5999990" onclick="save_ad(5999990); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>

                            <span class="utility" style="cursor: default;">

                                <i class="fa fa-share-square-o"></i>Deli na:

                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmaribor-studenci-stanovanje_5999990%2F"

   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"

   target="_blank" title="Facebook">-->

                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmaribor-studenci-stanovanje_5999990%2F', 'Facebook',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-facebook-square"></i>

                                </a>

                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmaribor-studenci-stanovanje_5999990%2F', 'Twitter',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-twitter"></i>

                                </a>

                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmaribor-studenci-stanovanje_5999990%2F', 'Google',500,350);" href="javascript:void(0);">

                                    <i class="fa fa-google-plus-square"></i>

                                </a>

                            </span>

                            <!--<a class="utility" data-id="5999990"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->

                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmaribor-studenci-stanovanje_5999990%2F" class="utility" data-id="5999990"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po?lji prijatelju</span></a>

                            <a href="/oglasi-prodaja/maribor-studenci-stanovanje_5999990/" class="utility contact-tooltip" title="031/523-548<br />Idila nepremi?nine, Damijan Kokol s.p."><i class="fa fa-phone"></i><span>O ponudniku</span></a>

                        </div>

                        <div class="clearer"></div>

                    </div>

                

                    <div class="oglas_container oglasbold oglas378" id="o5929181">

                        <h2><a href="/oglasi-prodaja/lj-bezigrad-zupanciceva-jama-velika-terasa-stanovanje_5929181/" title="5929181"><span class="title">LJ. BE?IGRAD, ZUPAN?I?EVA JAMA - VELIKA TERASA</span></a></h2>

                        <a class="slika" href="/oglasi-prodaja/lj-bezigrad-zupanciceva-jama-velika-terasa-stanovanje_5929181/"><img src="https://picbase.turbosist.si/slonep_oglasi2/3890129.jpg" /><div class="vec"></div></a>

                        <div class="teksti_container">

                            <span class="posr">Prodaja: Stanovanje</span>

                            <!--<div class="new-container">

                            

                            </div>-->

                            <div class="atributi">

                                <span class="atribut">Nadstropje: <strong>VP</strong></span><span class="atribut">Leto: <strong>2005</strong></span>

                            </div>

                            <!---->

                            



                            <div class="kratek_container">

                                <div class="kratek">58,6 m2, 2-sobno, zgrajeno l. 2005, visoko pritli?je, ?elezna cesta - lepo 2-sobno stanovanje z veliko teraso z vrtom (1...</div>

                            </div>

                            <!--<div class="kratek_container">

                                <table>

                                <tr>

                                <td>

                                58,6 m2, 2-sobno, zgrajeno l. 2005, visoko pritli?je, ?elezna cesta - lepo 2-sobno stanovanje z veliko teraso z vrtom (1...

                                </td>

                                </tr>

                                </table>

                            </div>-->



                            <div class="main-data">

                                <span class="velikost">58,60 m2</span><br />

                                <span class="cena">200.000,00 &euro;</span>

                            </div>

                        </div>

                        <div class="logo_container">

                            <div class="povezave">

                                <div class="prodajalec_o" title="Eventum d.o.o."><div class="logo"><a href="/oglasi-prodaja/lj-bezigrad-zupanciceva-jama-velika-terasa-stanovanje_5929181/"><img src="https://picbase.turbosist.si/slonep_agenc120/797.jpg?v=20161017" /></a></div></div>

                            </div>

                            <div class="clearer"></div>

                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5929181"></span>-->

                            <a class="ikona-sh3 utility" id="save-ad-5929181" href="#" data-id="5929181" onclick="save_ad(5929181); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>

                            <span class="utility" style="cursor: default;">

                                <i class="fa fa-share-square-o"></i>Deli na:

                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-bezigrad-zupanciceva-jama-velika-terasa-stanovanje_5929181%2F"

   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"

   target="_blank" title="Facebook">-->

                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-bezigrad-zupanciceva-jama-velika-terasa-stanovanje_5929181%2F', 'Facebook',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-facebook-square"></i>

                                </a>

                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-bezigrad-zupanciceva-jama-velika-terasa-stanovanje_5929181%2F', 'Twitter',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-twitter"></i>

                                </a>

                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-bezigrad-zupanciceva-jama-velika-terasa-stanovanje_5929181%2F', 'Google',500,350);" href="javascript:void(0);">

                                    <i class="fa fa-google-plus-square"></i>

                                </a>

                            </span>

                            <!--<a class="utility" data-id="5929181"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->

                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-bezigrad-zupanciceva-jama-velika-terasa-stanovanje_5929181%2F" class="utility" data-id="5929181"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po?lji prijatelju</span></a>

                            <a href="/oglasi-prodaja/lj-bezigrad-zupanciceva-jama-velika-terasa-stanovanje_5929181/" class="utility contact-tooltip" title="040/829-999<br />Eventum d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>

                        </div>

                        <div class="clearer"></div>

                    </div>

                

                    <div class="oglas_container oglasbold oglas285" id="o5990336">

                        <h2><a href="/oglasi-prodaja/miklavz-na-dravskem-polju-hisa_5990336/" title="5990336"><span class="title">MIKLAV? NA DRAVSKEM POLJU</span></a></h2>

                        <a class="slika" href="/oglasi-prodaja/miklavz-na-dravskem-polju-hisa_5990336/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4324147.jpg" /><div class="vec"></div></a>

                        <div class="teksti_container">

                            <span class="posr">Prodaja: Hi?a</span>

                            <!--<div class="new-container">

                            

                            </div>-->

                            <div class="atributi">

                                <span class="atribut">Nadstropje: <strong>K+P+1</strong></span><span class="atribut">Leto: <strong>1987</strong></span><span class="atribut">Zemlji??e: <strong>585 m2</strong></span>

                            </div>

                            <!---->

                            



                            <div class="kratek_container">

                                <div class="kratek">140 m2, samostojna, zgrajena l. 1987, 585 m2 zemlji??a, K+P+1, urejena in vzdr?evana hi?a v centru Miklav?a, vsi priklju...</div>

                            </div>

                            <!--<div class="kratek_container">

                                <table>

                                <tr>

                                <td>

                                140 m2, samostojna, zgrajena l. 1987, 585 m2 zemlji??a, K+P+1, urejena in vzdr?evana hi?a v centru Miklav?a, vsi priklju...

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

                                <div class="prodajalec_o" title="Inventa d.o.o."><div class="logo"><a href="/oglasi-prodaja/miklavz-na-dravskem-polju-hisa_5990336/"><img src="https://picbase.turbosist.si/slonep_agenc120/1320.jpg?v=20161017" /></a></div></div>

                            </div>

                            <div class="clearer"></div>

                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5990336"></span>-->

                            <a class="ikona-sh3 utility" id="save-ad-5990336" href="#" data-id="5990336" onclick="save_ad(5990336); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>

                            <span class="utility" style="cursor: default;">

                                <i class="fa fa-share-square-o"></i>Deli na:

                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmiklavz-na-dravskem-polju-hisa_5990336%2F"

   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"

   target="_blank" title="Facebook">-->

                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmiklavz-na-dravskem-polju-hisa_5990336%2F', 'Facebook',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-facebook-square"></i>

                                </a>

                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmiklavz-na-dravskem-polju-hisa_5990336%2F', 'Twitter',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-twitter"></i>

                                </a>

                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmiklavz-na-dravskem-polju-hisa_5990336%2F', 'Google',500,350);" href="javascript:void(0);">

                                    <i class="fa fa-google-plus-square"></i>

                                </a>

                            </span>

                            <!--<a class="utility" data-id="5990336"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->

                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmiklavz-na-dravskem-polju-hisa_5990336%2F" class="utility" data-id="5990336"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po?lji prijatelju</span></a>

                            <a href="/oglasi-prodaja/miklavz-na-dravskem-polju-hisa_5990336/" class="utility contact-tooltip" title="02/228-19-80<br />Inventa d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>

                        </div>

                        <div class="clearer"></div>

                    </div>

                

                    <div class="oglas_container oglasbold oglas483" id="o5931140">

                        <h2><a href="/oglasi-prodaja/solkan-center-poslovni-prostor_5931140/" title="5931140"><span class="title">SOLKAN, CENTER</span></a></h2>

                        <a class="slika" href="/oglasi-prodaja/solkan-center-poslovni-prostor_5931140/"><img src="https://picbase.turbosist.si/slonep_oglasi2/3898032.jpg" /><div class="vec"></div></a>

                        <div class="teksti_container">

                            <span class="posr">Prodaja: Poslovni prostor</span>

                            <!--<div class="new-container">

                            

                            </div>-->

                            <div class="atributi">

                                <span class="atribut">Leto: <strong>2012</strong></span><span class="atribut">Zemlji??e: <strong>217 m2</strong></span>

                            </div>

                            <!---->

                            



                            <div class="kratek_container">

                                <div class="kratek">176 m2, gostinski lokal, adaptiran l. 2012, 217 m2 zemlji??a, okrep?evalnica-bar, v centru Solkana, pritli?je, v celoti ...</div>

                            </div>

                            <!--<div class="kratek_container">

                                <table>

                                <tr>

                                <td>

                                176 m2, gostinski lokal, adaptiran l. 2012, 217 m2 zemlji??a, okrep?evalnica-bar, v centru Solkana, pritli?je, v celoti ...

                                </td>

                                </tr>

                                </table>

                            </div>-->



                            <div class="main-data">

                                <span class="velikost">176,00 m2</span><br />

                                <span class="cena">200.000,00 &euro;</span>

                            </div>

                        </div>

                        <div class="logo_container">

                            <div class="povezave">

                                <div class="prodajalec_o" title="Forma nepremi?nine, Klavdio ?trukelj s.p."><div class="logo"><a href="/oglasi-prodaja/solkan-center-poslovni-prostor_5931140/"><img src="https://picbase.turbosist.si/slonep_agenc120/293.jpg?v=20161017" /></a></div></div>

                            </div>

                            <div class="clearer"></div>

                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5931140"></span>-->

                            <a class="ikona-sh3 utility" id="save-ad-5931140" href="#" data-id="5931140" onclick="save_ad(5931140); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>

                            <span class="utility" style="cursor: default;">

                                <i class="fa fa-share-square-o"></i>Deli na:

                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsolkan-center-poslovni-prostor_5931140%2F"

   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"

   target="_blank" title="Facebook">-->

                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsolkan-center-poslovni-prostor_5931140%2F', 'Facebook',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-facebook-square"></i>

                                </a>

                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsolkan-center-poslovni-prostor_5931140%2F', 'Twitter',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-twitter"></i>

                                </a>

                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsolkan-center-poslovni-prostor_5931140%2F', 'Google',500,350);" href="javascript:void(0);">

                                    <i class="fa fa-google-plus-square"></i>

                                </a>

                            </span>

                            <!--<a class="utility" data-id="5931140"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->

                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fsolkan-center-poslovni-prostor_5931140%2F" class="utility" data-id="5931140"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po?lji prijatelju</span></a>

                            <a href="/oglasi-prodaja/solkan-center-poslovni-prostor_5931140/" class="utility contact-tooltip" title="05/333-00-20<br />Forma nepremi?nine, Klavdio ?trukelj s.p."><i class="fa fa-phone"></i><span>O ponudniku</span></a>

                        </div>

                        <div class="clearer"></div>

                    </div>

                

                    <div class="oglas_container oglasbold oglas503" id="o6028734">

                        <h2><a href="/oglasi-prodaja/zabukovica-soncno-in-dostopno-rahlo-pobocje-hisa_6028734/" title="6028734"><span class="title">ZABUKOVICA, SON?NO IN DOSTOPNO RAHLO POBO?JE</span></a></h2>

                        <a class="slika" href="/oglasi-prodaja/zabukovica-soncno-in-dostopno-rahlo-pobocje-hisa_6028734/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4632196.jpg" /><div class="vec"></div></a>

                        <div class="teksti_container">

                            <span class="posr">Prodaja: Hi?a</span>

                            <!--<div class="new-container">

                            

                            </div>-->

                            <div class="atributi">

                                <span class="atribut">Nadstropje: <strong>P+M</strong></span><span class="atribut">Leto: <strong>2002</strong></span><span class="atribut">Zemlji??e: <strong>1893 m2</strong></span>

                            </div>

                            <!---->

                            



                            <div class="kratek_container">

                                <div class="kratek">183 m2, samostojna, zgrajena l. 2002, 1.893 m2 zemlji??a, P+M, Son?na lokacija, rahlo pobo?je, dober javni dostop, Zabuk...</div>

                            </div>

                            <!--<div class="kratek_container">

                                <table>

                                <tr>

                                <td>

                                183 m2, samostojna, zgrajena l. 2002, 1.893 m2 zemlji??a, P+M, Son?na lokacija, rahlo pobo?je, dober javni dostop, Zabuk...

                                </td>

                                </tr>

                                </table>

                            </div>-->



                            <div class="main-data">

                                <span class="velikost">183,00 m2</span><br />

                                <span class="cena">200.000,00 &euro;</span>

                            </div>

                        </div>

                        <div class="logo_container">

                            <div class="povezave">

                                <div class="prodajalec_o" title="Center nepremi?nin, Geoprojekt, Geodetske storitve, projektiranje, in?eniring, nepremi?nine d.o.o."><div class="logo"><a href="/oglasi-prodaja/zabukovica-soncno-in-dostopno-rahlo-pobocje-hisa_6028734/"><img src="https://picbase.turbosist.si/slonep_agenc120/791.jpg?v=20161017" /></a></div></div>

                            </div>

                            <div class="clearer"></div>

                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="6028734"></span>-->

                            <a class="ikona-sh3 utility" id="save-ad-6028734" href="#" data-id="6028734" onclick="save_ad(6028734); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>

                            <span class="utility" style="cursor: default;">

                                <i class="fa fa-share-square-o"></i>Deli na:

                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fzabukovica-soncno-in-dostopno-rahlo-pobocje-hisa_6028734%2F"

   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"

   target="_blank" title="Facebook">-->

                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fzabukovica-soncno-in-dostopno-rahlo-pobocje-hisa_6028734%2F', 'Facebook',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-facebook-square"></i>

                                </a>

                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fzabukovica-soncno-in-dostopno-rahlo-pobocje-hisa_6028734%2F', 'Twitter',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-twitter"></i>

                                </a>

                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fzabukovica-soncno-in-dostopno-rahlo-pobocje-hisa_6028734%2F', 'Google',500,350);" href="javascript:void(0);">

                                    <i class="fa fa-google-plus-square"></i>

                                </a>

                            </span>

                            <!--<a class="utility" data-id="6028734"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->

                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fzabukovica-soncno-in-dostopno-rahlo-pobocje-hisa_6028734%2F" class="utility" data-id="6028734"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po?lji prijatelju</span></a>

                            <a href="/oglasi-prodaja/zabukovica-soncno-in-dostopno-rahlo-pobocje-hisa_6028734/" class="utility contact-tooltip" title="03/710-38-10<br />Center nepremi?nin, Geoprojekt, Geodetske storitve, projektiranje, in?eniring, nepremi?nine d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>

                        </div>

                        <div class="clearer"></div>

                    </div>

                

                    <div class="oglas_container oglasbold oglas413" id="o5738990">

                        <h2><a href="/oglasi-prodaja/fazana-hisa_5738990/" title="5738990"><span class="title">FA?ANA</span></a></h2>

                        <a class="slika" href="/oglasi-prodaja/fazana-hisa_5738990/"><img src="https://picbase.turbosist.si/slonep_oglasi2/2662216.jpg" /><div class="vec"></div></a>

                        <div class="teksti_container">

                            <span class="posr">Prodaja: Hi?a</span>

                            <!--<div class="new-container">

                            

                            </div>-->

                            <div class="atributi">

                                <span class="atribut">Leto: <strong>1970</strong></span><span class="atribut">Zemlji??e: <strong>900 m2</strong></span>

                            </div>

                            <!---->

                            



                            <div class="kratek_container">

                                <div class="kratek">104 m2, samostojna, zgrajena l. 1970, 900 m2 zemlji??a, prodamo. Cena: 200.000,00 EUR</div>

                            </div>

                            <!--<div class="kratek_container">

                                <table>

                                <tr>

                                <td>

                                104 m2, samostojna, zgrajena l. 1970, 900 m2 zemlji??a, prodamo. Cena: 200.000,00 EUR

                                </td>

                                </tr>

                                </table>

                            </div>-->



                            <div class="main-data">

                                <span class="velikost">104,00 m2</span><br />

                                <span class="cena">200.000,00 &euro;</span>

                            </div>

                        </div>

                        <div class="logo_container">

                            <div class="povezave">

                                <div class="prodajalec_o" title="Istra-immobilien obrt za poslovanje nekretninama"><div class="logo"><a href="/oglasi-prodaja/fazana-hisa_5738990/"><img src="https://picbase.turbosist.si/slonep_agenc120/1195.jpg?v=20161017" /></a></div></div>

                            </div>

                            <div class="clearer"></div>

                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5738990"></span>-->

                            <a class="ikona-sh3 utility" id="save-ad-5738990" href="#" data-id="5738990" onclick="save_ad(5738990); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>

                            <span class="utility" style="cursor: default;">

                                <i class="fa fa-share-square-o"></i>Deli na:

                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Ffazana-hisa_5738990%2F"

   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"

   target="_blank" title="Facebook">-->

                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Ffazana-hisa_5738990%2F', 'Facebook',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-facebook-square"></i>

                                </a>

                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Ffazana-hisa_5738990%2F', 'Twitter',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-twitter"></i>

                                </a>

                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Ffazana-hisa_5738990%2F', 'Google',500,350);" href="javascript:void(0);">

                                    <i class="fa fa-google-plus-square"></i>

                                </a>

                            </span>

                            <!--<a class="utility" data-id="5738990"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->

                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Ffazana-hisa_5738990%2F" class="utility" data-id="5738990"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po?lji prijatelju</span></a>

                            <a href="/oglasi-prodaja/fazana-hisa_5738990/" class="utility contact-tooltip" title="+385989161212<br />Istra-immobilien obrt za poslovanje nekretninama"><i class="fa fa-phone"></i><span>O ponudniku</span></a>

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

            //]]>--></script><noscript><a href='https://ok.internetmedia.si/www/delivery/ck.php?n=a280490d&amp;cb=1846997495&amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5=' target='_blank'><img src='https://ok.internetmedia.si/www/delivery/avw.php?zoneid=5&amp;cb=694347416&amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5=&amp;n=a280490d' border='0' alt='' /></a></noscript>

                </div>

            

                    <div class="oglas_container oglasbold oglas561" id="o5967479">

                        <h2><a href="/oglasi-prodaja/kranjska-gora-borovska-cesta-stanovanje_5967479/" title="5967479"><span class="title">KRANJSKA GORA, BOROV?KA CESTA</span></a></h2>

                        <a class="slika" href="/oglasi-prodaja/kranjska-gora-borovska-cesta-stanovanje_5967479/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4153325.jpg" /><div class="vec"></div></a>

                        <div class="teksti_container">

                            <span class="posr">Prodaja: Stanovanje</span>

                            <!--<div class="new-container">

                            

                            </div>-->

                            <div class="atributi">

                                <span class="atribut">Nadstropje: <strong>1</strong>/2</span><span class="atribut">Leto: <strong>1990</strong></span>

                            </div>

                            <!---->

                            



                            <div class="kratek_container">

                                <div class="kratek">51,44 m2, 2-sobno, zgrajeno l. 1990, 1/2 nad., prodamo. Cena: cca 200.000,00 EUR</div>

                            </div>

                            <!--<div class="kratek_container">

                                <table>

                                <tr>

                                <td>

                                51,44 m2, 2-sobno, zgrajeno l. 1990, 1/2 nad., prodamo. Cena: cca 200.000,00 EUR

                                </td>

                                </tr>

                                </table>

                            </div>-->



                            <div class="main-data">

                                <span class="velikost">51,44 m2</span><br />

                                <span class="cena">200.000,00 &euro;</span>

                            </div>

                        </div>

                        <div class="logo_container">

                            <div class="povezave">

                                <div class="prodajalec_o" title="Exedra nepremi?nine - Dragan Du?ani? s.p."><div class="logo"><a href="/oglasi-prodaja/kranjska-gora-borovska-cesta-stanovanje_5967479/"><img src="https://picbase.turbosist.si/slonep_agenc120/1441.jpg?v=20161017" /></a></div></div>

                            </div>

                            <div class="clearer"></div>

                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5967479"></span>-->

                            <a class="ikona-sh3 utility" id="save-ad-5967479" href="#" data-id="5967479" onclick="save_ad(5967479); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>

                            <span class="utility" style="cursor: default;">

                                <i class="fa fa-share-square-o"></i>Deli na:

                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkranjska-gora-borovska-cesta-stanovanje_5967479%2F"

   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"

   target="_blank" title="Facebook">-->

                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkranjska-gora-borovska-cesta-stanovanje_5967479%2F', 'Facebook',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-facebook-square"></i>

                                </a>

                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkranjska-gora-borovska-cesta-stanovanje_5967479%2F', 'Twitter',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-twitter"></i>

                                </a>

                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkranjska-gora-borovska-cesta-stanovanje_5967479%2F', 'Google',500,350);" href="javascript:void(0);">

                                    <i class="fa fa-google-plus-square"></i>

                                </a>

                            </span>

                            <!--<a class="utility" data-id="5967479"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->

                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fkranjska-gora-borovska-cesta-stanovanje_5967479%2F" class="utility" data-id="5967479"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po?lji prijatelju</span></a>

                            <a href="/oglasi-prodaja/kranjska-gora-borovska-cesta-stanovanje_5967479/" class="utility contact-tooltip" title="041/703-806<br />Exedra nepremi?nine - Dragan Du?ani? s.p."><i class="fa fa-phone"></i><span>O ponudniku</span></a>

                        </div>

                        <div class="clearer"></div>

                    </div>

                

                    <div class="oglas_container oglasbold oglas259" id="o5998051">

                        <h2><a href="/oglasi-prodaja/portoroz-posest_5998051/" title="5998051"><span class="title">PORTORO?</span></a></h2>

                        <a class="slika" href="/oglasi-prodaja/portoroz-posest_5998051/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4383009.jpg" /><div class="vec"></div></a>

                        <div class="teksti_container">

                            <span class="posr">Prodaja: Posest</span>

                            <!--<div class="new-container">

                            

                            </div>-->

                            <div class="atributi">

                                

                            </div>

                            <!---->

                            



                            <div class="kratek_container">

                                <div class="kratek">532 m2, zazidljiva, prodamo. Cena: 200.000,00 EUR</div>

                            </div>

                            <!--<div class="kratek_container">

                                <table>

                                <tr>

                                <td>

                                532 m2, zazidljiva, prodamo. Cena: 200.000,00 EUR

                                </td>

                                </tr>

                                </table>

                            </div>-->



                            <div class="main-data">

                                <span class="velikost">532,00 m2</span><br />

                                <span class="cena">200.000,00 &euro;</span>

                            </div>

                        </div>

                        <div class="logo_container">

                            <div class="povezave">

                                <div class="prodajalec_o" title="GRE d.o.o."><div class="logo"><a href="/oglasi-prodaja/portoroz-posest_5998051/"><img src="https://picbase.turbosist.si/slonep_agenc120/1134.jpg?v=20161017" /></a></div></div>

                            </div>

                            <div class="clearer"></div>

                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5998051"></span>-->

                            <a class="ikona-sh3 utility" id="save-ad-5998051" href="#" data-id="5998051" onclick="save_ad(5998051); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>

                            <span class="utility" style="cursor: default;">

                                <i class="fa fa-share-square-o"></i>Deli na:

                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fportoroz-posest_5998051%2F"

   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"

   target="_blank" title="Facebook">-->

                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fportoroz-posest_5998051%2F', 'Facebook',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-facebook-square"></i>

                                </a>

                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fportoroz-posest_5998051%2F', 'Twitter',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-twitter"></i>

                                </a>

                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fportoroz-posest_5998051%2F', 'Google',500,350);" href="javascript:void(0);">

                                    <i class="fa fa-google-plus-square"></i>

                                </a>

                            </span>

                            <!--<a class="utility" data-id="5998051"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->

                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fportoroz-posest_5998051%2F" class="utility" data-id="5998051"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po?lji prijatelju</span></a>

                            <a href="/oglasi-prodaja/portoroz-posest_5998051/" class="utility contact-tooltip" title="041/601-474<br />GRE d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>

                        </div>

                        <div class="clearer"></div>

                    </div>

                

                    <div class="oglas_container oglasbold oglas899" id="o5920171">

                        <h2><a href="/oglasi-prodaja/portoroz-pacug-posest_5920171/" title="5920171"><span class="title">PORTORO?, PACUG</span></a></h2>

                        <a class="slika" href="/oglasi-prodaja/portoroz-pacug-posest_5920171/"><img src="https://picbase.turbosist.si/slonep_oglasi2/3815674.jpg" /><div class="vec"></div></a>

                        <div class="teksti_container">

                            <span class="posr">Prodaja: Posest</span>

                            <!--<div class="new-container">

                            

                            </div>-->

                            <div class="atributi">

                                

                            </div>

                            <!---->

                            



                            <div class="kratek_container">

                                <div class="kratek">532 m2, zazidljiva, prodamo. Cena: 200.000,00 EUR</div>

                            </div>

                            <!--<div class="kratek_container">

                                <table>

                                <tr>

                                <td>

                                532 m2, zazidljiva, prodamo. Cena: 200.000,00 EUR

                                </td>

                                </tr>

                                </table>

                            </div>-->



                            <div class="main-data">

                                <span class="velikost">532,00 m2</span><br />

                                <span class="cena">200.000,00 &euro;</span>

                            </div>

                        </div>

                        <div class="logo_container">

                            <div class="povezave">

                                <div class="prodajalec_o" title="GRE d.o.o."><div class="logo"><a href="/oglasi-prodaja/portoroz-pacug-posest_5920171/"><img src="https://picbase.turbosist.si/slonep_agenc120/1134.jpg?v=20161017" /></a></div></div>

                            </div>

                            <div class="clearer"></div>

                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5920171"></span>-->

                            <a class="ikona-sh3 utility" id="save-ad-5920171" href="#" data-id="5920171" onclick="save_ad(5920171); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>

                            <span class="utility" style="cursor: default;">

                                <i class="fa fa-share-square-o"></i>Deli na:

                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fportoroz-pacug-posest_5920171%2F"

   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"

   target="_blank" title="Facebook">-->

                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fportoroz-pacug-posest_5920171%2F', 'Facebook',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-facebook-square"></i>

                                </a>

                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fportoroz-pacug-posest_5920171%2F', 'Twitter',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-twitter"></i>

                                </a>

                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fportoroz-pacug-posest_5920171%2F', 'Google',500,350);" href="javascript:void(0);">

                                    <i class="fa fa-google-plus-square"></i>

                                </a>

                            </span>

                            <!--<a class="utility" data-id="5920171"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->

                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fportoroz-pacug-posest_5920171%2F" class="utility" data-id="5920171"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po?lji prijatelju</span></a>

                            <a href="/oglasi-prodaja/portoroz-pacug-posest_5920171/" class="utility contact-tooltip" title="041/601-474<br />GRE d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>

                        </div>

                        <div class="clearer"></div>

                    </div>

                

                    <div class="oglas_container oglasbold oglas263" id="o5998056">

                        <h2><a href="/oglasi-prodaja/portoroz-pacug-posest_5998056/" title="5998056"><span class="title">PORTORO?, PACUG</span></a></h2>

                        <a class="slika" href="/oglasi-prodaja/portoroz-pacug-posest_5998056/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4383018.jpg" /><div class="vec"></div></a>

                        <div class="teksti_container">

                            <span class="posr">Prodaja: Posest</span>

                            <!--<div class="new-container">

                            

                            </div>-->

                            <div class="atributi">

                                

                            </div>

                            <!---->

                            



                            <div class="kratek_container">

                                <div class="kratek">532 m2, zazidljiva, prodamo. Cena: 200.000,00 EUR</div>

                            </div>

                            <!--<div class="kratek_container">

                                <table>

                                <tr>

                                <td>

                                532 m2, zazidljiva, prodamo. Cena: 200.000,00 EUR

                                </td>

                                </tr>

                                </table>

                            </div>-->



                            <div class="main-data">

                                <span class="velikost">532,00 m2</span><br />

                                <span class="cena">200.000,00 &euro;</span>

                            </div>

                        </div>

                        <div class="logo_container">

                            <div class="povezave">

                                <div class="prodajalec_o" title="GRE d.o.o."><div class="logo"><a href="/oglasi-prodaja/portoroz-pacug-posest_5998056/"><img src="https://picbase.turbosist.si/slonep_agenc120/1134.jpg?v=20161017" /></a></div></div>

                            </div>

                            <div class="clearer"></div>

                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5998056"></span>-->

                            <a class="ikona-sh3 utility" id="save-ad-5998056" href="#" data-id="5998056" onclick="save_ad(5998056); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>

                            <span class="utility" style="cursor: default;">

                                <i class="fa fa-share-square-o"></i>Deli na:

                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fportoroz-pacug-posest_5998056%2F"

   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"

   target="_blank" title="Facebook">-->

                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fportoroz-pacug-posest_5998056%2F', 'Facebook',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-facebook-square"></i>

                                </a>

                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fportoroz-pacug-posest_5998056%2F', 'Twitter',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-twitter"></i>

                                </a>

                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fportoroz-pacug-posest_5998056%2F', 'Google',500,350);" href="javascript:void(0);">

                                    <i class="fa fa-google-plus-square"></i>

                                </a>

                            </span>

                            <!--<a class="utility" data-id="5998056"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->

                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fportoroz-pacug-posest_5998056%2F" class="utility" data-id="5998056"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po?lji prijatelju</span></a>

                            <a href="/oglasi-prodaja/portoroz-pacug-posest_5998056/" class="utility contact-tooltip" title="041/601-474<br />GRE d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>

                        </div>

                        <div class="clearer"></div>

                    </div>

                

                    <div class="oglas_container oglasbold oglas146" id="o5956028">

                        <h2><a href="/oglasi-prodaja/ljubija-posest_5956028/" title="5956028"><span class="title">LJUBIJA</span></a></h2>

                        <a class="slika" href="/oglasi-prodaja/ljubija-posest_5956028/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4082304.jpg" /><div class="vec"></div></a>

                        <div class="teksti_container">

                            <span class="posr">Prodaja: Posest</span>

                            <!--<div class="new-container">

                            

                            </div>-->

                            <div class="atributi">

                                

                            </div>

                            <!---->

                            



                            <div class="kratek_container">

                                <div class="kratek">50.347 m2, kmetija, prodamo. Cena: 200.000,00 EUR</div>

                            </div>

                            <!--<div class="kratek_container">

                                <table>

                                <tr>

                                <td>

                                50.347 m2, kmetija, prodamo. Cena: 200.000,00 EUR

                                </td>

                                </tr>

                                </table>

                            </div>-->



                            <div class="main-data">

                                <span class="velikost">50.347,00 m2</span><br />

                                <span class="cena">200.000,00 &euro;</span>

                            </div>

                        </div>

                        <div class="logo_container">

                            <div class="povezave">

                                <div class="prodajalec_o" title="Janko nepremi?nine, Ema Janko s.p."><div class="logo"><a href="/oglasi-prodaja/ljubija-posest_5956028/"><img src="/images/ponudba-podjetja.png" /></a></div></div>

                            </div>

                            <div class="clearer"></div>

                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5956028"></span>-->

                            <a class="ikona-sh3 utility" id="save-ad-5956028" href="#" data-id="5956028" onclick="save_ad(5956028); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>

                            <span class="utility" style="cursor: default;">

                                <i class="fa fa-share-square-o"></i>Deli na:

                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fljubija-posest_5956028%2F"

   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"

   target="_blank" title="Facebook">-->

                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fljubija-posest_5956028%2F', 'Facebook',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-facebook-square"></i>

                                </a>

                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fljubija-posest_5956028%2F', 'Twitter',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-twitter"></i>

                                </a>

                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fljubija-posest_5956028%2F', 'Google',500,350);" href="javascript:void(0);">

                                    <i class="fa fa-google-plus-square"></i>

                                </a>

                            </span>

                            <!--<a class="utility" data-id="5956028"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->

                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fljubija-posest_5956028%2F" class="utility" data-id="5956028"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po?lji prijatelju</span></a>

                            <a href="/oglasi-prodaja/ljubija-posest_5956028/" class="utility contact-tooltip" title="051/307-035<br />Janko nepremi?nine, Ema Janko s.p."><i class="fa fa-phone"></i><span>O ponudniku</span></a>

                        </div>

                        <div class="clearer"></div>

                    </div>

                

                    <div class="oglas_container oglasbold oglas144" id="o5985166">

                        <h2><a href="/oglasi-prodaja/maribor-taborska-ulica-hisa_5985166/" title="5985166"><span class="title">MARIBOR, TABORSKA ULICA</span></a></h2>

                        <a class="slika" href="/oglasi-prodaja/maribor-taborska-ulica-hisa_5985166/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4285631.jpg" /><div class="vec"></div></a>

                        <div class="teksti_container">

                            <span class="posr">Prodaja: Hi?a</span>

                            <!--<div class="new-container">

                            

                            </div>-->

                            <div class="atributi">

                                <span class="atribut">Leto: <strong>1907</strong></span><span class="atribut">Zemlji??e: <strong>291 m2</strong></span>

                            </div>

                            <!---->

                            



                            <div class="kratek_container">

                                <div class="kratek">308 m2, hi?a, zgrajena l. 1907, 291 m2 zemlji??a, V Mariboru, Taborska ulica v bli?ini medicinske fakultete prodamo stan...</div>

                            </div>

                            <!--<div class="kratek_container">

                                <table>

                                <tr>

                                <td>

                                308 m2, hi?a, zgrajena l. 1907, 291 m2 zemlji??a, V Mariboru, Taborska ulica v bli?ini medicinske fakultete prodamo stan...

                                </td>

                                </tr>

                                </table>

                            </div>-->



                            <div class="main-data">

                                <span class="velikost">308,00 m2</span><br />

                                <span class="cena">200.000,00 &euro;</span>

                            </div>

                        </div>

                        <div class="logo_container">

                            <div class="povezave">

                                <div class="prodajalec_o" title="K2 finance d.o.o."><div class="logo"><a href="/oglasi-prodaja/maribor-taborska-ulica-hisa_5985166/"><img src="https://picbase.turbosist.si/slonep_agenc120/1351.jpg?v=20161017" /></a></div></div>

                            </div>

                            <div class="clearer"></div>

                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5985166"></span>-->

                            <a class="ikona-sh3 utility" id="save-ad-5985166" href="#" data-id="5985166" onclick="save_ad(5985166); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>

                            <span class="utility" style="cursor: default;">

                                <i class="fa fa-share-square-o"></i>Deli na:

                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmaribor-taborska-ulica-hisa_5985166%2F"

   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"

   target="_blank" title="Facebook">-->

                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmaribor-taborska-ulica-hisa_5985166%2F', 'Facebook',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-facebook-square"></i>

                                </a>

                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmaribor-taborska-ulica-hisa_5985166%2F', 'Twitter',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-twitter"></i>

                                </a>

                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmaribor-taborska-ulica-hisa_5985166%2F', 'Google',500,350);" href="javascript:void(0);">

                                    <i class="fa fa-google-plus-square"></i>

                                </a>

                            </span>

                            <!--<a class="utility" data-id="5985166"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->

                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmaribor-taborska-ulica-hisa_5985166%2F" class="utility" data-id="5985166"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po?lji prijatelju</span></a>

                            <a href="/oglasi-prodaja/maribor-taborska-ulica-hisa_5985166/" class="utility contact-tooltip" title="02/234-75-58<br />K2 finance d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>

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

            //]]>--></script><noscript><a href='https://ok.internetmedia.si/www/delivery/ck.php?n=a280490d&amp;cb=525439263&amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5=' target='_blank'><img src='https://ok.internetmedia.si/www/delivery/avw.php?zoneid=5&amp;cb=527093999&amp;f1=1&amp;f2=0&amp;f3=0&amp;f4=&amp;f5=&amp;n=a280490d' border='0' alt='' /></a></noscript>

                </div>

            

                    <div class="oglas_container oglasbold oglas672" id="o5952316">

                        <h2><a href="/oglasi-prodaja/lj-moste-stanovanje_5952316/" title="5952316"><span class="title">LJ. MOSTE</span></a></h2>

                        <a class="slika" href="/oglasi-prodaja/lj-moste-stanovanje_5952316/"><img src="https://picbase.turbosist.si/slonep_oglasi2/4054088.jpg" /><div class="vec"></div></a>

                        <div class="teksti_container">

                            <span class="posr">Prodaja: Stanovanje</span>

                            <!--<div class="new-container">

                            

                            </div>-->

                            <div class="atributi">

                                <span class="atribut">Nadstropje: <strong>P</strong>/1</span><span class="atribut">Leto: <strong>1900</strong></span>

                            </div>

                            <!---->

                            



                            <div class="kratek_container">

                                <div class="kratek">118,6 m2, 3,5-sobno, zgrajeno l. 1900, adaptirano l. 1965, P/1 nad., Stanovanje se nahaja v hi?i in je sestavljeno iz pr...</div>

                            </div>

                            <!--<div class="kratek_container">

                                <table>

                                <tr>

                                <td>

                                118,6 m2, 3,5-sobno, zgrajeno l. 1900, adaptirano l. 1965, P/1 nad., Stanovanje se nahaja v hi?i in je sestavljeno iz pr...

                                </td>

                                </tr>

                                </table>

                            </div>-->



                            <div class="main-data">

                                <span class="velikost">118,60 m2</span><br />

                                <span class="cena">200.000,00 &euro;</span>

                            </div>

                        </div>

                        <div class="logo_container">

                            <div class="povezave">

                                <div class="prodajalec_o" title="Kristal nepremi?nine d.o.o."><div class="logo"><a href="/oglasi-prodaja/lj-moste-stanovanje_5952316/"><img src="/images/ponudba-podjetja.png" /></a></div></div>

                            </div>

                            <div class="clearer"></div>

                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5952316"></span>-->

                            <a class="ikona-sh3 utility" id="save-ad-5952316" href="#" data-id="5952316" onclick="save_ad(5952316); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>

                            <span class="utility" style="cursor: default;">

                                <i class="fa fa-share-square-o"></i>Deli na:

                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-moste-stanovanje_5952316%2F"

   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"

   target="_blank" title="Facebook">-->

                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-moste-stanovanje_5952316%2F', 'Facebook',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-facebook-square"></i>

                                </a>

                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-moste-stanovanje_5952316%2F', 'Twitter',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-twitter"></i>

                                </a>

                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-moste-stanovanje_5952316%2F', 'Google',500,350);" href="javascript:void(0);">

                                    <i class="fa fa-google-plus-square"></i>

                                </a>

                            </span>

                            <!--<a class="utility" data-id="5952316"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->

                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Flj-moste-stanovanje_5952316%2F" class="utility" data-id="5952316"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po?lji prijatelju</span></a>

                            <a href="/oglasi-prodaja/lj-moste-stanovanje_5952316/" class="utility contact-tooltip" title="040/692-662<br />Kristal nepremi?nine d.o.o."><i class="fa fa-phone"></i><span>O ponudniku</span></a>

                        </div>

                        <div class="clearer"></div>

                    </div>

                

                    <div class="oglas_container oglasbold oglas767" id="o5629527">

                        <h2><a href="/oglasi-prodaja/malinska-hisa_5629527/" title="5629527"><span class="title">MALINSKA</span></a></h2>

                        <a class="slika" href="/oglasi-prodaja/malinska-hisa_5629527/"><img src="https://picbase.turbosist.si/slonep_oglasi2/2139815.jpg" /><div class="vec"></div></a>

                        <div class="teksti_container">

                            <span class="posr">Prodaja: Hi?a</span>

                            <!--<div class="new-container">

                            

                            </div>-->

                            <div class="atributi">

                                <span class="atribut">Leto: <strong>2011</strong></span><span class="atribut">Zemlji??e: <strong>198 m2</strong></span>

                            </div>

                            <!---->

                            



                            <div class="kratek_container">

                                <div class="kratek">118 m2, dvoj?ek, zgrajen l. 2011, 198 m2 zemlji??a, Prodaja nepremi?nin Malinska / Nov kakovosten dvoj?ek z veliko teras...</div>

                            </div>

                            <!--<div class="kratek_container">

                                <table>

                                <tr>

                                <td>

                                118 m2, dvoj?ek, zgrajen l. 2011, 198 m2 zemlji??a, Prodaja nepremi?nin Malinska / Nov kakovosten dvoj?ek z veliko teras...

                                </td>

                                </tr>

                                </table>

                            </div>-->



                            <div class="main-data">

                                <span class="velikost">118,00 m2</span><br />

                                <span class="cena">200.000,00 &euro;</span>

                            </div>

                        </div>

                        <div class="logo_container">

                            <div class="povezave">

                                <div class="prodajalec_o" title="Kvarner imobilije d.o.o. Njivice"><div class="logo"><a href="/oglasi-prodaja/malinska-hisa_5629527/"><img src="https://picbase.turbosist.si/slonep_agenc120/167.jpg?v=20161017" /></a></div></div>

                            </div>

                            <div class="clearer"></div>

                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5629527"></span>-->

                            <a class="ikona-sh3 utility" id="save-ad-5629527" href="#" data-id="5629527" onclick="save_ad(5629527); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>

                            <span class="utility" style="cursor: default;">

                                <i class="fa fa-share-square-o"></i>Deli na:

                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmalinska-hisa_5629527%2F"

   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"

   target="_blank" title="Facebook">-->

                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmalinska-hisa_5629527%2F', 'Facebook',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-facebook-square"></i>

                                </a>

                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmalinska-hisa_5629527%2F', 'Twitter',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-twitter"></i>

                                </a>

                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmalinska-hisa_5629527%2F', 'Google',500,350);" href="javascript:void(0);">

                                    <i class="fa fa-google-plus-square"></i>

                                </a>

                            </span>

                            <!--<a class="utility" data-id="5629527"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->

                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fmalinska-hisa_5629527%2F" class="utility" data-id="5629527"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po?lji prijatelju</span></a>

                            <a href="/oglasi-prodaja/malinska-hisa_5629527/" class="utility contact-tooltip" title="+385 (0)51 847 074<br />Kvarner imobilije d.o.o. Njivice"><i class="fa fa-phone"></i><span>O ponudniku</span></a>

                        </div>

                        <div class="clearer"></div>

                    </div>

                

                    <div class="oglas_container oglasbold oglas441" id="o5765287">

                        <h2><a href="/oglasi-prodaja/dobrinj-hisa_5765287/" title="5765287"><span class="title">DOBRINJ</span></a></h2>

                        <a class="slika" href="/oglasi-prodaja/dobrinj-hisa_5765287/"><img src="https://picbase.turbosist.si/slonep_oglasi2/2818980.jpg" /><div class="vec"></div></a>

                        <div class="teksti_container">

                            <span class="posr">Prodaja: Hi?a</span>

                            <!--<div class="new-container">

                            

                            </div>-->

                            <div class="atributi">

                                <span class="atribut">Leto: <strong>1900</strong></span><span class="atribut">Zemlji??e: <strong>90 m2</strong></span>

                            </div>

                            <!---->

                            



                            <div class="kratek_container">

                                <div class="kratek">114 m2, dvoj?ek, zgrajen l. 1900, adaptiran l. 2012, 90 m2 zemlji??a, Kamnita hi?a z zemlji??em in veliko &quot;konobo&q...</div>

                            </div>

                            <!--<div class="kratek_container">

                                <table>

                                <tr>

                                <td>

                                114 m2, dvoj?ek, zgrajen l. 1900, adaptiran l. 2012, 90 m2 zemlji??a, Kamnita hi?a z zemlji??em in veliko &quot;konobo&q...

                                </td>

                                </tr>

                                </table>

                            </div>-->



                            <div class="main-data">

                                <span class="velikost">114,00 m2</span><br />

                                <span class="cena">200.000,00 &euro;</span>

                            </div>

                        </div>

                        <div class="logo_container">

                            <div class="povezave">

                                <div class="prodajalec_o" title="Kvarner imobilije d.o.o. Njivice"><div class="logo"><a href="/oglasi-prodaja/dobrinj-hisa_5765287/"><img src="https://picbase.turbosist.si/slonep_agenc120/167.jpg?v=20161017" /></a></div></div>

                            </div>

                            <div class="clearer"></div>

                            <!--<span class="ikona-sh ajs" title="Shrani oglas" data-id="5765287"></span>-->

                            <a class="ikona-sh3 utility" id="save-ad-5765287" href="#" data-id="5765287" onclick="save_ad(5765287); return false;"><i class="fa fa-star-o"></i><i class="fa fa-star"></i><span>Shrani oglas</span></a>

                            <span class="utility" style="cursor: default;">

                                <i class="fa fa-share-square-o"></i>Deli na:

                                <!--<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fdobrinj-hisa_5765287%2F"

   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600,left=window.middle_h_screen,top=window.middle_v_screen');return false;"

   target="_blank" title="Facebook">-->

                                <a title="Facebook" onclick="popupCenter('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fdobrinj-hisa_5765287%2F', 'Facebook',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-facebook-square"></i>

                                </a>

                                <a title="Twitter" onclick="popupCenter('https://twitter.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fdobrinj-hisa_5765287%2F', 'Twitter',600,300);" href="javascript:void(0);">

                                    <i class="fa fa-twitter"></i>

                                </a>

                                <a title="Google+" onclick="popupCenter('https://plus.google.com/share?url=https%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fdobrinj-hisa_5765287%2F', 'Google',500,350);" href="javascript:void(0);">

                                    <i class="fa fa-google-plus-square"></i>

                                </a>

                            </span>

                            <!--<a class="utility" data-id="5765287"><i class="fa fa-trash-o"></i><i class="fa fa-trash"></i><span>Skrij oglas</span></a>-->

                            <a href="mailto:?subject=Zanimiva%20ponudba%20na%20NEPREMICNINE.net&amp;body=Pozdravljen-a!%0A%0ANa%20straneh%20NEPREMICNINE.net%20sem%20zasledil/a%20zanimivo%20ponudbo,%20ki%20te%20bo%20morda%20zanimala:%0A%0Ahttps%3A%2F%2Fwww.nepremicnine.net%2Foglasi-prodaja%2Fdobrinj-hisa_5765287%2F" class="utility" data-id="5765287"><i class="fa fa-envelope-o"></i><i class="fa fa-envelope"></i><span>Po?lji prijatelju</span></a>

                            <a href="/oglasi-prodaja/dobrinj-hisa_5765287/" class="utility contact-tooltip" title="+385 (0)51 847 074<br />Kvarner imobilije d.o.o. Njivice"><i class="fa fa-phone"></i><span>O ponudniku</span></a>

                        </div>

                        <div class="clearer"></div>

                    </div>

                </div><div class="spacer"></div><div id="pagination" class="fr"><ul><li><a href="/oglasi-prodaja/cena-do-200000-eur/?s=13" class="active">1</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/2/?s=13">2</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/3/?s=13">3</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/4/?s=13">4</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/5/?s=13">5</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/6/?s=13">6</a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/7/?s=13">7</a></li><span class="dots3">...</span><li><a href="/oglasi-prodaja/cena-do-200000-eur/2/?s=13" class="next">></a></li><li><a href="/oglasi-prodaja/cena-do-200000-eur/652/?s=13" class="last">>></a></li></ul></div>

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

		<strong>MEGANET d.o.o. ? 1998 - 2016</strong><br />

		Kontakt: 03/567-91-10<br />

		E-po?ta: <a href="mailto:info@nepremicnine.net" class="nn">info@nepremicnine.net</a>

	</div>

	<div class="spacer"></div>

	<div class="spacer"></div>

	<div class="block">

		<strong>Tehni?na podpora: </strong><br />

		INTERNET MEDIA d.o.o.<br />

				E-po?ta: <a href="mailto:podpora@nepremicnine.net" class="nn">podpora@nepremicnine.net</a>

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

			<li><a href="/nepremicnine.html?q=menjava nepremi?nine" title="menjava nepremi?nine"><strong>Menjava nepremi?nine</strong></a></li>

			<li><a href="/pravno-pojasnilo.html">Pravno pojasnilo</a></li>

			<li><a href="/nepremicnine-oglasevanje.html">Ogla?evanje</a></li>

			<li><a href="/cookies.html">O pi?kotkih</a></li>

			<li class="last"><a href="/pomoc-in-svetovanje.html">Pomo?</a></li>		</ul>

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






