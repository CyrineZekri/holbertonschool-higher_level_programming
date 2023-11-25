const add_button=document.getElementById('add_item');
const my_list= document.querySelector('.my_list');
add_button.addEventListener('click',function(){
    const new_item=document.createElement('li');
    new_item.textContent='item';
    my_list.appendChild(new_item);
});