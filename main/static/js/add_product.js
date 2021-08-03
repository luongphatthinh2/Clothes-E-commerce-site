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

$(document).ready(function(){
    $('.btn-add-item').on('click', function(){
        let product_id = $(this).attr('product_id');
        let url = $(this).attr('url');
        let $counter =  $('#ItemID'+product_id);
        $.ajax({
            url: url,
            success: function(){
                $counter.val( parseInt($counter.val()) + 1 );
            }
        });
        return false;  // use this for not reloading the page
    });
});