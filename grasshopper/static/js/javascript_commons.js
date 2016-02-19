//Javascript Commons File


      function defineCookie(cookie_name, cookie_result) {
                if (document.cookie != document.cookie) {index = document.cookie.indexOf(cookie_name);} else { index = -1;}
                if (index == -1) { document.cookie=cookie_name+"="+cookie_result+"; expires=Monday, 04-Apr-2020 05:00:00 GMT"; }
                console.log("hello");
                console.log(cookie_name);
                console.log(cookie_result);
                console.log("hello");
            }

            function close_accordion_section() {
                jQuery('.accordion .accordion-section-title').removeClass('active');
                jQuery('.accordion .accordion-section-content').slideUp(300).removeClass('open');
            }

            function passCookie(id,value){
                if (value != ''){
                    document.getElementById(id).innerHTML = value;
                    defineCookie(id, value);
                    console.log(id);
                    console.log(value);
                    close_accordion_section();
                }
            }

      function getCookie(cookie_name) {
        if(document.cookie) {
          index = document.cookie.indexOf(cookie_name);
          if (index != -1) {
            namestart = (document.cookie.indexOf("=", index) + 1);
            nameend = document.cookie.indexOf(";", index);
          if (nameend == -1) {nameend = document.cookie.length;}
            return document.cookie.substring(namestart, nameend);
          }
        }
      }

            function onLoad() {
              gapi.load('auth2', function() {
                gapi.auth2.init();
              });
            }
            function signOut() {
                var auth2 = gapi.auth2.getAuthInstance();
                auth2.signOut().then(function () {
                  console.log('User signed out.');
                });
                window.location = "http://andrewgoldstein.github.io/login.html" ;
            }
              
            function onSignIn(googleUser) {
              try {
                    console.log(googleUser);
              }
              catch(err) {
                    window.location = "http://andrewgoldstein.github.io/login.html" ;
              }
            }   

              function populate_dropdown(ports, div){
          for (var i = 0, l = ports.length; i < l; ++i) {
                                      document.getElementById(div).innerHTML += '<option value="'+ ports[i].city.toString() + '">' + ports[i].city.toString() +'</option>';
                                    };
        }






    function onSignIn2(googleUser) {
      var profile = googleUser.getBasicProfile();
            try {
                  console.log(googleUser);
                  defineCookie('current_user', profile.getName());  
                  window.location = "http://localhost:5000/users" ;
            }
            catch(err) {
                  console.log( "NO NO NO NO"  );
            }
      //console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
      console.log('Email: ' + profile.getEmail());
      console.log('Name: ' + profile.getName());
      //console.log('Image URL: ' + profile.getImageUrl());
    }



    
      function reloaddiv(div) {
          var origin = getCookie("origin");
          document.getElementById(div).innerHTML = '<option value="select">Select Destination</option>' ;
                var valid_airports = [];
                for (var i = 0, l = airports.length; i < l; ++i) {
                    if (origin != airports[i].city) {valid_airports.push(airports[i])}
                };
                populate_dropdown(valid_airports,div);
                                    
      }

                                            function haversineDistance(lat1,lon1, lat2,lon2) {
                                              function toRad(x) {
                                                return x * Math.PI / 180;
                                              }

                                              var R = 6371; // km

                                              var x1 = lat2 - lat1;
                                              var dLat = toRad(x1);
                                              var x2 = lon2 - lon1;
                                              var dLon = toRad(x2)
                                              var a = Math.sin(dLat / 2) * Math.sin(dLat / 2) +
                                                Math.cos(toRad(lat1)) * Math.cos(toRad(lat2)) *
                                                Math.sin(dLon / 2) * Math.sin(dLon / 2);
                                              var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
                                              var d = R * c;
                                              return d;
                                            } 
                                            function closest_airport(lat,lon)  {
                                                var home_airport = '';
                                                var dist = 1000000;
                                                for (i = 0; i < airports.length; i++) {
                                                  distance_from_airport = haversineDistance(airports[i].lat, airports[i].lon, lat, lon);
                                                  if (distance_from_airport < dist) {
                                                    dist = distance_from_airport;
                                                    home_airport = airports[i].city
                                                  }
                                                }
                                                if (home_airport != ''){
                                                  console.log(home_airport)
                                                  return home_airport
                                                }
                                                else {
                                                  return false
                                                }
                                            }