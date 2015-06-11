<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>ODTÜ Dernek Portalı</title>

    <!-- Bootstrap -->
    <link href="/static/css/bootstrap.min.css" rel="stylesheet">

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
    <link href="/static/css/style.css" rel="stylesheet" type="text/css">
  </head>
  <body>
  
  <link href="//netdna.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">
  
    <div class="navbar navbar-default navbar-fixed-top" role="navigation">
    
        <div class="container">
         <!-- Tarayıcı Boyutuna göre (Mobile vs.) otomatik ayar yapılır -->
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-ex1-collapse">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                
            </div>
            <div class="collapse navbar-collapse navbar-ex1-collapse">
                <ul class="nav navbar-nav">
                    <li class="menu-item"><a href="#">Hakkımızda</a></li></ul>
                    <ul class="nav navbar-nav">
                        <li class="menu-item"><a href="#">İletişim</a></li></ul>
                        <ul class="nav navbar-nav">
                            <li class="menu-item"><a href="#">Destek<i class="fa fa-support destek-blue"></i></a></li></ul>
                            <ul class="nav navbar-nav">
                                <li class="menu-item"><a href="#">Blog<i class="fa fa-comments-o blog-blue"></i></a></li></ul>
                            
                            <ul class="nav navbar-nav ">
                                <li>
                                    <form class="navbar-search navbar-form" action="" method="get">
                                        <input name="s" class="form-control" type="text" placeholder="Arama Yap">
                                    </form>
                                </li>
                                <li>
                                    <a title="Twitter" href="http://www.twitter.com/" target="_blank" rel="nofollow">
                                        <i class="fa fa-twitter-square fa-lg twitter-blue"></i>
                                    </a>
                                </li>
                                <li>
                                    <a title="Facebook" href="http://www.facebook.com/" target="_blank" rel="nofollow">
                                        <i class="fa fa-facebook-square fa-lg facebook-blue"></i>
                                    </a>
                                </li>
                                <li>
                                    <a title="Youtube" href="http://www.youtube.com/" target="_blank" rel="nofollow">
                                        <i class="fa fa-youtube fa-lg youtube-blue"></i>
                                    </a>
                                </li>
                                <li>
        					        <a title="Google+" href="https://plus.google.com/" target="_blank" rel="nofollow">
							        	<i class="fa fa-google-plus fa-lg google-blue"></i>
							        </a>
    					        </li>
                                 <li>
                                 <li>
        					        <a title="Instagram" href="http://instagram.com//" target="_blank" rel="nofollow">
							        	<i class="fa fa-instagram fa-lg instagram-blue"></i>
							        </a>
    					        </li>
                             </ul>
                        
                    
                
                <!-- DROPDOWN LOGIN STARTS HERE  -->
                <ul class="nav navbar-nav navbar-right" id="signInDropdown">
                    <li class="dropdown">
                        <button class="btn btn-info navbar-btn dropdown-toggle" id="dropdownMenu1" type="button" data-toggle="dropdown"><i class="glyphicon glyphicon-user"></i> Giriş Yap <span class="caret"></span></button>
                        <ul class="dropdown-menu">
                          <li style="width: 250px;">
                                <form class="navbar-form form" role="form">
                                    <div class="form-group">
                                      <div class="input-group">
                                            <span class="input-group-addon"><i class="glyphicon glyphicon-envelope color-blue"></i></span>
                                            <!--EMAIL ADDRESS-->
                                            <input class="form-control" id="emailInput" required="" onchange="try{setCustomValidity('')}catch(e){}" oninvalid="setCustomValidity('Please enter a valid email address!')" type="email" placeholder="email adresi">
                                      </div>
                                    </div>
                                    <div class="form-group">
                                        <div class="input-group">
                                            <span class="input-group-addon"><i class="glyphicon glyphicon-lock color-blue"></i></span>
                                            <!--PASSWORD-->
                                            <input class="form-control" id="passwordInput" required="" onchange="try{setCustomValidity('')}catch(e){}" oninvalid="setCustomValidity('Please enter a password!')" type="password" placeholder="parola">
                                        </div>
                                    </div>
                                    <!--  BASIC ERROR MESSAGE
                                    <div class="form-group">
                                    <label class="error-message color-red">*Email &amp; password don't match!</label>
                                    </div>
                                    -->
                                    <div class="form-group">
                                        <!--buton-->
                                        <button class="btn btn-primary form-control" type="submit">Giriş</button>
                                    </div>
                                    <div class="form-group">
                                        <!--parola sıfırlama linki-->
                                        <span class="pull-right"><a href="#">Şifremi Unuttum?</a></span>
                                    </div>
                                </form>
                          </li>
                        </ul>
                    </li>
                </ul>
                <!-- DROPDOWN LOGIN ENDS HERE  -->
                
            
        </div>
        
    </div>
    </div>

<!--header başlangıcı --->
	<header>
  <div id="masthead">
  <div class="container">
    <div class="row">
      <div class="col-md-6">
        <div class="logo">
         <a href="index1.php"><img src="/static/images/logo.png" class="img-responsive"></a>
          <h2><p class="lead"></p></h2>
          </div>
      </div>
      
      <div class="col-md-5">
        
        <div class="advertise">
          <img src="/static/images/728 x 90 advertise.jpg" class="img-responsive">
        </div>
      </div>
    </div>
  </div>
  </div>
</header>
<!--header bitimi --->

                   
    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="/static/js/bootstrap.min.js"></script>
  </body>
</html>
