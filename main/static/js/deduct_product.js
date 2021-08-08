// click to remove 1 whole item

function get_variations(product_id){
    let variations = document.getElementsByClassName('Variation'+product_id) ;
    data ={};
    for (let i=0; i<variations.length; i++) {
        category_value_array = variations[i].innerHTML.split(": ")
        data[category_value_array[0].toLowerCase()] = category_value_array[1] ;
    };
    return data;
}


$(document).ready(function(){
    $('.btn-deduct-whole-item').on('click', function(){
        let product_id = $(this).attr('product_id');
        let url_remove = $(this).attr('url_remove');
        let $subtotal_id =  'Subtotal' + product_id; // subtotal field
        let row  = 'Row' + product_id;

        // get variation of product
        data = get_variations(product_id);
        $.ajax({
            url: url_remove,
            data: data,
            success: function(data){           
                // set quantity of cart icon
                document.getElementById("quantity-cart").innerHTML = data.quantity;    
                document.getElementById(row).style.display= "none";
                if (data.total == 0){
                    console.log('data.total 0');
                    location.reload();
                }
                
                document.getElementById($subtotal_id).innerHTML = data.sub_total;
                document.getElementById('TotalPrice').innerHTML = data.total;
                document.getElementById('Tax').innerHTML = data.tax;
                document.getElementById('GrandTotal').innerHTML = data.grand_total;
            }
        });
        return false;  // use this for not reloading the page
    });
});


// click to remove 1 item
$(document).ready(function(){
    $('.btn-deduct-item').on('click', function(){
        let product_id = $(this).attr('product_id');
        let url_remove = $(this).attr('url_remove');

        let $counter =  $('#Quantity' + product_id); // quantity field
        let $subtotal_id =  'Subtotal' + product_id; // subtotal field
        let row  = 'Row' + product_id;

        // get the variation of 1 product
        data = get_variations(product_id);
        $.ajax({
            url: url_remove,
            data: data,
            success: function(data){                
                document.getElementById("quantity-cart").innerHTML = data.quantity;// set quantity of cart icon            
                $counter.val( parseInt($counter.val()) - 1 );            
                if ($counter.val() == 0) {  
                    document.getElementById(row).style.display= "none";
                    if (data.total == 0){                        
                        location.reload();
                    }
                }
                document.getElementById($subtotal_id).innerHTML = data.sub_total;
                document.getElementById('TotalPrice').innerHTML = data.total;
                document.getElementById('Tax').innerHTML = data.tax;
                document.getElementById('GrandTotal').innerHTML = data.grand_total;
            }
        });
        return false;  // use this for not reloading the page
    });
});