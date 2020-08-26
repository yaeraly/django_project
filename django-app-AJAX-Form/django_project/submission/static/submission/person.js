$(document).ready(function() {
	
	var csrfToken = $('input[name=csrfmiddlewaretoken]').val();

	$('#createButton').click('click', function() {
		var serializedData = $('#createPersonForm').serialize();

		$.ajax({

			url: $('#createPersonForm').data('url'),
			data: serializedData,
			type: 'post',
			success: function(response) {
				$('#personList').append('<div class="card mb-3" id="personCard" data-id="' + response.person.id + '">' +
											'<div class="card-body">'
												+ response.person.full_name +	
												'<button type="button" class="close" aria-label="Close">' +
	         										'<span aria-hidden="true">&times;</span>' +
	        									'</button>' +
											'</div>' +
										'</div>'
										)
									}

		});

		$('#createPersonForm')[0].reset();

	});


	$('button.close').on('click', '.card', function() {
		var dataId = $('#personCard').data('id');

		$.ajax({
			url: '/person/'+ dataId +'/delete/',
			data: {
				csrfmiddlewaretoken: csrfToken,
				id: dataId,
			},
			type: 'post',
			datatype: 'json',
			success: function() {

			}
		});
	});


}); 