// Click to add a whole new item
function getSelectedItem(type,product_id){
    let c = document.getElementById(type+product_id);
    let  color_option = c.options[c.selectedIndex].text;
    return color_option;

}
$(document).ready(function(){
    $('.btn-add-product').on('click', function(){
        let url = $(this).attr('url');
        let product_id = $(this).attr('product_id');
        // // get the color
        let color_option = getSelectedItem("Color",product_id);
        // // get the size
        let size_option =  getSelectedItem("Size",product_id)

        $.ajax({
            url: url,
            data: {
                "color": color_option,
                "size": size_option
            },
            success: function(data){
                // set quantity of cart icon
                document.getElementById("quantity-cart").innerHTML = data.quantity;
                alert('Add product to cart successfully');
            }
        });
        return false;  // use this for not reloading
    });
});

// Click to add 1 item
$(document).ready(function(){
    $('.btn-add-item').on('click', function(){
        let product_id = $(this).attr('product_id');
        let url = $(this).attr('url');
        let $counter =  $('#Quantity'+product_id); // quantity field
        let $subtotal_id =  'Subtotal'+product_id; // subtotal field
        let variations = document.getElementsByClassName('Variation'+product_id) ;
        data ={};
        for (let i=0; i<variations.length; i++) {
            category_value_array = variations[i].innerHTML.split(": ")
            data[category_value_array[0].toLowerCase()] = category_value_array[1] ;
        }
        console.log(data);
        $.ajax({
            url: url,
            data: data,
            success: function(data){
                // set quantity of cart icon
                document.getElementById("quantity-cart").innerHTML = data.quantity;
                $counter.val( parseInt($counter.val()) + 1 );
                document.getElementById($subtotal_id).innerHTML = data.sub_total;
                document.getElementById('TotalPrice').innerHTML = data.total;
                document.getElementById('Tax').innerHTML = data.tax;
                document.getElementById('GrandTotal').innerHTML = data.grand_total;
            }
        });
        return false;  // use this for not reloading the page
    });
});