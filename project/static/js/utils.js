function previewFile() {
    var preview = document.querySelector('#preview');
    var file    = document.querySelector('input[type=file]').files[0];
    var reader  = new FileReader();

    reader.onloadend = function () {
        preview.src = reader.result;
    }

    if (file) {
        reader.readAsDataURL(file);
    } else {
        preview.src = "";
    }
}

$(document).ready(function() {
    var max_fields = 10;
    var wrapperSteps = $(".input_steps");
    var wrapperIngredient = $(".input_ingredients");
    var c = 1;
    var v = 1;


    $(wrapperSteps).sortable({
        items: '.sort',
        stop: function( event, ui ) {
            numberingSteps();
        }
    });

    function numberingSteps(){
        $('.input_steps .form-group').each(function( i ) {
             $(this).find('label').attr('for', 'steps-'+i);
             $(this).find('label').text('Etape '+(i+1));
             $(this).find('textarea').attr('name', 'steps-'+i);
             $(this).find('textarea').attr('id', 'steps-'+i);
        });
    }

    function numberingIngredients(){
        $('.input_ingredients .input_ingredients').each(function( i ) {
             $(this).find("input[name$='isMain']").attr('name', 'contains-'+i+'-isMain')
             $(this).find("input[name$='isMain']").attr('id', 'contains-'+i+'-isMain')
             $(this).find("input[name$='quantity']").attr('name', 'contains-'+i+'-quantity')
             $(this).find("input[name$='quantity']").attr('id', 'contains-'+i+'-quantity')
             $(this).find("input[name$='ingredientName']").attr('name', 'contains-'+i+'-ingredientName')
             $(this).find("input[name$='ingredientName']").attr('id', 'contains-'+i+'-ingredientName')
             $(this).find("select[name$='unitID']").attr('name', 'contains-'+i+'-unitID')
             $(this).find("select[name$='unitID']").attr('id', 'contains-'+i+'-unitID')

             $('#contains-'+i+'-ingredientName').autocomplete({
                 source: ingredients,
                 delay: 0
             });
        });
    }
    numberingIngredients();
    $(".repeat-step").on('click', function (e) {
        e.preventDefault();
        if(c < max_fields){
            var $self = $(this);
            var block = $self.parent().prev().clone();
            $(block).addClass('sort');
            $(block).find('textarea').val('');
            if(c == 1)
                $(block).append('<a href="#" class="remove_field btn btn-primary btn-danger col-sm-1">Supprimer</a>')
            $self.parent().before(block);
            c++;
        }
        numberingSteps()
    });

    $(".repeat-ingredient").on('click', function (e) {
        e.preventDefault();
        if(v < max_fields){
            var $self = $(this);
            var block = $self.parent().prev().clone();
            if(v == 1)
                $(block).append('<a href="#" class="remove_field btn btn-primary btn-danger col-sm-1">Supprimer</a>')

            $self.parent().before(block);
            $(block).find(':input').not(':button, :submit, :reset, :hidden, :checkbox, :radio').val('');
            $(block).find(':checkbox, :radio').prop('checked', false);
            v++;
        }
        numberingIngredients();
    });

    $(wrapperIngredient).on("click",".remove_field", function(e){
        e.preventDefault(); $(this).parent('div').remove(); v--;
        numberingIngredients();
    })

    $(wrapperSteps).on("click",".remove_field", function(e){
        e.preventDefault(); $(this).parent('div').remove(); c--;
        numberingSteps();
    })

    numberingSteps();

});
