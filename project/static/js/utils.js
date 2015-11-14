

$(document).ready(function() {
    var max_fields      = 10; //maximum input boxes allowed
    var wrapper         = $(".input_fields_wrap"); //Fields wrapper
    var add_button      = $(".add_field_button"); //Add button ID


    function numbering(){
        $('.input_fields_wrap .form-group').each(function( i ) {
             $(this).find('label').attr('for', 'steps-'+i);
             $(this).find('label').text('Etape '+(i+1));
             $(this).find('input').attr('name', 'steps-'+i);
             $(this).find('input').attr('id', 'steps-'+i);
        });
    }
    /*$(wrapper).sortable({
        cancel: ".ui-state-disabled",
        stop: function( event, ui ) {numbering();}
    });*/
    $(wrapper).sortable({
        items: '.sort',
        stop: function( event, ui ) {
            numbering();
        }
    });

    var c = 1; //initlal text box count
    $(add_button).click(function(e){ //on add input button click
        e.preventDefault();
        if(c < max_fields){ //max input box allowed
            $(wrapper).append('<div class="form-group sort"><label for="" class="col-sm-2 control-label"></label><div class="col-sm-4"><textarea class="form-control" id="" rows="3"></textarea></div><a href="#" class="remove_field btn btn-primary btn-danger col-sm-1">Supprimer</a></div>'); //add input box
            c++; //text box increment
        }
        numbering();
    });

    $(wrapper).on("click",".remove_field", function(e){ //user click on remove text
        e.preventDefault(); $(this).parent('div').remove(); c--;
        numbering();
    })
});
/*
    var c = 1;
    function addInput(divName){
        var newDiv = document.createElement('div');
        newDiv.innerHTML = '<div class="form-group"><label for="steps-'+c+'">Etape '+ (c+1) +' </label><input class="form-control" id="steps-'+c+'" name="steps-'+c+'" type="text" value=""></div>'
        document.getElementById(divName).appendChild(newDiv);
        c++;
    }*/
