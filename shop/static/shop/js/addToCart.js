window.onload = function(){
  // Search 'Cart' object in the local storage
  if(localStorage.getItem('cart') == null){
    var cart = {};
  }
  else{
    cart = JSON.parse(localStorage.getItem('cart'));
    overwrite();
  }

  // Event Click Handler Function
  // Add to Cart Button Clicked Function
  $('.addTocart').click(function(){
  var product_btn_id = this.id.toString();
  if(cart[product_btn_id] != undefined){
    cart[product_btn_id] = cart[product_btn_id] + 1;
  }
  else{
    cart[product_btn_id] = 1;
  }
  localStorage.setItem('cart', JSON.stringify(cart));
  console.log(cart);
  // Function to overwrite in the 'Cart' link in NavBar
  overwrite();
  });

  // Function to return the sum of elements in the cart
  function sum_of_items(){
    let sum = 0;
    Object.values(cart).forEach(element => {
      sum+=element;
    });
    return sum;
  }

  // Funtion to change the cart number 
  // To overwrite the items number
  function overwrite(){
    document.getElementById("cartDetailLink").innerHTML = sum_of_items();
  }
}



