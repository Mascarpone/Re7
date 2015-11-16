$(document).ready(function() {
    var max_fields      = 10;
    var wrapper         = $(".input_fields_wrap");
    var add_button      = $(".add_field_button");

    function numbering(){
        $('.input_fields_wrap .form-group').each(function( i ) {
             $(this).find('label').attr('for', 'steps-'+i);
             $(this).find('label').text('Etape '+(i+1));
             $(this).find('textarea').attr('name', 'steps-'+i);
             $(this).find('textarea').attr('id', 'steps-'+i);
        });
    }

    $(wrapper).sortable({
        items: '.sort',
        stop: function( event, ui ) {
            numbering();
        }
    });

    var c = 1;
    $(add_button).click(function(e){
        e.preventDefault();
        if(c < max_fields){
            $(wrapper).append('<div class="form-group sort"><label for="" class="col-sm-2 control-label"></label><div class="col-sm-4"><textarea class="form-control" id="" rows="3" required="true"></textarea></div><a href="#" class="remove_field btn btn-primary btn-danger col-sm-1">Supprimer</a></div>');
            c++;
        }
        numbering();
    });

    $(wrapper).on("click",".remove_field", function(e){
        e.preventDefault(); $(this).parent('div').remove(); c--;
        numbering();
    })

    function previewFile() {
        var preview = document.querySelector('img');
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
});
