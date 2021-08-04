// Click to add a whole new item
$(document).ready(function(){
    $('.btn-add-product').on('click', function(){
        let url = $(this).attr('url')
        $.ajax({
            url: url,
            success: function(){
                alert('Add product to cart successfully')
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
        $.ajax({
            url: url,
            success: function(data){
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