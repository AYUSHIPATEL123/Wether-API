function getWeatherLocationAndSend(){
    if(navigator.geolocation){
        navigator.geolocation.getCurrentPosition(function(position){

            const lat = position.coords.latitude
            const log = position.coords.longitude

            fetch(WEATHER_URL,{

                method:"POST",

                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCsrfToken()
                },

                body:JSON.stringify({
                    lat:lat,
                    log:log
                })
            }).then(response => response.json())
            .then(data => console.log(data))

        })
    }else{
        alert("Geolocation not supported")
    }
}