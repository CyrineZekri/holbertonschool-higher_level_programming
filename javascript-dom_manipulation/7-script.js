fetch('https://swapi-api.hbtn.io/api/films/?format=json')
.then(function(response){
    return response.json();
})
.then(function(data){
    const movies=data.results;
    const list=document.getElementById('list_movies');
    movies.forEach(function(movie){
        const listItem=document.createElement('li');
        listItem.textContent=movie.title;
        list.appendChild(listItem);
    });
})
.catch(function(error){
    console.error('Error:',error);
});