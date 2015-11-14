

$(document).ready(function() {
    var max_fields      = 10;
    var wrapper         = $(".input_fields_wrap");
    var add_button      = $(".add_field_button");

    function numbering(){
        $('.input_fields_wrap .form-group').each(function( i ) {
             $(this).find('label').attr('for', 'steps-'+i);
             $(this).find('label').text('Etape '+(i+1));
             $(this).find('input').attr('name', 'steps-'+i);
             $(this).find('input').attr('id', 'steps-'+i);
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
            $(wrapper).append('<div class="form-group sort"><label for="" class="col-sm-2 control-label"></label><div class="col-sm-4"><input class="form-control" id="" rows="3" required="true"></input></div><a href="#" class="remove_field btn btn-primary btn-danger col-sm-1">Supprimer</a></div>');
            c++;
        }
        numbering();
    });

    $(wrapper).on("click",".remove_field", function(e){
        e.preventDefault(); $(this).parent('div').remove(); c--;
        numbering();
    })
});
