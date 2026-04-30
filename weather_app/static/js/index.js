function getWeatherLocationAndSend(){
    if(navigator.geolocation){
        navigator.geolocation.getCurrentPosition(function(position){

            const lat = position.coords.latitude
            const lon = position.coords.longitude

            console.log("SENDING:",lat,lon);

            fetch(WEATHER_URL,{

                method:"POST",

                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCsrfToken()
                },

                body: JSON.stringify({
                    lat:lat,
                    lon:lon
                })
        
            }).then(response => response.json())
            .then(data => {
                if(data.cod != 200){
                    alert(data.message)
                    return;
                }
                document.getElementById('city').innerText = data.name
                document.getElementById('temperature').innerText = data['main']['temp'] + 'c'
                document.getElementById('description').innerText = data['weather'][0]['description']
                document.getElementById('humidity').innerText = data['main']['humidity']
                document.getElementById('pressure').innerText = data['main']['pressure']
                document.getElementById('wind-speed').innerText = data['wind']['speed']
            })

        })
    }else{
        alert("Geolocation not supported")
    }
}