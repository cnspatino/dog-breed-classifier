$(document).ready( function() {

        $('#uploadFile').on('click', function()
        {
            var fd = new FormData();
            var files = $('#imgInp')[0].files[0];
            fd.append('file',files);

            $.ajax({
                url: '/prediction',
                method: 'POST',
                data: fd,
                contentType: false,
                processData: false,
                success: function(response){
                    //TODO: use returned json from flask route '/prediction' POST
                    //var myobj = JSON.parse(response.text);    
                    //$("#PredictedFriendlyMessage").text(myObj.PredictedFriendlyMessage);
                    alert(response.predictionText);
                },
            });
        });

        $(document).on('change', '.btn-file :file', function() {
        var input = $(this),
            label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
        input.trigger('fileselect', [label]);
        });

        $('.btn-file :file').on('fileselect', function(event, label) {
            
            var input = $(this).parents('.input-group').find(':text'),
                log = label;
            
            if( input.length ) {
                input.val(log);
            } else {
                if( log ) alert(log);
            }
        
        });
        function readURL(input) {
            if (input.files && input.files[0]) {
                var reader = new FileReader();
                
                reader.onload = function (e) {
                    $('#img-upload').attr('src', e.target.result);
                }
                
                reader.readAsDataURL(input.files[0]);
            }
        }

        $("#imgInp").change(function(){
            readURL(this);
        });     
    });